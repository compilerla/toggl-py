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


class WeeklyReportsApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post(
        self, workspace_id, weekly_export_post, **kwargs
    ):  # noqa: E501
        """Export weekly report  # noqa: E501

        Downloads weekly report in csv format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post(workspace_id, weekly_export_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param WeeklyExportPost weekly_export_post: Weekly report conditions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post_with_http_info(
                workspace_id, weekly_export_post, **kwargs
            )  # noqa: E501
        else:
            (data) = self.reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post_with_http_info(
                workspace_id, weekly_export_post, **kwargs
            )  # noqa: E501
            return data

    def reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post_with_http_info(
        self, workspace_id, weekly_export_post, **kwargs
    ):  # noqa: E501
        """Export weekly report  # noqa: E501

        Downloads weekly report in csv format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post_with_http_info(workspace_id, weekly_export_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param WeeklyExportPost weekly_export_post: Weekly report conditions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "weekly_export_post"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post`"
            )  # noqa: E501
        # verify the required parameter "weekly_export_post" is set
        if self.api_client.client_side_validation and (
            "weekly_export_post" not in params or params["weekly_export_post"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `weekly_export_post` when calling `reports_api_v3_workspace_workspace_id_weekly_time_entries_csv_post`"
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
        if "weekly_export_post" in params:
            body_params = params["weekly_export_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["text/csv"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/workspace/{workspace_id}/weekly/time_entries.csv",
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

    def reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post(
        self, workspace_id, weekly_export_pdf_post, **kwargs
    ):  # noqa: E501
        """Export weekly report  # noqa: E501

        Downloads weekly report in pdf format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post(workspace_id, weekly_export_pdf_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param WeeklyExportPDFPost weekly_export_pdf_post: Weekly report conditions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post_with_http_info(
                workspace_id, weekly_export_pdf_post, **kwargs
            )  # noqa: E501
        else:
            (data) = self.reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post_with_http_info(
                workspace_id, weekly_export_pdf_post, **kwargs
            )  # noqa: E501
            return data

    def reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post_with_http_info(
        self, workspace_id, weekly_export_pdf_post, **kwargs
    ):  # noqa: E501
        """Export weekly report  # noqa: E501

        Downloads weekly report in pdf format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post_with_http_info(workspace_id, weekly_export_pdf_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param WeeklyExportPDFPost weekly_export_pdf_post: Weekly report conditions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "weekly_export_pdf_post"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post`"
            )  # noqa: E501
        # verify the required parameter "weekly_export_pdf_post" is set
        if self.api_client.client_side_validation and (
            "weekly_export_pdf_post" not in params or params["weekly_export_pdf_post"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `weekly_export_pdf_post` when calling `reports_api_v3_workspace_workspace_id_weekly_time_entries_pdf_post`"
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
        if "weekly_export_pdf_post" in params:
            body_params = params["weekly_export_pdf_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/pdf"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/workspace/{workspace_id}/weekly/time_entries.pdf",
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

    def reports_api_v3_workspace_workspace_id_weekly_time_entries_post(self, workspace_id, post, **kwargs):  # noqa: E501
        """Search time entries  # noqa: E501

        Returns time entries for weekly report according to the given filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_workspace_workspace_id_weekly_time_entries_post(workspace_id, post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param BasePost post: Weekly report conditions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_workspace_workspace_id_weekly_time_entries_post_with_http_info(
                workspace_id, post, **kwargs
            )  # noqa: E501
        else:
            (data) = self.reports_api_v3_workspace_workspace_id_weekly_time_entries_post_with_http_info(
                workspace_id, post, **kwargs
            )  # noqa: E501
            return data

    def reports_api_v3_workspace_workspace_id_weekly_time_entries_post_with_http_info(
        self, workspace_id, post, **kwargs
    ):  # noqa: E501
        """Search time entries  # noqa: E501

        Returns time entries for weekly report according to the given filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_workspace_workspace_id_weekly_time_entries_post_with_http_info(workspace_id, post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param BasePost post: Weekly report conditions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "post"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reports_api_v3_workspace_workspace_id_weekly_time_entries_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `reports_api_v3_workspace_workspace_id_weekly_time_entries_post`"
            )  # noqa: E501
        # verify the required parameter "post" is set
        if self.api_client.client_side_validation and ("post" not in params or params["post"] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `post` when calling `reports_api_v3_workspace_workspace_id_weekly_time_entries_post`"
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
        if "post" in params:
            body_params = params["post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/workspace/{workspace_id}/weekly/time_entries",
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
