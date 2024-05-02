"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class MobileApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_mobile_feedback(self, mobile_feedback_post, **kwargs):  # noqa: E501
        """MobileFeedback  # noqa: E501

        Send Mobile Feedback.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_mobile_feedback(mobile_feedback_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsMobileFeedback mobile_feedback_post: Feedback parameters. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_mobile_feedback_with_http_info(mobile_feedback_post, **kwargs)  # noqa: E501
        else:
            (data) = self.post_mobile_feedback_with_http_info(mobile_feedback_post, **kwargs)  # noqa: E501
            return data

    def post_mobile_feedback_with_http_info(self, mobile_feedback_post, **kwargs):  # noqa: E501
        """MobileFeedback  # noqa: E501

        Send Mobile Feedback.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_mobile_feedback_with_http_info(mobile_feedback_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsMobileFeedback mobile_feedback_post: Feedback parameters. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["mobile_feedback_post"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_mobile_feedback" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "mobile_feedback_post" is set
        if self.api_client.client_side_validation and (
            "mobile_feedback_post" not in params or params["mobile_feedback_post"] is None  # noqa: E501
        ):
            raise ValueError(
                "Missing the required parameter `mobile_feedback_post` when calling `post_mobile_feedback`"  # noqa: E501
            )

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "mobile_feedback_post" in params:
            body_params = params["mobile_feedback_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/mobile/feedback",
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
