import sys
import re
if sys.version_info[0] < 3:
    raise "Must be using Python 3"

# Store the message to send
message = ""
bUpdated = False

# Get the page HTML
import urllib.request
listPageBody=str(urllib.request.urlopen("https://support.apple.com/en-us/HT201222").read())

# Search for iOS updates
# Should capture (1)-article link and (2)-version number
iReg = re.compile("<a [^>]*href=[',\"]([^',\"]*)[^>]*>(iOS [^<]*)</a>")
iRegMatch = iReg.search(listPageBody)
if (iRegMatch is None):
	raise "Our iOS regex didn't match, the site format may have changed"

iFoundVersion = iRegMatch.group(2)
iArticle = iRegMatch.group(1)


# Search for macOS updates
macReg = re.compile("<a [^>]*href=[',\"]([^',\"]*)[^>]*>(macOS [^<]*)</a>")
macRegMatch = macReg.search(listPageBody)
if (macRegMatch is None):
	raise "Our macOS regex didn't match, the site format may have changed"

macFoundVersion = macRegMatch.group(2)
macArticle = macRegMatch.group(1)	


# Check our stored info to see if it has changed
from CONFIG import *
if (iFoundVersion != lastIOSversion or macFoundVersion != lastMACOSversion):
	# Add message header text
	message+="\nIt looks like there's an update for your software:\n\n"
	if(iFoundVersion != lastIOSversion):
		# iOS update text
		message+=iFoundVersion+"\nYou can find information about the update here: "+iArticle+"\n\n\n"

	if (macFoundVersion != lastMACOSversion):
		# macOS update text
		message+=macFoundVersion+"\nYou can find information about the update here: "+macArticle+"\n\n\n"
	# Store our new versions
	config_out="lastIOSversion='"+iFoundVersion+"'\nlastMACOSversion='"+macFoundVersion+"'\n"
	fo = open("CONFIG.py", "w")
	fo.write(config_out)
	fo.close()

# Check to see if we have something worth messaging about...
if (lastIOSversion != '' and lastMACOSversion != '' and message !=''):
	bUpdated = True

if (bUpdated):
	# Print the message instead of sending for now
	print(message)