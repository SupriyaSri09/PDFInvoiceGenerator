from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("test/*.txt")
print(filepaths)

pdf = FPDF(orientation="P",unit="mm",format="A4")

for filename in filepaths:
    print(filename)
    animal_name = Path(filename).stem
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=30)
    pdf.cell(w=0,h=50,text=animal_name.title(),border=0)
    pdf.line(x1=10,x2=200,y1=42,y2=42)
    pdf.ln(32)
    with open(filename,'r') as file:
        content = file.read()
        #type(content)
        #print(content)
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0,h=8,text=content)


pdf.output("AllAboutAnimals.pdf")