# File Watcher

[![Build Status](https://travis-ci.org/nickyvanurk/file-watcher.svg?branch=master)](https://travis-ci.org/nickyvanurk/file-watcher)
[![Coverage Status](https://coveralls.io/repos/github/nickyvanurk/file-watcher/badge.svg?branch=master)](https://coveralls.io/github/nickyvanurk/file-watcher?branch=master)

Monitors a directory tree for file changes and executes specified commands when an update is detected.

## Usage
* Allow the script to be executed: `chmod +x file_watcher.py`
* Run the script: `./file_wachter.py`
* Kill the script how you usually would. (Most likely `CTRL+C`)

Optional arguments (with default values):

    -h        display help message and exit
    -p  .     path of directory tree to watch
    -f        path of file to watch
    -e  *     extensions to watch
    -c  make  commands to execute
