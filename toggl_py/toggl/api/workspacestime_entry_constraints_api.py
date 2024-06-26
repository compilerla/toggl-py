"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class WorkspacestimeEntryConstraintsApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_workspace_time_entry_constraints(self, workspace_id, time_entry_constraints, **kwargs):  # noqa: E501
        """Post workspace time entry constraints  # noqa: E501

        Post the time entry constraints for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_time_entry_constraints(workspace_id, time_entry_constraints, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :param ModelsTimeEntryConstraints time_entry_constraints: Input data of the time entry constraints. (required)
        :return: WorkspacesJSONResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_workspace_time_entry_constraints_with_http_info(
                workspace_id, time_entry_constraints, **kwargs
            )  # noqa: E501
        else:
            (data) = self.post_workspace_time_entry_constraints_with_http_info(
                workspace_id, time_entry_constraints, **kwargs
            )  # noqa: E501
            return data

    def post_workspace_time_entry_constraints_with_http_info(
        self, workspace_id, time_entry_constraints, **kwargs
    ):  # noqa: E501
        """Post workspace time entry constraints  # noqa: E501

        Post the time entry constraints for a given workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_time_entry_constraints_with_http_info(workspace_id, time_entry_constraints, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :param ModelsTimeEntryConstraints time_entry_constraints: Input data of the time entry constraints. (required)
        :return: WorkspacesJSONResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "time_entry_constraints"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method post_workspace_time_entry_constraints" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `post_workspace_time_entry_constraints`"
            )  # noqa: E501
        # verify the required parameter "time_entry_constraints" is set
        if self.api_client.client_side_validation and (
            "time_entry_constraints" not in params or params["time_entry_constraints"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `time_entry_constraints` when calling `post_workspace_time_entry_constraints`"
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
        if "time_entry_constraints" in params:
            body_params = params["time_entry_constraints"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/time_entry_constraints",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="WorkspacesJSONResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
