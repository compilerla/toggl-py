"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest

import toggl  # noqa: F401
from toggl.api.goals_api import GoalsApi
from toggl.rest import ApiException  # noqa: F401


@pytest.fixture
def api():
    return GoalsApi()


def test_GoalsApi_goals_cadences_get(api):
    """Test case for goals_cadences_get

    Get a list of goal cadences  # noqa: E501
    """
    response = api.goals_cadences_get()

    assert response


def test_GoalsApi_goals_get(api):
    """Test case for goals_get

    Get a list of goals  # noqa: E501
    """
    response = api.goals_get()

    assert response


def test_GoalsApi_goals_goal_id_delete(api):
    """Test case for goals_goal_id_delete

    Delete one goal  # noqa: E501
    """
    response = api.goals_goal_id_delete()

    assert response


def test_GoalsApi_goals_goal_id_get(api):
    """Test case for goals_goal_id_get

    Get one goal  # noqa: E501
    """
    response = api.goals_goal_id_get()

    assert response


def test_GoalsApi_goals_goal_id_patch(api):
    """Test case for goals_goal_id_patch

    Update a Goal  # noqa: E501
    """
    response = api.goals_goal_id_patch()

    assert response


def test_GoalsApi_goals_goal_id_stats_get(api):
    """Test case for goals_goal_id_stats_get

    Get stats for a goal  # noqa: E501
    """
    response = api.goals_goal_id_stats_get()

    assert response


def test_GoalsApi_goals_insight_post(api):
    """Test case for goals_insight_post

    Get a insight  # noqa: E501
    """
    response = api.goals_insight_post()

    assert response


def test_GoalsApi_goals_post(api):
    """Test case for goals_post

    Create a Goal  # noqa: E501
    """
    response = api.goals_post()

    assert response