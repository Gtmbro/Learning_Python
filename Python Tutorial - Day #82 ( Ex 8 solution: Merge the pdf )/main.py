import os
from pypdf import PdfWriter

merger = PdfWriter() #Assigning class PdfWriter to Writer

for file in os.listdir():
  if file.endswith("pdf"):
    merger.append(file) #Giving variable file to append method of PdfWriter

merger.write("Merged_Pdf.pdf")
merger.close()
