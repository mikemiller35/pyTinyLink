import sys, contextlib
from urllib.parse import urlencode
from urllib.request import urlopen

def tinify(url):
    tinyurl = ('http://localhost:5000/api-create?url=' + url)
    with contextlib.closing(urlopen(tinyurl)) as response:
        return response.read().decode('utf-8')

def main():
    for tinyurl in map(tinify, sys.argv[1:]):
        print(tinyurl)

if __name__ == '__main__':
    main()
