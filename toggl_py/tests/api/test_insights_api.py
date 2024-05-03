"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.insights_api import InsightsApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return InsightsApi()


def test_InsightsApi_insights_api_v1_workspace_workspace_id_data_trends_projects_post(api):
    """Test case for insights_api_v1_workspace_workspace_id_data_trends_projects_post

    Load projects' data trends  # noqa: E501
    """
    response = api.insights_api_v1_workspace_workspace_id_data_trends_projects_post()

    assert response


def test_InsightsApi_insights_api_v1_workspace_workspace_id_profitability_employees_extension_post(api):
    """Test case for insights_api_v1_workspace_workspace_id_profitability_employees_extension_post

    Export employee profitability insights  # noqa: E501
    """
    response = api.insights_api_v1_workspace_workspace_id_profitability_employees_extension_post()

    assert response


def test_InsightsApi_insights_api_v1_workspace_workspace_id_profitability_projects_extension_post(api):
    """Test case for insights_api_v1_workspace_workspace_id_profitability_projects_extension_post

    Export profitability project insights  # noqa: E501
    """
    response = api.insights_api_v1_workspace_workspace_id_profitability_projects_extension_post()

    assert response


def test_InsightsApi_insights_api_v1_workspace_workspace_id_trends_projects_extension_post(api):
    """Test case for insights_api_v1_workspace_workspace_id_trends_projects_extension_post

    Export projects data trends  # noqa: E501
    """
    response = api.insights_api_v1_workspace_workspace_id_trends_projects_extension_post()

    assert response
