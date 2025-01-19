import easygui
from PyPDF2 import PdfReader, PdfWriter

input_path = easygui.fileopenbox(
    title="Choice a file...",
    default="*.pdf"
)
if input_path == None:
    exit()
first_page = easygui.enterbox(
    title="Number of pages"
)
if first_page == None:
    exit()
first_page = int(first_page)
while first_page % 2 != 0:
    first_page = easygui.enterbox(
        title="Numer of pages"
    )
    if first_page == None:
        exit()
    first_page = int(first_page)


input_file = PdfReader(input_path)
quantity_pages = len(input_file.pages)

last_page = easygui.enterbox(
    title="The last page please."
)
if last_page == None:
    exit()
last_page = int(last_page)
while last_page < first_page or last_page > quantity_pages:
    last_page = easygui.enterbox(
        title="The last page please."
    )
    last_page = int(last_page)
    if last_page == None:
        exit()
save_path = easygui.filesavebox(
    title="The spot for saving",
    default="*.pdf"
)
if save_path == None:
    exit()
while save_path == input_path:
    easygui.msgbox(
        title="The same place",
        ok_button="Another place"
    )
    if save_path == None:
        exit()

output_file = PdfWriter()
for page_num in range(first_page - 1, last_page):
    page = input_file.pages[page_num]
    output_file.add_page(page)

with open(save_path, "wb") as output:
    output_file.write(output)

easygui.msgbox(
    title="The pages successful saved"
)
