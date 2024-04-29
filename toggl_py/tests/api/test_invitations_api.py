"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.invitations_api import InvitationsApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return InvitationsApi()


def test_InvitationsApi_get_invitations(api):
    """Test case for get_invitations

    Get an invitation  # noqa: E501
    """
    pass


def test_InvitationsApi_post_organization_accept_invitation(api):
    """Test case for post_organization_accept_invitation

    Accepts invitation  # noqa: E501
    """
    pass


def test_InvitationsApi_post_organization_invitation(api):
    """Test case for post_organization_invitation

    Creates a new invitation for the user  # noqa: E501
    """
    pass


def test_InvitationsApi_post_reject_invitation(api):
    """Test case for post_reject_invitation

    Rejects invitation  # noqa: E501
    """
    pass


def test_InvitationsApi_put_invitation(api):
    """Test case for put_invitation

    Resends user their invitation  # noqa: E501
    """
    pass
