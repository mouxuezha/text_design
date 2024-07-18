# 这个就是用来实现之前那种“给一个文件夹的书，能够一本一本的OCR出来，变成一个一个的Text的”

from pypdf import PdfReader
from pdf2image import convert_from_path
import pymupdf  # import the bindings
from cnocr import CnOcr
from PIL import Image
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ocr_from_pdf():
    def __init__(self):
        # 这个就是识别。
        self.ocr_location = r"./OCR/ocr_pdf/"
        self.txt_location = r"./OCR/ocr_txt/"
        self.ocr_runner = CnOcr()

    def load_pdf_name(self,location=""):
        if location == "":
            location = self.ocr_location
            
        # 这个就是加载pdf文件，先检测里面有多少pdf文件
        pdf_list = os.listdir(location)
        return pdf_list
    
    def ocr_pdf_single(self, pdf_name:str):
        # 这个就是识别特定的PDF文件，看是返回字符串还是直接写txt
        pdf_full_name = ocr.ocr_location + pdf_name
        result_dir = self.txt_location +r"/"+ pdf_name[0:-4]
        result_txt = result_dir + r"/result.txt"
        try:
            os.makedirs(result_dir)
        except:
            tishi = "文件夹已经存在，就这么着吧"
            print(tishi)
            # raise Exception(tishi)
        
        # 方法3
        fname = pdf_full_name  # get filename from command line
        doc = pymupdf.open(fname)  # open document
        page_num = doc.page_count  # get number of pages
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap(dpi=600)  # render page to an image
            name = result_dir + r"/page-"+str(page.number)+".png" 
            pix.save(name)  # store image as a PNG
            tu = Image.open(name)
            jieguo = self.ocr_runner.ocr(tu)
            self.write_result_page(jieguo,result_txt)
            self.write_txt(result_txt, "第"+str(page.number)+"页")
            print(pdf_name+"第"+str(page.number)+"页完成识别,"+str(page.number/page_num))
            self.del_all_png(result_dir)
            

        # # 方法2，倒是好使，但是有python以外的依赖项，鉴定为拉。
        # images = convert_from_path(pdf_name, dpi=600,poppler_path =r"E:\ruanjian\poppler-24.02.0\Library\bin")
        # for i, image in enumerate(images):
        #     image.save(self.txt_location + f'/page_{i + 1}.png', 'PNG')
        
        # 方法1，效果一般
        # reader = PdfReader(pdf_name)
        # number_of_pages = len(reader.pages)
        # page = reader.pages[0]
        # text = page.extract_text()    
        # print(text)    
        
        # # 删一下，防止储存爆炸。
        # self.del_all_png(result_dir)
    
    def write_txt(self, result_txt, result):
        result =result + "\n"
        with open(result_txt, 'a', encoding='utf-8') as f:
            f.write(result)

    def write_result_page(self,jieguo,result_txt):
        geshu = len(jieguo)
        for i in range(geshu):
            hang = jieguo[i]
            score = hang["score"]
            if score > 0.35:
                self.write_txt(result_txt,hang["text"])
        pass 

    def ocr_pdf_all(self, location):
        # 这个就是识别特定路径下的所有的pdf文件
        pdf_list = self.load_pdf_name()
        geshu = len(pdf_list)
        for i in range(geshu):
            self.ocr_pdf_single(pdf_list[i])
            print(pdf_list[i]+"第"+str(i+1)+"本完成识别,"+str((i+1)/geshu))
        pass
    
    def del_all_png(self, folder):
        # 这个就是删除特定文件夹下的所有png文件,防止储存爆炸。
        # 增加一个逻辑：多了才删，少了不删
       
        file_list = os.listdir(folder)
        if len(os.listdir(folder)) < 100:
            return
        else:
            print("文件夹内临时的png文件过多，删一轮")
            for file_name in file_list:
                if ".png" in file_name:
                    file_path = os.path.join(folder, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                


if __name__ == "__main__":
    ocr = ocr_from_pdf()
    # pdf_list = ocr.load_pdf_name()
    # print(pdf_list)
    # ocr.del_all_png(r"C:\Users\42418\Desktop\jushen\text_design\OCR\ocr_txt")
    # ocr.ocr_pdf_single(pdf_list[0])

    ocr.ocr_pdf_all(r"C:\Users\42418\Desktop\jushen\text_design\OCR\ocr_txt")

