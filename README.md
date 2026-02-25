<div align="center">

<h1 align="center"> ＲＡＪＩＯ - ＳＥＮ ( ラジオ船 ) </h1>
<p> ＵＮＤＥＲＧＲＯＵＮＤ ＦＲＥＱＵＥＮＣＩＥＳ // ＰＩＲＡＴＥ ＲＡＤＩＯ ＳＣＡＮＮＥＲ </p>

<p align="center">
<img alt="GitHub Version" src="https://img.shields.io/badge/version-1.1.0-C9B9E5?style=for-the-badge&logo=github">
<img alt="AUR Version" src="https://img.shields.io/aur/version/rajio-sen?style=for-the-badge&color=1793D1&logo=arch-linux">
<img alt="GitHub" src="https://img.shields.io/github/license/jullespio/rajio-sen?style=for-the-badge&color=4E3F61">
</p>

</div>

### ＯＶＥＲＶＩＥＷ (概要)

**Rajio-Sen** is a minimalist, vaporwave-themed terminal radio scanner. It allows you to tune into thousands of radio stations globally directly from your command line. 

This project is a heavily modified hard-fork of the original `radio-active` application. It has been completely rebuilt to bypass abandoned dependencies (such as `pyradios`) in favor of a modern, direct-REST API communication with the Radio-Browser database. The user interface has been redesigned using `rich` to provide a sleek terminal display with bilingual Japanese/English typography and a custom *Luminous Nebula* palette.

### ＦＥＡＴＵＲＥＳ (特徴)

- [x] **Direct API Integration:** Connects directly to the Radio-Browser network for live, real-time station data.
- [x] **Vaporwave TUI:** Stripped-down minimalist terminal interface featuring `rich` box styling and full-width characters.
- [x] **Update Notifications:** Checks for software updates against the official GitHub releases API.
- [x] Supports more than 40K stations globally.
- [x] Record audio from live radio streams on demand via FFmpeg.
- [x] Save and manage favorite stations effortlessly.
- [x] Discover stations by tag, country, or language.
- [x] VLC, MPV, and FFplay player support.
- [x] Integrated Sleep Timer functionality.

### ＩＮＳＴＡＬＬ (インストール)

#### ＡＵＲ
For users on Arch-based systems, it is recommended to install via the AUR:

```bash
# Using yay
yay -S rajio-sen

# Using paru
paru -S rajio-sen
```

#### Manual Installation
```bash
# Clone the repository
git clone https://github.com/jullespio/rajio-sen.git
cd rajio-sen

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install the application and dependencies
pip install .
```

*Note: You must have [FFmpeg](https://ffmpeg.org/download.html) installed on your system to process and record audio streams.*

### ＲＵＮ (起動)

Once installed, use the `rajio` command to initialize the interface:

```bash
# Search for a specific genre or name
rajio --search "city pop"

# Play directly from your favorites list
rajio --play "Night City"
```

### ＯＰＴＩＯＮＳ (設定)

| Options | Description | Default | Values |
| :--- | :--- | :--- | :--- |
| (No Option) | Select a station from menu to play | False | |
| `--search`, `-S` | Search station by name | None | |
| `--play`, `-P` | Play from favorites or direct URL | None | |
| `--country`, `-C` | Filter stations by country code | False | |
| `--tag` | Search stations by tags/genre | False | |
| `--record` , `-R` | Record current station to file | False | |
| `--limit` | Limit number of search results | 100 | |
| `--volume` , `-V` | Set playback volume | 80 | [0-100] |
| `--favorite`, `-F` | Add current station to favorites | False | |

### ＲＵＮＴＩＭＥ ＣＯＭＭＡＮＤＳ (操作)

Input commands during playback to perform the following actions:

```text
p             : Play/Pause
t / track     : Display current stream metadata
i / info      : Information about the station
r / record    : Toggle recording mode
l / list      : Display favorites list
f / fav       : Add station to favorites list
e / edit      : Edit favorites list
s / search    : Search by tag/genre
n / next      : Play next result in current list
timer / sleep : Set sleep timer duration (minutes)
q / quit      : Close the application
```

### ＣＯＮＦＩＧＵＲＡＴＩＯＮ (システム構成)

Configuration and data files are located in the user home directory:

- **Config**:  `~/rajio_sen/config.ini`
- **Favorites**: `~/rajio_sen/alias_map`
- **Recordings**: `~/rajio_sen/recordings`

### ＡＣＫＮＯＷＬＥＤＧＥＭＥＮＴＳ (謝辞)

*Rajio-Sen* is maintained by **ジュレス (juresu)**. 
Originally forked from `radio-active` by Dipankar Pal. Refactored for modern performance and aesthetic standards.

<div align="center">
<p align="center"> ＲＡＤＩＯ ＷＡＶＥＳ ＯＦ ＴＨＥ ＦＵＴＵＲＥ </p>
</div>