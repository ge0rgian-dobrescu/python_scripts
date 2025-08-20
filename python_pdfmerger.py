"""
The purpose of this script is to merge two different pdf files into a single one.
"""
import PyPDF2
import os 
import sys

cwd = os.curdir
merger = PyPDF2.PdfWriter()

for file in os.listdir(cwd):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedPDFS.pdf")


