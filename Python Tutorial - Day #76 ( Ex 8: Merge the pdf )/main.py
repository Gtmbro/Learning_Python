import os

from pypdf import PdfReader #To import class PdfReader.
from pypdf import PdfWriter #To import PdfWriter class.

writer = PdfWriter() # To create instance of the PdfWriter class.

for file in os.listdir():
  if file.endswith("pdf") and os.path.getsize(file) != 0:
    reader = PdfReader(file)
    for page in reader.pages:
      writer.add_page(page)

with open("Merged_Pdf.pdf",'wb') as f:
  writer.write(f)
