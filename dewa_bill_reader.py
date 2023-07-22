import pdfplumber
import re

headings = {'Invoice':[0,False],'Electricity':[0,False],"Water":[0,False],"Other Services":[0,False],"Housing":[0,False],"Sewerage":[0,False],
    "Additional Charges":[0,False],"Current month total":[0,False],"Total Due":[0,False]}

try:
    with pdfplumber.open("dewa_bill.pdf") as temp:

      first_page = temp.pages[0]

      with open("pdf.txt",mode='w') as f:
          f.write(first_page.extract_text())

except:
    print("File Does not Exist")
else:
    with open("pdf.txt",mode="r") as f:
        contents = f.readlines()

        for h in headings:
            if [x.strip() for x in contents if re.search('^'+h,x.strip())]:
                headings[h][0]=".".join(re.findall('[0-9]+',[x.strip() for x in contents if re.search('^'+h,x.strip())][0]))
                headings[h][1]=True
            elif [x.strip() for x in contents if re.search(h,x.strip())]:
                if not headings[h][1]:
                    headings[h][0]=".".join(re.findall('[0-9]+',[x.strip() for x in contents if re.search(h,x.strip())][0]))
                    headings[h][1]=True

        for summary,value in headings.items():
            print(f'{summary:20} {value[0]}')

