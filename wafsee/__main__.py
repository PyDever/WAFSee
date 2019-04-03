
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
import urllib2
import cookielib

try:
	import mechanize, requests, fuckit
	from bs4 import BeautifulSoup
except Exception:
	raise ModuleNotFound()

class WAFSee (object):

	def __init__ (self, url, form_name, input_field):

		self.url = url; self.form_name = form_name
		self.input_field = input_field

		self.cookiejar = cookielib.CookieJar()

	def __configure_send_normal_request (self):
		successful_normal_request = None

		http_url_opener = urllib2.build_opener(
			urllib2.HTTPCookieProcessor(self.cookiejar))
		http_url_opener.addheaders = [
			('User-Agent', all_user_agents['samsung-galaxy-s8']),
			('Content-Encoding','gzip')]
		try:
			response = http_url_opener.open(self.url).read()
			successful_normal_request = True

		except (urllib2.HTTPError, urllib2.URLError, Exception):
			successful_normal_request = False 

		return successful_normal_request

	def __configure_send_possibly_malicious_request (self):
		successful_possibly_malicious_request = None

		http_url_opener = urllib2.build_opener()
		http_url_opener.addheaders = [
			('User-Agent', all_user_agents['fuzz-script']), 
			('Content-Encoding','deflate')]
		try: 
			response = http_url_opener.open(self.url).read()
			successful_possibly_malicious_request = True

		except (urllib2.HTTPError, urllib2.URLError, Exception): 
			successful_possibly_malicious_request = False

		return successful_possibly_malicious_request

	def detect_header_based_firewall (self):
		normal_request_result = self.__configure_send_normal_request()
		possibly_malicious_request_result = self.__configure_send_possibly_malicious_request()

		if normal_request_result == True and possibly_malicious_request_result == False:
			print('[*] Webpage is MOST LIKELY using header-based security.')

		elif normal_request_result == True and possibly_malicious_request_result == True:
			print('[*] Webpage is NOT using header-based security.')

		elif normal_request_result == False and possibly_malicious_request_result == False:
			print('[!] Webpage might not exist or could be down.')

w = WAFSee('https://www.google.com/search?q=hello', 'formInput', 'usr_email')
with fuckit:
	w.detect_header_based_firewall()

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

