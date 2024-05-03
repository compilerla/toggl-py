"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.workspacesreportsshared_api import WorkspacesreportssharedApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return WorkspacesreportssharedApi()


def test_WorkspacesreportssharedApi_bulk_delete_saved_report_resource(api):
    """Test case for bulk_delete_saved_report_resource

    SavedReport  # noqa: E501
    """
    response = api.bulk_delete_saved_report_resource()

    assert response
