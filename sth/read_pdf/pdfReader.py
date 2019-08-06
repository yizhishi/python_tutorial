from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import os

#path = 'C:\\Users\\K\\Desktop\\2018考研英语二真题(完整版).pdf'


def getText(inputStr):
    inputStr = inputStr.lower().replace('a.', '').replace('b.', '').replace('c.', '').replace('d.', '').replace('’s', '')
    # 过滤汉字
    for ch in inputStr:
        if '\u4e00' <= ch <= '\u9fff':
            return ''
    '''
    # 过滤部分有规律
    if inputStr.endswith('directions:') or inputStr.startswith('read the following') or inputStr.endswith(' points)') or \
       inputStr.startswith('translate the following') or  inputStr.startswith('write an essay') or inputStr.startswith('you should write') or \
       inputStr.startswith('do not write your') or inputStr.startswith('do not use your own name'):
        return ''
    '''
    # 过滤标点
    for ch in  '1234567890<>,.?/:;"\'[]{}~!@#$%^&*()-+=_，。、《》？；：‘“！￥（）—':
        inputStr = inputStr.replace(ch, ' ')
    return inputStr

def readPdf(path):
    tmp = ''
    praser = PDFParser(open(path, 'rb'))
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)

    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in doc.get_pages():
            interpreter.process_page(page)                        
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBox):
                    line = x.get_text().strip().replace('\n', ' ')
                    line = getText(line)
                    tmp += line
                    
    return tmp

def main():
    li = []
    pdf_dir = 'C:\\tool\\python_tutorial\\sth\\read_pdf\\pdf\\'
    pdf_list = os.listdir(pdf_dir)
    for pdf in pdf_list:
        if os.path.isfile(pdf_dir + pdf):
            li.append(readPdf(pdf_dir + pdf))
    else:
        print('pdf loaded')

    counts = {}
    items = []

    for l in li:
        for  w in l.split():
            counts[w] = counts.get(w, 0) + 1
    else:
        items = list(counts.items())
        items.sort(key = lambda x:x[1], reverse = True)

    for i in range(100):
        word, count = items[i]
        print('{}\t{}'.format(word, count))

main()
