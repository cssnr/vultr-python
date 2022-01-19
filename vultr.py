import os
import requests
from typing import Optional, Union


class Vultr(object):
    url = 'https://api.vultr.com/v2'

    def __init__(self, api_key: Optional[str] = None):
        """
        :param str api_key: Vultr API Key or VULTR_API_KEY environment variable
        """
        self.api_key = api_key or os.getenv('VULTR_API_KEY')
        self.s = requests.session()
        if self.api_key:
            self.s.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def list_os(self):
        url = f'{self.url}/os'
        return self._get(url).json()['os']

    def list_plans(self, **kwargs):
        url = f'{self.url}/plans'
        return self._get(url, kwargs).json()['plans']

    def list_regions(self):
        url = f'{self.url}/regions'
        return self._get(url).json()['regions']

    def list_instances(self, **kwargs):
        url = f'{self.url}/instances'
        return self._get(url, kwargs).json()['instances']

    def get_instance(self, instance: Union[str, dict]):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}'
        return self._get(url).json()['instance']

    def create_instance(self, region: str, plan: str, **kwargs):
        data = {'region': region, 'plan': plan}
        data.update(kwargs)
        url = f'{self.url}/instances'
        return self._post(url, data).json()['instance']

    def create_instances(self, region: str, plan: str,
                         instances: Optional[int] = 1,
                         hostname_ai: Optional[str] = None,
                         label_ai: Optional[str] = None, **kwargs):
        results = list()
        for i in range(1, instances + 1):
            data = dict()
            if hostname_ai:
                data.update({'hostname': f'{hostname_ai}{i:02}'})
            if label_ai:
                data.update({'label': f'{label_ai}{i:02}'})
            data.update(kwargs)
            try:
                instance = self.create_instance(region, plan, **data)
                results.append(instance)
            except Exception as error:
                results.append(error)
        return results

    def update_instance(self, instance: Union[str, dict], **kwargs):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}'
        return self._patch(url, kwargs).json()['instance']

    def delete_instance(self, instance: Union[str, dict]):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}'
        return self._delete(url)

    def reboot_instance(self, instance: Union[str, dict]):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}/reboot'
        return self._post(url)

    def list_keys(self):
        url = f'{self.url}/ssh-keys'
        return self._get(url).json()['ssh_keys']

    def get_key(self, key: Union[str, dict]):
        key_id = self._get_obj_key(key)
        url = f'{self.url}/ssh-keys/{key_id}'
        return self._get(url).json()['ssh_key']

    def create_key(self, name: str, key: str, **kwargs):
        data = {'name': name, 'ssh_key': key}
        data.update(kwargs)
        url = f'{self.url}/ssh-keys'
        return self._post(url, data).json()['ssh_key']

    def update_key(self, key: Union[str, dict], **kwargs):
        key_id = self._get_obj_key(key)
        url = f'{self.url}/ssh-keys/{key_id}'
        return self._patch(url, kwargs).json()['ssh_key']

    def delete_key(self, key: Union[str, dict]):
        key_id = self._get_obj_key(key)
        url = f'{self.url}/ssh-keys/{key_id}'
        return self._delete(url)

    def list_scripts(self):
        url = f'{self.url}/startup-scripts'
        return self._get(url).json()['startup_scripts']

    def get_script(self, script: Union[str, dict]):
        script_id = self._get_obj_key(script)
        url = f'{self.url}/startup-scripts/{script_id}'
        return self._get(url).json()['startup_script']

    def create_script(self, name: str, script: str, **kwargs):
        data = {'name': name, 'script': script}
        data.update(kwargs)
        url = f'{self.url}/startup-scripts'
        return self._post(url, data).json()['startup_script']

    def update_script(self, script: Union[str, dict], **kwargs):
        script_id = self._get_obj_key(script)
        url = f'{self.url}/startup-scripts/{script_id}'
        return self._patch(url, kwargs).json()['startup_script']

    def delete_script(self, script: Union[str, dict]):
        script_id = self._get_obj_key(script)
        url = f'{self.url}/startup-scripts/{script_id}'
        return self._delete(url)

    def list_ipv4(self, instance: Union[str, dict], **kwargs):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}/ipv4'
        return self._get(url, kwargs).json()['ipv4s']

    def create_ipv4(self, instance: Union[str, dict], **kwargs):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}/ipv4'
        return self._post(url, kwargs).json()['ipv4']

    def delete_ipv4(self, instance: Union[str, dict]):
        instance_id = self._get_obj_key(instance)
        url = f'{self.url}/instances/{instance_id}/ipv4'
        return self._delete(url)

    @staticmethod
    def filter_keys(keys: list, name: str) -> dict:
        try:
            return next(d for d in keys if d['name'].lower() == name.lower())
        except StopIteration:
            return {}

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
    def filter_regions(regions: list, locations: list) -> list:
        return [d for d in regions if d['id'] in locations]

    def _get(self, url, params=None):
        r = self.s.get(url, params=params, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return r

    def _post(self, url, json=None):
        r = self.s.post(url, json=json, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return r

    def _patch(self, url, json=None):
        r = self.s.patch(url, json=json, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return r

    def _delete(self, url):
        r = self.s.delete(url, timeout=10)
        if not r.ok:
            r.raise_for_status()
        return None

    @staticmethod
    def _get_obj_key(obj, key='id'):
        if isinstance(obj, str):
            return obj
        elif isinstance(obj, int):
            return str(obj)
        elif isinstance(obj, dict):
            if key in obj:
                return obj[key]
        else:
            raise ValueError(f'Unable to parse object: {key}')
