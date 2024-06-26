"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class WorkspacesreportssharedApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_delete_saved_report_resource(self, workspace_id, input_data, **kwargs):  # noqa: E501
        """SavedReport  # noqa: E501

        Bulk delete saved report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_delete_saved_report_resource(workspace_id, input_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace. (required)
        :param SharedBulkDeleteInputData input_data: Input data (required)
        :return: list[ModelsSavedReport]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bulk_delete_saved_report_resource_with_http_info(workspace_id, input_data, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_delete_saved_report_resource_with_http_info(workspace_id, input_data, **kwargs)  # noqa: E501
            return data

    def bulk_delete_saved_report_resource_with_http_info(self, workspace_id, input_data, **kwargs):  # noqa: E501
        """SavedReport  # noqa: E501

        Bulk delete saved report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_delete_saved_report_resource_with_http_info(workspace_id, input_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace. (required)
        :param SharedBulkDeleteInputData input_data: Input data (required)
        :return: list[ModelsSavedReport]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "input_data"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method bulk_delete_saved_report_resource" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `bulk_delete_saved_report_resource`"
            )  # noqa: E501
        # verify the required parameter "input_data" is set
        if self.api_client.client_side_validation and (
            "input_data" not in params or params["input_data"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `input_data` when calling `bulk_delete_saved_report_resource`"
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
        if "input_data" in params:
            body_params = params["input_data"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/reports/shared/bulk_delete",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ModelsSavedReport]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
