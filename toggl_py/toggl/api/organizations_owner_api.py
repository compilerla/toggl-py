"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class OrganizationsOwnerApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ownership_transfer(self, organization_id, transfer_id, **kwargs):  # noqa: E501
        """Returns single organization transfer in the organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ownership_transfer(organization_id, transfer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :param int transfer_id: Numeric ID of the transfer. (required)
        :return: ModelsTransfer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_ownership_transfer_with_http_info(organization_id, transfer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ownership_transfer_with_http_info(organization_id, transfer_id, **kwargs)  # noqa: E501
            return data

    def get_ownership_transfer_with_http_info(self, organization_id, transfer_id, **kwargs):  # noqa: E501
        """Returns single organization transfer in the organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ownership_transfer_with_http_info(organization_id, transfer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :param int transfer_id: Numeric ID of the transfer. (required)
        :return: ModelsTransfer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id", "transfer_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_ownership_transfer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `get_ownership_transfer`"
            )  # noqa: E501
        # verify the required parameter "transfer_id" is set
        if self.api_client.client_side_validation and (
            "transfer_id" not in params or params["transfer_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `transfer_id` when calling `get_ownership_transfer`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "organization_id" in params:
            path_params["organization_id"] = params["organization_id"]  # noqa: E501
        if "transfer_id" in params:
            path_params["transfer_id"] = params["transfer_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/owner/transfer/{transfer_id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsTransfer",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_ownership_transfers(self, organization_id, **kwargs):  # noqa: E501
        """Returns list of organization transfers made in the organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ownership_transfers(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :param str ongoing: If true, returns only current, not finished transfer
        :return: list[ModelsTransfer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_ownership_transfers_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_ownership_transfers_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def get_ownership_transfers_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Returns list of organization transfers made in the organization  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ownership_transfers_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :param str ongoing: If true, returns only current, not finished transfer
        :return: list[ModelsTransfer]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id", "ongoing"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_ownership_transfers" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `get_ownership_transfers`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "organization_id" in params:
            path_params["organization_id"] = params["organization_id"]  # noqa: E501

        query_params = []
        if "ongoing" in params:
            query_params.append(("ongoing", params["ongoing"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/owner/transfer",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ModelsTransfer]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_ownership_transfer(self, organization_id, **kwargs):  # noqa: E501
        """Creates new ownership transfer process  # noqa: E501

        Return the ownership transfer for a given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ownership_transfer(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :return: ModelsTransfer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_ownership_transfer_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_ownership_transfer_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def post_ownership_transfer_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Creates new ownership transfer process  # noqa: E501

        Return the ownership transfer for a given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ownership_transfer_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :return: ModelsTransfer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_ownership_transfer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `post_ownership_transfer`"
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
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/owner/transfer",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsTransfer",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_ownership_transfer_actions(self, organization_id, transfer_id, action, **kwargs):  # noqa: E501
        """Updates transfer process and emails stakeholders  # noqa: E501

        Return the ownership transfer for a given organization and emails stakeholders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ownership_transfer_actions(organization_id, transfer_id, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :param int transfer_id: Numeric ID of the transfer. (required)
        :param str action: Action to update transfer with. (required)
        :return: ModelsTransfer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_ownership_transfer_actions_with_http_info(
                organization_id, transfer_id, action, **kwargs
            )  # noqa: E501
        else:
            (data) = self.post_ownership_transfer_actions_with_http_info(
                organization_id, transfer_id, action, **kwargs
            )  # noqa: E501
            return data

    def post_ownership_transfer_actions_with_http_info(self, organization_id, transfer_id, action, **kwargs):  # noqa: E501
        """Updates transfer process and emails stakeholders  # noqa: E501

        Return the ownership transfer for a given organization and emails stakeholders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_ownership_transfer_actions_with_http_info(organization_id, transfer_id, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization. (required)
        :param int transfer_id: Numeric ID of the transfer. (required)
        :param str action: Action to update transfer with. (required)
        :return: ModelsTransfer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id", "transfer_id", "action"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_ownership_transfer_actions" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `post_ownership_transfer_actions`"
            )  # noqa: E501
        # verify the required parameter "transfer_id" is set
        if self.api_client.client_side_validation and (
            "transfer_id" not in params or params["transfer_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `transfer_id` when calling `post_ownership_transfer_actions`"
            )  # noqa: E501
        # verify the required parameter "action" is set
        if self.api_client.client_side_validation and ("action" not in params or params["action"] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `action` when calling `post_ownership_transfer_actions`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "organization_id" in params:
            path_params["organization_id"] = params["organization_id"]  # noqa: E501
        if "transfer_id" in params:
            path_params["transfer_id"] = params["transfer_id"]  # noqa: E501
        if "action" in params:
            path_params["action"] = params["action"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/owner/transfer/{transfer_id}/{action}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsTransfer",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
