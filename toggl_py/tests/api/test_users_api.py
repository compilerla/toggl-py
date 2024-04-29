"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.users_api import UsersApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return UsersApi()


def test_UsersApi_delete_organization_users_leave(api):
    """Test case for delete_organization_users_leave

    Leaves organization  # noqa: E501
    """
    pass


def test_UsersApi_delete_workspace_user(api):
    """Test case for delete_workspace_user

    Delete workspace user  # noqa: E501
    """
    pass


def test_UsersApi_get_organization_users(api):
    """Test case for get_organization_users

    List of users in organization  # noqa: E501
    """
    pass


def test_UsersApi_get_organization_users_detailed(api):
    """Test case for get_organization_users_detailed

    List of users in organization with details  # noqa: E501
    """
    pass


def test_UsersApi_get_organization_workspaces_workspaceusers(api):
    """Test case for get_organization_workspaces_workspaceusers

    List of users who belong to the given workspace.  # noqa: E501
    """
    pass


def test_UsersApi_get_workspace_users(api):
    """Test case for get_workspace_users

    Get workspace users  # noqa: E501
    """
    pass


def test_UsersApi_get_workspace_workspace_users(api):
    """Test case for get_workspace_workspace_users

    Get workspace workspace-users  # noqa: E501
    """
    pass


def test_UsersApi_patch_organization_users(api):
    """Test case for patch_organization_users

    Apply changes in bulk to users in an organization  # noqa: E501
    """
    pass


def test_UsersApi_patch_organization_workspace_users(api):
    """Test case for patch_organization_workspace_users

    Changes the users in a workspace.  # noqa: E501
    """
    pass


def test_UsersApi_post_workspace_users_lost_password(api):
    """Test case for post_workspace_users_lost_password

    Change a lost password  # noqa: E501
    """
    pass


def test_UsersApi_put_organization_users(api):
    """Test case for put_organization_users

    Changes a single organization-user  # noqa: E501
    """
    pass


def test_UsersApi_put_organization_workspaces_assignments(api):
    """Test case for put_organization_workspaces_assignments

    Change assignments of users within a workspace.  # noqa: E501
    """
    pass


def test_UsersApi_put_workspace_users(api):
    """Test case for put_workspace_users

    Update workspace user  # noqa: E501
    """
    pass


def test_UsersApi_put_workspace_workspace_users(api):
    """Test case for put_workspace_workspace_users

    Update workspace-user  # noqa: E501
    """
    pass
