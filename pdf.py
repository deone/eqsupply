from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors

from django.conf import settings
from django.http import HttpResponse, Http404

from eqsupply import helpers as h

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]

style = getSampleStyleSheet()

page_info = "AERIX Global Solutions Nig Ltd. RC 683490. VAT - TIN: 02411144-0001/VIVIO. Thank you for your Business!"

def para_user_detail(first_name, last_name, company, quotation_no, quotation_date, email):
    return "<para leftIndent=-33><b>Attn:</b> " + first_name + " " + last_name + \
	    "<br/><b>Company:</b> " + company + \
	    "<br/><b>Quotation No:</b> " + quotation_no + \
	    "<br/><b>Date:</b> " + str(h.format_date(quotation_date)) + \
	    "<br/><b>Email:</b> " + email + "</para>"

def list_table_data(quotation):
    data = [
	[
	    Paragraph('<para fontSize=9><b>S/N</b></para>', style["BodyText"]), \
	    Paragraph('<para fontSize=9><b>Product ID</b></para>', style["BodyText"]), \
	    Paragraph('<para fontSize=9><b>Reference</b></para>', style["BodyText"]), \
	    Paragraph('<para fontSize=9><b>Description</b></para>', style["BodyText"]), \
	    Paragraph('<para fontSize=9><b>Qty</b></para>', style["BodyText"]), \
	    Paragraph('<para fontSize=9><b>Price/Unit (GBP)</b></para>', style["BodyText"]), \
	    Paragraph('<para fontSize=9><b>Total (GBP)</b></para>', style["BodyText"])
	]
    ]

    line_item_list = h.change_id_serialno(list(quotation.lineitem_set.all()))

    for l in line_item_list:
	row = []
	row.append(str(l.id))
	row.append(str(l.product.product.code))
	row.append(str(l.product.part_number))
	row.append(Paragraph(l.product.description, style["BodyText"]))
	row.append(str(l.quantity))
	row.append(str(l.cost_per_unit))
	row.append(str(l.cost))
	data.append(row)

    quotation_details = return_quote_details(quotation.cost, quotation.courier_charge)

    data.append(["", "", "", "", "", "Sub-Total", str(quotation_details[0])])
    data.append(["", "", "", "", "", "VAT @ 5%", str(quotation_details[1])])
    data.append(["", "", "", "", "", "Logistics", str(quotation_details[2])])
    data.append(["", "", "", "", "", Paragraph('<b>Grand Total</b>', style["BodyText"]), str(quotation_details[3])])

    return data

def return_quote_details(cost, courier_charge):
    quotation_cost = float(cost)
    courier_charge = float(courier_charge)

    vat = settings.VAT/100.0 * quotation_cost

    markup = h.compute_markup(quotation_cost, courier_charge)
    logistics = courier_charge + markup

    total = quotation_cost + vat + logistics

    return (quotation_cost, vat, logistics, total)

def return_other_details():
    return """<para leftIndent=-33><b>Terms and Conditions</b><br/><br/>
    <seq/>. Full payment due at time of order.<br/>
    <seq/>. Allow 2-4 weeks after receipt of payment for delivery of items.<br/>
    <seq/>. Quotation is valid until 21 days after issue.<br/><br/>
    <b>Banking Details</b><br/><br/>
    <b>Company Name:</b> Aerix Global Solutions Nigeria Ltd.<br/>
    <b>Banking Institution:</b> Diamond Bank Plc.<br/>
    <b>Bank Branch:</b> King George V Branch, Onikan, Lagos.<br/>
    <b>Account Name:</b> Aerix Global Solutions Nigeria Ltd.<br/>
    <b>Account Number:</b> 1202350000543<br/><br/>
    Feel free to contact us if you have any questions concerning this quote.
    """

def page_format(canvas, doc):
    canvas.saveState()
    canvas.drawImage("site_media/img/logo_small.gif", PAGE_WIDTH/1.65, PAGE_HEIGHT-108)
    canvas.setFont("Times-Roman", 7)
    canvas.drawString(inch, 0.75*inch, "Page %d %s" % (doc.page, page_info))
    canvas.restoreState()

def go(quotation, user, user_account):
    story = []
    story.append(Spacer(0.5, 0.3*inch))
    story.append(Paragraph(settings.AERIX_ADDRESS, style["BodyText"]))
    story.append(Spacer(0.5, 0.1*inch))

    user_detail = para_user_detail(user.first_name, user.last_name, user_account.company, \
	    quotation.quotation_no, str(quotation.time_created.date()), user.email)
    story.append(Paragraph(user_detail, style["BodyText"]))

    story.append(Spacer(0.5, 0.2*inch))

    table_data = list_table_data(quotation)
    t=Table(table_data)
    t.setStyle(TableStyle([
			    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
			]))

    t._argW = [0.35*inch, 1.1*inch, 1.1*inch, 2*inch, 0.35*inch, 1.1*inch, 1.1*inch]

    story.append(t)

    story.append(Spacer(0.5, 0.2*inch))

    other_details = return_other_details()
    story.append(Paragraph(other_details, style["BodyText"]))

    doc = SimpleDocTemplate(quotation.quotation_no + ".pdf", title="%s %s" % ("Aerix Equipment Supply Quotation", quotation.quotation_no))
    return doc.build(story, onFirstPage=page_format, onLaterPages=page_format)
