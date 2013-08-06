#!/usr/bin/python2

from mechanize import ParseResponse, urlopen, URLError

uri = "http://perdu.com"
user_name = "user@belgacomfon.be"
user_pass = "8_character_password"

def internet_on():
    try:
        response=urlopen(uri, timeout=1)
        return True
    except URLError:
        return False

connection_active = internet_on()
try:
    response = urlopen(uri)
    forms = ParseResponse(response, backwards_compat=False)
    form = forms[0]
    print('Sending login...')
    form["login[user]"] = user_name
    form["login[pass]"] = user_pass
except IndexError:
    if connection_active:
        print('You\'re already connected')
    else:
        print('No form found / Are you sure you are connected on a FON box?')
except URLError:
    print('Not connected to a FON box')

try:
    urlopen(form.click()).read()
    print('Connected to FON Network!')
except NameError:
    if not connection_active:
        print('Not connected to FON Network')

