#!/usr/bin/env python3
import requests

location = "Freising"
r = requests.get(f"https://www.wttr.in/{location}?format=3")

weather = r.text.split()
msg = weather[1] + "  " + weather[2]

print(msg)
