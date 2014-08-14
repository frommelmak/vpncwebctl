vpncwebctl
==========

Control your Cisco VPN client remotely

#Installation

This utility is written using Bottle, a Python web framework.

First of all, install the required dependencies.

##Using the Ubuntu/Debian package manager:

`apt-get install python-bottle`

##Or you can use the alternative python package installer:

`pip install bottle`

Then clone this repo:

```
git clone git@github.com:frommelmak/vpncwebctl.git
cd vpncwebctl
python server.py
```

#Optional:

Finaly you can install [supervisor](http://supervisord.org/) in order to manage the server process.
