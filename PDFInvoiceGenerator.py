import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import pandas

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    file_name=Path(filepath).stem
    invoice_num=file_name.split("-")[0]
    date=file_name.split("-")[1]
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=16)
    pdf.cell(w=0,h=24,text=f"Invoice No.{invoice_num}",border=0,ln=1)
    pdf.cell(w=0, h=24, text=f"Date{date}", border=0,ln=1)

    # Read Excel
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    columns = list(df.columns)
    total_price_invoice=str(df["total_price"].sum())

    #Add Header
    columns=[item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=24, text=columns[0], border=1, align="C")
    pdf.cell(w=50, h=24, text=columns[1], border=1, align="C")
    pdf.cell(w=50, h=24, text=columns[2], border=1, align="C")
    pdf.cell(w=30, h=24, text=columns[3], border=1, align="C")
    pdf.cell(w=30, h=24, text=columns[4], border=1,ln=1, align="C")


    for index,rows in df.iterrows():
        product_id=str(rows["product_id"])
        product_name=str(rows["product_name"])
        amount_purchased = str(rows["amount_purchased"])
        price_per_unit=str(rows["price_per_unit"])
        total_price=str(rows["total_price"])

        pdf.set_font(family="Times",  size=12)
        pdf.cell(w=30, h=24, text=product_id, border=1,align="C")

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=50, h=24, text=product_name, border=1,align="C")

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=50, h=24, text=amount_purchased, border=1, align="C")

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30, h=24, text=price_per_unit, border=1,align="C")

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30, h=24, text=total_price, border=1, ln=1,align="C")

    pdf.set_font(family="Times", size=12)
    pdf.cell(w=30, h=24, text="", border=1, align="C")
    pdf.cell(w=50, h=24, text="", border=1, align="C")
    pdf.cell(w=50, h=24, text="", border=1, align="C")
    pdf.cell(w=30, h=24, text="", border=1, align="C")
    pdf.cell(w=30, h=24, text=total_price_invoice, border=1, align="C",ln=1)


    pdf.output(f"{file_name}1.pdf")