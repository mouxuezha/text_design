# 这个就是用来实现之前那种“给一个文件夹的书，能够一本一本的OCR出来，变成一个一个的Text的”

from pypdf import PdfReader
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ocr_from_pdf():
    def __init__(self):
        # 这个就是识别。
        self.ocr_location = r"./OCR/ocr_pdf/"
        self.txt_location = r"./OCR/ocr_txt/"

    def load_pdf_name(self,location=""):
        if location == "":
            location = self.ocr_location
            
        # 这个就是加载pdf文件，先检测里面有多少pdf文件
        pdf_list = os.listdir(location)
        return pdf_list
    
if __name__ == "__main__":
    ocr = ocr_from_pdf()
    pdf_list = ocr.load_pdf_name()
    print(pdf_list)
