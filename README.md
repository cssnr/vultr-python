[![Discord](https://img.shields.io/discord/899171661457293343?color=7289da&label=discord&logo=discord&logoColor=white&style=flat)](https://discord.gg/wXy6m2X8wY)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9b356c4327df41e395c81de1c717ce11)](https://www.codacy.com/gh/cssnr/vultr-python/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cssnr/vultr-python&amp;utm_campaign=Badge_Grade)
[![](https://repository-images.githubusercontent.com/441314848/513fb2f4-39cb-4bbc-8d47-a2cde9ccbd65)](https://www.vultr.com/?ref=6905748)
# Vultr Python

Python wrapper for the Vultr API.

*   [https://www.vultr.com](https://www.vultr.com/?ref=6905748)
*   [https://www.vultr.com/api](https://www.vultr.com/api/?ref=6905748)

This is currently a WIP and not complete, but has some functions. Feel free to request additional functions in [Discord](https://discord.gg/wXy6m2X8wY).

## Examples

You will need to create a token and whitelist your IP address.
Most functions do not work without an API Token.

*   [https://my.vultr.com/settings/#settingsapi](https://my.vultr.com/settings/#settingsapi)

Initialize the class with your API Token
```python
from vultr import Vultr

vultr = Vultr('XXXXXXXXXX')
```
List plans and get available regions for that plan
```python
plans = vultr.list_plans()
plan = plans[0]  # 0 seems to be the basic 5 dollar plan
regions = vultr.list_regions()
available = vultr.filter_regions(regions, plan['locations'])
```
Get the OS list and filter by name
```python
os_list = vultr.list_os()
ubuntu_lts = vultr.filter_os(os_list, 'Ubuntu 20.04 x64')
```
Create a new ssh key from key string
```python
sshkey = vultr.create_key('shane-secure-102916', 'ssh-rsa AAAA...')
```
Create a new instance
```python
hostname = 'my-new-host'
data = {
    'region': available[0]['id'],
    'plan': plan['id'],
    'os_id': ubuntu_lts['id'],
    'sshkey_id': sshkey['id'],
    'hostname': hostname,
    'label': hostname,
}
instance = vultr.create_instance(**data)
```

View the full documentation here: [https://www.vultr.com/api](https://www.vultr.com/api/?ref=6905748)
