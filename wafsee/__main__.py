
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
from bs4 import BeautifulSoup

# test for presence of header-analyzation WAF
def header_WAF_presence_test (url):
	"""
	In essence, this function will analyze the response when
	using malicious and non-malicious user agents in the HTTP headers.
	"""

	normal = requests.Session(); malicious = requests.Session()

	normal.headers['User-Agent'] = all_user_agents['samsung-galaxy-s8']
	malicious.headers['User-Agent'] = all_user_agents['fuzz-script']

	try:
		normal_response = normal.get(url)
		malicious_response = malicious.get(url)
	except Exception:
		raise FailedConnection()

	if normal_response.status_code == 200 and malicious_response.status_code == 200:
		
		if normal_response.content == malicious_response.content:
			print('-> Site is NOT BEHIND a header-based WAF or IPS service.')
		else:
			print('-> Site is DEFINITELY BEHIND a header-based WAF or IPS service.')

	else:
		raise FailedConnection()

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

