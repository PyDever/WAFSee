
<img src="https://lh3.ggpht.com/Eo7y02OP6nsOqTx-MsYORxLsIXltk-_0DQUkNztdPUrr_2ZIoR_RgaDXt3y6qrcdIT4" width="150"><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="320"/>

 [![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness) 
[![Coveralls](https://coveralls.io/repos/github/tygerbytes/ResourceFitness/badge.svg?branch=master)](https://coveralls.io/github/tygerbytes/ResourceFitness?branch=master) 
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)

# ***WAFSee*** #
💥 Powerful yet scalable WAF (web-app firewall) detection/bypass script 💥 

* detects header-based/signature-based WAFs
* detects differences in responses between valid/invalid `POST` content
* formulates bypass methods for most common firewalls
* fingerprints most common firewalls and logs banners

### installation
WAFSee does not require compilation. Simply download the script
and install the requirements.
```
$ git clone https://github.com/PyDever/WAFSee
$ cd WAFSee/
$ pip install -r requirements.txt
```

### usage
Using WAFSee is as simple as setting up.
```
$ chmod +x wafsee/__main__.py
$ ./wafsee --help
```
