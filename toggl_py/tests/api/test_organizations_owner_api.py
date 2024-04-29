"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.organizations_owner_api import OrganizationsOwnerApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return OrganizationsOwnerApi()


def test_OrganizationsOwnerApi_get_ownership_transfer(api):
    """Test case for get_ownership_transfer

    Returns single organization transfer in the organization  # noqa: E501
    """
    pass


def test_OrganizationsOwnerApi_get_ownership_transfers(api):
    """Test case for get_ownership_transfers

    Returns list of organization transfers made in the organization  # noqa: E501
    """
    pass


def test_OrganizationsOwnerApi_post_ownership_transfer(api):
    """Test case for post_ownership_transfer

    Creates new ownership transfer process  # noqa: E501
    """
    pass


def test_OrganizationsOwnerApi_post_ownership_transfer_actions(api):
    """Test case for post_ownership_transfer_actions

    Updates transfer process and emails stakeholders  # noqa: E501
    """
    pass
