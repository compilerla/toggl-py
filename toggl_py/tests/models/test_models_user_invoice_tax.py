"""
Public Toggl API. Note: We use BasicAuth in a specific way. By the standard you provide `Authentication` header with `base64(user_name:password)` as a `credential`. In our case it will be `base64(user_name:api_token)`.  # noqa: E501

This file is auto generated by the swagger code generator program.
Do not edit this file manually.

OpenAPI spec version: 9
Generated by: https://github.com/compilerla/toggl-py
"""

import pytest  # noqa: F401
import toggl  # noqa: F401
from toggl.models.models_user_invoice_tax import ModelsUserInvoiceTax  # noqa: E501


def test_ModelsUserInvoiceTax():
    model = ModelsUserInvoiceTax()  # noqa: E501

    assert model
