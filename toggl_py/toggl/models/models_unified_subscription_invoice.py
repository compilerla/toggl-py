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


class ModelsUnifiedSubscriptionInvoice:
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    swagger_types = {
        "creation_date": "datetime",
        "currency": "str",
        "description": "str",
        "hosted_url": "str",
        "id": "str",
        "invoice_number": "str",
        "pdf_url": "str",
        "total_amount": "int",
    }

    attribute_map = {
        "creation_date": "creation_date",
        "currency": "currency",
        "description": "description",
        "hosted_url": "hosted_url",
        "id": "id",
        "invoice_number": "invoice_number",
        "pdf_url": "pdf_url",
        "total_amount": "total_amount",
    }

    def __init__(
        self,
        creation_date=None,
        currency=None,
        description=None,
        hosted_url=None,
        id=None,
        invoice_number=None,
        pdf_url=None,
        total_amount=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelsUnifiedSubscriptionInvoice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_date = None
        self._currency = None
        self._description = None
        self._hosted_url = None
        self._id = None
        self._invoice_number = None
        self._pdf_url = None
        self._total_amount = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if currency is not None:
            self.currency = currency
        if description is not None:
            self.description = description
        if hosted_url is not None:
            self.hosted_url = hosted_url
        if id is not None:
            self.id = id
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if pdf_url is not None:
            self.pdf_url = pdf_url
        if total_amount is not None:
            self.total_amount = total_amount

    @property
    def creation_date(self):
        """Gets the creation_date of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The creation_date of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ModelsUnifiedSubscriptionInvoice.


        :param creation_date: The creation_date of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def currency(self):
        """Gets the currency of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The currency of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ModelsUnifiedSubscriptionInvoice.


        :param currency: The currency of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The description of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelsUnifiedSubscriptionInvoice.


        :param description: The description of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hosted_url(self):
        """Gets the hosted_url of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The hosted_url of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._hosted_url

    @hosted_url.setter
    def hosted_url(self, hosted_url):
        """Sets the hosted_url of this ModelsUnifiedSubscriptionInvoice.


        :param hosted_url: The hosted_url of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: str
        """

        self._hosted_url = hosted_url

    @property
    def id(self):
        """Gets the id of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The id of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsUnifiedSubscriptionInvoice.


        :param id: The id of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_number(self):
        """Gets the invoice_number of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The invoice_number of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this ModelsUnifiedSubscriptionInvoice.


        :param invoice_number: The invoice_number of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def pdf_url(self):
        """Gets the pdf_url of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The pdf_url of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: str
        """
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, pdf_url):
        """Sets the pdf_url of this ModelsUnifiedSubscriptionInvoice.


        :param pdf_url: The pdf_url of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: str
        """

        self._pdf_url = pdf_url

    @property
    def total_amount(self):
        """Gets the total_amount of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501


        :return: The total_amount of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :rtype: int
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this ModelsUnifiedSubscriptionInvoice.


        :param total_amount: The total_amount of this ModelsUnifiedSubscriptionInvoice.  # noqa: E501
        :type: int
        """

        self._total_amount = total_amount

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
        if issubclass(ModelsUnifiedSubscriptionInvoice, dict):
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
        if not isinstance(other, ModelsUnifiedSubscriptionInvoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelsUnifiedSubscriptionInvoice):
            return True

        return self.to_dict() != other.to_dict()
