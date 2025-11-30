import os
import warnings
from typing import Any, List, Optional, Union

import requests


class Vultr(object):
    url = "https://api.vultr.com/v2"

    def __init__(self, api_key: Optional[str] = None):
        """:param api_key: Vultr API Key or `VULTR_API_KEY` Environment Variable"""
        self.api_key = api_key or os.getenv("VULTR_API_KEY")
        """Provide the API key here or with the `VULTR_API_KEY` environment variable"""
        self._session = requests.session()
        if self.api_key:
            self._session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get(self, url: str, params: Optional[dict] = None) -> Any:
        """
        GET Data
        :param url: Request URL. Example `/instances`
        :param params: Query Parameters Dictionary
        :return: Response Data
        :raises: `VultrException`
        """
        return self._req("get", f"{self.url}/{url.lstrip('/')}", params)

    def post(self, url: str, **kwargs) -> Any:
        """
        POST Data
        :param url: Request URL. Example `/instances`
        :param kwargs: Request Data Keyword Arguments
        :return: Response Data
        :raises: `VultrException`
        """
        return self._req("post", f"{self.url}/{url.lstrip('/')}", kwargs)

    def patch(self, url: str, **kwargs) -> Any:
        """
        PATCH Data
        :param url: Request URL. Example `/instances/{instance-id}`
        :param kwargs: Request Data Keyword Arguments
        :return: Response Data
        :raises: `VultrException`
        """
        return self._req("patch", f"{self.url}/{url.lstrip('/')}", kwargs)

    def put(self, url: str, **kwargs) -> Any:
        """
        PUT Data
        :param url: Request URL. Example `/instances/{instance-id}`
        :param kwargs: Request Data Keyword Arguments
        :return: Response Data
        :raises: `VultrException`
        """
        return self._req("put", f"{self.url}/{url.lstrip('/')}", kwargs)

    def delete(self, url: str) -> None:
        """
        DELETE a Resource
        :param url: Request URL. Example `/instances/{instance-id}`
        :return: None
        :raises: `VultrException`
        """
        return self._req("delete", f"{self.url}/{url.lstrip('/')}")

    def list_os(self, params: Optional[dict] = None) -> list:
        url = f"{self.url}/os"
        return self._req("get", url, params)["os"]

    def list_plans(self, params: Optional[dict] = None) -> list:
        url = f"{self.url}/plans"
        return self._req("get", url, params)["plans"]

    def list_regions(self, params: Optional[dict] = None) -> list:
        url = f"{self.url}/regions"
        return self._req("get", url, params)["regions"]

    def list_instances(self, params: Optional[dict] = None) -> list:
        url = f"{self.url}/instances"
        return self._req("get", url, params)["instances"]

    def get_instance(self, instance: Union[str, dict], params: Optional[dict] = None) -> dict:
        instance_id = self._get_obj_key(instance)
        url = f"{self.url}/instances/{instance_id}"
        return self._req("get", url, params)["instance"]

    def create_instance(self, region: Union[str, dict], plan: Union[str, dict], **kwargs) -> dict:
        data = {"region": self._get_obj_key(region), "plan": self._get_obj_key(plan)}
        data.update(kwargs)
        url = f"{self.url}/instances"
        return self._req("post", url, data)["instance"]

    def update_instance(self, instance: Union[str, dict], **kwargs) -> dict:
        instance_id = self._get_obj_key(instance)
        url = f"{self.url}/instances/{instance_id}"
        return self._req("patch", url, kwargs)["instance"]

    def delete_instance(self, instance: Union[str, dict]) -> None:
        instance_id = self._get_obj_key(instance)
        url = f"{self.url}/instances/{instance_id}"
        return self._req("delete", url)

    def list_keys(self, params: Optional[dict] = None) -> list:
        url = f"{self.url}/ssh-keys"
        return self._req("get", url, params)["ssh_keys"]

    def get_key(self, key: Union[str, dict], params: Optional[dict] = None) -> dict:
        key_id = self._get_obj_key(key)
        url = f"{self.url}/ssh-keys/{key_id}"
        return self._req("get", url, params)["ssh_key"]

    def create_key(self, name: str, key: str, **kwargs) -> dict:
        data = {"name": name, "ssh_key": key}
        data.update(kwargs)
        url = f"{self.url}/ssh-keys"
        return self._req("post", url, data)["ssh_key"]

    def update_key(self, key: Union[str, dict], **kwargs) -> None:
        key_id = self._get_obj_key(key)
        url = f"{self.url}/ssh-keys/{key_id}"
        return self._req("patch", url, kwargs)["ssh_key"]

    def delete_key(self, key: Union[str, dict]) -> None:
        key_id = self._get_obj_key(key)
        url = f"{self.url}/ssh-keys/{key_id}"
        return self._req("delete", url)

    def list_scripts(self, params: Optional[dict] = None) -> list:
        url = f"{self.url}/startup-scripts"
        return self._req("get", url, params)["startup_scripts"]

    def get_script(self, script: Union[str, dict], params: Optional[dict] = None) -> dict:
        script_id = self._get_obj_key(script)
        url = f"{self.url}/startup-scripts/{script_id}"
        return self._req("get", url, params)["startup_script"]

    def create_script(self, name: str, script: str, **kwargs) -> dict:
        data = {"name": name, "script": script}
        data.update(kwargs)
        url = f"{self.url}/startup-scripts"
        return self._req("post", url, data)["startup_script"]

    def update_script(self, script: Union[str, dict], **kwargs) -> None:
        script_id = self._get_obj_key(script)
        url = f"{self.url}/startup-scripts/{script_id}"
        return self._req("patch", url, kwargs)["startup_script"]

    def delete_script(self, script: Union[str, dict]) -> None:
        script_id = self._get_obj_key(script)
        url = f"{self.url}/startup-scripts/{script_id}"
        return self._req("delete", url)

    def list_ipv4(self, instance: Union[str, dict], params: Optional[dict] = None) -> list:
        instance_id = self._get_obj_key(instance)
        url = f"{self.url}/instances/{instance_id}/ipv4"
        return self._req("get", url, params)["ipv4s"]

    def create_ipv4(self, instance: Union[str, dict], **kwargs) -> dict:
        instance_id = self._get_obj_key(instance)
        url = f"{self.url}/instances/{instance_id}/ipv4"
        return self._req("post", url, kwargs)["ipv4"]

    def delete_ipv4(self, instance: Union[str, dict]) -> None:
        instance_id = self._get_obj_key(instance)
        url = f"{self.url}/instances/{instance_id}/ipv4"
        return self._req("delete", url)

    @staticmethod
    def filter_list(item_list: List[dict], value: str, key: str = "name") -> dict:
        """
        Helper Function to get an Item from a List of Dictionaries
        :param item_list: List to filter
        :param value: Value of the Key
        :param key: Key to check for Value
        :return: Item or {}
        """
        return next((d for d in item_list if str(d.get(key, "")).lower() == value.lower()), {})

    @staticmethod
    def filter_regions(regions: list, locations: list) -> list:
        return [d for d in regions if d["id"] in locations]

    @staticmethod
    def filter_keys(keys: list, name: str) -> dict:
        """Soft Deprecated in 0.2.0. Use `Vultr.filter_list()`"""
        warnings.warn("Soft Deprecated in 0.2.0. Use filter_list()", PendingDeprecationWarning, stacklevel=2)
        try:
            return next(d for d in keys if d["name"].lower() == name.lower())
        except StopIteration:
            return {}

    @staticmethod
    def filter_os(os_list: list, name: str) -> dict:
        """Soft Deprecated in 0.2.0. Use `Vultr.filter_list()`"""
        warnings.warn("Soft Deprecated in 0.2.0. Use filter_list()", PendingDeprecationWarning, stacklevel=2)
        try:
            return next(d for d in os_list if d["name"].lower() == name.lower())
        except StopIteration:
            return {}

    @staticmethod
    def filter_scripts(scripts: list, name: str) -> dict:
        """Soft Deprecated in 0.2.0. Use `Vultr.filter_list()`"""
        warnings.warn("Soft Deprecated in 0.2.0. Use filter_list()", PendingDeprecationWarning, stacklevel=2)
        try:
            return next(d for d in scripts if d["name"].lower() == name.lower())
        except StopIteration:
            return {}

    def _req(self, method, url, params: Optional[dict] = None) -> Any:
        r = self._session.request(method, url, params=params, timeout=10)
        if not r.ok:
            raise VultrException(r)
        if r.status_code == 204:
            return None
        if r.headers.get("content-type") == "application/json":
            return r.json()
        return r.text

    @staticmethod
    def _get_obj_key(obj, key="id"):
        if isinstance(obj, str):
            return obj
        elif isinstance(obj, int):
            return str(obj)
        elif isinstance(obj, dict):
            if key in obj:
                return obj[key]
        else:
            raise ValueError(f"Unable to parse object: {key}")


class VultrException(Exception):
    """Exception class for all Vultr error responses."""

    def __init__(self, response: requests.Response):
        try:
            data = response.json()
            error = data.get("error", response.text)
        except ValueError:
            error = response.text
        status = response.status_code
        self.error: str = error
        """Error Message for 400 Codes"""
        self.status: int = status
        """Response Status Code"""
        super().__init__(f"Error {self.status}: {self.error}")
