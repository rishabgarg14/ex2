import unittest
from tests.home.header_test import HeaderTests
from tests.home.footer_test import FooterTests
from pages.home.footer_page import FooterPage
from pages.home.header_page import HeaderPage

ts1 = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
ts2 = unittest.TestLoader().loadTestsFromTestCase(FooterTests)

regressionTest = unittest.TestSuite([ts1, ts2])

unittest.TextTestRunner(verbosity=2).run(regressionTest)
