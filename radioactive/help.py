from os import path

from rich.console import Console
from rich.table import Table
from rich import box

user = path.expanduser("~")

def show_help():
    """Show help message as table"""
    console = Console()

    # Applying the minimalist style and custom hex colors
    table = Table(
        show_header=True, 
        header_style="bold #00FFFF", 
        box=box.MINIMAL,
        border_style="#4E3F61"
    )
    
    table.add_column("引数 (Arguments)", justify="left", style="#C9B9E5")
    table.add_column("説明 (Description)", justify="left")
    table.add_column("初期値 (Default)", justify="center", style="#4E3F61")

    table.add_row("--search , -S", "Search for a station name online", "")
    table.add_row("--uuid , -U", "Play a station directly via UUID", "")
    table.add_row("--country, -C", "Discover stations by ISO country code", "")
    table.add_row("--state", "Discover stations by country state", "")
    table.add_row("--tag", "Discover stations by tags/genre", "")
    table.add_row("--language", "Discover stations by language", "")
    table.add_row("--play , -P", "Play from favorite list or a direct URL", "")
    table.add_row("--last", "Play the most recently tuned station", "False")
    table.add_row("--random", "Play a random favorite station", "False")
    table.add_row("--add , -A", "Manually add a station to favorites", "False")
    table.add_row("--favorite, -F", "Add current station to favorites", "False")
    table.add_row("--list", "Display your favorite list", "False")
    table.add_row("--remove", "Remove entries from favorite list", "False")
    table.add_row("--flush", "Wipe the entire favorite list", "False")
    table.add_row("--limit, -L", "Limit the number of search results", "100")
    table.add_row("--sort", "Sort results (name, votes, bitrate, etc.)", "clickcount")
    table.add_row("--volume, -V", "Volume level (0-100)", "80")
    table.add_row("--record, -R", "Record the current audio stream", "False")
    table.add_row("--filepath", "Directory for audio recordings", f"~/rajio_sen/recordings")
    table.add_row("--filename, -N", "Output filename for recording", "<name-date>")
    table.add_row("--filetype, -T", "Recording codec (mp3/auto)", "mp3")
    table.add_row("--kill, -K", "Terminate background radio processes", "False")
    table.add_row("--loglevel", "Set verbosity: info, warning, error, debug", "info")
    table.add_row("--player", "Audio engine: vlc, mpv, or ffplay", "ffplay")

    console.print(table)
    
    # Updated to point to your repository
    console.print(
        "\n[#C9B9E5]ＤＯＣＵＭＥＮＴＡＴＩＯＮ:[/] [#00FFFF]https://github.com/jullespio/rajio-sen[/]\n"
    )