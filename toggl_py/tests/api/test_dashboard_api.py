"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.dashboard_api import DashboardApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return DashboardApi()


def test_DashboardApi_get_workspace_all_activities(api):
    """Test case for get_workspace_all_activities

    Get last activity for every workspace user  # noqa: E501
    """
    response = api.get_workspace_all_activities()

    assert response


def test_DashboardApi_get_workspace_most_active(api):
    """Test case for get_workspace_most_active

    Get most active users  # noqa: E501
    """
    response = api.get_workspace_most_active()

    assert response


def test_DashboardApi_get_workspace_top_activity(api):
    """Test case for get_workspace_top_activity

    Get top activities  # noqa: E501
    """
    response = api.get_workspace_top_activity()

    assert response