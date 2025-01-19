import io
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter


def add_page_numbers(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        packet = io.BytesIO()
        c = canvas.Canvas(packet)
        # add the number of page
        c.drawString(500, 10, f"{page_num + 1}")
        c.save()

        # the page with number in pdf transfer
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])

        writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)


add_page_numbers("Pro GIT.pdf", "Pro GIT v2.pdf")



