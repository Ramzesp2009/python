import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfReader, PdfWriter

# 1. Output the window for choose a file to open PDF document
input_path = gui.fileopenbox(
    title="Select a PDF to rotate...",
    default="*.pdf"
)

# 2. User cansel the dialog window, close the program
if input_path is None:
    exit()

# 3. Ask the user to choose the angle of rotation
#    90, 100 or 270 degree
choices = ("90", "180", "270")
degrees = gui.buttonbox(
    msg="Rotate the PDF clockwise by how many degrees?",
    title="Choose rotation...",
    choices=choices,
)

while degrees == None:
    degrees = gui.buttonbox(
        msg="Rotate the PDF clockwise by how many degrees?",
        title="Choose rotation...",
        choices=choices,
    )

degrees = int(degrees)

# 4. Open dialog window for to choose the file to open PDF document with
#    the turned sides.

save_title = "Save the rotated PDF as..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title, default=file_type)

# 5. If the user try to save the file with the same name how the source file
while input_path == output_path:
    # - Prevent the user with a window with a massage that operation isn't available
    gui.msgbox(msg="Cannot overwrite original file!")
    # - Return to step 4
    output_path = gui.filesavebox(title=save_title, default=file_type)

# 6. If the user cancel the window of save the file
#    to end the work of program
if output_path is None:
    exit()

# 7. To perform the turn of pages:
#    to open the choose file
input_file = PdfReader(input_path)
output_pdf = PdfWriter()

# - turn all the pages
for page in input_file.pages:
    # page = input_file.getPage(page)
    page = page.rotate(degrees)
    output_pdf.add_page(page)

# - to save the document PDF with turn pages
with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)

gui.msgbox(msg="PDF successfully rotated and saved!", title="Success")

# print(input_path)