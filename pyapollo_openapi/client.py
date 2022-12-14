#!/usr/bin/python
# coding=utf-8

# Copyright 2022 Python Apollo OpenApi Client
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# title                     Python Apollo OpenApi Client
# description               functions to call openapi through python
# author                    ikool
# date                      2022-09-22
# reference website         https://www.apolloconfig.com/#/zh/usage/apollo-open-api-platform?id=_32-api%e6%8e%a5%e5%8f%a3%e5%88%97%e8%a1%a8

import logging
from typing import Dict
import requests


class ApiClient(object):
    """
    Python Apollo OpenApi Client
    """

    def __new__(cls, *args, **kwargs):
        """
        singleton model
        """
        kwargs = {x: kwargs[x] for x in sorted(kwargs)}
        key = repr((args, sorted(kwargs)))
        if hasattr(cls, "_instance"):
            if key not in cls._instance:
                cls._instance[key] = super().__new__(cls)
        else:
            cls._instance = {key: super().__new__(cls)}
        return cls._instance[key]

    def __init__(self, host: str, token: str, timeout: int = 3):
        """
        init method
        :param host: with the format 'http://localhost:8070'
        :param env: environment, default value is 'DEV'
        :param timeout: http request timeout seconds, default value is 30 seconds
        """
        self.host = host if host else "http://localhost:8070"
        self.token = token
        self.timeout = timeout

    def _http_get(self, api: str, params: Dict = None) -> requests.Response:
        """
        handle http request with get method
        :param url:
        :param params:
        :return:
        """
        url = f"{self.host}/{api}"
        try:
            return requests.get(
                url=url,
                params=params,
                timeout=self.timeout,
                headers={"Authorization": self.token, "Content-Type": "application/json;charset=UTF-8"},
            )
        except requests.exceptions.ReadTimeout as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False
        except Exception as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False

    def _http_post(self, api: str, data: Dict = None) -> requests.Response:
        """
        handle http request with get method
        :param url:
        :param params:
        :return:
        """
        url = f"{self.host}/{api}"
        try:
            return requests.post(
                url=f"{self.host}/{api}",
                json=data,
                timeout=self.timeout,
                headers={"Authorization": self.token, "Content-Type": "application/json;charset=UTF-8"},
            )
        except requests.exceptions.ReadTimeout as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False
        except Exception as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False

    def _http_put(self, api: str, data: Dict = None) -> requests.Response:
        """
        handle http request with get method
        :param url:
        :param params:
        :return:
        """
        url = f"{self.host}/{api}"
        try:
            return requests.put(
                url=f"{self.host}/{api}",
                json=data,
                timeout=self.timeout,
                headers={"Authorization": self.token, "Content-Type": "application/json;charset=UTF-8"},
            )
        except requests.exceptions.ReadTimeout as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False
        except Exception as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False

    def _http_delete(self, api: str) -> requests.Response:
        """
        handle http request with get method
        :param url:
        :param params:
        :return:
        """
        url = f"{self.host}/{api}"
        try:
            return requests.delete(
                url=f"{self.host}/{api}",
                timeout=self.timeout,
                headers={"Authorization": self.token, "Content-Type": "application/json;charset=UTF-8"},
            )
        except requests.exceptions.ReadTimeout as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False
        except Exception as e:
            logging.error("request url: %s, error:%s" % (url, str(e)))
            return False

    def get_envclusters(self, appid: str):
        """
        ?????????????????????????????????
        :param appid:
        :return:
        """
        api = f"openapi/v1/apps/{appid}/envclusters"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_apps(self):
        """
        ??????APP??????
        :return:
        """
        api = "openapi/v1/apps"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_cluster(self, appid, env="dev", cluster_name="default"):
        """
        ????????????????????????
        :param appid:
        :param env:
        :param cluster_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def create_cluster(self, appid, env, cluster_name, create_by):
        """
        ????????????
        :param appid:
        :param env:
        :param cluster_name:
        :param create_by:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters"
        data = {
            "name": cluster_name,
            "appId": appid,
            "dataChangeCreatedBy": create_by
        }
        resp = self._http_post(api, data)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_namespaces(self, appid, env="dev", cluster_name="default"):
        """
        ?????????????????????Namespace??????
        :param appid:
        :param env:
        :param cluster_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_namespace(self, appid, env="dev", cluster_name="default", namespace_name="application"):
        """
        ????????????Namespace??????
        :param appid:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def create_namespace(self, appid, namespace_name, create_by, format="properties", is_public=False, comment=""):
        """
        ??????Namespace
        :param appid:
        :param namespace_name:
        :param create_by:
        :param format:
        :param is_public:
        :param comment:
        :return:
        """
        api = f"openapi/v1/apps/{appid}/appnamespaces"
        data = {
            "name": namespace_name,
            "appId": appid,
            "format": format,
            "isPublic": is_public,
            "comment": comment,
            "dataChangeCreatedBy": create_by
        }
        resp = self._http_post(api, data)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_namespace_locked_by(self, appid, env="dev", cluster_name="default", namespace_name="application"):
        """
        ????????????Namespace?????????????????????
        :param appid:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/lock"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_item(self, appid, key, env="dev", cluster_name="default", namespace_name="application"):
        """
         ????????????key???????????? (??????????????????????????????????????????????????????????????????????????????)
        :param appid:
        :param key:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/items/{key}"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def created_item(self, appid, key, value, create_by, env="dev", cluster_name="default", namespace_name="application", comment=""):
        """
        ????????????
        :param appid:
        :param key:
        :param value:
        :param create_by:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :param comment:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/items"
        data = {
            "key": key,
            "value": value,
            "comment": comment,
            "dataChangeCreatedBy": create_by
        }
        resp = self._http_post(api, data)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def update_item(self, appid, key, value, create_by, env="dev", cluster_name="default", namespace_name="application", comment=""):
        """
        ????????????
        :param appid:
        :param key:
        :param value:
        :param create_by:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :param comment:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/items/{key}"
        data = {
            "key": key,
            "value": value,
            "comment": comment,
            "dataChangeLastModifiedBy": create_by,
            "dataChangeCreatedBy": create_by
        }
        resp = self._http_put(api, data)
        if resp and resp.status_code == 200:
            return True
        return False

    def delete_item(self, appid, key, operator, env="dev", cluster_name="default", namespace_name="application"):
        """
        ????????????
        :param appid:
        :param key:
        :param operator:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/items/{key}?operator={operator}"
        resp = self._http_delete(api)
        if resp and resp.status_code == 200:
            return True
        return False

    def releases(self, appid, release_title, release_comment, released_by, env="dev", cluster_name="default", namespace_name="application"):
        """
        ????????????
        :param appid:
        :param release_title:
        :param release_comment:
        :param released_by:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/releases"
        data = {
            "releaseTitle": release_title,
            "releaseComment": release_comment,
            "releasedBy": released_by
        }
        resp = self._http_post(api, data)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def get_latest_releases(self, appid, env="dev", cluster_name="default", namespace_name="application"):
        """
        ????????????Namespace??????????????????????????????
        :param appid:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/releases/latest"
        resp = self._http_get(api)
        if resp and resp.status_code == 200:
            return resp.json()
        return False

    def rollback(self, release_id, operator, env="dev"):
        """
        ?????????????????????
        :param release_id:
        :param operator:
        :param env:
        :return:
        """
        api = f"openapi/v1/envs/{env}/releases/{release_id}/rollback?operator={operator}"
        resp = self._http_put(api)
        print(resp.status_code, resp.text)
        if resp and resp.status_code == 200:
            return True
        return False

    def get_latest_releases_by_page(self, appid, page, size, env="dev", cluster_name="default", namespace_name="application"):
        """
        ?????????????????????
        :param appid:
        :param page:
        :param size:
        :param env:
        :param cluster_name:
        :param namespace_name:
        :return:
        """
        api = f"openapi/v1/envs/{env}/apps/{appid}/clusters/{cluster_name}/namespaces/{namespace_name}/items?page={page}&size={size}"
        resp = self._http_get(api)
        print(resp.text)
        if resp and resp.status_code == 200:
            return resp.json()
        return False
