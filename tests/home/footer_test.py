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

    def test_homeownersLink(self):
        result = self.fp.getHomeownersLinkStatus()
        self.ts.markFinal("test_homeownersLink", result, "Footer_Verified Homeowners Link")

    def test_faqLink(self):
        result = self.fp.getFAQLinkStatus()
        self.ts.markFinal("test_faqLink", result, "Footer_Verified FAQ Link")

    def test_emailSignupLink(self):
        result = self.fp.getEmailSignupLinkStatus()
        self.ts.markFinal("test_emailSignupLink", result, "Footer_Verified Homeowners Link")

    def test_contactUsLink(self):
        result = self.fp.getContactUsLinkStatus()
        self.ts.markFinal("test_contactUsLink", result, "Footer_Verified Contact Us Link")

    def test_careersLink(self):
        result = self.fp.getCareersLinkStatus()
        self.ts.markFinal("test_careersLink", result, "Footer_Verified Careers Link")

    def test_forMediaLink(self):
        result = self.fp.getForMediaLinkStatus()
        self.ts.markFinal("test_forMediaLink", result, "Footer_Verified For Media Link")

    def test_forRealtorsLink(self):
        result = self.fp.getForRealtorsLinkStatus()
        self.ts.markFinal("test_forRealtorsLink", result, "Footer_Verified For Realtors Link")

    def test_investorsLink(self):
        result = self.fp.getInvestorsLinkStatus()
        self.ts.markFinal("test_investorsLink", result, "Footer_Verified Investors Link")

    def test_privacyPolicyLink(self):
        result = self.fp.getPrivacyLinkStatus()
        self.ts.markFinal("test_privacyPolicyLink", result, "Footer_Verified Privacy Policy Link")

    def test_termsAndConditionsLink(self):
        result = self.fp.getTnCLinkStatus()
        self.ts.markFinal("test_termsAndConditionsLink", result, "Footer_Verified TnC Link")

    def test_accessibilityLink(self):
        result = self.fp.getAccessibilityLinkStatus()
        self.ts.markFinal("test_accessibilityLink", result, "Footer_Verified Accessibility Link")

    def test_copyrightText(self):
        result = self.fp.getCopyrightTextStatus()
        self.ts.markFinal("test_copyrightText", result, "Footer_Verified Copyright text")