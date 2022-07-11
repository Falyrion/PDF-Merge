import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileMerger


def merge_pdfs(pdfs, out_file):
    """ Merge all pdf files from a given list into one output file

    :param pdfs: List; List of Filepaths
    :param out_file: String; The name of the output file
    :return: None
    """
    merger = PdfFileMerger()

    for pdf_file in pdfs:
        try:
            print(f"Merging file {pdf_file}")
            merger.append(pdf_file)
        except FileNotFoundError:
            print(f"File {pdf_file} not found")

    print("Writing result file...")
    merger.write(out_file)
    merger.close()


# Get filenames and paths to merge with dialog
files = filedialog.askopenfilenames(
    parent=tkinter.Tk(), title="Choose pdf-files to merge")

# Create list with all file paths
pdfs = []
for file in tkinter.Tk().tk.splitlist(files):
    pdfs.append(file)

# Merge files
merge_pdfs(pdfs, "out.pdf")
print("Finished merging pdfs")
