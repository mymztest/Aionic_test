import pypdf

def pdf_to_text(pdffile,outputfile):
    try:
        #### read pdf data
        with open(pdffile,'rb') as pdffile:
            reader = pypdf.PdfReader(pdffile)
            text=''
            for page_no in range(len(reader.pages)):
                page = reader.pages[page_no]
                text += page.extract_text(extraction_mode="plain")
                #### write pdf data in text file
                with open(outputfile,'w', encoding='utf-8') as txtfile:
                    txtfile.write(text)
    except:
        print(f"Error in process:") 
    else:
        print(f"Text successsfully extracted:")

if __name__ == '__main__':
    pdffile = "D:\\practice_projects\\Aionic_test\\data\\sample_pdf.pdf"
    outputfile = "D:\\practice_projects\\Aionic_test\\data\\output.txt"
    pdf_to_text(pdffile,outputfile)