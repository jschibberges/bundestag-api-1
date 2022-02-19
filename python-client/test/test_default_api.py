"""
    Bundestag: Live Informationen

    Bundestag Informationen API   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.bundestag.api.default_api import DefaultApi  # noqa: E501

from deutschland import bundestag


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get(self):
        """Test case for blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get

        Artikel Details  # noqa: E501
        """
        pass

    def test_iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get(self):
        """Test case for iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get

        Abruf eines Videos  # noqa: E501
        """
        pass

    def test_static_appdata_plenum_v2_conferences_xml_get(self):
        """Test case for static_appdata_plenum_v2_conferences_xml_get

        Sitzungstag übersicht  # noqa: E501
        """
        pass

    def test_static_appdata_plenum_v2_speaker_xml_get(self):
        """Test case for static_appdata_plenum_v2_speaker_xml_get

        Aktuelle Sprecher*in  # noqa: E501
        """
        pass

    def test_xml_v2_ausschuesse_ausschussid_xml_get(self):
        """Test case for xml_v2_ausschuesse_ausschussid_xml_get

        Übersicht über die Ausschüsse  # noqa: E501
        """
        pass

    def test_xml_v2_ausschuesse_index_xml_get(self):
        """Test case for xml_v2_ausschuesse_index_xml_get

        Übersicht über die Ausschüsse  # noqa: E501
        """
        pass

    def test_xml_v2_mdb_biografien_mdbid_xml_get(self):
        """Test case for xml_v2_mdb_biografien_mdbid_xml_get

        Abruf Details eines MDBS  # noqa: E501
        """
        pass

    def test_xml_v2_mdb_index_xml_get(self):
        """Test case for xml_v2_mdb_index_xml_get

        Übersicht über alle MDBS  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
