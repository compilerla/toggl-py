"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient
from toggl.models.saved_report_output import SavedReportOutput  # noqa: F401


class SavedReportsApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reports_api_v3_shared_report_token_csv_post(self, report_token: str, **kwargs) -> str:  # noqa: E501
        """Export CSV for saved report  # noqa: E501

        <p>Downloads a previously saved report in csv.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_csv_post(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param str end_date: End date in the format YYYY-MM-DD
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_shared_report_token_csv_post_with_http_info(report_token, **kwargs)  # noqa: E501
        else:
            (data) = self.reports_api_v3_shared_report_token_csv_post_with_http_info(report_token, **kwargs)  # noqa: E501
            return data

    def reports_api_v3_shared_report_token_csv_post_with_http_info(self, report_token: str, **kwargs) -> str:  # noqa: E501
        """Export CSV for saved report  # noqa: E501

        <p>Downloads a previously saved report in csv.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_csv_post_with_http_info(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param str end_date: End date in the format YYYY-MM-DD
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["report_token", "start_date", "end_date"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method reports_api_v3_shared_report_token_csv_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "report_token" is set
        if self.api_client.client_side_validation and (
            "report_token" not in params or params["report_token"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `report_token` when calling `reports_api_v3_shared_report_token_csv_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "report_token" in params:
            path_params["report_token"] = params["report_token"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "end_date" in params:
            body_params = params["end_date"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["text/csv"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["text/plain"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/shared/{report_token}.csv",
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

    def reports_api_v3_shared_report_token_pdf_post(self, report_token: str, **kwargs) -> str:  # noqa: E501
        """Export saved report in pdf format  # noqa: E501

        <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_pdf_post(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param str end_date: End date in the format YYYY-MM-DD
        :param str display_mode: Display mode for time data, only for detailed reports. Possible values: 'date_only', 'time_only', 'date_time'. Default value: 'date_and_time'
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_shared_report_token_pdf_post_with_http_info(report_token, **kwargs)  # noqa: E501
        else:
            (data) = self.reports_api_v3_shared_report_token_pdf_post_with_http_info(report_token, **kwargs)  # noqa: E501
            return data

    def reports_api_v3_shared_report_token_pdf_post_with_http_info(self, report_token: str, **kwargs) -> str:  # noqa: E501
        """Export saved report in pdf format  # noqa: E501

        <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_pdf_post_with_http_info(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param str end_date: End date in the format YYYY-MM-DD
        :param str display_mode: Display mode for time data, only for detailed reports. Possible values: 'date_only', 'time_only', 'date_time'. Default value: 'date_and_time'
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["report_token", "start_date", "end_date", "display_mode"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method reports_api_v3_shared_report_token_pdf_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "report_token" is set
        if self.api_client.client_side_validation and (
            "report_token" not in params or params["report_token"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `report_token` when calling `reports_api_v3_shared_report_token_pdf_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "report_token" in params:
            path_params["report_token"] = params["report_token"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "display_mode" in params:
            body_params = params["display_mode"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/pdf"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["text/plain"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/shared/{report_token}/pdf",
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

    def reports_api_v3_shared_report_token_post(self, report_token: str, **kwargs) -> SavedReportOutput:  # noqa: E501
        """Load the previously saved report  # noqa: E501

        <p>Returns the previously saved report.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_post(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param int first_timestamp: Unix timestamp(UTC) or null for proper pagination. This parameter only works in Detailed and Summary reports.
        :param str end_date: End date in the format YYYY-MM-DD. This parameter only works in Detailed and Summary reports.
        :param list[int] group_ids: Integer array with group_ids
        :param list[int] user_ids: Integer array with user_ids
        :param list[int] client_ids: Integer array with client_ids
        :param list[int] project_ids: Integer array with project_ids
        :param list[int] task_ids: Integer array with task_ids
        :param list[int] tag_ids: Integer array with tag_ids
        :param str description: Case insensitive pattern that matches `.*(description).*`
        :param bool billable: Is billable filter on
        :param int rounding: How the rounding is done: 1 is rounding up, -1 down, 0 for no rounding.
        :param int rounding_minutes: Rounding amount in minutes
        :param bool grouped: If it is grouped or not. This parameter only works for Detailed report.
        :param str grouping: Criteria to group by. This parameter only works for Summary report.
        :param str sub_grouping: Criteria to subgroup. This parameter only works for Summary report.
        :return: SavedReportOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_shared_report_token_post_with_http_info(report_token, **kwargs)  # noqa: E501
        else:
            (data) = self.reports_api_v3_shared_report_token_post_with_http_info(report_token, **kwargs)  # noqa: E501
            return data

    def reports_api_v3_shared_report_token_post_with_http_info(
        self, report_token: str, **kwargs
    ) -> SavedReportOutput:  # noqa: E501
        """Load the previously saved report  # noqa: E501

        <p>Returns the previously saved report.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_post_with_http_info(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param int first_timestamp: Unix timestamp(UTC) or null for proper pagination. This parameter only works in Detailed and Summary reports.
        :param str end_date: End date in the format YYYY-MM-DD. This parameter only works in Detailed and Summary reports.
        :param list[int] group_ids: Integer array with group_ids
        :param list[int] user_ids: Integer array with user_ids
        :param list[int] client_ids: Integer array with client_ids
        :param list[int] project_ids: Integer array with project_ids
        :param list[int] task_ids: Integer array with task_ids
        :param list[int] tag_ids: Integer array with tag_ids
        :param str description: Case insensitive pattern that matches `.*(description).*`
        :param bool billable: Is billable filter on
        :param int rounding: How the rounding is done: 1 is rounding up, -1 down, 0 for no rounding.
        :param int rounding_minutes: Rounding amount in minutes
        :param bool grouped: If it is grouped or not. This parameter only works for Detailed report.
        :param str grouping: Criteria to group by. This parameter only works for Summary report.
        :param str sub_grouping: Criteria to subgroup. This parameter only works for Summary report.
        :return: SavedReportOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "report_token",
            "start_date",
            "first_timestamp",
            "end_date",
            "group_ids",
            "user_ids",
            "client_ids",
            "project_ids",
            "task_ids",
            "tag_ids",
            "description",
            "billable",
            "rounding",
            "rounding_minutes",
            "grouped",
            "grouping",
            "sub_grouping",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method reports_api_v3_shared_report_token_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "report_token" is set
        if self.api_client.client_side_validation and (
            "report_token" not in params or params["report_token"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `report_token` when calling `reports_api_v3_shared_report_token_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "report_token" in params:
            path_params["report_token"] = params["report_token"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "sub_grouping" in params:
            body_params = params["sub_grouping"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["text/plain"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/shared/{report_token}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SavedReportOutput",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def reports_api_v3_shared_report_token_xlsx_post(self, report_token: str, **kwargs) -> str:  # noqa: E501
        """Export XSLX saved report  # noqa: E501

        <p>Downloads a previously saved report in xlsx.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_xlsx_post(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param str end_date: End date in the format YYYY-MM-DD
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.reports_api_v3_shared_report_token_xlsx_post_with_http_info(report_token, **kwargs)  # noqa: E501
        else:
            (data) = self.reports_api_v3_shared_report_token_xlsx_post_with_http_info(report_token, **kwargs)  # noqa: E501
            return data

    def reports_api_v3_shared_report_token_xlsx_post_with_http_info(self, report_token: str, **kwargs) -> str:  # noqa: E501
        """Export XSLX saved report  # noqa: E501

        <p>Downloads a previously saved report in xlsx.</p> <p><b>Authentication</b></p><p>A public report is accessible by anyone, a private one is only accessible by the report's owner or workspace admin. If the criteria aren't met it returns 403 status code.</p> <p><b>Parameters</b></p><p>The report can be executed without parameters, and in this case the saved or default parameters will be used.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reports_api_v3_shared_report_token_xlsx_post_with_http_info(report_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str report_token: Token for the saved report (required)
        :param str start_date: Starting date in the format YYYY-MM-DD
        :param str end_date: End date in the format YYYY-MM-DD
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["report_token", "start_date", "end_date"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method reports_api_v3_shared_report_token_xlsx_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "report_token" is set
        if self.api_client.client_side_validation and (
            "report_token" not in params or params["report_token"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `report_token` when calling `reports_api_v3_shared_report_token_xlsx_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "report_token" in params:
            path_params["report_token"] = params["report_token"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "end_date" in params:
            body_params = params["end_date"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["text/xlsx"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["text/plain"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/reports/api/v3/shared/{report_token}.xlsx",
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
