from pdf2docx import Converter

pdf_path = "c4611_sample_explain.pdf"
doc_path = "c4611_sample_explain.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=doc_path)
cv.close()