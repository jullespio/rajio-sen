"""
UI components for Rajio-Sen using Rich.
Vaporwave / Minimalist Edition
"""

from rich import print, box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from zenlog import log

# Global variable to store current station info for display
global_current_station_info = {}


def handle_welcome_screen() -> None:
    """Print the Rajio-Sen boot screen panel."""
    welcome = Panel(
        """
 [#C9B9E5]ＮＥＯ - ＴＯＫＹＯ ＡＵＤＩＯ ＳＹＮＤＩＣＡＴＥ[/]
 [#00FFFF]接続を確立しています...[/]  (Establishing connection...)

 [#4E3F61]=====================================================[/]

 [#C9B9E5]コマンド (ＨＥＬＰ)[/] : --help
 [#C9B9E5]終了 (ＥＸＩＴ)[/]     : Ctrl+C
        """,
        title="[b #00FFFF] ラジオ船 ( ＲＡＪＩＯ - ＳＥＮ ) [/]",
        width=85,
        expand=True,
        box=box.MINIMAL,
        border_style="#4E3F61"
    )
    print(welcome)


def handle_update_screen(app) -> None:
    """Check for updates and print a HUD message if available."""
    if app.is_update_available():
        update_msg = (
            "\n\t[blink #00FFFF]［ 新着アップデート ］ ＵＰＤＡＴＥ ＡＶＡＩＬＡＢＬＥ[/]\n"
            f"\t[#C9B9E5]バージョン (ＶＥＲＳＩＯＮ):[/] {app.get_remote_version()}\n"
            "\t[#4E3F61]Execute: git pull origin main[/]\n"
        )
        update_panel = Panel(
            update_msg,
            width=85,
            box=box.MINIMAL,
            border_style="#00FFFF"
        )
        print(update_panel)
    else:
        log.debug("System up to date.")


def handle_favorite_table(alias) -> None:
    """Print the user's favorite list in a minimalist table."""
    table = Table(
        show_header=True,
        header_style="bold #C9B9E5",
        min_width=85,
        box=box.SIMPLE,
        border_style="#4E3F61",
        expand=True,
    )
    table.add_column("放送局 (ＳＴＡＴＩＯＮ)", justify="left")
    table.add_column("周波数 (ＵＲＬ / ＵＵＩＤ)", justify="left")

    if len(alias.alias_map) > 0:
        for entry in alias.alias_map:
            table.add_row(
                f"[#C9B9E5]{entry['name']}[/]", 
                f"[#4E3F61]{entry['uuid_or_url']}[/]"
            )
        print(table)
        log.info(f"Saved frequencies located in {alias.alias_path}")
    else:
        log.info("[ 空白 ] You have no saved stations.")


def handle_show_station_info() -> None:
    """Show important information regarding the current station."""
    global global_current_station_info
    
    if not global_current_station_info:
        log.error("[ 空白 ] No telemetry available.")
        return

    # Formatting the raw data into a clean readout
    info_text = (
        f"[#C9B9E5]ID:[/]      {global_current_station_info.get('stationuuid', 'N/A')}\n"
        f"[#C9B9E5]NAME:[/]    {global_current_station_info.get('name', 'N/A')}\n"
        f"[#C9B9E5]COUNTRY:[/] {global_current_station_info.get('country', 'N/A')}\n"
        f"[#C9B9E5]TAGS:[/]    {global_current_station_info.get('tags', 'N/A')}\n"
        f"[#C9B9E5]CODEC:[/]   {global_current_station_info.get('codec', 'N/A')} @ {global_current_station_info.get('bitrate', '0')}kbps\n"
        f"[#4E3F61]URL:[/]      {global_current_station_info.get('url', 'N/A')}"
    )
    
    info_panel = Panel(
        info_text,
        title="[#00FFFF] データ (ＴＥＬＥＭＥＴＲＹ) [/]",
        width=85,
        box=box.MINIMAL,
        border_style="#4E3F61"
    )
    print(info_panel)


def handle_current_play_panel(curr_station_name: str = "") -> None:
    """Print the currently playing station panel."""
    panel_station_name = Text(f"► 再生中 : {curr_station_name}", justify="center", style="bold #C9B9E5")

    station_panel = Panel(
        panel_station_name, 
        title="[blink #00FFFF] ＯＮ ＡＩＲ [/]", 
        width=85,
        box=box.MINIMAL,
        border_style="#4E3F61"
    )
    console = Console()
    console.print(station_panel)


def set_global_station_info(info: dict) -> None:
    """Helper to update global station info from other modules."""
    global global_current_station_info
    global_current_station_info = info


def get_global_station_info() -> dict:
    """Helper to get global station info."""
    global global_current_station_info
    return global_current_station_info