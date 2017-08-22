# DS_Store Kill
Simple daemon which will kill .DS_Store files immediately as they are born, using fsevents to hunt them down.

## Requirements:
* Python 3.x, maybe 2.7 would work too, I don't know
* `pip install macfsevents`

## How to use:

Save the file somewhere, make sure it's owned by your user and not writable by anyone else.  
Create a Launch Agent for it, for example:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>dsstorekiller</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/local/bin/python3</string>
    <string>…/dsstorekiller.py</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
</dict>
</plist>
```

To start for the first time without rebooting, use `launchctl load …` (as usual)
