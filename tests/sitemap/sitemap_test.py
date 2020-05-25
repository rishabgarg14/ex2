import unittest
import pytest
from utilities.casestatus import CaseStatus
from pages.sitemap.sitemap_page import SitemapPage
from Data.config import Config

@pytest.mark.usefixtures("oneTimeSetUp")
class SitemapTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.sm = SitemapPage(self.driver)
        self.ts = CaseStatus(self.driver)
        self.conf = Config()

    def test_sitemap_url(self):
        self.url = "https://www.renewedhope.us/sitemap.xml"
        # Test URL "https://www.mobilityservicesdirect.co.uk/sitemap.xml"
        # self.conf.base_url + "sitemap/sitemap.xml"
        result = self.sm.verifySitemapUrl(url=self.url, resultSheetName="SitemapResult")
        self.ts.markFinal("test_sitemap_url", result, "Verified all Sitemap Links")



