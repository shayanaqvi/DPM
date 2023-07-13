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
Input `dpm` followed by one of the following arguments:
- browse (b)
- search (f)
- shuffle (s)
- options (o)
- current (c)
- help (h)
## browse
Browse the library.  
**Usage**: Input `dpm browse` or `dpm b`
## search
Search the library.  
**Usage**: Input `dpm search` or `dpm f` (f for find)
## shuffle
Shuffle the entire library and start playing.  
**Usage**: Input `dpm shuffle` or `dpm s`
## options
Manage playlist settings.  
**Usage**: Input `dpm options` or `dpm o`. Optionally, follow this with one of the following arguments:
- r (toggle repeat)
- z (toggle random)
- c (toggle consume)
- o (toggle single)
- t (toggle playback)
- s (shuffle current playlist)
- p (previous song)
- n (next song)
- x (stop playback)
- e (clear playlist)
For example, input `dpm options x` or `dpm o x` to stop playback.
## current
View the current playlist, including the currently playing song**.  
**Usage**: input `dpm current` or `dpm c`
# Screenshots
## Browsing the Library
![browse_library](screenshots/browse_library.png)
## Searching the Library
![search_results](screenshots/search_results.png)
## Playlist Options
![playlist_options](screenshots/playlist_options.png)
## Currently Playing
![currently_playing](screenshots/currently_playing.png)
