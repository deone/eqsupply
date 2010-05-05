from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors

from django.http import HttpResponse, Http404

from eqsupply import settings
from eqsupply import helpers as h

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]

style = getSampleStyleSheet()

page_info = "AERIX Global Solutions Nig Ltd. RC 683490. VAT - TIN: 02411144-0001/VIVIO. Thank you for your Business!"

def first_page(canvas, doc):
    canvas.saveState()
    canvas.drawImage("site_media/img/logo_small.gif", PAGE_WIDTH/1.65, PAGE_HEIGHT-108)

    canvas.setFont("Times-Roman", 10)
    address = canvas.beginText()
    address.setTextOrigin(5.2*inch, 10*inch)
    address.textLines(settings.AERIX_ADDRESS)
    canvas.drawText(address)

    canvas.setFont("Times-Roman", 7)
    canvas.drawString(inch, 0.75*inch, "Page %d %s" % (doc.page, page_info))
    canvas.restoreState()

def other_pages(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 9)
    canvas.drawString(inch, 0.75*inch, "Page %d %s" % (doc.page, page_info))
    canvas.restoreState()

def go(quotation):
    doc = SimpleDocTemplate("quote.pdf")
    story = []
    story.append(Spacer(1, 2.5*inch))

    data =  [
	['S/N', 'Product ID', 'Reference', 'Description', 'Qty', 'Price/Unit (GBP)', 'Total (GBP)'],
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

    quotation_cost = float(quotation.cost)
    courier_charge = float(quotation.courier_charge)

    vat = settings.VAT/100.0 * quotation_cost

    markup = h.compute_markup(quotation_cost, courier_charge)
    logistics = courier_charge + markup

    total = quotation_cost + vat + logistics

    data.append(["", "", "", "", "", "Sub-Total", str(quotation_cost)])
    data.append(["", "", "", "", "", "VAT @ 5%", str(vat)])
    data.append(["", "", "", "", "", "Logistics", str(logistics)])
    data.append(["", "", "", "", "", "Grand Total", str(total)])

    t=Table(data)
    t.setStyle(TableStyle([
			    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
			]))

    t._argW[0] = 0.35*inch
    t._argW[1] = 1.1*inch
    t._argW[2] = 1.1*inch
    t._argW[3] = 2*inch
    t._argW[4] = 0.35*inch
    t._argW[5] = 1.1*inch
    t._argW[6] = 1.1*inch

    story.append(t)

    return doc.build(story, onFirstPage=first_page, onLaterPages=other_pages)
