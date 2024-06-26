"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class IcalApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ical(self, **kwargs):  # noqa: E501
        """Ical file  # noqa: E501

        Returns ical file with TEs from last 14 days  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ical(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_ical_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ical_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ical_with_http_info(self, **kwargs):  # noqa: E501
        """Ical file  # noqa: E501

        Returns ical file with TEs from last 14 days  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ical_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_ical" % key)
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
        header_params["Accept"] = self.api_client.select_header_accept(["text/calendar"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/ical/workspace_user/{token}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_workspace_ical_reset(self, workspace_id, **kwargs):  # noqa: E501
        """Reset iCal token  # noqa: E501

        Reset the iCal token for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_ical_reset(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_workspace_ical_reset_with_http_info(workspace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_workspace_ical_reset_with_http_info(workspace_id, **kwargs)  # noqa: E501
            return data

    def post_workspace_ical_reset_with_http_info(self, workspace_id, **kwargs):  # noqa: E501
        """Reset iCal token  # noqa: E501

        Reset the iCal token for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_ical_reset_with_http_info(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_workspace_ical_reset" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `post_workspace_ical_reset`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "workspace_id" in params:
            path_params["workspace_id"] = params["workspace_id"]  # noqa: E501

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
            "/workspaces/{workspace_id}/ical/reset",
            "POST",
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

    def post_workspace_ical_toggle(self, workspace_id, **kwargs):  # noqa: E501
        """Toggle the iCal token  # noqa: E501

        Toggle the iCal token on/off for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_ical_toggle(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_workspace_ical_toggle_with_http_info(workspace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_workspace_ical_toggle_with_http_info(workspace_id, **kwargs)  # noqa: E501
            return data

    def post_workspace_ical_toggle_with_http_info(self, workspace_id, **kwargs):  # noqa: E501
        """Toggle the iCal token  # noqa: E501

        Toggle the iCal token on/off for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_ical_toggle_with_http_info(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_workspace_ical_toggle" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `post_workspace_ical_toggle`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "workspace_id" in params:
            path_params["workspace_id"] = params["workspace_id"]  # noqa: E501

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
            "/workspaces/{workspace_id}/ical/toggle",
            "POST",
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
