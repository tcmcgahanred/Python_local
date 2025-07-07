import re

dnd = 'CN=MCGAHAN TIMOTHY, THING=xxx'
        
cn = re.findall("CN=(\w+) ", dnd) + re.findall(" (\w+),", dnd)
username = cn[1] + " " + cn[0]

type(username)