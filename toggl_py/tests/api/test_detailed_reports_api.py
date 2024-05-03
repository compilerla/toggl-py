"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.detailed_reports_api import DetailedReportsApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return DetailedReportsApi()


def test_DetailedReportsApi_reports_api_v3_workspace_workspace_id_search_time_entries_extension_post(api):
    """Test case for reports_api_v3_workspace_workspace_id_search_time_entries_extension_post

    Export detailed report  # noqa: E501
    """
    response = api.reports_api_v3_workspace_workspace_id_search_time_entries_extension_post()

    assert response


def test_DetailedReportsApi_reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post(api):
    """Test case for reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post

    Export detailed report  # noqa: E501
    """
    response = api.reports_api_v3_workspace_workspace_id_search_time_entries_pdf_post()

    assert response


def test_DetailedReportsApi_reports_api_v3_workspace_workspace_id_search_time_entries_post(api):
    """Test case for reports_api_v3_workspace_workspace_id_search_time_entries_post

    Search time entries  # noqa: E501
    """
    response = api.reports_api_v3_workspace_workspace_id_search_time_entries_post()

    assert response


def test_DetailedReportsApi_reports_api_v3_workspace_workspace_id_search_time_entries_totals_post(api):
    """Test case for reports_api_v3_workspace_workspace_id_search_time_entries_totals_post

    Load totals detailed report  # noqa: E501
    """
    response = api.reports_api_v3_workspace_workspace_id_search_time_entries_totals_post()

    assert response
