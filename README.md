[![Discord](https://img.shields.io/discord/899171661457293343?color=7289da&label=discord&logo=discord&logoColor=white&style=flat)](https://discord.gg/wXy6m2X8wY)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9b356c4327df41e395c81de1c717ce11)](https://app.codacy.com/gh/cssnr/vultr-python/dashboard)
[![PyPI](https://img.shields.io/pypi/v/vultr-python)](https://pypi.org/project/vultr-python/)
[![](https://repository-images.githubusercontent.com/441314848/513fb2f4-39cb-4bbc-8d47-a2cde9ccbd65)](https://www.vultr.com/?ref=6905748)
# Vultr Python

Python 3 wrapper for the Vultr API v2.

*   Vultr: [https://www.vultr.com](https://www.vultr.com/?ref=6905748)
*   Vultr API: [https://www.vultr.com/api](https://www.vultr.com/api/?ref=6905748)
*   Vultr Python Docs: [https://vultr-python.sapps.me](https://vultr-python.sapps.me/)

This is currently a WIP and not complete, but has some useful functions.
Feel free to request additional functions and more on [Discord](https://discord.gg/wXy6m2X8wY).

## Install

From PyPi using pip:
```text
python -m pip install vultr-python
```

From Source using setuptools:
```text
git clone https://github.com/cssnr/vultr-python.git
cd vultr-python
python setup.py install
```

## Usage

You will need to create an api key and whitelist your IP address.
Most functions do not work without an API Key.

*   [https://my.vultr.com/settings/#settingsapi](https://my.vultr.com/settings/#settingsapi)

Initialize the class with your API Key or with the `VULTR_API_KEY` environment variable.
```python
from vultr import Vultr

vultr = Vultr('VULTR_API_KEY')
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
sshkey = vultr.create_key('key-name', 'ssh-rsa AAAA...')
```
Create a new instance
```python
hostname = 'my-new-host'
data = {
    'region': available[0]['id'],
    'plan': plan['id'],
    'os_id': ubuntu_lts['id'],
    'sshkey_id': [sshkey['id']],
    'hostname': hostname,
    'label': hostname,
}
instance = vultr.create_instance(**data)
```

View all functions at the Doc site: [https://vultr-python.sapps.me](https://vultr-python.sapps.me/)

View the full API documentation at Vultr: [https://www.vultr.com/api](https://www.vultr.com/api/?ref=6905748)

If you have more questions, concerns, or comments? Join our [Discord](https://discord.gg/wXy6m2X8wY) for more information...
