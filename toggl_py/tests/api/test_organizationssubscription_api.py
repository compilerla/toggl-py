"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.organizationssubscription_api import OrganizationssubscriptionApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return OrganizationssubscriptionApi()


def test_OrganizationssubscriptionApi_post_organization_subscription_calculate(api):
    """Test case for post_organization_subscription_calculate

    SubscriptionCalculation  # noqa: E501
    """
    pass
