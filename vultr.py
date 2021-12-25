import requests
from typing import Optional, Union


class Vultr(object):
    url = 'https://api.vultr.com/v2'

    def __init__(self, api_token: Optional[str] = None):
        """
        :param str api_token: Vultr API Token
        """
        self.token = api_token
        self.s = requests.session()
        if api_token:
            self.s.headers.update({'Authorization': f'Bearer {api_token}'})

    def list_regions(self):
        url = f'{self.url}/regions'
        return self._get(url)['regions']

    def list_plans(self):
        url = f'{self.url}/plans'
        return self._get(url)['plans']

    def list_os(self):
        url = f'{self.url}/os'
        return self._get(url)['os']

    def list_scripts(self):
        url = f'{self.url}/startup-scripts'
        return self._get(url)['startup_scripts']

    def get_script(self, script: Union[str, dict]):
        script_id = self._get_object_value(script)
        url = f'{self.url}/startup-scripts/{script_id}'
        return self._get(url)['startup_script']

    def create_script(self, name: str, script: str, **kwargs):
        url = f'{self.url}/startup-scripts'
        data = {'name': name, 'script': script}
        data.update(kwargs)
        return self._post(url, data)['startup_script']

    def update_script(self, script: Union[str, dict], **kwargs):
        script_id = self._get_object_value(script)
        url = f'{self.url}/startup-scripts/{script_id}'
        return self._patch(url, kwargs)['startup_script']

    def delete_script(self, script: Union[str, dict]):
        script_id = self._get_object_value(script)
        url = f'{self.url}/startup-scripts/{script_id}'
        return self._delete(url)

    def list_keys(self):
        url = f'{self.url}/ssh-keys'
        return self._get(url)['ssh_keys']

    def get_key(self, key: Union[str, dict]):
        key_id = self._get_object_value(key)
        url = f'{self.url}/ssh-keys/{key_id}'
        return self._get(url)['ssh_key']

    def update_key(self, key: Union[str, dict], **kwargs):
        key_id = self._get_object_value(key)
        url = f'{self.url}/ssh-keys/{key_id}'
        return self._patch(url, kwargs)['ssh_key']

    def create_key(self, name: str, key: str, **kwargs):
        url = f'{self.url}/ssh-keys'
        data = {'name': name, 'ssh_key': key}
        data.update(kwargs)
        return self._post(url, data)['ssh_key']

    def delete_key(self, key: Union[str, dict]):
        key_id = self._get_object_value(key)
        url = f'{self.url}/ssh-keys/{key_id}'
        return self._delete(url)

    def list_instances(self):
        url = f'{self.url}/instances'
        return self._get(url)['instances']

    def get_instance(self, instance: Union[str, dict]):
        instance_id = self._get_object_value(instance)
        url = f'{self.url}/instances/{instance_id}'
        return self._get(url)['instance']

    def create_instance(self, region: str, plan: str, **kwargs):
        url = f'{self.url}/instances'
        data = {'region': region, 'plan': plan}
        data.update(kwargs)
        return self._post(url, data)['instance']

    def update_instance(self, instance: Union[str, dict], **kwargs):
        instance_id = self._get_object_value(instance)
        url = f'{self.url}/instances/{instance_id}'
        return self._patch(url, kwargs)['instance']

    def delete_instance(self, instance: Union[str, dict]):
        instance_id = self._get_object_value(instance)
        url = f'{self.url}/instances/{instance_id}'
        return self._delete(url)

    @staticmethod
    def filter_regions(regions: list, locations: list) -> list:
        return [d for d in regions if d['id'] in locations]

    @staticmethod
    def filter_os(os_list: list, name: str) -> dict:
        try:
            return next(d for d in os_list if d['name'].lower() == name.lower())
        except StopIteration:
            return {}

    @staticmethod
    def filter_scripts(scripts: list, name: str) -> dict:
        try:
            return next(d for d in scripts if d['name'].lower() == name.lower())
        except StopIteration:
            return {}

    @staticmethod
    def filter_keys(keys: list, name: str) -> dict:
        try:
            return next(d for d in keys if d['name'].lower() == name.lower())
        except StopIteration:
            return {}

    def _get(self, url):
        r = self.s.get(url, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return r.json()

    def _post(self, url, data):
        r = self.s.post(url, json=data, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return r.json()

    def _patch(self, url, data):
        r = self.s.patch(url, json=data, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return r.json()

    def _delete(self, url):
        r = self.s.delete(url, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return None

    @staticmethod
    def _get_object_value(obj, value='id'):
        if isinstance(obj, str):
            return obj
        elif isinstance(obj, int):
            return str(obj)
        elif isinstance(obj, dict):
            if value in obj:
                return obj[value]
        else:
            raise ValueError(f'Unable to parse object: {value}')
