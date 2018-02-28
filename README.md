# Tab Extract

A quick hack to pull out the addresses in all of your Google Chrome for Android tabs.

## What

This is a quick Python 3 script I wrote to extract all of the URLs (or URIs) from Chrome tab files usually located somewhere like */data/data/com.android.chrome/app_tabs* and probably accessible only via root. Use adb shell or something and copy all those files somewhere to analyze them.

## Why

I got myself into a weird thing where I kept opening up tabs as one does and before I knew it I just had too many. They weren't available on the "tabs from other devices" and such in Chrome on my desktop, so I decided to come up with something to find them.

## How

Do something like:

	find . -name "tab*" |xargs ./extract.py |sort |uniq > urls.txt

## But...

Yeah, this is a hack. I don't really parse the files, I just look for things that start with something like a url. A short list of issues are:

- Weird characters sometimes ... I just look for \x00 to terminate the string and obviously something else is going on with this format
- Weird encoding errors ... I just fudged in Latin-1 but you will probably want something else if you aren't mostly browsing English sites. With the script as is it should spit out the name of the problem file, so maybe skip the sort and uniq above first.
- Multiple results per file ... Not sure... sometimes the address I want is the first, sometimes it is the last, I have some flags in there for your to try but for now I just dump them all out.

## But!

Okay! Let me know. Not sure how much I can help, but maybe you can?

Last update: February 2018


