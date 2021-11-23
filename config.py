import os
import json

osPath = os.path.join("config", "config.json")
with open(osPath) as jsonFile: 
    data = json.load(jsonFile)
    global SCREEN_HEIGHT 
    SCREEN_HEIGHT = data["SCREEN_HEIGHT"]
    global SCREEN_WIDTH
    SCREEN_WIDTH = data["SCREEN_WIDTH"]