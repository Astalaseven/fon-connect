#!/usr/bin/python2

from mechanize import ParseResponse, urlopen, URLError
from urllib2 import URLError as PlainURLError
from urllib2 import urlopen as Plainurlopen


class SSIDException(RuntimeError):
    pass


class LinkException(RuntimeError):
    pass


def connected(url):
    try:
        Plainurlopen(url, timeout=2)
    except:
        return False
    else:
        return True


def connect(url, username, password):
    try:
        if connected(url):
            raise LinkException('You are already connected')
        try:
            response = urlopen(url)
        except URLError:
            raise SSIDException('You are not connected on a FON box')

        forms = ParseResponse(response, backwards_compat=False)

        try:
            form = forms[0]
            form["login[USERNAME]"] = username
            form["login[PASSWORD]"] = password
        except IndexError:
            raise SSIDException('You are not connected on a FON box')

        try:
            response_page = urlopen(form.click()).read()
        except NameError:
            raise SSIDException('You are not connected on a FON box')

        return not 'class="form_error"' in response_page
    except PlainURLError:
        if connected(url):
            return True
        else:
            raise RuntimeError("Connection failed.")
