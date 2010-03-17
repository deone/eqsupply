import datetime

from eqsupply.test_helpers import EqsupplyTestCase

class QuoteTests(EqsupplyTestCase):
    def test_quotation(self):
	# content tests
	self.assertEquals(self.quotation.user, self.user)
	self.assert_(self.quotation.time_created < datetime.datetime.now())
	self.assertNotEqual(self.quotation.quotation_no, "")
	self.assertNotEqual(self.quotation.cost, "")
	self.assertNotEqual(self.quotation.status, True)

	# type tests
	self.assert_(isinstance(self.quotation.time_created, datetime.datetime))
	self.assert_(isinstance(self.quotation.quotation_no, str))
	self.assert_(isinstance(self.quotation.cost, str))
	self.assert_(isinstance(self.quotation.status, bool))

    def test_line_item(self):
	# content tests
	self.failUnlessEqual(self.line_item.quotation, self.quotation)
	self.failUnlessEqual(self.line_item.product, self.product_variant)
	self.failUnlessEqual(self.line_item.quantity, 20)
	self.failIfEqual(self.line_item.cost, 110)

	# type tests
	self.failUnless(isinstance(self.line_item.quantity, int))
	self.failUnless(isinstance(self.line_item.cost, str))
