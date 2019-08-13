# vulnvps
This repo makes your vps vulnerable. Helpful in av scan engine testing.
 
Tested on python3.6 on ubuntu. 

## Flow
![https://i.loli.net/2019/08/13/2CufAOmplhTXt7j.jpg](https://i.loli.net/2019/08/13/2CufAOmplhTXt7j.jpg)

## Vul support now

| port  | vuln desc                                 | Link                                                         |
| ----- | ----------------------------------------- | ------------------------------------------------------------ |
| 2222  | ssh fake password. Login: `root` `root`   |                                                              |
| 9200  | dvwa fake web applation.                  | [http://www.dvwa.co.uk/](http://www.dvwa.co.uk/)             |
| 9201  | SQLInjLib                                 | [https://github.com/Audi-1/sqli-labs](https://github.com/Audi-1/sqli-labs) |
| 11211 | MemcachedUnAuth                           |                                                              |
| 3306  | mysql fake password. Login: `root` `root` |                                                              |
| 6379  | Redis unauth.                             |                                                              |
| 21    | ftp fake password. Login: `test` `123456` |                                                              |

(waiting for you pull request to support more vuls!)

## pre requirements
This repo assume a local docker is running and is reachable.
eg: run `docker search hello` you can get some output.

## usage
1. install docker.
2. run `docker search hello` to see is docker works well.
3. install requirements. `pip install -r requirements.txt`. (virtualenv is advised.)
4. `python vuls.py` Rock and roll.

This scripts only tested on my own vps.
Issue and pr are very welcome! 

