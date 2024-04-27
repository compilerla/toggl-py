"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.approvals_api import ApprovalsApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return ApprovalsApi()


def test_ApprovalsApi_delete_timesheet_setups(api):
    """Test case for delete_timesheet_setups

    Delete a timesheet setup  # noqa: E501
    """
    response = api.delete_timesheet_setups()

    assert response


def test_ApprovalsApi_get_timesheet_setups(api):
    """Test case for get_timesheet_setups

    Get timesheet setups  # noqa: E501
    """
    response = api.get_timesheet_setups()

    assert response


def test_ApprovalsApi_get_workspace_timesheet_hours_handler(api):
    """Test case for get_workspace_timesheet_hours_handler

    Get timesheets hours  # noqa: E501
    """
    response = api.get_workspace_timesheet_hours_handler()

    assert response


def test_ApprovalsApi_get_workspace_timesheet_time_entries_handler(api):
    """Test case for get_workspace_timesheet_time_entries_handler

    Get timesheet time entries  # noqa: E501
    """
    response = api.get_workspace_timesheet_time_entries_handler()

    assert response


def test_ApprovalsApi_get_workspace_timesheets_handler(api):
    """Test case for get_workspace_timesheets_handler

    Get timesheets  # noqa: E501
    """
    response = api.get_workspace_timesheets_handler()

    assert response


def test_ApprovalsApi_post_timesheet_setups(api):
    """Test case for post_timesheet_setups

    Create a timesheet setup  # noqa: E501
    """
    response = api.post_timesheet_setups()

    assert response


def test_ApprovalsApi_put_timesheet_setups(api):
    """Test case for put_timesheet_setups

    Update a timesheet setup  # noqa: E501
    """
    response = api.put_timesheet_setups()

    assert response


def test_ApprovalsApi_put_workspace_timesheets_handler(api):
    """Test case for put_workspace_timesheets_handler

    Update timesheets  # noqa: E501
    """
    response = api.put_workspace_timesheets_handler()

    assert response