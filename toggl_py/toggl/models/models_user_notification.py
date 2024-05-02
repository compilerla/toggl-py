"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pprint
import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import Any

from toggl.configuration import Configuration
from toggl.models.i18n_message import I18nMessage  # noqa: F401
from toggl.models.models_actions import ModelsActions  # noqa: F401


class ModelsUserNotification:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {
        "actions": "ModelsActions",
        "_class": "int",
        "content": "I18nMessage",
        "created_at": "str",
        "id": "int",
        "notification_type": "str",
        "organization_id": "int",
        "read_at": "str",
        "title": "I18nMessage",
        "user_id": "int",
        "workspace_id": "int",
    }

    attribute_map = {
        "actions": "actions",
        "_class": "class",
        "content": "content",
        "created_at": "created_at",
        "id": "id",
        "notification_type": "notification_type",
        "organization_id": "organization_id",
        "read_at": "read_at",
        "title": "title",
        "user_id": "user_id",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self,
        actions: ModelsActions = None,
        _class: int = None,
        content: I18nMessage = None,
        created_at: str = None,
        id: int = None,
        notification_type: str = None,
        organization_id: int = None,
        read_at: str = None,
        title: I18nMessage = None,
        user_id: int = None,
        workspace_id: int = None,
        _configuration: Configuration = None,  # noqa: E501
    ):
        """
        ModelsUserNotification - a model defined in Swagger

        Parameters:
          actions (ModelsActions): Optional
          _class (int): Optional
          content (I18nMessage): Optional
          created_at (str): Optional
          id (int): Optional
          notification_type (str): Optional
          organization_id (int): Optional
          read_at (str): Optional
          title (I18nMessage): Optional
          user_id (int): Optional
          workspace_id (int): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._actions = None
        self.__class = None
        self._content = None
        self._created_at = None
        self._id = None
        self._notification_type = None
        self._organization_id = None
        self._read_at = None
        self._title = None
        self._user_id = None
        self._workspace_id = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if _class is not None:
            self._class = _class
        if content is not None:
            self.content = content
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if notification_type is not None:
            self.notification_type = notification_type
        if organization_id is not None:
            self.organization_id = organization_id
        if read_at is not None:
            self.read_at = read_at
        if title is not None:
            self.title = title
        if user_id is not None:
            self.user_id = user_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def actions(self) -> ModelsActions:
        """Gets the actions of this ModelsUserNotification.  # noqa: E501


        :return: The actions of this ModelsUserNotification.  # noqa: E501
        :rtype: ModelsActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions: ModelsActions):
        """Sets the actions of this ModelsUserNotification.


        :param actions: The actions of this ModelsUserNotification.  # noqa: E501
        :type: ModelsActions
        """

        self._actions = actions

    @property
    def _class(self) -> int:
        """Gets the _class of this ModelsUserNotification.  # noqa: E501


        :return: The _class of this ModelsUserNotification.  # noqa: E501
        :rtype: int
        """
        return self.__class

    @_class.setter
    def _class(self, _class: int):
        """Sets the _class of this ModelsUserNotification.


        :param _class: The _class of this ModelsUserNotification.  # noqa: E501
        :type: int
        """

        self.__class = _class

    @property
    def content(self) -> I18nMessage:
        """Gets the content of this ModelsUserNotification.  # noqa: E501


        :return: The content of this ModelsUserNotification.  # noqa: E501
        :rtype: I18nMessage
        """
        return self._content

    @content.setter
    def content(self, content: I18nMessage):
        """Sets the content of this ModelsUserNotification.


        :param content: The content of this ModelsUserNotification.  # noqa: E501
        :type: I18nMessage
        """

        self._content = content

    @property
    def created_at(self) -> str:
        """Gets the created_at of this ModelsUserNotification.  # noqa: E501


        :return: The created_at of this ModelsUserNotification.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this ModelsUserNotification.


        :param created_at: The created_at of this ModelsUserNotification.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self) -> int:
        """Gets the id of this ModelsUserNotification.  # noqa: E501


        :return: The id of this ModelsUserNotification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ModelsUserNotification.


        :param id: The id of this ModelsUserNotification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this ModelsUserNotification.  # noqa: E501


        :return: The notification_type of this ModelsUserNotification.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this ModelsUserNotification.


        :param notification_type: The notification_type of this ModelsUserNotification.  # noqa: E501
        :type: str
        """

        self._notification_type = notification_type

    @property
    def organization_id(self) -> int:
        """Gets the organization_id of this ModelsUserNotification.  # noqa: E501


        :return: The organization_id of this ModelsUserNotification.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: int):
        """Sets the organization_id of this ModelsUserNotification.


        :param organization_id: The organization_id of this ModelsUserNotification.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def read_at(self) -> str:
        """Gets the read_at of this ModelsUserNotification.  # noqa: E501


        :return: The read_at of this ModelsUserNotification.  # noqa: E501
        :rtype: str
        """
        return self._read_at

    @read_at.setter
    def read_at(self, read_at: str):
        """Sets the read_at of this ModelsUserNotification.


        :param read_at: The read_at of this ModelsUserNotification.  # noqa: E501
        :type: str
        """

        self._read_at = read_at

    @property
    def title(self) -> I18nMessage:
        """Gets the title of this ModelsUserNotification.  # noqa: E501


        :return: The title of this ModelsUserNotification.  # noqa: E501
        :rtype: I18nMessage
        """
        return self._title

    @title.setter
    def title(self, title: I18nMessage):
        """Sets the title of this ModelsUserNotification.


        :param title: The title of this ModelsUserNotification.  # noqa: E501
        :type: I18nMessage
        """

        self._title = title

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ModelsUserNotification.  # noqa: E501


        :return: The user_id of this ModelsUserNotification.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ModelsUserNotification.


        :param user_id: The user_id of this ModelsUserNotification.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def workspace_id(self) -> int:
        """Gets the workspace_id of this ModelsUserNotification.  # noqa: E501


        :return: The workspace_id of this ModelsUserNotification.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id: int):
        """Sets the workspace_id of this ModelsUserNotification.


        :param workspace_id: The workspace_id of this ModelsUserNotification.  # noqa: E501
        :type: int
        """

        self._workspace_id = workspace_id

    def to_dict(self) -> dict[str, Any]:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items())
                )
            else:
                result[attr] = value
        if issubclass(ModelsUserNotification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelsUserNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsUserNotification):
            return True

        return self.to_dict() != other.to_dict()
