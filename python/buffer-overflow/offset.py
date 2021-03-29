#!/usr/bin/python3
import os
import sys
if len(sys.argv) != 2:
    print('you need a para such as 39694438 to get the offset')
    sys.exit()
os.system("cd /usr/share/metasploit-framework/tools/exploit && ./pattern_offset.rb -q " + sys.argv[1] + " && cd")
