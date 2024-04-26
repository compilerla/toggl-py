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


class UserInvoicesApi:

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_workspace_invoice(self, workspace_id, user_invoice_id, **kwargs):  # noqa: E501
        """Delete user invoice.  # noqa: E501

        Deletes user invoice by ID if exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspace_invoice(workspace_id, user_invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :param int user_invoice_id: User invoice ID to be deleted (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_workspace_invoice_with_http_info(workspace_id, user_invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_workspace_invoice_with_http_info(workspace_id, user_invoice_id, **kwargs)  # noqa: E501
            return data

    def delete_workspace_invoice_with_http_info(self, workspace_id, user_invoice_id, **kwargs):  # noqa: E501
        """Delete user invoice.  # noqa: E501

        Deletes user invoice by ID if exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspace_invoice_with_http_info(workspace_id, user_invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :param int user_invoice_id: User invoice ID to be deleted (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "user_invoice_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method delete_workspace_invoice" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `delete_workspace_invoice`"
            )  # noqa: E501
        # verify the required parameter "user_invoice_id" is set
        if self.api_client.client_side_validation and (
            "user_invoice_id" not in params or params["user_invoice_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `user_invoice_id` when calling `delete_workspace_invoice`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "workspace_id" in params:
            path_params["workspace_id"] = params["workspace_id"]  # noqa: E501
        if "user_invoice_id" in params:
            path_params["user_invoice_id"] = params["user_invoice_id"]  # noqa: E501

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
            "/workspaces/{workspace_id}/invoices/{user_invoice_id}",
            "DELETE",
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

    def get_workspace_invoices(self, **kwargs):  # noqa: E501
        """Get workspace invoices.  # noqa: E501

        Get invoices for given workspace with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_invoices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort_order: Sort order, default ASC.
        :param int per_page: Number of items per page, default 50.
        :param int page: Page number, default 1.
        :param str sort_field: Sort field, default created_at.
        :return: list[ModelsUserInvoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_workspace_invoices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_invoices_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_workspace_invoices_with_http_info(self, **kwargs):  # noqa: E501
        """Get workspace invoices.  # noqa: E501

        Get invoices for given workspace with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_invoices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort_order: Sort order, default ASC.
        :param int per_page: Number of items per page, default 50.
        :param int page: Page number, default 1.
        :param str sort_field: Sort field, default created_at.
        :return: list[ModelsUserInvoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["sort_order", "per_page", "page", "sort_field"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_workspace_invoices" % key)
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "sort_order" in params:
            form_params.append(("sort_order", params["sort_order"]))  # noqa: E501
        if "per_page" in params:
            form_params.append(("per_page", params["per_page"]))  # noqa: E501
        if "page" in params:
            form_params.append(("page", params["page"]))  # noqa: E501
        if "sort_field" in params:
            form_params.append(("sort_field", params["sort_field"]))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/invoices",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ModelsUserInvoice]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_workspace_user_invoice(self, workspace_id, tag_post, **kwargs):  # noqa: E501
        """Create user invoice  # noqa: E501

        Creates new user invoice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_user_invoice(workspace_id, tag_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :param ModelsUserInvoice tag_post: Post data (required)
        :return: list[ModelsUserInvoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_workspace_user_invoice_with_http_info(workspace_id, tag_post, **kwargs)  # noqa: E501
        else:
            (data) = self.post_workspace_user_invoice_with_http_info(workspace_id, tag_post, **kwargs)  # noqa: E501
            return data

    def post_workspace_user_invoice_with_http_info(self, workspace_id, tag_post, **kwargs):  # noqa: E501
        """Create user invoice  # noqa: E501

        Creates new user invoice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_user_invoice_with_http_info(workspace_id, tag_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int workspace_id: Numeric ID of the workspace (required)
        :param ModelsUserInvoice tag_post: Post data (required)
        :return: list[ModelsUserInvoice]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["workspace_id", "tag_post"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in params["kwargs"].items():
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method post_workspace_user_invoice" % key)
            params[key] = val
        del params["kwargs"]
        # verify the required parameter "workspace_id" is set
        if self.api_client.client_side_validation and (
            "workspace_id" not in params or params["workspace_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `workspace_id` when calling `post_workspace_user_invoice`"
            )  # noqa: E501
        # verify the required parameter "tag_post" is set
        if self.api_client.client_side_validation and ("tag_post" not in params or params["tag_post"] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `tag_post` when calling `post_workspace_user_invoice`"
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
        if "tag_post" in params:
            body_params = params["tag_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])  # noqa: E501

        # Authentication setting
        auth_settings = ["BasicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/workspaces/{workspace_id}/invoices",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ModelsUserInvoice]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
