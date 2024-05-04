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
    from toggl.models.file import file  # noqa: F401


class FeedbackApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_feedback_web(self, toggl_version: str, _date: str, details: str, **kwargs):  # noqa: E501
        """FeedbackWeb  # noqa: E501

        Send Feedback web.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_feedback_web(toggl_version, _date, details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str toggl_version: Toggl version. (required)
        :param str _date: Feedback date. (required)
        :param str details: Feedback details. (required)
        :param str update_channel: Update channel.
        :param str subject: Email subject.
        :param bool latest: Latest feedback.
        :param file files: One or more files.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_feedback_web_with_http_info(toggl_version, _date, details, **kwargs)  # noqa: E501
        else:
            (data) = self.post_feedback_web_with_http_info(toggl_version, _date, details, **kwargs)  # noqa: E501
            return data

    def post_feedback_web_with_http_info(self, toggl_version: str, _date: str, details: str, **kwargs):  # noqa: E501
        """FeedbackWeb  # noqa: E501

        Send Feedback web.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_feedback_web_with_http_info(toggl_version, _date, details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str toggl_version: Toggl version. (required)
        :param str _date: Feedback date. (required)
        :param str details: Feedback details. (required)
        :param str update_channel: Update channel.
        :param str subject: Email subject.
        :param bool latest: Latest feedback.
        :param file files: One or more files.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["toggl_version", "_date", "details", "update_channel", "subject", "latest", "files"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_feedback_web" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "toggl_version" is set
        if self.api_client.client_side_validation and (
            "toggl_version" not in params or params["toggl_version"] is None  # noqa: E501
        ):
            raise ValueError("Missing the required parameter `toggl_version` when calling `post_feedback_web`")  # noqa: E501
        # verify the required parameter "_date" is set
        if self.api_client.client_side_validation and ("_date" not in params or params["_date"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `_date` when calling `post_feedback_web`")  # noqa: E501
        # verify the required parameter "details" is set
        if self.api_client.client_side_validation and ("details" not in params or params["details"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `details` when calling `post_feedback_web`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "toggl_version" in params:
            form_params.append(("toggl_version", params["toggl_version"]))  # noqa: E501
        if "_date" in params:
            form_params.append(("date", params["_date"]))  # noqa: E501
        if "details" in params:
            form_params.append(("details", params["details"]))  # noqa: E501
        if "update_channel" in params:
            form_params.append(("update_channel", params["update_channel"]))  # noqa: E501
        if "subject" in params:
            form_params.append(("subject", params["subject"]))  # noqa: E501
        if "latest" in params:
            form_params.append(("latest", params["latest"]))  # noqa: E501
        if "files" in params:
            local_var_files["files"] = params["files"]  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/feedback/web",
            "POST",
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

    def post_unified_feedback(self, toggl_version: str, _date: str, details: str, **kwargs):  # noqa: E501
        """Feedback  # noqa: E501

        Send Feedback  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_unified_feedback(toggl_version, _date, details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str toggl_version: Toggl version. (required)
        :param str _date: Feedback date. (required)
        :param str details: Feedback details. (required)
        :param str update_channel: Update channel.
        :param str subject: Email subject.
        :param str device_model: Device Model.
        :param str build_number: Build Number.
        :param str operating_system: Operating system.
        :param bool latest: Latest feedback.
        :param file files: One or more files.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_unified_feedback_with_http_info(toggl_version, _date, details, **kwargs)  # noqa: E501
        else:
            (data) = self.post_unified_feedback_with_http_info(toggl_version, _date, details, **kwargs)  # noqa: E501
            return data

    def post_unified_feedback_with_http_info(self, toggl_version: str, _date: str, details: str, **kwargs):  # noqa: E501
        """Feedback  # noqa: E501

        Send Feedback  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_unified_feedback_with_http_info(toggl_version, _date, details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str toggl_version: Toggl version. (required)
        :param str _date: Feedback date. (required)
        :param str details: Feedback details. (required)
        :param str update_channel: Update channel.
        :param str subject: Email subject.
        :param str device_model: Device Model.
        :param str build_number: Build Number.
        :param str operating_system: Operating system.
        :param bool latest: Latest feedback.
        :param file files: One or more files.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "toggl_version",
            "_date",
            "details",
            "update_channel",
            "subject",
            "device_model",
            "build_number",
            "operating_system",
            "latest",
            "files",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_unified_feedback" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "toggl_version" is set
        if self.api_client.client_side_validation and (
            "toggl_version" not in params or params["toggl_version"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `toggl_version` when calling `post_unified_feedback`"  # noqa: E501
            )
        # verify the required parameter "_date" is set
        if self.api_client.client_side_validation and ("_date" not in params or params["_date"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `_date` when calling `post_unified_feedback`")  # noqa: E501
        # verify the required parameter "details" is set
        if self.api_client.client_side_validation and ("details" not in params or params["details"] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `details` when calling `post_unified_feedback`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "toggl_version" in params:
            form_params.append(("toggl_version", params["toggl_version"]))  # noqa: E501
        if "_date" in params:
            form_params.append(("date", params["_date"]))  # noqa: E501
        if "details" in params:
            form_params.append(("details", params["details"]))  # noqa: E501
        if "update_channel" in params:
            form_params.append(("update_channel", params["update_channel"]))  # noqa: E501
        if "subject" in params:
            form_params.append(("subject", params["subject"]))  # noqa: E501
        if "device_model" in params:
            form_params.append(("device_model", params["device_model"]))  # noqa: E501
        if "build_number" in params:
            form_params.append(("build_number", params["build_number"]))  # noqa: E501
        if "operating_system" in params:
            form_params.append(("operating_system", params["operating_system"]))  # noqa: E501
        if "latest" in params:
            form_params.append(("latest", params["latest"]))  # noqa: E501
        if "files" in params:
            local_var_files["files"] = params["files"]  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/feedback",
            "POST",
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
