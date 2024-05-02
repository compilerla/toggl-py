"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient
from toggl.models.models_avatar import ModelsAvatar  # noqa: F401


class AvatarsApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_avatars(self, **kwargs) -> str:  # noqa: E501
        """Avatars  # noqa: E501

        Handles DELETE avatar requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_avatars(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_avatars_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_avatars_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_avatars_with_http_info(self, **kwargs) -> str:  # noqa: E501
        """Avatars  # noqa: E501

        Handles DELETE avatar requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_avatars_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method delete_avatars" % key)
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/avatars",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="str",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_avatars(self, file: str, **kwargs) -> ModelsAvatar:  # noqa: E501
        """Avatars  # noqa: E501

        Handles POST avatar requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_avatars(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: file form data (required)
        :return: ModelsAvatar
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_avatars_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.post_avatars_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def post_avatars_with_http_info(self, file: str, **kwargs) -> ModelsAvatar:  # noqa: E501
        """Avatars  # noqa: E501

        Handles POST avatar requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_avatars_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: file form data (required)
        :return: ModelsAvatar
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["file"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_avatars" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "file" is set
        if self.api_client.client_side_validation and ("file" not in params or params["file"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `post_avatars`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "file" in params:
            form_params.append(("file", params["file"]))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/avatars",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsAvatar",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_use_gravatar(self, **kwargs) -> ModelsAvatar:  # noqa: E501
        """UseGravatar  # noqa: E501

        Change user avatar to gravatar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_use_gravatar(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ModelsAvatar
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_use_gravatar_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_use_gravatar_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_use_gravatar_with_http_info(self, **kwargs) -> ModelsAvatar:  # noqa: E501
        """UseGravatar  # noqa: E501

        Change user avatar to gravatar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_use_gravatar_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ModelsAvatar
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_use_gravatar" % key)
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/avatars/use_gravatar",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsAvatar",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
