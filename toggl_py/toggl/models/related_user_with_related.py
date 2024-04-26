"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Last changed: 2024-04-26T22:13:16.785Z
Generated by: https://github.com/compilerla/toggl-py/tree/main/codegen
"""

import pprint
import re  # noqa: F401

from toggl.configuration import Configuration


class RelatedUserWithRelated:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "api_token": "str",
        "at": "datetime",
        "authorization_updated_at": "str",
        "beginning_of_week": "int",
        "clients": "list[ModelsClient]",
        "country_id": "int",
        "created_at": "datetime",
        "default_workspace_id": "int",
        "email": "str",
        "fullname": "str",
        "has_password": "bool",
        "id": "int",
        "image_url": "str",
        "intercom_hash": "str",
        "oauth_providers": "list[str]",
        "openid_email": "str",
        "openid_enabled": "bool",
        "options": "ModelsOptions",
        "projects": "list[ModelsProject]",
        "tags": "list[ModelsTag]",
        "tasks": "list[ModelsTask]",
        "time_entries": "list[ModelsTimeEntry]",
        "timezone": "str",
        "updated_at": "datetime",
        "workspaces": "list[WorkspaceWorkspace]",
    }

    attribute_map = {
        "api_token": "api_token",
        "at": "at",
        "authorization_updated_at": "authorization_updated_at",
        "beginning_of_week": "beginning_of_week",
        "clients": "clients",
        "country_id": "country_id",
        "created_at": "created_at",
        "default_workspace_id": "default_workspace_id",
        "email": "email",
        "fullname": "fullname",
        "has_password": "has_password",
        "id": "id",
        "image_url": "image_url",
        "intercom_hash": "intercom_hash",
        "oauth_providers": "oauth_providers",
        "openid_email": "openid_email",
        "openid_enabled": "openid_enabled",
        "options": "options",
        "projects": "projects",
        "tags": "tags",
        "tasks": "tasks",
        "time_entries": "time_entries",
        "timezone": "timezone",
        "updated_at": "updated_at",
        "workspaces": "workspaces",
    }

    def __init__(
        self,
        api_token=None,
        at=None,
        authorization_updated_at=None,
        beginning_of_week=None,
        clients=None,
        country_id=None,
        created_at=None,
        default_workspace_id=None,
        email=None,
        fullname=None,
        has_password=None,
        id=None,
        image_url=None,
        intercom_hash=None,
        oauth_providers=None,
        openid_email=None,
        openid_enabled=None,
        options=None,
        projects=None,
        tags=None,
        tasks=None,
        time_entries=None,
        timezone=None,
        updated_at=None,
        workspaces=None,
        _configuration=None,
    ):  # noqa: E501
        """RelatedUserWithRelated - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_token = None
        self._at = None
        self._authorization_updated_at = None
        self._beginning_of_week = None
        self._clients = None
        self._country_id = None
        self._created_at = None
        self._default_workspace_id = None
        self._email = None
        self._fullname = None
        self._has_password = None
        self._id = None
        self._image_url = None
        self._intercom_hash = None
        self._oauth_providers = None
        self._openid_email = None
        self._openid_enabled = None
        self._options = None
        self._projects = None
        self._tags = None
        self._tasks = None
        self._time_entries = None
        self._timezone = None
        self._updated_at = None
        self._workspaces = None
        self.discriminator = None

        if api_token is not None:
            self.api_token = api_token
        if at is not None:
            self.at = at
        if authorization_updated_at is not None:
            self.authorization_updated_at = authorization_updated_at
        if beginning_of_week is not None:
            self.beginning_of_week = beginning_of_week
        if clients is not None:
            self.clients = clients
        if country_id is not None:
            self.country_id = country_id
        if created_at is not None:
            self.created_at = created_at
        if default_workspace_id is not None:
            self.default_workspace_id = default_workspace_id
        if email is not None:
            self.email = email
        if fullname is not None:
            self.fullname = fullname
        if has_password is not None:
            self.has_password = has_password
        if id is not None:
            self.id = id
        if image_url is not None:
            self.image_url = image_url
        if intercom_hash is not None:
            self.intercom_hash = intercom_hash
        if oauth_providers is not None:
            self.oauth_providers = oauth_providers
        if openid_email is not None:
            self.openid_email = openid_email
        if openid_enabled is not None:
            self.openid_enabled = openid_enabled
        if options is not None:
            self.options = options
        if projects is not None:
            self.projects = projects
        if tags is not None:
            self.tags = tags
        if tasks is not None:
            self.tasks = tasks
        if time_entries is not None:
            self.time_entries = time_entries
        if timezone is not None:
            self.timezone = timezone
        if updated_at is not None:
            self.updated_at = updated_at
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def api_token(self):
        """Gets the api_token of this RelatedUserWithRelated.  # noqa: E501

        will be omitted if empty  # noqa: E501

        :return: The api_token of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this RelatedUserWithRelated.

        will be omitted if empty  # noqa: E501

        :param api_token: The api_token of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def at(self):
        """Gets the at of this RelatedUserWithRelated.  # noqa: E501


        :return: The at of this RelatedUserWithRelated.  # noqa: E501
        :rtype: datetime
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this RelatedUserWithRelated.


        :param at: The at of this RelatedUserWithRelated.  # noqa: E501
        :type: datetime
        """

        self._at = at

    @property
    def authorization_updated_at(self):
        """Gets the authorization_updated_at of this RelatedUserWithRelated.  # noqa: E501

        AuthorizationUpdatedAt timestamp when the authorization user session object was last updated.  # noqa: E501

        :return: The authorization_updated_at of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._authorization_updated_at

    @authorization_updated_at.setter
    def authorization_updated_at(self, authorization_updated_at):
        """Sets the authorization_updated_at of this RelatedUserWithRelated.

        AuthorizationUpdatedAt timestamp when the authorization user session object was last updated.  # noqa: E501

        :param authorization_updated_at: The authorization_updated_at of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._authorization_updated_at = authorization_updated_at

    @property
    def beginning_of_week(self):
        """Gets the beginning_of_week of this RelatedUserWithRelated.  # noqa: E501


        :return: The beginning_of_week of this RelatedUserWithRelated.  # noqa: E501
        :rtype: int
        """
        return self._beginning_of_week

    @beginning_of_week.setter
    def beginning_of_week(self, beginning_of_week):
        """Sets the beginning_of_week of this RelatedUserWithRelated.


        :param beginning_of_week: The beginning_of_week of this RelatedUserWithRelated.  # noqa: E501
        :type: int
        """

        self._beginning_of_week = beginning_of_week

    @property
    def clients(self):
        """Gets the clients of this RelatedUserWithRelated.  # noqa: E501

        Clients, null if with_related_data was not set to true or if the user does not have any clients  # noqa: E501

        :return: The clients of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[ModelsClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this RelatedUserWithRelated.

        Clients, null if with_related_data was not set to true or if the user does not have any clients  # noqa: E501

        :param clients: The clients of this RelatedUserWithRelated.  # noqa: E501
        :type: list[ModelsClient]
        """

        self._clients = clients

    @property
    def country_id(self):
        """Gets the country_id of this RelatedUserWithRelated.  # noqa: E501


        :return: The country_id of this RelatedUserWithRelated.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this RelatedUserWithRelated.


        :param country_id: The country_id of this RelatedUserWithRelated.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def created_at(self):
        """Gets the created_at of this RelatedUserWithRelated.  # noqa: E501


        :return: The created_at of this RelatedUserWithRelated.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RelatedUserWithRelated.


        :param created_at: The created_at of this RelatedUserWithRelated.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def default_workspace_id(self):
        """Gets the default_workspace_id of this RelatedUserWithRelated.  # noqa: E501


        :return: The default_workspace_id of this RelatedUserWithRelated.  # noqa: E501
        :rtype: int
        """
        return self._default_workspace_id

    @default_workspace_id.setter
    def default_workspace_id(self, default_workspace_id):
        """Sets the default_workspace_id of this RelatedUserWithRelated.


        :param default_workspace_id: The default_workspace_id of this RelatedUserWithRelated.  # noqa: E501
        :type: int
        """

        self._default_workspace_id = default_workspace_id

    @property
    def email(self):
        """Gets the email of this RelatedUserWithRelated.  # noqa: E501


        :return: The email of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RelatedUserWithRelated.


        :param email: The email of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fullname(self):
        """Gets the fullname of this RelatedUserWithRelated.  # noqa: E501


        :return: The fullname of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this RelatedUserWithRelated.


        :param fullname: The fullname of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def has_password(self):
        """Gets the has_password of this RelatedUserWithRelated.  # noqa: E501


        :return: The has_password of this RelatedUserWithRelated.  # noqa: E501
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this RelatedUserWithRelated.


        :param has_password: The has_password of this RelatedUserWithRelated.  # noqa: E501
        :type: bool
        """

        self._has_password = has_password

    @property
    def id(self):
        """Gets the id of this RelatedUserWithRelated.  # noqa: E501


        :return: The id of this RelatedUserWithRelated.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelatedUserWithRelated.


        :param id: The id of this RelatedUserWithRelated.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this RelatedUserWithRelated.  # noqa: E501


        :return: The image_url of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this RelatedUserWithRelated.


        :param image_url: The image_url of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def intercom_hash(self):
        """Gets the intercom_hash of this RelatedUserWithRelated.  # noqa: E501

        will be omitted if empty  # noqa: E501

        :return: The intercom_hash of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._intercom_hash

    @intercom_hash.setter
    def intercom_hash(self, intercom_hash):
        """Sets the intercom_hash of this RelatedUserWithRelated.

        will be omitted if empty  # noqa: E501

        :param intercom_hash: The intercom_hash of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._intercom_hash = intercom_hash

    @property
    def oauth_providers(self):
        """Gets the oauth_providers of this RelatedUserWithRelated.  # noqa: E501


        :return: The oauth_providers of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[str]
        """
        return self._oauth_providers

    @oauth_providers.setter
    def oauth_providers(self, oauth_providers):
        """Sets the oauth_providers of this RelatedUserWithRelated.


        :param oauth_providers: The oauth_providers of this RelatedUserWithRelated.  # noqa: E501
        :type: list[str]
        """

        self._oauth_providers = oauth_providers

    @property
    def openid_email(self):
        """Gets the openid_email of this RelatedUserWithRelated.  # noqa: E501


        :return: The openid_email of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._openid_email

    @openid_email.setter
    def openid_email(self, openid_email):
        """Sets the openid_email of this RelatedUserWithRelated.


        :param openid_email: The openid_email of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._openid_email = openid_email

    @property
    def openid_enabled(self):
        """Gets the openid_enabled of this RelatedUserWithRelated.  # noqa: E501


        :return: The openid_enabled of this RelatedUserWithRelated.  # noqa: E501
        :rtype: bool
        """
        return self._openid_enabled

    @openid_enabled.setter
    def openid_enabled(self, openid_enabled):
        """Sets the openid_enabled of this RelatedUserWithRelated.


        :param openid_enabled: The openid_enabled of this RelatedUserWithRelated.  # noqa: E501
        :type: bool
        """

        self._openid_enabled = openid_enabled

    @property
    def options(self):
        """Gets the options of this RelatedUserWithRelated.  # noqa: E501

        will be omitted if empty  # noqa: E501

        :return: The options of this RelatedUserWithRelated.  # noqa: E501
        :rtype: ModelsOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this RelatedUserWithRelated.

        will be omitted if empty  # noqa: E501

        :param options: The options of this RelatedUserWithRelated.  # noqa: E501
        :type: ModelsOptions
        """

        self._options = options

    @property
    def projects(self):
        """Gets the projects of this RelatedUserWithRelated.  # noqa: E501

        Projects, null if with_related_data was not set to true or if the user does not have any projects  # noqa: E501

        :return: The projects of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[ModelsProject]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this RelatedUserWithRelated.

        Projects, null if with_related_data was not set to true or if the user does not have any projects  # noqa: E501

        :param projects: The projects of this RelatedUserWithRelated.  # noqa: E501
        :type: list[ModelsProject]
        """

        self._projects = projects

    @property
    def tags(self):
        """Gets the tags of this RelatedUserWithRelated.  # noqa: E501

        Tags, null if with_related_data was not set to true, or if the user does not have any tags  # noqa: E501

        :return: The tags of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[ModelsTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RelatedUserWithRelated.

        Tags, null if with_related_data was not set to true, or if the user does not have any tags  # noqa: E501

        :param tags: The tags of this RelatedUserWithRelated.  # noqa: E501
        :type: list[ModelsTag]
        """

        self._tags = tags

    @property
    def tasks(self):
        """Gets the tasks of this RelatedUserWithRelated.  # noqa: E501

        Tasks, null if with_related_data was not set to true or if the user does not have any tasks  # noqa: E501

        :return: The tasks of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[ModelsTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this RelatedUserWithRelated.

        Tasks, null if with_related_data was not set to true or if the user does not have any tasks  # noqa: E501

        :param tasks: The tasks of this RelatedUserWithRelated.  # noqa: E501
        :type: list[ModelsTask]
        """

        self._tasks = tasks

    @property
    def time_entries(self):
        """Gets the time_entries of this RelatedUserWithRelated.  # noqa: E501

        TimeEntries, null if with_related_data was not set to true or if the user does not have any time entries  # noqa: E501

        :return: The time_entries of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[ModelsTimeEntry]
        """
        return self._time_entries

    @time_entries.setter
    def time_entries(self, time_entries):
        """Sets the time_entries of this RelatedUserWithRelated.

        TimeEntries, null if with_related_data was not set to true or if the user does not have any time entries  # noqa: E501

        :param time_entries: The time_entries of this RelatedUserWithRelated.  # noqa: E501
        :type: list[ModelsTimeEntry]
        """

        self._time_entries = time_entries

    @property
    def timezone(self):
        """Gets the timezone of this RelatedUserWithRelated.  # noqa: E501


        :return: The timezone of this RelatedUserWithRelated.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this RelatedUserWithRelated.


        :param timezone: The timezone of this RelatedUserWithRelated.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def updated_at(self):
        """Gets the updated_at of this RelatedUserWithRelated.  # noqa: E501


        :return: The updated_at of this RelatedUserWithRelated.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RelatedUserWithRelated.


        :param updated_at: The updated_at of this RelatedUserWithRelated.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def workspaces(self):
        """Gets the workspaces of this RelatedUserWithRelated.  # noqa: E501

        Workspaces, null if with_related_data was not set to true or if the user does not have any workspaces  # noqa: E501

        :return: The workspaces of this RelatedUserWithRelated.  # noqa: E501
        :rtype: list[WorkspaceWorkspace]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this RelatedUserWithRelated.

        Workspaces, null if with_related_data was not set to true or if the user does not have any workspaces  # noqa: E501

        :param workspaces: The workspaces of this RelatedUserWithRelated.  # noqa: E501
        :type: list[WorkspaceWorkspace]
        """

        self._workspaces = workspaces

    def to_dict(self):
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
        if issubclass(RelatedUserWithRelated, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelatedUserWithRelated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedUserWithRelated):
            return True

        return self.to_dict() != other.to_dict()
