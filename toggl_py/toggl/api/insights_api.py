"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

from __future__ import annotations  # noqa: F401
import re  # noqa: F401
from typing import TYPE_CHECKING

from toggl.api_client import ApiClient

if TYPE_CHECKING:
    from toggl.models.projects_project_trend import ProjectsProjectTrend  # noqa: F401
    from toggl.models.projects_project_trends import ProjectsProjectTrends  # noqa: F401
    from toggl.models.requests_employee_profitability import RequestsEmployeeProfitability  # noqa: F401
    from toggl.models.requests_project_profitability import RequestsProjectProfitability  # noqa: F401


class InsightsApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def insights_api_v1_workspace_workspace_id_data_trends_projects_post(
        self, workspace_id: int, project_trend_post: ProjectsProjectTrend, **kwargs
    ) -> list[ProjectsProjectTrends]:  # noqa: E501
        """Load projects' data trends  # noqa: E501

        Returns the projects' data trends projects from a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_data_trends_projects_post(workspace_id, project_trend_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param ProjectsProjectTrend project_trend_post: Projects filter conditions (required)
        :return: list[ProjectsProjectTrends]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.insights_api_v1_workspace_workspace_id_data_trends_projects_post_with_http_info(
                workspace_id, project_trend_post, **kwargs
            )  # noqa: E501
        else:
            (data) = self.insights_api_v1_workspace_workspace_id_data_trends_projects_post_with_http_info(
                workspace_id, project_trend_post, **kwargs
            )  # noqa: E501
            return data

    def insights_api_v1_workspace_workspace_id_data_trends_projects_post_with_http_info(
        self, workspace_id: int, project_trend_post: ProjectsProjectTrend, **kwargs
    ) -> list[ProjectsProjectTrends]:  # noqa: E501
        """Load projects' data trends  # noqa: E501

        Returns the projects' data trends projects from a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_data_trends_projects_post_with_http_info(workspace_id, project_trend_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param ProjectsProjectTrend project_trend_post: Projects filter conditions (required)
        :return: list[ProjectsProjectTrends]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "project_trend_post"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insights_api_v1_workspace_workspace_id_data_trends_projects_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `insights_api_v1_workspace_workspace_id_data_trends_projects_post`"  # noqa: E501
            )
        # verify the required parameter "project_trend_post" is set
        if self.api_client.client_side_validation and (
            "project_trend_post" not in params or params["project_trend_post"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `project_trend_post` when calling `insights_api_v1_workspace_workspace_id_data_trends_projects_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "workspace_id" in params:
            path_params["workspace_id"] = params["workspace_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "project_trend_post" in params:
            body_params = params["project_trend_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/insights/api/v1/workspace/{workspace_id}/data_trends/projects",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ProjectsProjectTrends]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(
        self, parameters: RequestsEmployeeProfitability, **kwargs
    ) -> str:  # noqa: E501
        """Export employee profitability insights  # noqa: E501

        Downloads employee profitability insights in the specified format: csv or xlsx.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestsEmployeeProfitability parameters: Parameters for report (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post_with_http_info(
                parameters, **kwargs
            )  # noqa: E501
        else:
            (data) = self.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post_with_http_info(
                parameters, **kwargs
            )  # noqa: E501
            return data

    def insights_api_v1_workspace_workspace_id_profitability_employees_extension_post_with_http_info(
        self, parameters: RequestsEmployeeProfitability, **kwargs
    ) -> str:  # noqa: E501
        """Export employee profitability insights  # noqa: E501

        Downloads employee profitability insights in the specified format: csv or xlsx.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post_with_http_info(parameters, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestsEmployeeProfitability parameters: Parameters for report (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["parameters"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insights_api_v1_workspace_workspace_id_profitability_employees_extension_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "parameters" is set
        if self.api_client.client_side_validation and (
            "parameters" not in params or params["parameters"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `parameters` when calling `insights_api_v1_workspace_workspace_id_profitability_employees_extension_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "parameters" in params:
            body_params = params["parameters"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["text/csv", "text/xlsx"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/insights/api/v1/workspace/{workspace_id}/profitability/employees.{extension}",
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

    def insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(
        self, parameters: RequestsProjectProfitability, extension: str, **kwargs
    ) -> str:  # noqa: E501
        """Export profitability project insights  # noqa: E501

        Downloads profitability project insights in the specified format: csv or xlsx.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(parameters, extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestsProjectProfitability parameters: Parameters for report (required)
        :param str extension: csv,xlsx (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post_with_http_info(
                parameters, extension, **kwargs
            )  # noqa: E501
        else:
            (data) = self.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post_with_http_info(
                parameters, extension, **kwargs
            )  # noqa: E501
            return data

    def insights_api_v1_workspace_workspace_id_profitability_projects_extension_post_with_http_info(
        self, parameters: RequestsProjectProfitability, extension: str, **kwargs
    ) -> str:  # noqa: E501
        """Export profitability project insights  # noqa: E501

        Downloads profitability project insights in the specified format: csv or xlsx.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post_with_http_info(parameters, extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestsProjectProfitability parameters: Parameters for report (required)
        :param str extension: csv,xlsx (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["parameters", "extension"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insights_api_v1_workspace_workspace_id_profitability_projects_extension_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "parameters" is set
        if self.api_client.client_side_validation and (
            "parameters" not in params or params["parameters"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `parameters` when calling `insights_api_v1_workspace_workspace_id_profitability_projects_extension_post`"  # noqa: E501
            )
        # verify the required parameter "extension" is set
        if self.api_client.client_side_validation and ("extension" not in params or params["extension"] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `extension` when calling `insights_api_v1_workspace_workspace_id_profitability_projects_extension_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "extension" in params:
            path_params["extension"] = params["extension"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "parameters" in params:
            body_params = params["parameters"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["text/csv", "text/xlsx"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/insights/api/v1/workspace/{workspace_id}/profitability/projects.{extension}",
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

    def insights_api_v1_workspace_workspace_id_trends_projects_extension_post(
        self, workspace_id: int, extension: str, **kwargs
    ) -> list[ProjectsProjectTrends]:  # noqa: E501
        """Export projects data trends  # noqa: E501

        Downloads projects data trends in the specified format: csv or xlsx.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_trends_projects_extension_post(workspace_id, extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param str extension: csv,xlsx (required)
        :param ProjectsProjectTrend project_trend: Projects filter conditions
        :return: list[ProjectsProjectTrends]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.insights_api_v1_workspace_workspace_id_trends_projects_extension_post_with_http_info(
                workspace_id, extension, **kwargs
            )  # noqa: E501
        else:
            (data) = self.insights_api_v1_workspace_workspace_id_trends_projects_extension_post_with_http_info(
                workspace_id, extension, **kwargs
            )  # noqa: E501
            return data

    def insights_api_v1_workspace_workspace_id_trends_projects_extension_post_with_http_info(
        self, workspace_id: int, extension: str, **kwargs
    ) -> list[ProjectsProjectTrends]:  # noqa: E501
        """Export projects data trends  # noqa: E501

        Downloads projects data trends in the specified format: csv or xlsx.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insights_api_v1_workspace_workspace_id_trends_projects_extension_post_with_http_info(workspace_id, extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Workspace ID (required)
        :param str extension: csv,xlsx (required)
        :param ProjectsProjectTrend project_trend: Projects filter conditions
        :return: list[ProjectsProjectTrends]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "extension", "project_trend"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insights_api_v1_workspace_workspace_id_trends_projects_extension_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `insights_api_v1_workspace_workspace_id_trends_projects_extension_post`"  # noqa: E501
            )
        # verify the required parameter "extension" is set
        if self.api_client.client_side_validation and ("extension" not in params or params["extension"] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `extension` when calling `insights_api_v1_workspace_workspace_id_trends_projects_extension_post`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}
        if "workspace_id" in params:
            path_params["workspace_id"] = params["workspace_id"]  # noqa: E501
        if "extension" in params:
            path_params["extension"] = params["extension"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "project_trend" in params:
            body_params = params["project_trend"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/insights/api/v1/workspace/{workspace_id}/trends/projects.{extension}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ProjectsProjectTrends]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
