## Operational Tasks
1. detect header-based WAFs
	* utilize `all_user_agents`
	* send HTTP `OPEN` as Firefox
	* send HTTP `OPEN` as urllib2
2. detect signature-based WAFs
	* test an input form with a 
	  variety of XSS payloads
	* utilize `signature_based`
	* log any common WAFs detected
3. infer presence of WAF based on 
   differences between valid/invalid 
   `POST` request responses
4. fingerprint response banners for 
   any common WAFs found 

***NOTE: Only use 3 as a last resort***

## DevOps Tasks

1. implement `pytest` unit testing
2. implement `Travis` integration suite
3. implement `FuckIt.py` error suite
4. implement `pycodestyle` pep8 enforcer
5. implement `requirements.txt`
6. implement `setuptools` installation 

* ensure that 
`setup.py`/`setuptools`/`requirements.txt` 
all function properly together and use 
standardized naming conventions
* ensure that `pytest` does not get in 
the way of `FuckIt.py` or `pycodestyle` 
* ensure that `.gitignore` does not 
ignore IDE settings files 

