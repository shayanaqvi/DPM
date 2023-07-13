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
- For now, clone the repository and run `main.py`
## Dependencies
- Rich (install with `pip install rich`)
- python-mpd2 (install with `pip install python-mpd2`)
- MPD (default hostname is `"localhost"` and port is `6600`. Change this is client.py, if desired)
# Usage
Refer to help.md
# Screenshots
TODO: Update screenshots
## Main Menu
![main_menu](screenshots/main_menu.png)
## Browsing the Library
![browse_artist](screenshots/browse_artist.png)
![browse_albums](screenshots/browse_albums.png)
![browse_title](screenshots/browse_title.png)
## Searching the Library
![search_results](screenshots/search_results.png)
## Playlist Options
![playlist_options](screenshots/playlist_options.png)
## Currently Playing
![currently_playing](screenshots/currently_playing.png)
