"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.me_api import MeApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return MeApi()


def test_MeApi_delete_push_services(api):
    """Test case for delete_push_services

    PushServices  # noqa: E501
    """
    pass


def test_MeApi_get_clients(api):
    """Test case for get_clients

    Clients  # noqa: E501
    """
    pass


def test_MeApi_get_lost_password(api):
    """Test case for get_lost_password

    LostPassword  # noqa: E501
    """
    pass


def test_MeApi_get_me(api):
    """Test case for get_me

    Me  # noqa: E501
    """
    pass


def test_MeApi_get_me_features(api):
    """Test case for get_me_features

    Features  # noqa: E501
    """
    pass


def test_MeApi_get_me_flags(api):
    """Test case for get_me_flags

    Flags  # noqa: E501
    """
    pass


def test_MeApi_get_me_location(api):
    """Test case for get_me_location

    User's last known location  # noqa: E501
    """
    pass


def test_MeApi_get_me_notifications(api):
    """Test case for get_me_notifications

    Notifications  # noqa: E501
    """
    pass


def test_MeApi_get_me_projects(api):
    """Test case for get_me_projects

    Projects  # noqa: E501
    """
    pass


def test_MeApi_get_me_projects_paginated(api):
    """Test case for get_me_projects_paginated

    ProjectsPaginated  # noqa: E501
    """
    pass


def test_MeApi_get_me_timesheets(api):
    """Test case for get_me_timesheets

    User's Timesheets  # noqa: E501
    """
    pass


def test_MeApi_get_me_track_reminders(api):
    """Test case for get_me_track_reminders

    TrackReminders  # noqa: E501
    """
    pass


def test_MeApi_get_organizations(api):
    """Test case for get_organizations

    Organizations that a user is part of  # noqa: E501
    """
    pass


def test_MeApi_get_push_services(api):
    """Test case for get_push_services

    PushServices  # noqa: E501
    """
    pass


def test_MeApi_get_tags(api):
    """Test case for get_tags

    Tags  # noqa: E501
    """
    pass


def test_MeApi_get_tasks(api):
    """Test case for get_tasks

    Tasks  # noqa: E501
    """
    pass


def test_MeApi_get_web_timer(api):
    """Test case for get_web_timer

    WebTimer  # noqa: E501
    """
    pass


def test_MeApi_get_workspaces(api):
    """Test case for get_workspaces

    Workspaces  # noqa: E501
    """
    pass


def test_MeApi_me_logged_get(api):
    """Test case for me_logged_get

    Logged  # noqa: E501
    """
    pass


def test_MeApi_post_close_account(api):
    """Test case for post_close_account

    CloseAccount  # noqa: E501
    """
    pass


def test_MeApi_post_lost_password(api):
    """Test case for post_lost_password

    LostPassword  # noqa: E501
    """
    pass


def test_MeApi_post_lost_password_confirm(api):
    """Test case for post_lost_password_confirm

    LostPassword conformation  # noqa: E501
    """
    pass


def test_MeApi_post_me_accept_tos(api):
    """Test case for post_me_accept_tos

    AcceptTOS  # noqa: E501
    """
    pass


def test_MeApi_post_me_disable_product_emails(api):
    """Test case for post_me_disable_product_emails

    Disable product emails  # noqa: E501
    """
    pass


def test_MeApi_post_me_disable_weekly_report(api):
    """Test case for post_me_disable_weekly_report

    Disable weekly report  # noqa: E501
    """
    pass


def test_MeApi_post_me_flags(api):
    """Test case for post_me_flags

    Flags  # noqa: E501
    """
    pass


def test_MeApi_post_push_services(api):
    """Test case for post_push_services

    PushServices  # noqa: E501
    """
    pass


def test_MeApi_put_me(api):
    """Test case for put_me

    Me  # noqa: E501
    """
    pass


def test_MeApi_put_notifications(api):
    """Test case for put_notifications

    Notifications  # noqa: E501
    """
    pass
