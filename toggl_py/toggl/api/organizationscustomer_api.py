"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import re  # noqa: F401

from toggl.api_client import ApiClient


class OrganizationscustomerApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_organization_customer(self, organization_id, **kwargs):  # noqa: E501
        """Customer  # noqa: E501

        Allows to fetch customer data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organization_customer(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: ModelsCustomer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_organization_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_organization_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def get_organization_customer_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Customer  # noqa: E501

        Allows to fetch customer data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_organization_customer_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: ModelsCustomer
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_organization_customer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `get_organization_customer`"
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
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/customer",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsCustomer",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_unified_customer(self, organization_id, **kwargs):  # noqa: E501
        """Retrieve unified customer  # noqa: E501

        Retrieve unified customer belonging to the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unified_customer(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: CustomerUnifiedCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_unified_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_unified_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def get_unified_customer_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Retrieve unified customer  # noqa: E501

        Retrieve unified customer belonging to the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unified_customer_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: CustomerUnifiedCustomerResponse
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_unified_customer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `get_unified_customer`"
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
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/subscription/customer",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CustomerUnifiedCustomerResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_organization_customer(self, organization_id, contact_detail_request, **kwargs):  # noqa: E501
        """ContactDetails  # noqa: E501

        Allows to save contact details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_organization_customer(organization_id, contact_detail_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the workspace. (required)
        :param SubscriptionContactDetailRequest contact_detail_request: Input data for contact details. (required)
        :return: ModelsContactDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_organization_customer_with_http_info(
                organization_id, contact_detail_request, **kwargs
            )  # noqa: E501
        else:
            (data) = self.post_organization_customer_with_http_info(
                organization_id, contact_detail_request, **kwargs
            )  # noqa: E501
            return data

    def post_organization_customer_with_http_info(self, organization_id, contact_detail_request, **kwargs):  # noqa: E501
        """ContactDetails  # noqa: E501

        Allows to save contact details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_organization_customer_with_http_info(organization_id, contact_detail_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the workspace. (required)
        :param SubscriptionContactDetailRequest contact_detail_request: Input data for contact details. (required)
        :return: ModelsContactDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["organization_id", "contact_detail_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_organization_customer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `post_organization_customer`"
            )  # noqa: E501
        # verify the required parameter "contact_detail_request" is set
        if self.api_client.client_side_validation and (
            "contact_detail_request" not in params or params["contact_detail_request"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `contact_detail_request` when calling `post_organization_customer`"
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
        if "contact_detail_request" in params:
            body_params = params["contact_detail_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/customer/contact_detail",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ModelsContactDetail",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_unified_customer(self, organization_id, **kwargs):  # noqa: E501
        """Create unified customer  # noqa: E501

        Creates unified customer for organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_unified_customer(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: CustomerUnifiedCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_unified_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_unified_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def post_unified_customer_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Create unified customer  # noqa: E501

        Creates unified customer for organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_unified_customer_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: CustomerUnifiedCustomerResponse
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_unified_customer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `post_unified_customer`"
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
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/subscription/customer",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CustomerUnifiedCustomerResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_unified_customer(self, organization_id, **kwargs):  # noqa: E501
        """Update unified customer  # noqa: E501

        Allows to update unified customer data. Customer name, email, country & postal code are mandatory fields. Optional fields will be cleared if they don't have a value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_unified_customer(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: CustomerUnifiedCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_unified_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_unified_customer_with_http_info(organization_id, **kwargs)  # noqa: E501
            return data

    def put_unified_customer_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """Update unified customer  # noqa: E501

        Allows to update unified customer data. Customer name, email, country & postal code are mandatory fields. Optional fields will be cleared if they don't have a value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_unified_customer_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int organization_id: Numeric ID of the organization (required)
        :return: CustomerUnifiedCustomerResponse
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
                raise TypeError("Got an unexpected keyword argument '%s'" " to method put_unified_customer" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "organization_id" is set
        if self.api_client.client_side_validation and (
            "organization_id" not in params or params["organization_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `organization_id` when calling `put_unified_customer`"
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
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/organizations/{organization_id}/subscription/customer",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CustomerUnifiedCustomerResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
