# vulnvps
This repo makes your vps vulnerable. Helpful in av scan engine testing.
 
Tested on python3.6 on ubuntu. 

## Flow
![https://i.loli.net/2019/08/13/2CufAOmplhTXt7j.jpg](https://i.loli.net/2019/08/13/2CufAOmplhTXt7j.jpg)

## Vul support now

| name               | image                     | ports                | ttl        | desc                                                                                      |
|--------------------|---------------------------|----------------------|------------|-------------------------------------------------------------------------------------------|
| dvwa               | imfht/dvwa-nologin:latest | ['80/tcp']           | 144000 min | dvwa是一个用来进行安全脆弱性鉴定的PHP/MySQL Web应用。                                     |
| ftp-fake-pass      | fauria/vsftpd:latest      | ['21/tcp', '20/tcp'] | 60 min     | 一个真实的FTP弱口令环境。test:123456                                                      |
| redis-unauth       | redis:latest              | ['6379/tcp']         | 10 min     | 一个未授权的Redis服务。                                                                   |
| mysql_fake_pass    | mysql:5                   | ['3306']             | 10 min     | 一个弱口令MySQL服务                                                                       |
| memcached_unauth   | memcached:latest          | ['11211']            | 60 min     | 一个未授权的memcached服务。                                                               |
| mongo_unauth       | mongo:3                   | ['27017/tcp']        | 60 min     | 一个未授权的MongoDB服务.                                                                  |
| postgres_fake_pass | postgres:9                | ['5432']             | 60 min     | 一个未授权的postgres服务.                                                                 |
| rdp                | dtagdevsec/rdpy:1903      | ['3389/tcp']         | 60 min     | 一个开放的rdp服务                                                                         |
| socks5             | serjs/go-socks5-proxy     | ['1080']             | 1440 min   | 一个开放的socks5服务。                                                                    |
| http_proxy         | sameersbn/squid:3.5.27-2  | ['3128']             | 1440 min   | 一个开放的HTTP代理服务                                                                    |
| wavsep             | imfht/wavsep              | ['8080/tcp']         | 1440 min   | WAVSEP 是一个包含漏洞的web应用程序，目的是帮助测试web应用漏洞扫描器的功能、质量和准确性。 |
| owasp benchmark    | owasp/benchmark           | ['8080/tcp']         | 1440 min   | OWASP benchmark是OWASP组织用来评估那些自动化安全扫描工具的速度、覆盖范围和准确性          |

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

