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


+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| name               | desc                                                                                                                                                           |
|--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dvwa               | dvwa是一个用来进行安全脆弱性鉴定的PHP/MySQL Web应用。                                                                                                          |
| ftp-fake-pass      | 一个真实的FTP弱口令环境。test:123456                                                                                                                           |
| redis-unauth       | 一个未授权的Redis服务。                                                                                                                                        |
| mysql_fake_pass    | 一个弱口令MySQL服务                                                                                                                                            |
| memcached_unauth   | 一个未授权的memcached服务。                                                                                                                                    |
| mongo_unauth       | 一个未授权的MongoDB服务.                                                                                                                                       |
| postgres_fake_pass | 一个未授权的postgres服务.                                                                                                                                      |
| rdp                | 一个开放的rdp服务                                                                                                                                              |
| socks5             | 一个开放的socks5服务。                                                                                                                                         |
| http_proxy         | 一个开放的HTTP代理服务                                                                                                                                         |
| wavsep             | WAVSEP 是一个包含漏洞的web应用程序，目的是帮助测试web应用漏洞扫描器的功能、质量和准确性。                                                                      |
| owasp benchmark    | OWASP benchmark是OWASP组织下的一个开源项目，又叫作OWASP基准测试项目，它是免费且开放的测试套件。 它可以用来评估那些自动化安全扫描工具的速度、覆盖范围和准确性。 |

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

