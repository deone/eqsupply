from eqsupply.test_helpers import EqsupplyTestCase

class QuoteTests(EqsupplyTestCase):
    def test_quotation(self):
	self.assertEquals(self.quotation.user.username, "deone")
	self.assertEquals(self.quotation.user.email, "alwaysdeone@yahoo.com")
