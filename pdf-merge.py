# from PyPDF2 import PdfMerger
# import os

# merger = PdfMerger()
# root = r"C:\Users\13607\Downloads\MIT-Linear-Algebra-Notes-master\MIT-Linear-Algebra-Notes-master"

# for path, subdirs, files in os.walk(root):
#     for name in files:
#         if name.endswith('.pdf'):
#             merger.append(os.path.join(path, name))

# merger.write(r"C:\Users\13607\Downloads\merged-pdf.pdf")
# merger.close()


# # --------------------------------------
#
# from PyPDF2 import PdfMerger
# import os
#
# merger = PdfMerger()
# root = r"C:\Users\13607\Downloads\MIT-Linear-Algebra"
#
# for name in os.listdir(root):
#     if name.endswith('.pdf'):
#         merger.append(os.path.join(root, name))
#
# merger.write(r"C:\Users\13607\Downloads\MIT-Linear-Algebra.pdf")
# merger.close()