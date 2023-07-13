# dpm
dpm is a TUI frontend to MPD
## Features
The feature set, at present, is somewhat limited. Right now, it can:
- browse your library
- search for media
- manage playlist settings
- shuffle your library
- view the current playlist
## Limitations
- browsing works only with a 3-level directory structure (i.e. artist -> album -> songs)
- managing playlist settings does not include managing the queue
## Issues
- if left idle for too long, the app loses connection to MPD
# Installation
- Download the executable. Place in your $PATH (i.e. ~/.local/bin)
## Dependencies
- Rich (install with `pip install rich`)
- python-mpd2 (install with `pip install python-mpd2`)
- MPD (default hostname is `"localhost"` and port is `6600`. Change this is client.py, if desired)
# Usage
Refer to help.md
# Screenshots
## Browsing the Library
![browse_library](screenshots/browse_library.png)
## Searching the Library
![search_results](screenshots/search_results.png)
## Playlist Options
![playlist_options](screenshots/playlist_options.png)
## Currently Playing
![currently_playing](screenshots/currently_playing.png)
