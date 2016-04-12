======
maruko
======

| Maruko is malware crawler inspired by 'ちびまる子ちゃん'

| This script crawl following sources.

- Malware Domain List: http://www.malwaredomainlist.com/hostslist/mdl.xml
- VX Vault: http://vxvault.siri-urz.net/URL_List.php
- Malc0de: http://malc0de.com/rss

Installation
============

------------
Dependencies
------------

| Maruko use python-magic module. `python-magic <https://github.com/ahupp/python-magic>`_ is a python interface to the libmagic file type identification library. It is dependent on libmagic. You need to install *libmagic* before you install maruko.

| On OSX:

- When using Homebrew: `brew install libmagic`
- When using macports: `port install file`


----
PyPI
----
The recommended process is to install the PyPI package, as it allows easily staying update.

::

    $ pip install maruko

------
github
------
| Download from https://github.com/tkmru/maruko/.
| Let's push star!!

::

    $ git clone git@github.com:tkmru/maruko.git
    $ cd maruko
    $ python setup.py install

Usage
=====

| Downloaded malware is stored in */opt/malware/unsorted/* by default.

::

    $ sudo maruko


| '-p' change stored path.

::

    $ sudo maruko -p <path>


License
=======

| "THE BEER-WARE LICENSE"
| If we meet some day, and you think
| this stuff is worth it, you can buy me a beer in return.
