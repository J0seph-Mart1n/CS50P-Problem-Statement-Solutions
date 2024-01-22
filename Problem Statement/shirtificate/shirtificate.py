from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation='P', unit='mm', format=(210,297))
pdf.add_page()
pdf.image('shirtificate.png',x=10,y=60,h=200,w=190)
pdf.set_font("Helvetica","B",40)
pdf.cell(190, 40, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.set_font("Helvetica",'',25)
pdf.set_text_color(255, 255, 255)
pdf.cell(190,150, name, align='C')
pdf.output("shirtificate.pdf")
