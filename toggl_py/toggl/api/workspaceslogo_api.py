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


class WorkspaceslogoApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_workspace_logo(self, workspace_id, **kwargs):  # noqa: E501
        """Get workspace logo  # noqa: E501

        Get the logo for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_logo(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: ModelsLogo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_workspace_logo_with_http_info(workspace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_logo_with_http_info(workspace_id, **kwargs)  # noqa: E501
            return data

    def get_workspace_logo_with_http_info(self, workspace_id, **kwargs):  # noqa: E501
        """Get workspace logo  # noqa: E501

        Get the logo for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_logo_with_http_info(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: ModelsLogo
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_workspace_logo" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_workspace_logo`")  # noqa: E501

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
            "/workspaces/{workspace_id}/logo",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsLogo",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_workspace_logo_0(self, workspace_id, **kwargs):  # noqa: E501
        """Delete workspace logo  # noqa: E501

        Delete the logo for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_logo_0(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: ModelsLogo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_workspace_logo_0_with_http_info(workspace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_logo_0_with_http_info(workspace_id, **kwargs)  # noqa: E501
            return data

    def get_workspace_logo_0_with_http_info(self, workspace_id, **kwargs):  # noqa: E501
        """Delete workspace logo  # noqa: E501

        Delete the logo for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_logo_0_with_http_info(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: ModelsLogo
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_workspace_logo_0" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_workspace_logo_0`")  # noqa: E501

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
            "/workspaces/{workspace_id}/logo",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsLogo",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_workspace_logo(self, workspace_id, **kwargs):  # noqa: E501
        """Post workspace logo  # noqa: E501

        Post the logo for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_logo(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: ModelsLogo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_workspace_logo_with_http_info(workspace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_workspace_logo_with_http_info(workspace_id, **kwargs)  # noqa: E501
            return data

    def post_workspace_logo_with_http_info(self, workspace_id, **kwargs):  # noqa: E501
        """Post workspace logo  # noqa: E501

        Post the logo for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_logo_with_http_info(workspace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :return: ModelsLogo
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_workspace_logo" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_id` when calling `post_workspace_logo`")  # noqa: E501

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
            "/workspaces/{workspace_id}/logo",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsLogo",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
