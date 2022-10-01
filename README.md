# COVID Fitbit Analysis: A script to extract FitBit heartrate data during exercise, pre- and post-COVID

I got COVID six weeks before going on what was supposed to be a vacation with a lot of hiking and other strenous activity. I'd heard a lot about the effects that even mild cases of COVID can have on cardiovascular health and conditioning, so I decided to get some data to keep track of whether my heart was working too hard and I needed to take it easy. Thankfully, it doesn't look like my heart is working any harder after COVID than it was before.

To use this script, you will need to do request your [FitBit account archive](https://www.fitbit.com/settings/data/export). This will be a big .zip file with a bunch of folders in it, amonst them `physical-activity`. This script analyzes the `exercise-#.json` files from this archive.

In `constants.py`, enter:
- the locations of your FitBit exercise files
- the day you first tested positive for COVID or first experienced symptoms of COVID
- the time zones you were in during the period of time you would like to analyze

and then just run `main.py`.