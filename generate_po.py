from reportlab.lib.pagesizes import legal
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os


def money(value):
    return f"PHP {value:,.2f}"


def generate_po(order_id):
    os.makedirs("static", exist_ok=True)

    filename = f"po_{order_id}.pdf"
    filepath = os.path.join("static", filename)

    c = canvas.Canvas(filepath, pagesize=legal)
    width, height = legal

    # =========================
    # SAMPLE DATA
    # =========================
    company_name = "JDMT Information Technology Services"
    company_address_1 = "46 M. Gonzaga St. Brgy. Hagdan Bato Itaas"
    company_address_2 = "Mandaluyong City, 1550"

    po_number = f"J{order_id}"
    po_date = "04/15/2019"
    requisitioner = ""
    shipped_via = "For Pickup"
    fob_point = ""
    terms = "COD"

    to_name = "Grand Tech Intl Ent Corp"
    to_addr_1 = "#705 Rogacy Commercial Bldg., JP Rizal St. cor Pililia St."
    to_addr_2 = "Brgy. Valenzuela, Makati City"

    ship_to_name = "JDMT Information Technology Services"
    ship_to_addr_1 = "46 M. Gonzaga St. Brgy. Hagdan Bato Itaas"
    ship_to_addr_2 = "Mandaluyong City, 1550"
    ship_to_phone = "0917-8425175"

    items = [
        {"qty": 4, "unit": "PCS", "description": "1235228-PRINTER HEAD", "unit_price": 980.00},
        {"qty": 3, "unit": "PCS", "description": "2081600-FFC CABLE", "unit_price": 50.00},
        {"qty": 1, "unit": "PC", "description": "2184101-AC ADAPTER", "unit_price": 3500.00},
    ]

    subtotal = sum(item["qty"] * item["unit_price"] for item in items)
    shipping_handling = 0.00
    other = 0.00
    total = subtotal + shipping_handling + other

    authorized_by = "(Sgd.) Rommel John Taniegra"
    auth_date = "04/04/2019"

    # =========================
    # HELPERS
    # =========================
    left = 26
    right = width - 26
    top = height - 26

    def line(x1, y1, x2, y2, w=1):
        c.setLineWidth(w)
        c.line(x1, y1, x2, y2)

    def rect(x, y, w, h, lw=1):
        c.setLineWidth(lw)
        c.rect(x, y, w, h)

    def draw_text(x, y, text, size=8, font="Helvetica", color=colors.black):
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawString(x, y, str(text))

    def draw_center(x, y, text, size=8, font="Helvetica", color=colors.black):
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawCentredString(x, y, str(text))

    def draw_right(x, y, text, size=8, font="Helvetica", color=colors.black):
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawRightString(x, y, str(text))

    # =========================
    # HEADER
    # =========================
    draw_text(left, top, company_name, size=13, font="Helvetica-Bold")
    draw_text(left, top - 18, company_address_1, size=7.5)
    draw_text(left, top - 28, company_address_2, size=7.5)

    draw_right(right, top - 2, "PURCHASE ORDER", size=22, font="Helvetica-Bold", color=colors.HexColor("#2E3192"))

    # =========================
    # PO NOTE
    # =========================
    note_y = top - 85
    draw_text(left, note_y, "The following number must appear on all related", size=7.3)
    draw_text(left, note_y - 10, "correspondence, shipping papers, and invoices:", size=7.3)
    draw_text(left, note_y - 24, f"P.O. NUMBER: {po_number}", size=8.5, font="Helvetica-Bold")

    # =========================
    # TO / SHIP TO
    # =========================
    block_y = top - 145
    ship_x = width / 2 + 10

    draw_text(left, block_y, "TO:", size=8, font="Helvetica-Bold")
    draw_text(left, block_y - 14, to_name, size=7.5)
    draw_text(left, block_y - 26, to_addr_1, size=7.5)
    draw_text(left, block_y - 38, to_addr_2, size=7.5)

    draw_text(ship_x, block_y, "SHIP TO:", size=8, font="Helvetica-Bold")
    draw_text(ship_x, block_y - 14, ship_to_name, size=7.5)
    draw_text(ship_x, block_y - 26, ship_to_addr_1, size=7.5)
    draw_text(ship_x, block_y - 38, ship_to_addr_2, size=7.5)
    draw_text(ship_x, block_y - 50, ship_to_phone, size=7.5)

    # =========================
    # INFO TABLE
    # =========================
    info_top = top - 230
    info_left = left - 6
    info_width = right - info_left
    info_header_h = 20
    info_value_h = 20

    info_cols = [110, 110, 110, 110, 110]
    info_headers = ["P.O. DATE", "REQUISITIONER", "SHIPPED VIA", "F.O.B. POINT", "TERMS"]
    info_values = [po_date, requisitioner, shipped_via, fob_point, terms]

    rect(info_left, info_top - (info_header_h + info_value_h), info_width, info_header_h + info_value_h, lw=1.2)
    line(info_left, info_top - info_header_h, info_left + info_width, info_top - info_header_h, w=0.8)

    x = info_left
    for w in info_cols[:-1]:
        x += w
        line(x, info_top, x, info_top - (info_header_h + info_value_h), w=0.8)

    x = info_left
    for i, h in enumerate(info_headers):
        draw_center(x + info_cols[i] / 2, info_top - 13, h, size=7.5, font="Helvetica-Bold")
        x += info_cols[i]

    x = info_left
    for i, v in enumerate(info_values):
        draw_text(x + 5, info_top - info_header_h - 13, v, size=7.3)
        x += info_cols[i]

    # =========================
    # MAIN TABLE
    # =========================
    table_top = info_top - 55
    table_left = info_left
    table_width = info_width
    table_height = 225
    header_h = 20

    col_qty = 70
    col_unit = 70
    col_desc = 235
    col_unit_price = 85
    col_total = table_width - (col_qty + col_unit + col_desc + col_unit_price)

    x1 = table_left
    x2 = x1 + col_qty
    x3 = x2 + col_unit
    x4 = x3 + col_desc
    x5 = x4 + col_unit_price
    x6 = table_left + table_width

    rect(table_left, table_top - table_height, table_width, table_height, lw=1.2)
    line(table_left, table_top - header_h, table_left + table_width, table_top - header_h, w=0.8)

    for xx in [x2, x3, x4, x5]:
        line(xx, table_top, xx, table_top - table_height, w=0.8)

    draw_center((x1 + x2) / 2, table_top - 13, "QTY", size=7.5, font="Helvetica-Bold")
    draw_center((x2 + x3) / 2, table_top - 13, "UNIT", size=7.5, font="Helvetica-Bold")
    draw_center((x3 + x4) / 2, table_top - 13, "DESCRIPTION", size=7.5, font="Helvetica-Bold")
    draw_center((x4 + x5) / 2, table_top - 13, "UNIT PRICE", size=7.5, font="Helvetica-Bold")
    draw_center((x5 + x6) / 2, table_top - 13, "TOTAL", size=7.5, font="Helvetica-Bold")

    row_y = table_top - 34
    row_gap = 18

    for item in items:
        item_total = item["qty"] * item["unit_price"]
        draw_center((x1 + x2) / 2, row_y, item["qty"], size=7.5)
        draw_center((x2 + x3) / 2, row_y, item["unit"], size=7.5)
        draw_text(x3 + 8, row_y, item["description"], size=7.5)
        draw_text(x4 + 8, row_y, money(item["unit_price"]), size=7.5)
        draw_text(x5 + 8, row_y, money(item_total), size=7.5)
        row_y -= row_gap

    # =========================
    # FIXED TOTALS BOX
    # =========================
    # Naka-align sa right edge ng main table at nasa ilalim niya
    totals_width = 180
    totals_left = x6 - totals_width
    totals_top = table_top - table_height
    totals_height = 112
    totals_bottom = totals_top - totals_height

    rect(totals_left, totals_bottom, totals_width, totals_height, lw=0.0)

    label_col_width = 125
    split_x = totals_left + label_col_width
    line(split_x, totals_top, split_x, totals_bottom, w=0.8)

    row_h = totals_height / 4
    y1 = totals_top - row_h
    y2 = totals_top - (row_h * 2)
    y3 = totals_top - (row_h * 3)

    # for yy in [y1, y2, y3]:
    #     line(totals_left, yy, totals_left + totals_width, yy, w=0.8)

    labels = ["SUBTOTAL", "SHIPPING & HANDLING", "OTHER", "TOTAL"]
    values = [money(subtotal), "", "", money(total)]

    current_y = totals_top - 18
    for i, (label, value) in enumerate(zip(labels, values)):
        font_name = "Helvetica-Bold" if label == "TOTAL" else "Helvetica"
        draw_right(split_x - 8, current_y, label, size=7.2, font=font_name)
        draw_text(split_x + 8, current_y, value, size=7.2, font=font_name)
        current_y -= row_h

    # =========================
    # FOOTNOTE
    # =========================
    foot_y = totals_bottom - 38
    draw_text(left + 14, foot_y, "Enter this order in accordance with the prices, terms, delivery method,", size=6.6)
    draw_text(left + 14, foot_y - 10, "and specifications listed above.", size=6.6)
    draw_text(left + 14, foot_y - 26, "Please notify us immediately if you are unable to ship as specified.", size=6.6)

    # =========================
    # FIXED SIGNATURE SECTION
    # =========================
    sign_y = 80

    auth_line_left = 280
    auth_line_width = 210
    auth_line_right = auth_line_left + auth_line_width

    date_line_left = 515
    date_line_width = 95
    date_line_right = date_line_left + date_line_width

    # names above lines
    draw_text(auth_line_left + 8, sign_y + 20, authorized_by, size=8.4)
    draw_text(date_line_left + 12, sign_y + 20, auth_date, size=8.4)

    # actual lines
    line(auth_line_left, sign_y, auth_line_right, sign_y, w=0.8)
    line(date_line_left, sign_y, date_line_right, sign_y, w=0.8)

    # labels below
    draw_text(auth_line_left + 4, sign_y - 14, "Authorized by", size=6.5)
    draw_text(date_line_left + 28, sign_y - 14, "Date", size=6.5)

    c.save()
    return filename