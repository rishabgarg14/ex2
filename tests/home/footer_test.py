import unittest
from pages.home.footer_page import FooterPage
import pytest
from utilities.casestatus import CaseStatus


@pytest.mark.usefixtures("oneTimeSetUp")
class FooterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.fp = FooterPage(self.driver)
        self.ts = CaseStatus(self.driver)

    def setUp(self):
        self.fp.scrollToFooter()

    def test_facebookSocialIcon(self):
        result = self.fp.getFacebookIconStatus()
        self.ts.markFinal("test_facebookSocialIcon", result, "Footer_Verified Facebook Social Icon")

    def test_instagramSocialIcon(self):
        result = self.fp.getInstagramIconStatus()
        self.ts.markFinal("test_instagramSocialIcon", result, "Footer_Verified Instagram Social Icon")

    def test_pinterestSocialIcon(self):
        result = self.fp.getPinterestStatus()
        self.ts.markFinal("test_pinterestSocialIcon", result, "Footer_Verified Pinterest Social Icon")

    def test_linkedinSocialIcon(self):
        result = self.fp.getLinkedInIconStatus()
        self.ts.markFinal("test_linkedinSocialIcon", result, "Footer_Verified LinkedIn Social Icon")

    def test_youtubeSocialIcon(self):
        result = self.fp.getYoutubeIconStatus()
        self.ts.markFinal("test_youtubeSocialIcon", result, "Footer_Verified Instagram Social Icon")

    """
    def test_homeownersLink(self):
        result = self.fp.getHomeownersLinkStatus()
        self.ts.markFinal("test_homeownersLink", result, "Footer_Verified Homeowners Link")"""