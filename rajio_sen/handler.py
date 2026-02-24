"""
    Rajio-Sen (ラジオ船) Handler
    Direct-to-API engine. Purged of all pyradios dependencies.
"""

import sys
import random
import requests
from typing import List, Optional, Dict, Any

from rich.console import Console
from rich.table import Table
from zenlog import log
from rich import box

from rajio_sen.filter import filter_expressions

try:
    from rajio_sen.feature_flags import MINIMAL_FEATURE
except ImportError:
    MINIMAL_FEATURE = False

console = Console()

def trim_string(text: str, max_length: int = 40) -> str:
    if not isinstance(text, str): return str(text)
    return text[:max_length] + "..." if len(text) > max_length else text

def print_table(response, columns, sort_by, filter_expression):
    if not response:
        # Replaced standard log with stylized output
        print("   [#FF0055]► ［ 失敗 ］ No stations found for that query.[/]")
        return []

    if filter_expression.lower() != "none":
        response = filter_expressions(response, filter_expression)
        if not response:
            print("   [#FF0055]► ［ 失敗 ］ No stations found after filtering.[/]")
            return []

    # Injecting Neo-Tokyo border styles
    table = Table(
        show_header=True, 
        header_style="bold #00FFFF", 
        expand=True, 
        min_width=85,
        box=box.SIMPLE_HEAD,      # Match the HUD box style
        border_style="#4E3F61"    # Dark purple borders
    )
    
    # ID Column
    table.add_column("ID", justify="center", style="bold #00FFFF")

    # Parsing dynamic columns and adding them with a default Lavender style
    parsed_columns = []
    for col_spec in columns:
        col_name, rest = col_spec.split(":")
        res_key, max_len = rest.split("@")
        parsed_columns.append((col_name, res_key, int(max_len)))
        # Applying the Lavender text color to the content columns
        table.add_column(col_name, justify="left", style="#C9B9E5")

    for i, station in enumerate(response):
        row_data = [str(i + 1)]
        for _, res_key, max_len in parsed_columns:
            val = str(station.get(res_key, ""))
            row_data.append(trim_string(val, max_length=max_len))
        table.add_row(*row_data)

    console.print("\n")
    console.print(table)
    return response

class Handler:
    def __init__(self):
        self.base_url = self.discover_mirror()

    def discover_mirror(self) -> str:
        """Find an active API mirror."""
        try:
            resp = requests.get("https://all.api.radio-browser.info/json/servers", timeout=5)
            resp.raise_for_status()
            return f"https://{random.choice(resp.json())['name']}"
        except Exception as e:
            log.critical(f"Connection failure: {e}")
            sys.exit(1)

    def _api_call(self, endpoint: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Safe transmission to the mirror network."""
        try:
            url = f"{self.base_url}/json/{endpoint}"
            # Sorting logic: API expects order (key) and reverse (bool)
            # We default to reverse=true for popular metrics (clickcount, votes)
            if params.get("order") and params["order"] != "name":
                params["reverse"] = "true"
            
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            log.debug(f"API Error: {e}")
            return []

    def search_by_station_name(self, name, limit, sort_by, filter_with):
        params = {"name": name, "limit": limit, "order": sort_by, "hidebroken": "true"}
        response = self._api_call("stations/byname", params)
        return print_table(response, ["Station:name@30", "Country:country@20", "Tags:tags@20"], sort_by, filter_with)

    def play_by_station_uuid(self, uuid):
        # Direct lookup doesn't need search params
        url = f"{self.base_url}/json/stations/byuuid/{uuid}"
        try:
            resp = requests.get(url, timeout=10)
            response = resp.json()
            if response:
                self.vote_for_uuid(uuid)
                return response
        except Exception as e:
            log.debug(f"UUID lookup failed: {e}")
        log.error("Invalid UUID station.")
        sys.exit(1)

    def discover_by_country(self, country, limit, sort_by, filter_with):
        key = "countrycode" if len(country.strip()) == 2 else "country"
        params = {key: country, "limit": limit, "order": sort_by}
        response = self._api_call("stations/search", params)
        return print_table(response, ["Station:name@30", "State:state@20", "Tags:tags@20"], sort_by, filter_with)

    def discover_by_state(self, state, limit, sort_by, filter_with):
        params = {"state": state, "limit": limit, "order": sort_by}
        response = self._api_call("stations/search", params)
        return print_table(response, ["Station:name@30", "Country:country@20", "Tags:tags@20"], sort_by, filter_with)

    def discover_by_language(self, language, limit, sort_by, filter_with):
        params = {"language": language, "limit": limit, "order": sort_by}
        response = self._api_call("stations/search", params)
        return print_table(response, ["Station:name@30", "Country:country@20", "Language:language@20"], sort_by, filter_with)

    def discover_by_tag(self, tag, limit, sort_by, filter_with):
        params = {"tag": tag, "limit": limit, "order": sort_by}
        response = self._api_call("stations/search", params)
        return print_table(response, ["Station:name@30", "Country:country@20", "Tags:tags@50"], sort_by, filter_with)

    def vote_for_uuid(self, uuid):
        """Register a click to support the station's popularity."""
        try:
            # The click endpoint is /json/url/{uuid}
            requests.post(f"{self.base_url}/json/url/{uuid}", timeout=5)
        except Exception as e:
            log.debug(f"Click not registered: {e}")