from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

doc = SimpleDocTemplate(
    "/workspace/Event5_VO4_Submission.pdf",
    pagesize=A4,
    rightMargin=2.5*cm,
    leftMargin=2.5*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm,
)

styles = getSampleStyleSheet()

# Custom styles
normal = ParagraphStyle('normal', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=4)
bold = ParagraphStyle('bold', fontName='Helvetica-Bold', fontSize=10, leading=14, spaceAfter=4)
heading = ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=11, leading=16, spaceAfter=6, spaceBefore=10, underlineWidth=1)
small = ParagraphStyle('small', fontName='Helvetica', fontSize=9, leading=13, spaceAfter=4)
right = ParagraphStyle('right', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_RIGHT)
justify = ParagraphStyle('justify', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=6, alignment=TA_JUSTIFY)
italic = ParagraphStyle('italic', fontName='Helvetica-Oblique', fontSize=10, leading=14, spaceAfter=4)
bold_underline = ParagraphStyle('bold_underline', fontName='Helvetica-Bold', fontSize=10, leading=14, spaceAfter=6)

story = []

# ── SENDER BLOCK ──────────────────────────────────────────────────────────────
story.append(Paragraph("Power Building Pty Ltd", bold))
story.append(Paragraph("15 Leichhardt Street", normal))
story.append(Paragraph("Wynnum West QLD 4178", normal))
story.append(Paragraph("ACN 665 652 880 | QBCC Licence No. 1236148", normal))
story.append(Paragraph("Phone: 07 3287 3158 | Email: joe@powerbuilding.com.au", normal))
story.append(Spacer(1, 0.3*cm))
story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
story.append(Spacer(1, 0.4*cm))

# ── DATE & PROJECT REF ────────────────────────────────────────────────────────
story.append(Paragraph("25 September 2026", normal))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("Project No: 26-002", normal))
story.append(Spacer(1, 0.4*cm))

# ── RECIPIENT BLOCK ───────────────────────────────────────────────────────────
story.append(Paragraph("Trever Mal", bold))
story.append(Paragraph("Superintendent's Representative", normal))
story.append(Paragraph("Balmain Consulting Pty Ltd", normal))
story.append(Paragraph("64 Bishop Street", normal))
story.append(Paragraph("West End QLD 4101", normal))
story.append(Spacer(1, 0.5*cm))

# ── SALUTATION ────────────────────────────────────────────────────────────────
story.append(Paragraph("Dear Mr Mal", normal))
story.append(Spacer(1, 0.3*cm))

# ── SUBJECT LINE ─────────────────────────────────────────────────────────────
story.append(Paragraph(
    "<b>RE: New Sports Centre, Charlwood — Project No. 26-002<br/>"
    "Submission of Price for Variation Order No. 4 (VO4) — Additional Carpark Works</b>",
    bold_underline
))
story.append(Spacer(1, 0.3*cm))

# ── OPENING PARAGRAPH ─────────────────────────────────────────────────────────
story.append(Paragraph(
    "We refer to Variation Order No. 4 (VO4) issued by the Superintendent's Representative "
    "on 18 September 2026, directing Power Building Pty Ltd to:",
    justify
))
story.append(Spacer(1, 0.15*cm))
story.append(Paragraph("1.&nbsp;&nbsp;&nbsp;Construct an additional 68m² of asphalt to the carpark area; and", justify))
story.append(Paragraph("2.&nbsp;&nbsp;&nbsp;Construct an additional 25 lineal metres (lm) of kerb to the carpark area.", justify))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(
    "Pursuant to clause 40.2(a) of the Contract, and in accordance with the direction in VO4 "
    "to submit our price within 5 business days, please find below our price for the variation "
    "works, together with supporting evidence of cost.",
    justify
))
story.append(Spacer(1, 0.3*cm))

# ── VALUATION METHOD ──────────────────────────────────────────────────────────
story.append(Paragraph("Valuation", heading))
story.append(Paragraph(
    "In accordance with clause 40.5(d)(iv) of the Contract, the variation has been valued on the "
    "basis of the reasonable direct cost to the Contractor, including subcontract costs, with profit "
    "and overhead applied at the rates stated in Item 5 of Annexure B — Commercial Framework "
    "(15% on subcontractor costs; 10% on the Contractor's own costs).",
    justify
))
story.append(Spacer(1, 0.3*cm))

# ── ITEM 1 ────────────────────────────────────────────────────────────────────
story.append(Paragraph("<b><i>Item 1 — Additional Asphalt (68m²) — Subcontract Work</i></b>", bold))
story.append(Spacer(1, 0.1*cm))
story.append(Paragraph(
    "The asphalt works will be carried out by Asphalt Solutions (Quote No. 132, dated "
    "21 September 2026, attached). The quote is GST inclusive and has been converted to "
    "exclude GST in accordance with clause 48 and Item 9 of Annexure B.",
    justify
))
story.append(Spacer(1, 0.2*cm))

asphalt_data = [
    ["Description", "Amount\n(excl. GST)"],
    [
        "Asphalt Solutions Quote No. 132 — 30mm asphalt incl. preparation\nof substrate, 68m² @ $66/m² (GST inclusive) ÷ 1.1",
        "$4,080.00"
    ],
    [
        "Add: Profit & Overhead @ 15% on subcontractor costs\n(Annexure B, Item 5 — clause 40.5(d)(iv)(C))",
        "$612.00"
    ],
    ["Subtotal — Asphalt (excl. GST)", "$4,692.00"],
]

asphalt_table = Table(asphalt_data, colWidths=[12*cm, 3.5*cm])
asphalt_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D9E1F2')),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E2EFDA')),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (0, -1), 6),
]))
story.append(asphalt_table)
story.append(Spacer(1, 0.4*cm))

# ── ITEM 2 ────────────────────────────────────────────────────────────────────
story.append(Paragraph("<b><i>Item 2 — Additional Kerb (25 lm) — Contractor's Own Staff</i></b>", bold))
story.append(Spacer(1, 0.1*cm))
story.append(Paragraph(
    "The kerb works will be carried out by the Contractor's own staff at the applicable "
    "rate of $45.00 per lineal metre, excluding GST.",
    justify
))
story.append(Spacer(1, 0.2*cm))

kerb_data = [
    ["Description", "Amount\n(excl. GST)"],
    ["25 lm × $45.00/lm (Contractor's own staff)", "$1,125.00"],
    [
        "Add: Profit & Overhead @ 10% on Contractor's own costs\n(Annexure B, Item 5 — clause 40.5(d)(iv)(C))",
        "$112.50"
    ],
    ["Subtotal — Kerb (excl. GST)", "$1,237.50"],
]

kerb_table = Table(kerb_data, colWidths=[12*cm, 3.5*cm])
kerb_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D9E1F2')),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#E2EFDA')),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (0, -1), 6),
]))
story.append(kerb_table)
story.append(Spacer(1, 0.4*cm))

# ── SUMMARY TABLE ─────────────────────────────────────────────────────────────
story.append(Paragraph("<b><i>Summary — Variation Order No. 4</i></b>", bold))
story.append(Spacer(1, 0.1*cm))

summary_data = [
    ["Description", "Amount\n(excl. GST)"],
    ["Item 1 — Additional Asphalt (68m²)", "$4,692.00"],
    ["Item 2 — Additional Kerb (25 lm)", "$1,237.50"],
    ["Total excl. GST", "$5,929.50"],
    ["GST (10%)", "$592.95"],
    ["Total incl. GST", "$6,522.45"],
]

summary_table = Table(summary_data, colWidths=[12*cm, 3.5*cm])
summary_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D9E1F2')),
    ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#FFF2CC')),
    ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#E2EFDA')),
    ('FONTNAME', (0, 3), (-1, 3), 'Helvetica-Bold'),
    ('FONTNAME', (0, 5), (-1, 5), 'Helvetica-Bold'),
    ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (0, -1), 6),
]))
story.append(summary_table)
story.append(Spacer(1, 0.4*cm))

# ── NO DELAY STATEMENT ───────────────────────────────────────────────────────
story.append(Paragraph(
    "We confirm that there is no delay to the Works as a result of this variation and accordingly "
    "no extension of time or delay costs are claimed in connection with VO4.",
    justify
))
story.append(Spacer(1, 0.3*cm))

# ── REQUEST ──────────────────────────────────────────────────────────────────
story.append(Paragraph(
    "We request that the Superintendent assess and confirm the approved value of VO4 in "
    "accordance with clause 40.5(a) of the Contract, and that the Contract Sum be adjusted "
    "accordingly by <b>$5,929.50 excluding GST ($6,522.45 including GST)</b>.",
    justify
))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "Should you have any queries regarding this submission, please do not hesitate to contact "
    "the undersigned.",
    justify
))
story.append(Spacer(1, 0.4*cm))

# ── CLOSING ──────────────────────────────────────────────────────────────────
story.append(Paragraph("Yours sincerely", normal))
story.append(Spacer(1, 0.8*cm))
story.append(Paragraph("<b>Joe Perera</b>", bold))
story.append(Paragraph("Contractor's Representative", normal))
story.append(Paragraph("Power Building Pty Ltd", normal))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("<i>Attachment: Asphalt Solutions Quote No. 132, dated 21 September 2026</i>", italic))
story.append(Spacer(1, 0.5*cm))

# ── CLAUSE REFERENCE TABLE ───────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph("<b>Contract Clauses Relied Upon</b>", bold))
story.append(Spacer(1, 0.1*cm))

clauses_data = [
    ["Clause", "Purpose"],
    ["Clause 40.1(a)", "Superintendent's authority to direct a variation prior to the date of practical completion"],
    ["Clause 40.2(a)", "Contractor's obligation to advise effect on contract sum within timeframe directed"],
    ["Clause 40.3(a)", "Contractor's entitlement to claim costs incurred in carrying out a directed variation"],
    ["Clause 40.5(a)", "Contract sum to be adjusted by the amount of the valuation"],
    ["Clause 40.5(d)(iv)", "Valuation by reference to reasonable direct costs (labour, materials, plant) and subcontract costs, plus P&OH"],
    ["Clause 40.5(d)(iv)(C)", "P&OH applied at percentages stated in the Commercial Framework"],
    ["Annexure B — Item 5", "P&OH rates: 15% on subcontractor costs; 10% on Contractor's own costs"],
    ["Annexure B — Item 9 / Clause 48", "All prices are exclusive of GST"],
]

clauses_table = Table(clauses_data, colWidths=[4.5*cm, 11*cm])
clauses_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8.5),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#D9E1F2')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
]))
story.append(clauses_table)

doc.build(story)
print("PDF created successfully: /workspace/Event5_VO4_Submission.pdf")
