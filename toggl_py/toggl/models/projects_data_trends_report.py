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
from toggl.models.projects_data_trends_graph import ProjectsDataTrendsGraph  # noqa: F401


class ProjectsDataTrendsReport:
    """
    Attributes:
      swagger_types (dict): The key is attr name
                            and the value is attr type.
      attribute_map (dict): The key is attr name
                            and the value is json key in definition.
    """

    swagger_types = {"currency": "str", "graph": "ProjectsDataTrendsGraph"}

    attribute_map = {"currency": "currency", "graph": "graph"}

    def __init__(
        self, currency: str = None, graph: ProjectsDataTrendsGraph = None, _configuration: Configuration = None  # noqa: E501
    ):
        """
        ProjectsDataTrendsReport - a model defined in Swagger

        Parameters:
          currency (str): Optional
          graph (ProjectsDataTrendsGraph): Optional
        """
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._currency = None
        self._graph = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if graph is not None:
            self.graph = graph

    @property
    def currency(self) -> str:
        """Gets the currency of this ProjectsDataTrendsReport.  # noqa: E501


        :return: The currency of this ProjectsDataTrendsReport.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this ProjectsDataTrendsReport.


        :param currency: The currency of this ProjectsDataTrendsReport.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def graph(self) -> ProjectsDataTrendsGraph:
        """Gets the graph of this ProjectsDataTrendsReport.  # noqa: E501


        :return: The graph of this ProjectsDataTrendsReport.  # noqa: E501
        :rtype: ProjectsDataTrendsGraph
        """
        return self._graph

    @graph.setter
    def graph(self, graph: ProjectsDataTrendsGraph):
        """Sets the graph of this ProjectsDataTrendsReport.


        :param graph: The graph of this ProjectsDataTrendsReport.  # noqa: E501
        :type: ProjectsDataTrendsGraph
        """

        self._graph = graph

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
        if issubclass(ProjectsDataTrendsReport, dict):
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
        if not isinstance(other, ProjectsDataTrendsReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectsDataTrendsReport):
            return True

        return self.to_dict() != other.to_dict()
