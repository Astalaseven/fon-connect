from os import path
import ConfigParser
import argparse
from time import sleep

from fon import connect, connected, LinkException, SSIDException
from meta import __version__


def getconfig(config_file=None):
    if not config_file:
        home = path.expanduser("~")
        config_file = path.join(home, ".config", "fon")

    if not path.isfile(config_file):
        exit('No file.')

    try:
        configParser = ConfigParser.RawConfigParser()
        configParser.read(config_file)
    except ConfigParser.Error:
        exit("Malformatted .config/fon")

    try:
        url = configParser.get('fon', 'url')
    except ConfigParser.NoSectionError:
        exit("Missing the [fon] section")
    except ConfigParser.NoOptionError:
        url = None
    try:
        username = configParser.get('fon', 'username')
    except ConfigParser.NoOptionError:
        username = None
    try:
        password = configParser.get('fon', 'password')
    except ConfigParser.NoOptionError:
        password = None

    return url, username, password


def version():
    exit('Fon connect {}\nhttps://github.com/C4ptainCrunch/fon-connect'.format(__version__))


def get_values(args):
    config_file = None if args.config == args.config else args.config
    from_config = getconfig(config_file)
    url = args.url if not args.url == "http://perdu.com" else from_config[0]
    username = args.username if args.username else from_config[1]
    password = args.password if args.password else from_config[2]
    if not url:
        url = "http://perdu.com"
    if not username:
        exit("Missing username")
    if not password:
        exit("Missing password")

    return url, username, password


def try_connect(url, username, password):
    try:
        if connect(url, username, password):
            return "You are now connected"
        else:
            return "Wrong username or password."
    except SSIDException:
        return "You seem not connected to a FON box"
    except LinkException:
        return "You are already connected"
    except RuntimeError:
        return "Unkown error, try again"

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', '--username', type=str, nargs='?', help='your fon username')
parser.add_argument('-p', '--password', type=str, nargs='?', help='your fon password')
parser.add_argument('--url', type=str, nargs='?', help='url to test if the conection is active', default="http://perdu.com")
parser.add_argument("-v", "--version", help="output version", action="store_true")
parser.add_argument("-c", "--config", help="configuration file", default="~/.config/fon")
parser.add_argument("-P", "--persist", help="keep trying to connect", action="store_true")


def main():
    args = parser.parse_args()
    if args.version:
        version()

    url, username, password = get_values(args)
    persist = args.persist

    if not persist:
        print try_connect(url, username, password)
    else:
        print "Persistant connection :"
        while True:
            print "Reconnecting"
            try_connect(url, username, password)
            print "Connected"
            while connected(url):
                sleep(10)

if __name__ == '__main__':
    main()
