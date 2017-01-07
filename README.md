# linux-audio-switcher
_Switch audio inputs on Linux between HDMI and USB audio_

I wrote this specifically for my usage, but it can easily be customized for your own usage.

Running `pacmd list-sinks` in Terminal will show all of your audio outputs. Use this to determine the names of the outputs you want to switch between.

Change the name in quotes in line 16 to reflect the name of one output (I recommend the headphones).

Change the name in quotes in line 18 to reflect the name of the other output (I recommend the speakers).

The command line argument for selecting the first output is **h** (headphones)

The command line argument for selecting the second output is **s** (speakers)

Now, running `python audioswitcher.py h` in Terminal will switch to the first output (headphones), and `python audioswitcher.py s` will switch to the speakers.

For ease of use, I recommend creating an **alias** to run the command in Terminal.
For example, I used `alias hd="python audioswitcher.py h"` to allow me to type JUST `hd` into the terminal and audio will switch to headphones, and `alias spk="python audioswitcher.py s"` to switch to speakers.
