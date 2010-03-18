import datetime

from eqsupply.test_helpers import EqsupplyTestCase

class QuoteTests(EqsupplyTestCase):
    def test_quotation(self):
	# content
	self.assert_(self.quotation.user == self.user)
	self.failIf(self.quotation.time_created > datetime.datetime.now())
	self.failIf(self.quotation.quotation_no == "")
	self.failIf(self.quotation.cost == "")
	self.failIf(self.quotation.status, True)

	# type
	self.assert_(isinstance(self.quotation.time_created, datetime.datetime))
	self.assert_(isinstance(self.quotation.status, bool))

    def test_line_item(self):
	self.failUnless(self.line_item.quotation == self.quotation)
	self.failUnless(self.line_item.product == self.product_variant)
	self.failUnless(self.line_item.quantity == 20)
	self.failIf(self.line_item.cost == "110")
