# annoying-as-a-service
I used to have a co-worker who would parade around the office every time there was an update for iOS or macOS. He's been replaced by this script.

The script checks an [Apple KB page](https://support.apple.com/en-us/HT201222), then searches the page with a regex for new version numbers. That was really the best source of info I could find on updates, please let me know if you can find a better authority for this (or an RSS feed).

Test Usage: 
```
python3 checkMacUpdates.py
```

Or you can schedule it by adding this to crontab:
```
*/30 * * * * python3 ~/annoying-as-a-service/checkMacUpdates.py
```
