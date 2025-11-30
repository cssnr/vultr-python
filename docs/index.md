[![PyPI Version](https://img.shields.io/pypi/v/vultr-python?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/vultr-python/)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fvultr-python%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/vultr-python?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/vultr-python?logo=pypi&logoColor=white)](https://pypistats.org/packages/vultr-python)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/vultr-python?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/vultr-python)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9b356c4327df41e395c81de1c717ce11)](https://app.codacy.com/gh/cssnr/vultr-python/dashboard)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_vultr-python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_vultr-python)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/vultr-python?logo=github)](https://github.com/cssnr/vultr-python/issues)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/vultr-python?logo=github)](https://github.com/cssnr/vultr-python/graphs/contributors)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/vultr-python?logo=github)](https://github.com/cssnr/vultr-python/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/vultr-python?style=flat&logo=github)](https://github.com/cssnr/vultr-python/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/vultr-python?style=flat&logo=github)](https://github.com/cssnr/vultr-python/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

Python 3 wrapper for the [Vultr](https://www.vultr.com/?ref=6905748) API v2.

[![GitHub](https://img.shields.io/badge/github-232925?style=for-the-badge&logo=github)](https://github.com/cssnr/vultr-python?tab=readme-ov-file#readme)
[![PyPi](https://img.shields.io/badge/pypi-006dad?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/vultr-python)
[![Docs](https://img.shields.io/badge/docs-198754?style=for-the-badge&logo=mdbook)](#Vultr)
[![Vultr](https://img.shields.io/badge/vultr-007bfc?style=for-the-badge&logo=vultr)](https://www.vultr.com/api/?ref=6905748)

[⬇️ Jump to the API Documentation](#Vultr)

## Install

From PyPi: <https://pypi.org/project/vultr-python>

```text
python -m pip install vultr-python
```

From Source:

```text
git clone https://github.com/cssnr/vultr-python.git
python -m pip install vultr-python
```

## Usage

You will need to create an api key and whitelist your IP address for most functions.

- [https://my.vultr.com/settings/#settingsapi](https://my.vultr.com/settings/#settingsapi)

Initialize the `Vultr` class with your API Key or use the `VULTR_API_KEY` environment variable.

```python
from vultr import Vultr

vultr = Vultr('VULTR_API_KEY')
```

List plans and get available regions for that plan

```python
plans = vultr.list_plans({'type': 'vc2'})  # Filter by type
plan = plans[0]  # 0 seems to be the base plan
regions = vultr.list_regions()
available = vultr.filter_regions(regions, plan['locations'])
```

Get the OS list and filter by name

```python
os_list = vultr.list_os()
ubuntu_lts = vultr.filter_os(os_list, 'Ubuntu 24.04 LTS x64')
```

Create a new ssh key from key string

```python
sshkey = vultr.create_key('key-name', 'ssh-rsa AAAA...')
```

Create a new instance

```python
data = {
    'os_id': ubuntu_lts['id'],
    'sshkey_id': [sshkey['id']],
    'hostname': 'my-new-host',
    'label': 'my-new-host',
}
instance = vultr.create_instance(available[0], plan, **data)
```

Arbitrary Methods [get](#Vultr.get), [post](#Vultr.post), [patch](#Vultr.patch), [put](#Vultr.put), [delete](#Vultr.delete)

```python
plans = vultr.get('plans', {'type': 'vc2'})
sshkey = vultr.post('ssh-keys', name='key-name', ssh_key='ssh-rsa AAAA...')
instance = vultr.patch('instances', plan=plans[1]['id'])
instance = vultr.patch('blocks/{block-id}', plan=plans[1]['id'])
vultr.delete("instances/{instance-id}")
```

Error Handling

```python
>>> instance = vultr.create_instance("atl", "vc2-1c-0.5gb-v6", **data)
Traceback (most recent call last):
vultr.vultr.VultrException: Error 400: Server add failed: Ubuntu 24.04 LTS x64 requires a plan with at least 1000 MB memory.
```

Using the `VultrException` class

```python
from vultr import VultrException

try:
    instance = vultr.create_instance("atl", "vc2-1c-0.5gb-v6", os_id=2284)
except VultrException as error:
    print(error.error)
    # 'Server add failed: Ubuntu 24.04 LTS x64 requires a plan with at least 1000 MB memory.'
    print(error.status)
    # 400
```

&nbsp;

Vultr API Reference: [https://www.vultr.com/api](https://www.vultr.com/api/?ref=6905748)

---

<p style="font-size: 2em; font-weight: 300;">API Documentation</p>
