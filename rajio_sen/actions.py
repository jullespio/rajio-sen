"""
Core logical actions for rajio-sen.
Vaporwave / Minimalist Refit
"""

import datetime
import json
import os
import subprocess
import sys
from random import randint
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
from rajio_sen.logger import log
from rich import print # ADDED: Rich print for UI

try:
    from rajio_sen.feature_flags import RECORDING_FEATURE
except ImportError:
    RECORDING_FEATURE = True

if RECORDING_FEATURE:
    from rajio_sen.recorder import record_audio_auto_codec, record_audio_from_url
from rajio_sen.last_station import Last_station


def handle_fetch_song_title(url: str) -> None:
    """Fetch currently playing track information"""
    print("   [#00FFFF]► 周波数をスキャン中 (Scanning frequencies...)[/]")
    log.debug(f"Attempting to retrieve track info from: {url}")
    
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_entries",
        "format=icy",
        url,
    ]
    track_name = ""

    try:
        output = subprocess.check_output(cmd).decode("utf-8")
        data = json.loads(output)
        log.debug(f"station info: {data}")
        track_name = data.get("format", {}).get("tags", {}).get("StreamTitle", "")
    except Exception:
        log.debug("Error while fetching the track name via ffprobe")

    if track_name != "":
        print(f"   [#C9B9E5]► 現在の曲 (CURRENT TRACK): {track_name}[/]")
    else:
        print("   [#FF0055]► ［ 無効 ］ NO TRACK INFORMATION AVAILABLE[/]")


def handle_record(
    target_url: str,
    curr_station_name: str,
    record_file_path: str,
    record_file: str,
    record_file_format: str, 
    loglevel: str,
) -> None:
    """Handle audio recording logic."""
    if not RECORDING_FEATURE:
        print("   [#FF0055]► ［ エラー ］ Recording feature is disabled in this build.[/]")
        sys.exit(1)

    print("   [#4E3F61]► Press 'q' to stop recording at any time.[/]")
    force_mp3 = False

    if record_file_format not in ["mp3", "auto"]:
        record_file_format = "mp3"
        log.debug("Error: wrong codec supplied!. falling back to mp3")
        force_mp3 = True
    elif record_file_format == "auto":
        log.debug("Codec: fetching stream codec")
        codec = record_audio_auto_codec(target_url)
        if codec is None:
            record_file_format = "mp3"
            force_mp3 = True
            log.debug("Error: could not detect codec. falling back to mp3")
        else:
            record_file_format = codec
            log.debug(f"Codec: found {codec}")
    elif record_file_format == "mp3":
        force_mp3 = True

    if record_file_path and not os.path.exists(record_file_path):
        log.debug(f"filepath: {record_file_path}")
        try:
            os.makedirs(record_file_path, exist_ok=True)
        except Exception as e:
            print(f"   [#FF0055]► ［ 失敗 ］ Could not create directory: {e}[/]")

    elif not record_file_path:
        from rajio_sen.paths import get_recordings_path
        log.debug("filepath: fallback to default path")
        record_file_path = get_recordings_path()
        try:
            os.makedirs(record_file_path, exist_ok=True)
        except Exception as e:
            print(f"   [#FF0055]► ［ 失敗 ］ Could not create default directory: {e}[/]")

    now = datetime.datetime.now()
    month_name = now.strftime("%b").upper()
    am_pm = now.strftime("%p")
    formatted_date_time = now.strftime(f"%d-{month_name}-%Y@%I-%M-%S-{am_pm}")

    if not record_file_format.strip():
        record_file_format = "mp3"

    if not record_file:
        record_file = "{}-{}".format(
            curr_station_name.strip(), formatted_date_time
        ).replace(" ", "-")

    tmp_filename = f"{record_file}.{record_file_format}"
    outfile_path = os.path.join(record_file_path, tmp_filename)

    print(f"   [#00FFFF]► 録音開始 (RECORDING TO): [#C9B9E5]{outfile_path}[/]")

    record_audio_from_url(target_url, outfile_path, force_mp3, loglevel)


def handle_add_station(alias) -> None:
    """Add a new station to favorites via user input."""
    try:
        left = input("   ► 局名 (Station Name): ")
        right = input("   ► 周波数 (Stream URL / UUID): ")
    except EOFError:
        print()
        log.debug("Ctrl+D (EOF) detected. Exiting gracefully.")
        sys.exit(0)

    if left.strip() == "" or right.strip() == "":
        print("   [#FF0055]► ［ エラー ］ Empty inputs not allowed[/]")
        sys.exit(1)
        
    alias.add_entry(left, right)
    print(f"   [#00FFFF]► 新規登録 (New Entry): {left} = {right}[/]")
    sys.exit(0)


def handle_add_to_favorite(alias, station_name: str, station_uuid_url: str) -> None:
    """Add the current station to favorites."""
    try:
        response = alias.add_entry(station_name, station_uuid_url)
        if not response:
            try:
                user_input = input("   ► 別の名前を入力 (Enter a different name): ")
            except EOFError:
                print()
                sys.exit(0)

            if user_input.strip() != "":
                alias.add_entry(user_input.strip(), station_uuid_url)
                print(f"   [#00FFFF]► お気に入りに追加しました (Added to favorites): {user_input.strip()}[/]")
        else:
             print(f"   [#00FFFF]► お気に入りに追加しました (Added to favorites): {station_name}[/]")
    except Exception as e:
        log.debug(f"Favorite Error: {e}")
        print("   [#FF0055]► ［ 警告 ］ Could not add. Already in list?[/]")


def handle_save_last_station(last_station, station_name: str, station_url: str) -> None:
    """Save the last played station."""
    last_played_station = {
        "name": station_name,
        "uuid_or_url": station_url
    }
    log.debug(f"Saving the current station: {last_played_station}")
    last_station.save_info(last_played_station)


def check_sort_by_parameter(sort_by: str) -> str:
    """Validate and return the sort parameter."""
    accepted = ["name", "votes", "codec", "bitrate", "lastcheckok", "lastchecktime", "clickcount", "clicktrend", "random"]
    if sort_by not in accepted:
        log.warning("Sort parameter unknown. Falling back to 'name'")
        return "name"
    return sort_by


def handle_search_stations(handler, station_name: str, limit: int, sort_by: str, filter_with: str) -> Any:
    log.debug(f"Searching API for: {station_name}")
    return handler.search_by_station_name(station_name, limit, sort_by, filter_with)


def handle_station_uuid_play(handler, station_uuid: str) -> Tuple[str, str]:
    """Play a station by UUID and register a vote."""
    log.debug(f"Searching API for: {station_uuid}")

    # The handler returns a list of matching stations (usually just 1 for a UUID)
    response = handler.play_by_station_uuid(station_uuid)

    log.debug(f"increased click count for: {station_uuid}")
    handler.vote_for_uuid(station_uuid)

    try:
        if response and len(response) > 0:
            station = response[0]
            station_name = station["name"]
            station_url = station["url"]
            return station_name, station_url
        else:
            raise ValueError("No station data returned from API for that UUID.")
            
    except Exception as e:
        log.debug(f"UUID Play Error: {e}")
        print("   [#FF0055]► ［ 失敗 ］ UUID UPLINK FAILURE[/]")
        sys.exit(1)

def handle_direct_play(alias, station_name_or_url: str = "") -> Tuple[str, str]:
    if "://" in station_name_or_url.strip():
        log.debug("Direct play: URL provided")
        station_name = handle_get_station_name_from_metadata(station_name_or_url)
        return station_name, station_name_or_url
    else:
        log.debug("Direct play: station name provided")
        response = alias.search(station_name_or_url)
        if not response:
            print("   [#FF0055]► ［ 失敗 ］ No station found in favorites with that name.[/]")
            sys.exit(1)
        else:
            return response["name"], response["uuid_or_url"]


def handle_play_last_station(last_station) -> Tuple[str, str]:
    station_obj = last_station.get_info()
    return station_obj["name"], station_obj["uuid_or_url"]


def handle_get_station_name_from_metadata(url: str) -> str:
    log.debug(f"Attempting to retrieve station name from: {url}")
    cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_entries", "format=icy", url,
    ]
    station_name = "Unknown Station"
    try:
        output = subprocess.check_output(cmd).decode("utf-8")
        data = json.loads(output)
        station_name = data.get("format", {}).get("tags", {}).get("icy-name", "Unknown Station")
    except Exception:
        log.debug("Could not fetch the station name via ffprobe")
    return station_name


def handle_station_name_from_headers(url: str) -> str:
    log.debug(f"Attempting to retrieve station name from: {url}")
    station_name = "Unknown Station"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == requests.codes.ok:
            if response.headers.get("Icy-Name"):
                station_name = response.headers.get("Icy-Name")
    except Exception as e:
        log.debug(f"Header fetch error: {e}")
    return station_name


def handle_play_random_station(alias) -> Tuple[str, str]:
    log.debug("playing a random station")
    alias_map = alias.alias_map
    if not alias_map:
        print("   [#FF0055]► ［ 空白 ］ No favorite stations found.[/]")
        sys.exit(1)

    index = randint(0, len(alias_map) - 1)
    station = alias_map[index]
    return station["name"], station["uuid_or_url"]