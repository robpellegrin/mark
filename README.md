# mark
A small command-line tool for saving and jumping to directories across shell sessions.

## Usage
```
usage: marks [-h] [-a ADD] [-d REMOVE] [-g GO_TO] [-l LIST] [index]

positional arguments:
  index                position in list

options:
  -h, --help           show this help message and exit
  -a, --add ADD        add a new path
  -d, --remove REMOVE  remove an item by index
  -g, --go-to GO_TO    go to (cd) path at index
  -l, --list LIST      list all entries
```
