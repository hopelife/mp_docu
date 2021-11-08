from pdf2docx import Converter

pdf_file = 'C:/Users/user/Downloads/Problem-Solving_Strategies_Engel.pdf'
docx_file = 'C:/Users/user/Downloads/Problem-Solving_Strategies_Engel.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()