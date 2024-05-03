"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.alerts_api import AlertsApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return AlertsApi()


def test_AlertsApi_delete_alerts(api):
    """Test case for delete_alerts

    Alerts  # noqa: E501
    """
    response = api.delete_alerts()

    assert response


def test_AlertsApi_get_alerts(api):
    """Test case for get_alerts

    Alerts  # noqa: E501
    """
    response = api.get_alerts()

    assert response


def test_AlertsApi_post_alerts(api):
    """Test case for post_alerts

    Alerts  # noqa: E501
    """
    response = api.post_alerts()

    assert response


def test_AlertsApi_put_alerts(api):
    """Test case for put_alerts

    Alerts  # noqa: E501
    """
    response = api.put_alerts()

    assert response
