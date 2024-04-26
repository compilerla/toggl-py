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


class OrganizationssubscriptionbillingApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_billing_portal_session(self, organization_id, params, **kwargs):  # noqa: E501
        """Create a billing portal session in the unified subscription system  # noqa: E501

        Create a subscription billing portal session in the unified subscription system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_billing_portal_session(organization_id, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :param BillingportalPayload params: The billing portal session data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_billing_portal_session_with_http_info(organization_id, params, **kwargs)  # noqa: E501
        else:
            (data) = self.create_billing_portal_session_with_http_info(organization_id, params, **kwargs)  # noqa: E501
            return data

    def create_billing_portal_session_with_http_info(self, organization_id, params, **kwargs):  # noqa: E501
        """Create a billing portal session in the unified subscription system  # noqa: E501

        Create a subscription billing portal session in the unified subscription system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_billing_portal_session_with_http_info(organization_id, params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :param BillingportalPayload params: The billing portal session data (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id", "params"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method create_billing_portal_session" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `create_billing_portal_session`"
            )  # noqa: E501
        # verify the required parameter "params" is set
        if self.api_client.client_side_validation and ("params" not in params or params["params"] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `params` when calling `create_billing_portal_session`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "organization_id" in params:
            path_params["organization_id"] = params["organization_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "params" in params:
            body_params = params["params"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/subscription/billing_portal",
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
