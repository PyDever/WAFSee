
"""entry point main control script"""

from __future__ import print_function
from os import urandom, system
import sys, time

# build global exceptions for entry point main
class ModuleNotFound (Exception):
	def __str__ (self):
		return "Could not import required module."

class ResourceNotFound (Exception):
	def __str__ (self):
		return "Could not import required resource folder."

class FailedConnection (Exception):
	def __str__ (self):
		return "Could not establish proper HTTP connection."

try:
	from headers.user_agents import all_user_agents
	'''
	from payloads.injectx import signature_based
	from payloads.injectx import encoded_bypass
	'''
except Exception:
	raise ResourceNotFound()

# make default dependency imports
import mechanize
import requests, urllib2
import cookielib
from bs4 import BeautifulSoup

def browser_style_request (url):

	cookiejar_object = cookielib.CookieJar()
	http_url_opener = urllib2.build_opener(
		urllib2.HTTPCookieProcessor(cookiejar_object))
	http_url_opener.addheaders = [
		('User-Agent', all_user_agents['samsung-galaxy-s8']), 
		('Content-Encoding','gzip')]
	try: response = http_url_opener.open(url).read(); return True
	except urllib2.URLError: print('[!] URL given is most likely invalid.'); return None
	except (urllib2.HTTPError, Exception): return False 
	
def possibly_malicious_request (url):

	http_url_opener = urllib2.build_opener()
	http_url_opener.addheaders = [
		('User-Agent', all_user_agents['fuzz-script']), 
		('Content-Encoding','deflate')]
	try: response = http_url_opener.open(url).read(); return True
	except (urllib2.HTTPError, Exception): return False 
	except urllib2.URLError: print('[!] URL given is most likely invalid.'); return None

def check_for_header_based (url):

	if browser_style_request(url) != possibly_malicious_request(url):
		print('[*] Webpage IS BEHIND a header-based WAF...')
	else:
		print('[*] Webpage DOES NOT seem to use a header-based WAF...')



"""
C:\Users\Student>python
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests, mechanize
>>> req = mechanize.Browser()
>>> req.open('https://www.myhta.org/system/login/')
<response_seek_wrapper at 0x305b760 whose wrapped object = <closeable_response at 0x305d8f0 whose fp = <socket._fileobject object at 0x0304CA70>>>
>>> req.select_form('formInput')
>>> payload = "<svg><script>alert&grave;1&grave;<p>"
>>> req.form['usr_email'] = payload
>>> req.submit()
<response_seek_wrapper at 0x3050418 whose wrapped object = <closeable_response at 0x38b8738 whose fp = <socket._fileobject object at 0x03890EF0>>>
>>> resp = req.response().read()
>>> if resp.find('Cloudflare')(:
  File "<stdin>", line 1
    if resp.find('Cloudflare')(:
                               ^
SyntaxError: invalid syntax
>>> if resp.find('Cloudflare'):
...     print(1)
...
1
>>>
"""

