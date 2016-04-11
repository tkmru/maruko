======
maruko
======

| Maruko is malware crawler inspired by 'ちびまる子ちゃん'

| This script crawl following sources.

- Malware Domain List: http://www.malwaredomainlist.com/hostslist/mdl.xml
- VX Vault: http://vxvault.siri-urz.net/URL_List.php
- Malc0de: http://malc0de.com/rss

Usage
=====

| Downloaded malware is stored in *'/opt/malware/unsorted/'* by default.

::

    $ sudo python maruko.py


| '-p' change stored path.

::

    $ sudo python maruko.py -p <path>


License
=======

| "THE BEER-WARE LICENSE" 
| If we meet some day, and you think
| this stuff is worth it, you can buy me a beer in return.
