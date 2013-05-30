#!/usr/bin/env python

import commands
import sys
import os
import stat

if __name__ == "__main__":

    try:
	tmp = commands.getoutput("pgrep -f flashplayer");
	found = False;
	for ttmp in tmp.split("\n"):
	        output = commands.getoutput("wmctrl -lp | grep " + ttmp + " | awk '{ print $1 }' | xargs -I PID xprop -id PID | grep -q _NET_WM_STATE_FULLSCREEN && echo true || echo false")

	        for filepath in output.split("\n"):
	            if filepath == "true":
			found = True;

	if (found):
		print 3;
	else:
		print 1;

    except Exception, data:
        print 2
        print output.__len__()
        sys.exit(2)
