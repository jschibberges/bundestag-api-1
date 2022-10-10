# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3
from deutschland.bundestag import api_client, configuration, schemas
from deutschland.bundestag.paths.blueprint_servlet_content_article_id_as_app_v2_newsarticle_xml import (  # noqa: E501
    get,
)

from deutschland import bundestag

from .. import ApiTestMixin


class TestBlueprintServletContentARTICLEIDAsAppV2NewsarticleXml(
    ApiTestMixin, unittest.TestCase
):
    """
    BlueprintServletContentARTICLEIDAsAppV2NewsarticleXml unit test stubs
        Artikel Details  # noqa: E501
    """

    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200


if __name__ == "__main__":
    unittest.main()
