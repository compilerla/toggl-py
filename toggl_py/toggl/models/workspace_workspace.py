"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pprint
import re  # noqa: F401

from toggl.configuration import Configuration


class WorkspaceWorkspace:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "admin": "bool",
        "api_token": "str",
        "at": "str",
        "business_ws": "bool",
        "csv_upload": "ModelsCsvUpload",
        "default_currency": "str",
        "default_hourly_rate": "float",
        "hide_start_end_times": "bool",
        "ical_enabled": "bool",
        "ical_url": "str",
        "id": "int",
        "last_modified": "str",
        "logo_url": "str",
        "max_data_retention_days": "int",
        "name": "str",
        "only_admins_may_create_projects": "bool",
        "only_admins_may_create_tags": "bool",
        "only_admins_see_billable_rates": "bool",
        "only_admins_see_team_dashboard": "bool",
        "organization_id": "int",
        "permissions": "str",
        "premium": "bool",
        "profile": "int",
        "projects_billable_by_default": "bool",
        "projects_private_by_default": "bool",
        "rate_last_updated": "str",
        "reports_collapse": "bool",
        "role": "str",
        "rounding": "int",
        "rounding_minutes": "int",
        "server_deleted_at": "datetime",
        "subscription": "ModelsSubscription",
        "suspended_at": "datetime",
        "te_constraints": "ModelsTimeEntryConstraints",
        "working_hours_in_minutes": "int",
    }

    attribute_map = {
        "admin": "admin",
        "api_token": "api_token",
        "at": "at",
        "business_ws": "business_ws",
        "csv_upload": "csv_upload",
        "default_currency": "default_currency",
        "default_hourly_rate": "default_hourly_rate",
        "hide_start_end_times": "hide_start_end_times",
        "ical_enabled": "ical_enabled",
        "ical_url": "ical_url",
        "id": "id",
        "last_modified": "last_modified",
        "logo_url": "logo_url",
        "max_data_retention_days": "max_data_retention_days",
        "name": "name",
        "only_admins_may_create_projects": "only_admins_may_create_projects",
        "only_admins_may_create_tags": "only_admins_may_create_tags",
        "only_admins_see_billable_rates": "only_admins_see_billable_rates",
        "only_admins_see_team_dashboard": "only_admins_see_team_dashboard",
        "organization_id": "organization_id",
        "permissions": "permissions",
        "premium": "premium",
        "profile": "profile",
        "projects_billable_by_default": "projects_billable_by_default",
        "projects_private_by_default": "projects_private_by_default",
        "rate_last_updated": "rate_last_updated",
        "reports_collapse": "reports_collapse",
        "role": "role",
        "rounding": "rounding",
        "rounding_minutes": "rounding_minutes",
        "server_deleted_at": "server_deleted_at",
        "subscription": "subscription",
        "suspended_at": "suspended_at",
        "te_constraints": "te_constraints",
        "working_hours_in_minutes": "working_hours_in_minutes",
    }

    def __init__(
        self,
        admin=None,
        api_token=None,
        at=None,
        business_ws=None,
        csv_upload=None,
        default_currency=None,
        default_hourly_rate=None,
        hide_start_end_times=None,
        ical_enabled=None,
        ical_url=None,
        id=None,
        last_modified=None,
        logo_url=None,
        max_data_retention_days=None,
        name=None,
        only_admins_may_create_projects=None,
        only_admins_may_create_tags=None,
        only_admins_see_billable_rates=None,
        only_admins_see_team_dashboard=None,
        organization_id=None,
        permissions=None,
        premium=None,
        profile=None,
        projects_billable_by_default=None,
        projects_private_by_default=None,
        rate_last_updated=None,
        reports_collapse=None,
        role=None,
        rounding=None,
        rounding_minutes=None,
        server_deleted_at=None,
        subscription=None,
        suspended_at=None,
        te_constraints=None,
        working_hours_in_minutes=None,
        _configuration=None,
    ):  # noqa: E501
        """WorkspaceWorkspace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin = None
        self._api_token = None
        self._at = None
        self._business_ws = None
        self._csv_upload = None
        self._default_currency = None
        self._default_hourly_rate = None
        self._hide_start_end_times = None
        self._ical_enabled = None
        self._ical_url = None
        self._id = None
        self._last_modified = None
        self._logo_url = None
        self._max_data_retention_days = None
        self._name = None
        self._only_admins_may_create_projects = None
        self._only_admins_may_create_tags = None
        self._only_admins_see_billable_rates = None
        self._only_admins_see_team_dashboard = None
        self._organization_id = None
        self._permissions = None
        self._premium = None
        self._profile = None
        self._projects_billable_by_default = None
        self._projects_private_by_default = None
        self._rate_last_updated = None
        self._reports_collapse = None
        self._role = None
        self._rounding = None
        self._rounding_minutes = None
        self._server_deleted_at = None
        self._subscription = None
        self._suspended_at = None
        self._te_constraints = None
        self._working_hours_in_minutes = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if api_token is not None:
            self.api_token = api_token
        if at is not None:
            self.at = at
        if business_ws is not None:
            self.business_ws = business_ws
        if csv_upload is not None:
            self.csv_upload = csv_upload
        if default_currency is not None:
            self.default_currency = default_currency
        if default_hourly_rate is not None:
            self.default_hourly_rate = default_hourly_rate
        if hide_start_end_times is not None:
            self.hide_start_end_times = hide_start_end_times
        if ical_enabled is not None:
            self.ical_enabled = ical_enabled
        if ical_url is not None:
            self.ical_url = ical_url
        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if logo_url is not None:
            self.logo_url = logo_url
        if max_data_retention_days is not None:
            self.max_data_retention_days = max_data_retention_days
        if name is not None:
            self.name = name
        if only_admins_may_create_projects is not None:
            self.only_admins_may_create_projects = only_admins_may_create_projects
        if only_admins_may_create_tags is not None:
            self.only_admins_may_create_tags = only_admins_may_create_tags
        if only_admins_see_billable_rates is not None:
            self.only_admins_see_billable_rates = only_admins_see_billable_rates
        if only_admins_see_team_dashboard is not None:
            self.only_admins_see_team_dashboard = only_admins_see_team_dashboard
        if organization_id is not None:
            self.organization_id = organization_id
        if permissions is not None:
            self.permissions = permissions
        if premium is not None:
            self.premium = premium
        if profile is not None:
            self.profile = profile
        if projects_billable_by_default is not None:
            self.projects_billable_by_default = projects_billable_by_default
        if projects_private_by_default is not None:
            self.projects_private_by_default = projects_private_by_default
        if rate_last_updated is not None:
            self.rate_last_updated = rate_last_updated
        if reports_collapse is not None:
            self.reports_collapse = reports_collapse
        if role is not None:
            self.role = role
        if rounding is not None:
            self.rounding = rounding
        if rounding_minutes is not None:
            self.rounding_minutes = rounding_minutes
        if server_deleted_at is not None:
            self.server_deleted_at = server_deleted_at
        if subscription is not None:
            self.subscription = subscription
        if suspended_at is not None:
            self.suspended_at = suspended_at
        if te_constraints is not None:
            self.te_constraints = te_constraints
        if working_hours_in_minutes is not None:
            self.working_hours_in_minutes = working_hours_in_minutes

    @property
    def admin(self):
        """Gets the admin of this WorkspaceWorkspace.  # noqa: E501

        Current user is workspace admin  # noqa: E501

        :return: The admin of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this WorkspaceWorkspace.

        Current user is workspace admin  # noqa: E501

        :param admin: The admin of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def api_token(self):
        """Gets the api_token of this WorkspaceWorkspace.  # noqa: E501

        deprecated  # noqa: E501

        :return: The api_token of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this WorkspaceWorkspace.

        deprecated  # noqa: E501

        :param api_token: The api_token of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def at(self):
        """Gets the at of this WorkspaceWorkspace.  # noqa: E501

        Timestamp of last workspace change  # noqa: E501

        :return: The at of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this WorkspaceWorkspace.

        Timestamp of last workspace change  # noqa: E501

        :param at: The at of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._at = at

    @property
    def business_ws(self):
        """Gets the business_ws of this WorkspaceWorkspace.  # noqa: E501

        Workspace on Premium subscription  # noqa: E501

        :return: The business_ws of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._business_ws

    @business_ws.setter
    def business_ws(self, business_ws):
        """Sets the business_ws of this WorkspaceWorkspace.

        Workspace on Premium subscription  # noqa: E501

        :param business_ws: The business_ws of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._business_ws = business_ws

    @property
    def csv_upload(self):
        """Gets the csv_upload of this WorkspaceWorkspace.  # noqa: E501

        CSV upload data  # noqa: E501

        :return: The csv_upload of this WorkspaceWorkspace.  # noqa: E501
        :rtype: ModelsCsvUpload
        """
        return self._csv_upload

    @csv_upload.setter
    def csv_upload(self, csv_upload):
        """Sets the csv_upload of this WorkspaceWorkspace.

        CSV upload data  # noqa: E501

        :param csv_upload: The csv_upload of this WorkspaceWorkspace.  # noqa: E501
        :type: ModelsCsvUpload
        """

        self._csv_upload = csv_upload

    @property
    def default_currency(self):
        """Gets the default_currency of this WorkspaceWorkspace.  # noqa: E501

        Default currency, premium feature, optional, only for existing WS, will be 'USD' initially  # noqa: E501

        :return: The default_currency of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this WorkspaceWorkspace.

        Default currency, premium feature, optional, only for existing WS, will be 'USD' initially  # noqa: E501

        :param default_currency: The default_currency of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._default_currency = default_currency

    @property
    def default_hourly_rate(self):
        """Gets the default_hourly_rate of this WorkspaceWorkspace.  # noqa: E501

        The default hourly rate, premium feature, optional, only for existing WS, will be 0.0 initially  # noqa: E501

        :return: The default_hourly_rate of this WorkspaceWorkspace.  # noqa: E501
        :rtype: float
        """
        return self._default_hourly_rate

    @default_hourly_rate.setter
    def default_hourly_rate(self, default_hourly_rate):
        """Sets the default_hourly_rate of this WorkspaceWorkspace.

        The default hourly rate, premium feature, optional, only for existing WS, will be 0.0 initially  # noqa: E501

        :param default_hourly_rate: The default_hourly_rate of this WorkspaceWorkspace.  # noqa: E501
        :type: float
        """

        self._default_hourly_rate = default_hourly_rate

    @property
    def hide_start_end_times(self):
        """Gets the hide_start_end_times of this WorkspaceWorkspace.  # noqa: E501


        :return: The hide_start_end_times of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._hide_start_end_times

    @hide_start_end_times.setter
    def hide_start_end_times(self, hide_start_end_times):
        """Sets the hide_start_end_times of this WorkspaceWorkspace.


        :param hide_start_end_times: The hide_start_end_times of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._hide_start_end_times = hide_start_end_times

    @property
    def ical_enabled(self):
        """Gets the ical_enabled of this WorkspaceWorkspace.  # noqa: E501

        Calendar integration enabled  # noqa: E501

        :return: The ical_enabled of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._ical_enabled

    @ical_enabled.setter
    def ical_enabled(self, ical_enabled):
        """Sets the ical_enabled of this WorkspaceWorkspace.

        Calendar integration enabled  # noqa: E501

        :param ical_enabled: The ical_enabled of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._ical_enabled = ical_enabled

    @property
    def ical_url(self):
        """Gets the ical_url of this WorkspaceWorkspace.  # noqa: E501

        URL of calendar  # noqa: E501

        :return: The ical_url of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._ical_url

    @ical_url.setter
    def ical_url(self, ical_url):
        """Sets the ical_url of this WorkspaceWorkspace.

        URL of calendar  # noqa: E501

        :param ical_url: The ical_url of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._ical_url = ical_url

    @property
    def id(self):
        """Gets the id of this WorkspaceWorkspace.  # noqa: E501

        Identifier of the workspace  # noqa: E501

        :return: The id of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceWorkspace.

        Identifier of the workspace  # noqa: E501

        :param id: The id of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this WorkspaceWorkspace.  # noqa: E501

        Last modification of data in the workspace  # noqa: E501

        :return: The last_modified of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this WorkspaceWorkspace.

        Last modification of data in the workspace  # noqa: E501

        :param last_modified: The last_modified of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def logo_url(self):
        """Gets the logo_url of this WorkspaceWorkspace.  # noqa: E501

        URL of workspace logo  # noqa: E501

        :return: The logo_url of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this WorkspaceWorkspace.

        URL of workspace logo  # noqa: E501

        :param logo_url: The logo_url of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def max_data_retention_days(self):
        """Gets the max_data_retention_days of this WorkspaceWorkspace.  # noqa: E501

        How far back free workspaces can access data.  # noqa: E501

        :return: The max_data_retention_days of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._max_data_retention_days

    @max_data_retention_days.setter
    def max_data_retention_days(self, max_data_retention_days):
        """Sets the max_data_retention_days of this WorkspaceWorkspace.

        How far back free workspaces can access data.  # noqa: E501

        :param max_data_retention_days: The max_data_retention_days of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._max_data_retention_days = max_data_retention_days

    @property
    def name(self):
        """Gets the name of this WorkspaceWorkspace.  # noqa: E501

        Name of the workspace  # noqa: E501

        :return: The name of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceWorkspace.

        Name of the workspace  # noqa: E501

        :param name: The name of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def only_admins_may_create_projects(self):
        """Gets the only_admins_may_create_projects of this WorkspaceWorkspace.  # noqa: E501

        Only admins will be able to create projects, optional, only for existing WS, will be false initially  # noqa: E501

        :return: The only_admins_may_create_projects of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._only_admins_may_create_projects

    @only_admins_may_create_projects.setter
    def only_admins_may_create_projects(self, only_admins_may_create_projects):
        """Sets the only_admins_may_create_projects of this WorkspaceWorkspace.

        Only admins will be able to create projects, optional, only for existing WS, will be false initially  # noqa: E501

        :param only_admins_may_create_projects: The only_admins_may_create_projects of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._only_admins_may_create_projects = only_admins_may_create_projects

    @property
    def only_admins_may_create_tags(self):
        """Gets the only_admins_may_create_tags of this WorkspaceWorkspace.  # noqa: E501

        Only admins will be able to create tags, optional, only for existing WS, will be false initially  # noqa: E501

        :return: The only_admins_may_create_tags of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._only_admins_may_create_tags

    @only_admins_may_create_tags.setter
    def only_admins_may_create_tags(self, only_admins_may_create_tags):
        """Sets the only_admins_may_create_tags of this WorkspaceWorkspace.

        Only admins will be able to create tags, optional, only for existing WS, will be false initially  # noqa: E501

        :param only_admins_may_create_tags: The only_admins_may_create_tags of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._only_admins_may_create_tags = only_admins_may_create_tags

    @property
    def only_admins_see_billable_rates(self):
        """Gets the only_admins_see_billable_rates of this WorkspaceWorkspace.  # noqa: E501

        Whether only admins will be able to see billable rates, premium feature, optional, only for existing WS. Will be false initially  # noqa: E501

        :return: The only_admins_see_billable_rates of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._only_admins_see_billable_rates

    @only_admins_see_billable_rates.setter
    def only_admins_see_billable_rates(self, only_admins_see_billable_rates):
        """Sets the only_admins_see_billable_rates of this WorkspaceWorkspace.

        Whether only admins will be able to see billable rates, premium feature, optional, only for existing WS. Will be false initially  # noqa: E501

        :param only_admins_see_billable_rates: The only_admins_see_billable_rates of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._only_admins_see_billable_rates = only_admins_see_billable_rates

    @property
    def only_admins_see_team_dashboard(self):
        """Gets the only_admins_see_team_dashboard of this WorkspaceWorkspace.  # noqa: E501

        Only admins will be able to see the team dashboard, optional, only for existing WS, will be false initially  # noqa: E501

        :return: The only_admins_see_team_dashboard of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._only_admins_see_team_dashboard

    @only_admins_see_team_dashboard.setter
    def only_admins_see_team_dashboard(self, only_admins_see_team_dashboard):
        """Sets the only_admins_see_team_dashboard of this WorkspaceWorkspace.

        Only admins will be able to see the team dashboard, optional, only for existing WS, will be false initially  # noqa: E501

        :param only_admins_see_team_dashboard: The only_admins_see_team_dashboard of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._only_admins_see_team_dashboard = only_admins_see_team_dashboard

    @property
    def organization_id(self):
        """Gets the organization_id of this WorkspaceWorkspace.  # noqa: E501

        Identifier of the organization  # noqa: E501

        :return: The organization_id of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this WorkspaceWorkspace.

        Identifier of the organization  # noqa: E501

        :param organization_id: The organization_id of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def permissions(self):
        """Gets the permissions of this WorkspaceWorkspace.  # noqa: E501

        Permissions list  # noqa: E501

        :return: The permissions of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this WorkspaceWorkspace.

        Permissions list  # noqa: E501

        :param permissions: The permissions of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._permissions = permissions

    @property
    def premium(self):
        """Gets the premium of this WorkspaceWorkspace.  # noqa: E501

        Workspace on Starter subscription  # noqa: E501

        :return: The premium of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._premium

    @premium.setter
    def premium(self, premium):
        """Sets the premium of this WorkspaceWorkspace.

        Workspace on Starter subscription  # noqa: E501

        :param premium: The premium of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._premium = premium

    @property
    def profile(self):
        """Gets the profile of this WorkspaceWorkspace.  # noqa: E501

        deprecated  # noqa: E501

        :return: The profile of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this WorkspaceWorkspace.

        deprecated  # noqa: E501

        :param profile: The profile of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._profile = profile

    @property
    def projects_billable_by_default(self):
        """Gets the projects_billable_by_default of this WorkspaceWorkspace.  # noqa: E501

        New projects billable by default  # noqa: E501

        :return: The projects_billable_by_default of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._projects_billable_by_default

    @projects_billable_by_default.setter
    def projects_billable_by_default(self, projects_billable_by_default):
        """Sets the projects_billable_by_default of this WorkspaceWorkspace.

        New projects billable by default  # noqa: E501

        :param projects_billable_by_default: The projects_billable_by_default of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._projects_billable_by_default = projects_billable_by_default

    @property
    def projects_private_by_default(self):
        """Gets the projects_private_by_default of this WorkspaceWorkspace.  # noqa: E501

        Workspace setting for default project visbility.  # noqa: E501

        :return: The projects_private_by_default of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._projects_private_by_default

    @projects_private_by_default.setter
    def projects_private_by_default(self, projects_private_by_default):
        """Sets the projects_private_by_default of this WorkspaceWorkspace.

        Workspace setting for default project visbility.  # noqa: E501

        :param projects_private_by_default: The projects_private_by_default of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._projects_private_by_default = projects_private_by_default

    @property
    def rate_last_updated(self):
        """Gets the rate_last_updated of this WorkspaceWorkspace.  # noqa: E501

        Timestamp of last workspace rate update  # noqa: E501

        :return: The rate_last_updated of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._rate_last_updated

    @rate_last_updated.setter
    def rate_last_updated(self, rate_last_updated):
        """Sets the rate_last_updated of this WorkspaceWorkspace.

        Timestamp of last workspace rate update  # noqa: E501

        :param rate_last_updated: The rate_last_updated of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._rate_last_updated = rate_last_updated

    @property
    def reports_collapse(self):
        """Gets the reports_collapse of this WorkspaceWorkspace.  # noqa: E501

        Whether reports should be collapsed by default, optional, only for existing WS, will be true initially  # noqa: E501

        :return: The reports_collapse of this WorkspaceWorkspace.  # noqa: E501
        :rtype: bool
        """
        return self._reports_collapse

    @reports_collapse.setter
    def reports_collapse(self, reports_collapse):
        """Sets the reports_collapse of this WorkspaceWorkspace.

        Whether reports should be collapsed by default, optional, only for existing WS, will be true initially  # noqa: E501

        :param reports_collapse: The reports_collapse of this WorkspaceWorkspace.  # noqa: E501
        :type: bool
        """

        self._reports_collapse = reports_collapse

    @property
    def role(self):
        """Gets the role of this WorkspaceWorkspace.  # noqa: E501

        Role of the current user in the workspace  # noqa: E501

        :return: The role of this WorkspaceWorkspace.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this WorkspaceWorkspace.

        Role of the current user in the workspace  # noqa: E501

        :param role: The role of this WorkspaceWorkspace.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def rounding(self):
        """Gets the rounding of this WorkspaceWorkspace.  # noqa: E501

        Default rounding, premium feature, optional, only for existing WS. 0 - nearest, 1 - round up, -1 - round down  # noqa: E501

        :return: The rounding of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding):
        """Sets the rounding of this WorkspaceWorkspace.

        Default rounding, premium feature, optional, only for existing WS. 0 - nearest, 1 - round up, -1 - round down  # noqa: E501

        :param rounding: The rounding of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._rounding = rounding

    @property
    def rounding_minutes(self):
        """Gets the rounding_minutes of this WorkspaceWorkspace.  # noqa: E501

        Default rounding in minutes, premium feature, optional, only for existing WS  # noqa: E501

        :return: The rounding_minutes of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._rounding_minutes

    @rounding_minutes.setter
    def rounding_minutes(self, rounding_minutes):
        """Sets the rounding_minutes of this WorkspaceWorkspace.

        Default rounding in minutes, premium feature, optional, only for existing WS  # noqa: E501

        :param rounding_minutes: The rounding_minutes of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._rounding_minutes = rounding_minutes

    @property
    def server_deleted_at(self):
        """Gets the server_deleted_at of this WorkspaceWorkspace.  # noqa: E501

        Timestamp of deletion  # noqa: E501

        :return: The server_deleted_at of this WorkspaceWorkspace.  # noqa: E501
        :rtype: datetime
        """
        return self._server_deleted_at

    @server_deleted_at.setter
    def server_deleted_at(self, server_deleted_at):
        """Sets the server_deleted_at of this WorkspaceWorkspace.

        Timestamp of deletion  # noqa: E501

        :param server_deleted_at: The server_deleted_at of this WorkspaceWorkspace.  # noqa: E501
        :type: datetime
        """

        self._server_deleted_at = server_deleted_at

    @property
    def subscription(self):
        """Gets the subscription of this WorkspaceWorkspace.  # noqa: E501

        deprecated  # noqa: E501

        :return: The subscription of this WorkspaceWorkspace.  # noqa: E501
        :rtype: ModelsSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this WorkspaceWorkspace.

        deprecated  # noqa: E501

        :param subscription: The subscription of this WorkspaceWorkspace.  # noqa: E501
        :type: ModelsSubscription
        """

        self._subscription = subscription

    @property
    def suspended_at(self):
        """Gets the suspended_at of this WorkspaceWorkspace.  # noqa: E501

        Timestamp of suspension  # noqa: E501

        :return: The suspended_at of this WorkspaceWorkspace.  # noqa: E501
        :rtype: datetime
        """
        return self._suspended_at

    @suspended_at.setter
    def suspended_at(self, suspended_at):
        """Sets the suspended_at of this WorkspaceWorkspace.

        Timestamp of suspension  # noqa: E501

        :param suspended_at: The suspended_at of this WorkspaceWorkspace.  # noqa: E501
        :type: datetime
        """

        self._suspended_at = suspended_at

    @property
    def te_constraints(self):
        """Gets the te_constraints of this WorkspaceWorkspace.  # noqa: E501

        Time entry constraints setting  # noqa: E501

        :return: The te_constraints of this WorkspaceWorkspace.  # noqa: E501
        :rtype: ModelsTimeEntryConstraints
        """
        return self._te_constraints

    @te_constraints.setter
    def te_constraints(self, te_constraints):
        """Sets the te_constraints of this WorkspaceWorkspace.

        Time entry constraints setting  # noqa: E501

        :param te_constraints: The te_constraints of this WorkspaceWorkspace.  # noqa: E501
        :type: ModelsTimeEntryConstraints
        """

        self._te_constraints = te_constraints

    @property
    def working_hours_in_minutes(self):
        """Gets the working_hours_in_minutes of this WorkspaceWorkspace.  # noqa: E501

        Working hours in minutes  # noqa: E501

        :return: The working_hours_in_minutes of this WorkspaceWorkspace.  # noqa: E501
        :rtype: int
        """
        return self._working_hours_in_minutes

    @working_hours_in_minutes.setter
    def working_hours_in_minutes(self, working_hours_in_minutes):
        """Sets the working_hours_in_minutes of this WorkspaceWorkspace.

        Working hours in minutes  # noqa: E501

        :param working_hours_in_minutes: The working_hours_in_minutes of this WorkspaceWorkspace.  # noqa: E501
        :type: int
        """

        self._working_hours_in_minutes = working_hours_in_minutes

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
        if issubclass(WorkspaceWorkspace, dict):
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
        if not isinstance(other, WorkspaceWorkspace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceWorkspace):
            return True

        return self.to_dict() != other.to_dict()
