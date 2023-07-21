# HELP! How do I use this?  
In order to run dpm, you need to provide an argument. As of now, available arguments are:  
- `b` for browse  
- `p` for playlist browsing  
- `o` for managing playlist options  
- `f` for searching (f for find)  
- `s` for shuffling the music library    
- `c` for viewing the currently playing screen  
# Navigating the app
The character `➙` denotes a prompt. This is where input such as index numbers and `a` are accepted.  
At any point during usage, inputting `Ctrl+c` will go back.
# Browsing the library
In order to browse your libray, input `dpm b`.  
This will bring up an interface that looks as follows:

```
       Artists
 ─────────────────────────────────────────
   1   Artist One
   2   Artist Two 
   3   Artist Three
   4   Artist Four
   5   Artist Five

  ➙
```

To view the albums by a particular artist, simple input the index next to them on the left.  
For example, to view albums by Artist Four, simply input `4`. This operation is supported only on the first two levels.  
To add something to the queue at any point, input `a` followed by the desired index. To add Artist Five to the queue, input `a 5`.
# Playlists
To browse saved playlists, input `dpm p`.  
This will being up an interface similar to the one illustrated above.  
Here, the only supported operation is `a`. This follows the same usage as detailed above.
# Managing playlist options
To access this interface, input `dpm o`.  

```
       Playlist Options
 ───────────────────────
   1   Repeat
   2   Random
   3   Single
   4   Consume
   5   Clear Playlist
   6   Crop Playlist
   7   Shuffle Playlist
   8   Play/Pause
   9   Stop Playback
  10   Next
  11   Previous

➙
```
Simply input the index of the action you want to perform.  
You can interact with this interface directly from the command line, by following `dpm o` with one of the following:
- `r` to toggle repeat  
- `z` to toggle random mode  
- `o` to toggle single mode  
- `c` to toggle consume  
- `e` to clear the current playlist  
- `k` to crop the current playlist  
- `s` to shuffle the current playlist  
- `t` to toggle play/pause  
- `x` to stop playback  
- `n` to play the next song in the queue  
- `p` to play the previous song in the queue  
# Searching the library
The search interface is brought up with `dpm f`. 
The interface will look as follows:

```
  Search:
```

Here, simply search for whatver you're looking for. This will bring up a list of results:

```
  Search: a moon shaped pool

       Search Results
 ───────────────────────────────────────────────────────────────────────────────────────────────────────
   1   Radiohead ➙ A Moon Shaped Pool ➙ Burn the Witch
   2   Radiohead ➙ A Moon Shaped Pool ➙ Daydreaming
   3   Radiohead ➙ A Moon Shaped Pool ➙ Decks Dark
   4   Radiohead ➙ A Moon Shaped Pool ➙ Desert Island Disk
   5   Radiohead ➙ A Moon Shaped Pool ➙ Ful Stop
   6   Radiohead ➙ A Moon Shaped Pool ➙ Glass Eyes
   7   Radiohead ➙ A Moon Shaped Pool ➙ Identikit
   8   Radiohead ➙ A Moon Shaped Pool ➙ The Numbers
   9   Radiohead ➙ A Moon Shaped Pool ➙ Present Tense
  10   Radiohead ➙ A Moon Shaped Pool ➙ Tinker Tailor Soldier Sailor Rich Man Poor Man Beggar Man Thief
  11   Radiohead ➙ A Moon Shaped Pool ➙ True Love Waits
  12   Radiohead ➙ A Moon Shaped Pool ➙ The Numbers (Jonny, Thom & a CR78)
  13   Radiohead ➙ A Moon Shaped Pool ➙ Present Tense (Jonny, Thom & a CR78)

➙
```

Only `a` is supported here. Its operation is the same as above. Here, however, you can also input `a *` to add all search results to the queue.
# Shuffling the library
Input `dpm s` to shuffle all songs in your library. Playback will start automatically.
# Currently playing screen
This can be accessed with `dpm c`.  
It looks something like what follows:

```
  ⏵ 1       Here Comes the Sun                        Abbey Road   The Beatles   3:12
            0:39 / 3:12
  +2        Because                                   Abbey Road   The Beatles   2:46
  +3        You Never Give Me Your Money              Abbey Road   The Beatles   4:03
  +4        Sun King                                  Abbey Road   The Beatles   2:26
  +5        Mean Mr. Mustard                          Abbey Road   The Beatles   1:07
  +6        Polythene Pam                             Abbey Road   The Beatles   1:13
  +7        She Came In Through the Bathroom Window   Abbey Road   The Beatles   1:59
  +8        Golden Slumbers                           Abbey Road   The Beatles   1:32
  +9        Carry That Weight                         Abbey Road   The Beatles   1:37
  +10       The End                                   Abbey Road   The Beatles   2:22
  +11       Her Majesty                               Abbey Road   The Beatles   0:26
```
