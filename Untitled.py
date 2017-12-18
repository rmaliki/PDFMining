
# coding: utf-8

# In[2]:


from PdfMinerWrapper import PdfMinerWrapper


# In[12]:


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox,LTChar, LTFigure,LTTextLineHorizontal, LTText
import sys


# In[19]:


with PdfMinerWrapper('rochdtest.pdf') as doc:
    for page in doc:
        if page.pageid==1:
            for tbox in page:
                if isinstance(tbox,LTTextLineHorizontal):
                    print(tbox.get_text())

