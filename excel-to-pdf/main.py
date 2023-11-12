from pathlib import Path
from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob("excel-to-pdf/invoices/*.xlsx")
for filepath in filepaths:
    filename = Path(filepath).stem
    pdf = FPDF(orientation='P', unit="mm", format='A4')
    pdf.set_font(family='Times', size=16, style='B')
    pdf.add_page()

    invoice_nr, invoice_date = filename.split('-')

    pdf.cell(w=50, h=8, ln=1, txt=f"Invoice nr. {invoice_nr}")
    pdf.cell(w=50, h=8, ln=1, txt=f"Date: {invoice_date}")

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # df = pd.read_excel('excel-to-pdf/invoices/10001-2023.1.18.xlsx', sheet_name="Sheet 1")

    columns = [item.replace('_', ' ').title() for item in df.columns]
    pdf.set_font(family='Times', size=11, style='B')
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)



    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    for index, row in df.iterrows():
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    output = pdf.output(f"excel-to-pdf/PDFs/{filename}.pdf")
