<div align=center>

<h1 align=center> ＲＡＪＩＯ - ＳＥＮ ( ラジオ船 ) </h1>
<p> ＵＮＤＥＲＧＲＯＵＮＤ ＦＲＥＱＵＥＮＣＩＥＳ // ＰＩＲＡＴＥ ＲＡＤＩＯ ＳＣＡＮＮＥＲ </p>

<p align=center>
<img alt="GitHub Version" src="https://img.shields.io/badge/version-0.1.0-C9B9E5?style=for-the-badge&logo=github">
<img alt="GitHub" src="https://img.shields.io/github/license/jullespio/rajio-sen?style=for-the-badge&color=4E3F61">
</p>

</div>

### ＯＶＥＲＶＩＥＷ (概要)

**Rajio-Sen** is a minimalist, vaporwave-themed terminal radio scanner. It allows you to tune into thousands of radio stations globally directly from your command line. 

This project is a heavily modified hard-fork of the original `radio-active` application. It has been completely rebuilt in the engine room to bypass abandoned dependencies (such as `pyradios`) in favor of a modern, direct-REST API communication array using the Radio-Browser database. The user interface has been redesigned using `rich` to provide a sleek, Neo-Tokyo heads-up display (HUD) with bilingual Japanese/English typography and a custom *Luminous Nebula* palette.

### ＦＥＡＴＵＲＥＳ (特徴)

- [x] **Direct API Uplink:** Bypasses bloated packages to connect directly to the Radio-Browser network for live, uncached sub-space telemetry.
- [x] **Vaporwave HUD:** Stripped-down minimalist terminal interface featuring `rich` box styling, Kanji headers, and fullwidth characters.
- [x] **Independent Transponder:** Checks for software updates exclusively against the custom GitHub releases API.
- [x] Supports more than 40K stations globally.
- [x] Record audio from live radio streams on demand.
- [x] Save and manage favorite stations effortlessly.
- [x] Discover stations by tag, country, or language.
- [x] VLC, MPV, and FFplay player support.
- [x] Sleep Timer (pomodoro) functionality.

### ＩＮＳＴＡＬＬ (インストール)

As this is a custom fork, the vessel must be constructed in your local drydock.

```bash
# Clone the repository
git clone [https://github.com/jullespio/rajio-sen.git](https://github.com/jullespio/rajio-sen.git)
cd rajio-sen

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the application and dependencies
pip install -e .
```

*Note: You must have [FFmpeg](https://ffmpeg.org/download.html) installed on your system to process and record audio streams.*

### ＲＵＮ (起動)

Search for a station and initialize the HUD:
```bash
python -m rajio_sen --search "city pop"
```
*(You may also use the `radio` or `rajio_sen` entry points depending on your environment alias setup).*

### ＯＰＴＩＯＮＳ (設定)

| Options            | Description                                    | Default       | Values                 |
| ------------------ | ---------------------------------------------- | ------------- | ---------------------- |
| (No Option)        | Select a station from menu to play             | False         |                        |
| `--search`, `-S`   | Station name                                   | None          |                        |
| `--play`, `-P`     | A station from fav list or url for direct play | None          |                        |
| `--country`, `-C`  | Discover stations by country code              | False         |                        |
| `--tag`            | Discover stations by tags/genre                | False         |                        |
| `--record` , `-R`  | Record a station and save to file              | False         |                        |
| `--limit`          | Limit the # of results in the Discover table   | 100           |                        |
| `--volume` , `-V`  | Change the volume passed into ffplay           | 80            | [0-100]                |
| `--favorite`, `-F` | Add current station to fav list                | False         |                        |

### ＲＵＮＴＩＭＥ ＣＯＭＭＡＮＤＳ (操作)

Input a command during the radio playback to perform an action:

```text
t/T/track     : Current song name (track info)
r/R/record    : Record a station
f/F/fav       : Add station to favorite list
s/S/search    : Search for a new station
n/N/next      : Play next station from search results or favorite list
timer/sleep   : Set a sleep timer (duration in minutes)
q/Q/quit      : Quit Rajio-Sen
```

### ＣＯＮＦＩＧＵＲＡＴＩＯＮ (システム構成)

All data files are stored in a dedicated directory under your user home path:

- **Configuration**:  `~/rajio_sen/config.ini`
- **Favorites**: `~/rajio_sen/alias_map`
- **Last Station**: `~/rajio_sen/last_station`
- **Recordings**: `~/rajio_sen/recordings`

### ＡＣＫＮＯＷＬＥＤＧＥＭＥＮＴＳ (謝辞)

*Rajio-Sen* is maintained by **ジュレス (juresu)**. 
This project was originally forked from the excellent `radio-active` CLI built by Dipankar Pal (deep5050). The hull was stripped down, the warp core replaced, and the UI redesigned to fit a new operational profile. 

<div align=center>
<p align=center> ＲＡＤＩＯ ＷＡＶＥＳ ＯＦ ＴＨＥ ＦＵＴＵＲＥ </p>
</div>