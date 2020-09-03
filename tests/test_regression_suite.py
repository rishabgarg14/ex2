import unittest
from tests.home.header_test import HeaderTests
from tests.home.footer_test import FooterTests
from tests.sitemap.sitemap_test import SitemapTests

ts1 = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
ts2 = unittest.TestLoader().loadTestsFromTestCase(FooterTests)
ts3 = unittest.TestLoader().loadTestsFromTestCase(SitemapTests)

regressionTest = unittest.TestSuite([ts1, ts2])

unittest.TextTestRunner(verbosity=2).run(regressionTest)
