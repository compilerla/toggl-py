"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Last changed: 2024-04-26T22:13:16.785Z
Generated by: https://github.com/compilerla/toggl-py/tree/main/codegen
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class AlertsApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_alerts(self, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Handles DELETE alert requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alerts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_alerts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_alerts_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_alerts_with_http_info(self, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Handles DELETE alert requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alerts_with_http_info(async_req=True)
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method delete_alerts" % key)
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
            "/workspaces/{workspace_id}/alerts/{alert_id}",
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

    def get_alerts(self, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Returns a list of existing alerts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alerts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ModelsAlert]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_alerts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_alerts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_alerts_with_http_info(self, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Returns a list of existing alerts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alerts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ModelsAlert]
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_alerts" % key)
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/alerts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ModelsAlert]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_alerts(self, request, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Handles POST alert requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alerts(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object request: Alert data (required)
        :return: ModelsAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_alerts_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_alerts_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_alerts_with_http_info(self, request, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Handles POST alert requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alerts_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object request: Alert data (required)
        :return: ModelsAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_alerts" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "request" is set
        if self.api_client.client_side_validation and ("request" not in params or params["request"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `post_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "request" in params:
            body_params = params["request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/alerts",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsAlert",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_alerts(self, request, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Handles PUT alert requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_alerts(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object request: Alert data (required)
        :return: ModelsAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_alerts_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.put_alerts_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def put_alerts_with_http_info(self, request, **kwargs):  # noqa: E501
        """Alerts  # noqa: E501

        Handles PUT alert requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_alerts_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object request: Alert data (required)
        :return: ModelsAlert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method put_alerts" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "request" is set
        if self.api_client.client_side_validation and ("request" not in params or params["request"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `put_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "request" in params:
            body_params = params["request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/alerts/{alert_id}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsAlert",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
