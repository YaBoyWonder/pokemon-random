import os
import random
import sys
import json
import utils

from collections import namedtuple
from flask import Flask, jsonify, send_from_directory, abort, send_file, render_template

try:
    with open("config.json", encoding='utf-8') as data:
        config = json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
except FileNotFoundError:
    print("Unable to Read config.json")
    sys.exit()

app = Flask(__name__)

# Cache all images
cache_images = [img for img in os.listdir(config.imagefolder)]

# Check for changes in image folder
extra_dirs = [config.imagefolder, "index"]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)





if __name__ == '__main__':
    utils.randomize(config.imagefolder, config.suffix)
    app.run(port=config.port, debug=config.debug, extra_files=extra_files)
