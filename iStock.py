from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime, date
import requests
from requests import *
import time
from time import sleep
import textwrap3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys
from win10toast import ToastNotifier

print("iStock [Version 1.2.0.1] | © 2019 | All rights reserved. ")
now = datetime.now()
toaster = ToastNotifier()

req = Request("https://live.mystocks.co.ke/ ")
try:
    response = urlopen(req)
except URLError as e:
    toaster.show_toast("No Connection :( ",
                            "Please check your internet connection and try again. Closing in 5 seconds.",
                            icon_path="stockcon.ico",
                            duration=5)
    time.sleep(6)
    sys.exit()
    time.sleep(0.5)
    
URL1= 'https://live.mystocks.co.ke/'
URL2 = 'https://live.mystocks.co.ke/price_list/'
payload = {
                "Username": "mwago.gatahi@gmail.com",
                "Password": "9whZZKFP"
            }
with requests.Session() as session:
    post = session.post(URL1, data=payload)
    r = session.get(URL2)

    print("\n")
    print("********************")
    print(datetime.now())
    print("********************")

    def main():
        print("\n")
        print("Pick a category:- ")
        print("1. Industries.")
        print("2. Indices.")
        print("3. Breaking News streams.")
        print("\n")
        choice=input("Your choice? ")
        print("\n")
        if choice =="1":
            print("Pick an industry. ")
            print("\n")
            print("1. Agricultural\n2. Automobiles\n3. Banking\n4. Commercial Services\n5. Construction & Allied\n6. Energy\n7. Insurance\n8. Investment\n9. Investment Services\n10. Manufacturing and Allied\n11. Telecoms\n12. REITS\n13. ETFs\n14. Preference Shares.")
            print("\n")
            jibu=input("Answer: ")
            
            if jibu=="1":
                print("\n")
                print("AGRICULTURE.")
                print("Companies include 1 coffee company, 4 Tea companies and 1 multi-agricultural company. ")
                print("Generating data.....")
                print("\n")
                name1="Eaagads"
                quote_page = "https://live.mystocks.co.ke/stock=EGAD"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/EGAD?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Eaagads_Chart.rtf', 'wb').write(r.content)
                

                import csv
                with open("Eaagads.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("********************")
                
                print("\n")
                name1="Kakuzi Tea"
                quote_page = "https://live.mystocks.co.ke/stock=KUKZ"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KUKZ?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Kakuzi_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Kakuzi Tea.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("********************")
                
                print("\n")
                name1="Kapchorua Tea"
                quote_page = "https://live.mystocks.co.ke/stock=KAPC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KAPC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Kapchorua_Chart.rtf', 'wb').write(r.content)
                
                    
                import csv
                with open("KapchoruaTea.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

##                print("\n")
##                name1="Limuru Tea"
##                quote_page = "https://live.mystocks.co.ke/stock=LIMT"
##                page = urllib.request.urlopen(quote_page)
##                soup = BeautifulSoup(page, "lxml")
##                companyName=soup.find("td", attrs={"id": "stkName"})
##                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
##                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
##                name_box2 = soup.find("div", attrs={"id": "rtTime"})
##                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
##                name_box4 = soup.find("div", attrs={"id": "rtChange"})
##                print("Company Profile: ", companyName.text)
##                list=textwrap3.wrap(stockProfile.text, width=95)
##                for element in list:
##                    print(element)
##                print("\n")
##                print(name_box2.text)
##                print("Current Price: ", name_box3.text)
##                Currentprice=name_box3.text
##                print("Previous Price: ", name_box1.text)
##                previousPrice=name_box1.text
##                print("Change: ", name_box4.text)
##                print("\n")
##                print("52 Week range")
##                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
##                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
##                print("Low: ", sharesIssued1.text)
##                print("High: ", sharesIssued2.text)
##                print("\n")
##                #print(companyName.text, "related news")
##                #news=soup.find("div", attrs={"id": "newsJson"})
##                #print(news.text)
##
##                import csv
##                with open("Limuru Tea.csv", "a", encoding="utf-8") as csv_file:
##                    writer = csv.writer(csv_file)
##                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
##                    Name=name1
##                    CompanyProfile=stockProfile.text
##                    CurrentPrice= Currentprice
##                    PreviousPrice=previousPrice
##                    Change=name_box4.text
##                    LowestPrice=sharesIssued1.text
##                    HighestPrice=sharesIssued2.text
##                    
##                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
##                print("\n")
##                print("********************")

                print("\n")
                name1="Sasini Tea"
                quote_page = "https://live.mystocks.co.ke/stock=SASN"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/SASN?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Sasini_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Sasini Tea.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Williamson Tea"
                quote_page = "https://live.mystocks.co.ke/stock=WTK"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/WTK?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Williamson_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Williamson Tea.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

               
            if jibu=="2":
                print("AUTOMOBILES.")
                print("Car and General is the only listed company in automobiles. ")
                print("Generating data.....")
                print("\n")
                name1="Car & General"
                quote_page = "https://live.mystocks.co.ke/stock=C%2526G"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/C%2526G?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Car&General_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("CarGeneral.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="3":
                print("BANKING.")
                print("11 out of 43 Kenya licensed banks are also listed on the NSE. ")
                print("Generating data.....")
                print("\n")
                name1="Barclays Bank"
                quote_page = "https://live.mystocks.co.ke/stock=BBK"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/BBK?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Barclays_Bank_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Barclays.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                print("\n")
                name1="Co-operative Bank"
                quote_page = "https://live.mystocks.co.ke/stock=COOP"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/COOP?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Coop_Bank_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Co-op.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Diamond Trust Bank"
                quote_page = "https://live.mystocks.co.ke/stock=DTK"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/DTK?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Diamond_Trust_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("DiamondTrustBank.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Equity Bank"
                quote_page = "https://live.mystocks.co.ke/stock=EQTY"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)               
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/EQTY?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Equity_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Equity-Bank.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Housing Finance"
                quote_page = "https://live.mystocks.co.ke/stock=HFCK"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/HFCK?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Housing_Finance_Chart.rtf', 'wb').write(r.content)
                

                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("HousingFinance.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="I&M Bank"
                quote_page = "https://live.mystocks.co.ke/stock=I%2526M"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)          
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/I%2526M?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('I&M_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("I&M.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="KCB Bank"
                quote_page = "https://live.mystocks.co.ke/stock=KCB"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)             
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KCB?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KCB_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("KCB.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="National Bank"
                quote_page = "https://live.mystocks.co.ke/stock=NBK"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/NBK?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('National_Bank_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("NationalBank.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="NIC Bank"
                quote_page = "https://live.mystocks.co.ke/stock=NIC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)            
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/NIC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('NIC_Bank_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("NIC Bank.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Stanbic Holdings Bank"
                quote_page = "https://live.mystocks.co.ke/stock=CFC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)            
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/CFC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Stanbic_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("StanbicHoldings.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Standard Chartered"
                quote_page = "https://live.mystocks.co.ke/stock=CFC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")          
                Download="https://live.mystocks.co.ke/graphs/chart/SCBK?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('StandardChartered_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("StanChart Bank.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                            
            if jibu=="4":
                print("COMMERCIAL.")
                print("Companies in Commerce and Services include those in Media, publishing, aviation, retail, fashion and hospitality. ")
                print("Generating data.....")
                print("\n")
                name1="Deacons"
                quote_page = "https://live.mystocks.co.ke/stock=DCON"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                print("On Monday November 19, 2018, ", companyName.text, "was suspended from trading at the NSE")
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/DCON?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Deacons_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Deacons.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Eveready"
                quote_page = "https://live.mystocks.co.ke/stock=EVRD"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/EVRD?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Eveready_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Eveready.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Express"
                quote_page = "https://live.mystocks.co.ke/stock=XPRS"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/XPRS?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Express_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Express.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="KQ"
                quote_page = "https://live.mystocks.co.ke/stock=KQ"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KQ?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KQ_Chart.rtf', 'wb').write(r.content)
                

                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("KQ.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="LongHorn"
                quote_page = "https://live.mystocks.co.ke/stock=LKL"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/LKL?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Longhorn_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Longhorn.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Nairobi Business Ventures"
                quote_page = "https://live.mystocks.co.ke/stock=NBV"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/NBV?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('NairobiBusinessVentures_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("NairobiBusiness.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Nation Media"
                quote_page = "https://live.mystocks.co.ke/stock=NMG"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")

                Download="https://live.mystocks.co.ke/graphs/chart/NMG?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Nation_Media_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("NationMedia.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Sameer"
                quote_page = "https://live.mystocks.co.ke/stock=FIRE"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")

                Download="https://live.mystocks.co.ke/graphs/chart/FIRE?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Sameer_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Sameer.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                
                print("\n")
                name1="Standard Group"
                quote_page = "https://live.mystocks.co.ke/stock=SGL"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/SGL?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('StandardGroup_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Standard.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="TPS Serena"
                quote_page = "https://live.mystocks.co.ke/stock=TPSE"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/TPSE?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Serena_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("TPSSerena.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Uchumi"
                quote_page = "https://live.mystocks.co.ke/stock=UCHM"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/UCHM?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Uchumi_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("Uchumi.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="ScanGroup"
                quote_page = "https://live.mystocks.co.ke/stock=SCAN"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/SCAN?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('ScanGroup_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                #open a csv file with append, so old data will not be erased
                with open("ScanGroup.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
         
            if jibu=="5":
                print("CONSTRUCTION.")
                print("Companies in Construction include 3 cement companies, 1 cable installation company and 1 paint manufacturer. ")
                print("Generating data.....")
                print("\n")
                name1="ARM Cement"
                quote_page = "https://live.mystocks.co.ke/stock=ARM"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/ARM?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('ARMCement_Chart.rtf', 'wb').write(r.content)
                
                 
                import csv
                with open("ARMCement.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Bamburi Cement"
                quote_page = "https://live.mystocks.co.ke/stock=BAMB"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/BAMB?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('BamburiCement_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("BamburiCement.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Crown Berger"
                quote_page = "https://live.mystocks.co.ke/stock=BERG"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/BERG?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('CrownBerger_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("CrownBerger.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="EACables"
                quote_page = "https://live.mystocks.co.ke/stock=CABL"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/CABL?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('EACables_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("EACables.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="PortlandCement"
                quote_page = "https://live.mystocks.co.ke/stock=PORT"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/PORT?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('EAPortland_Cement_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("PortlandCement.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                    
                print("\n")
                print("********************")      

            if jibu=="11":
                print("\n")
                print("ICT")
                print("Safaricom is the only listed company in technology. ")
                print("Generating data.....")
                print("\n")
                name1="Safaricom"
                quote_page = "https://live.mystocks.co.ke/stock=SCOM"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/SCOM?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Safaricom_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Safaricom.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                
            if jibu=="12":
                print("\n")
                print("REITS - Real Estate Investment Trusts.")
                print("Generating data.....")
                print("\n")
                name1="Stanlib Fahari REIT"
                quote_page = "https://live.mystocks.co.ke/stock=FAHR"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/SCOM?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Stanlib_Fahari_REIT_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("StanlibFahariREIT.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="13":
                print("\n")
                print("ETF - Exchange Traded Funds")
                print("Generating data.....")
                print("\n")
                name1="Barclays NewGold ETF (GLD)"
                quote_page = "https://live.mystocks.co.ke/stock=GLD"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/GLD?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Barclays_NewGold_ETF_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("BarclaysNewGoldETF.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="14":
                print("\n")
                print("Preference Shares")
                print("Generating data.....")
                print("\n")
                name1="Kenya Power and Lighting Ltd 4% (KPLC-P4)"
                quote_page = "https://live.mystocks.co.ke/stock=KPLC-P4"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KPLC-P4?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KPLC-P4_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("KPLC4%P4.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                
                name2="Kenya Power and Lighting Ltd 7% (KPLC-P7)"
                quote_page = "https://live.mystocks.co.ke/stock=KPLC-P7"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KPLC-P7?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KPLC-P7_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("KPLC7%P7.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name2
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="6":
                print("\n")
                print("ENERGY")
                print("Companies in Energy include 2 petroluem companies, 2 Kenyan electricity distributors and 1 Ugandan Electricity Distributor. ")
                print("Generating data.....")
                print("\n")
                name1="KenolKobil"
                quote_page = "https://live.mystocks.co.ke/stock=KENO"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KENO?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KenolKobil_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("KenolKobil.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="KenGen"
                quote_page = "https://live.mystocks.co.ke/stock=KEGN"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KEGN?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KenGen_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("KenGen.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Kenya Power"
                quote_page = "https://live.mystocks.co.ke/stock=KPLC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KPLC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KenyaPower_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("KPLC.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Total Kenya"
                quote_page = "https://live.mystocks.co.ke/stock=TOTL"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/TOTL?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('TotalKenya_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("TotalKenya.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Umeme"
                quote_page = "https://live.mystocks.co.ke/stock=UMME"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/UMME?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Umeme_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Umeme.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="7":
                print("\n")
                print("INSURANCE. ")
                print("Generating data.....")
                print("\n")
                name1="Britam"
                quote_page = "https://live.mystocks.co.ke/stock=BRIT"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/BRIT?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Britam_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Britam.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="CIC"
                quote_page = "https://live.mystocks.co.ke/stock=CIC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/CIC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('CIC_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("CIC.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="JubileeHoldings"
                quote_page = "https://live.mystocks.co.ke/stock=JUB"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/JUB?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Jubilee_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Jubilee.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="KenyaRe"
                quote_page = "https://live.mystocks.co.ke/stock=KNRE"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KNRE?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KenyaRE_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("KenyaRe.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="LibertyKenya Holdings"
                quote_page = "https://live.mystocks.co.ke/stock=CFCI"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/CFCI?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('LibertyKenya_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("LibertyKenya.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Sanlam"
                quote_page = "https://live.mystocks.co.ke/stock=PAFR"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/PAFR?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Sanlam_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Sanlam.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="8":
                print("\n")
                print("INVESTMENT COMPANIES ")
                print("Generating data.....")
                print("\n")
                name1="Centum"
                quote_page = "https://live.mystocks.co.ke/stock=ICDC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/ICDC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Centum_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Centum.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="HomeAfrica"
                quote_page = "https://live.mystocks.co.ke/stock=HAFR"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/HAFR?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('HomeAfrika_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("HomeAfrica.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Kurwitu"
                quote_page = "https://live.mystocks.co.ke/stock=KURV"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/KURV?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Kurwitu_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Kurwitu.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                
                print("\n")
                name1="Olympia Capital"
                quote_page = "https://live.mystocks.co.ke/stock=OCH"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/OCH?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('OlympiaCapital_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Olympia.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Transcentury"
                quote_page = "https://live.mystocks.co.ke/stock=TCL"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/TCL?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Transcentury_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Transcentury.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="9":
                print("\n")
                print("Generating data.....")
                print("\n")
                name="***Nairobi Securities Exchange PLC (NSE)***"
                name1="NSE"
                print(name)
                quote_page = "https://live.mystocks.co.ke/stock=NSE"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/NSE?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('NSE_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("NSE.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

            if jibu=="10":
                print("\n")
                print("MANUFACTURING & ALLIED.")
                print("Generating data.....")
                print("\n")
                name1="BOCKenya"
                quote_page = "https://live.mystocks.co.ke/stock=BOC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/BOC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('BOC_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("BOC.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="BATKenya"
                quote_page = "https://live.mystocks.co.ke/stock=BAT"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/BAT?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('BAT_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("BAT.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Carbacid"
                quote_page = "https://live.mystocks.co.ke/stock=CARB"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/CARB?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Carbacid_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Carbacid.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="EABL"
                quote_page = "https://live.mystocks.co.ke/stock=EABL"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/EABL?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('EABL_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("EABL.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="FlameTree"
                quote_page = "https://live.mystocks.co.ke/stock=FTGH"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/FTGH?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('FlameTree_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("FlameTree.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Kenya Orchards"
                quote_page = "https://live.mystocks.co.ke/stock=ORCH"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/ORCH?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('KenyaOrchards_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Kenya Orchards.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Mumias"
                quote_page = "https://live.mystocks.co.ke/stock=MSC"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/MSC?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Mumias_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("Mumias.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")

                print("\n")
                name1="Unga"
                quote_page = "https://live.mystocks.co.ke/stock=UNGA"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                companyName=soup.find("td", attrs={"id": "stkName"})
                stockProfile=soup.find("div", attrs={"class": "stockProfile"})
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print("Company Profile: ", companyName.text)
                list=textwrap3.wrap(stockProfile.text, width=95)
                for element in list:
                    print(element)
                print("\n")
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/UNGA?r=30;f=a;t=avg;dual;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('Unga_Chart.rtf', 'wb').write(r.content)
                
                
                import csv
                with open("UngaGroup.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CompanyProfile", "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name1
                    CompanyProfile=stockProfile.text
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name, CompanyProfile, CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
            main()
         
        if choice =="2":
            #while True:
            print("Pick an Index.")
            print("1. NSE All Share Index.")
            print("2. NSE 20 Share Index.")
            print("3. NSE 25 Share Index.")
            print("\n")
            ans=input("Your Pick? ")
            
            if ans =="1":
                quote_page = "https://live.mystocks.co.ke/stock=%5ENASI"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                print("\n")
                name="NSE All Share Index"
                print("****", name, "****")
                print("\n")
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/%255ENASI?r=30;f=a;t=avg;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('NASI_Chart.rtf', 'wb').write(r.content)
                

                import csv
                #open a csv file with append, so old data will not be erased
                with open("NSEAllShare-Index.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name,  CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                main()

            if ans=="2":
                quote_page = "https://live.mystocks.co.ke/stock=%5EN20I"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")
                print("\n")
                name="NSE 20-Share Index"
                print("****", name, "****")
                print("\n")
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print(name_box2.text)
                print("Current Price: ", name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price: ", name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/%255EN20I?r=30;f=a;t=avg;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('NSE20Share_Chart.rtf', 'wb').write(r.content)
                

                import csv
                #open a csv file with append, so old data will not be erased
                with open("NSE20Share-Index.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name,  CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                main()

            if ans=="3":
                quote_page = "https://live.mystocks.co.ke/stock=%255EN25I"
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "lxml")

                name="NSE 25-Share Index"
                print("****", name, "****")
                print("\n")
                name_box1 = soup.find("b", attrs={"id": "rtPrev"})
                name_box2 = soup.find("div", attrs={"id": "rtTime"})
                name_box3 = soup.find("div", attrs={"id": "rtPrice"})
                name_box4 = soup.find("div", attrs={"id": "rtChange"})
                print(name_box2.text)
                print(name_box3.text)
                Currentprice=name_box3.text
                print("Previous Price")
                print(name_box1.text)
                previousPrice=name_box1.text
                print("Change: ", name_box4.text)
                print("\n")
                print("52 Week range")
                sharesIssued1 = soup.find("span", attrs={"id": "rtYrLow"})
                sharesIssued2 = soup.find("span", attrs={"id": "rtYrHigh"})
                print("Low: ", sharesIssued1.text)
                print("High: ", sharesIssued2.text)
                
                print("\n")
                Download="https://live.mystocks.co.ke/graphs/chart/%255EN25I?r=30;f=a;t=avg;w=628;lgnd;format=rtf"
                r = requests.get(Download, allow_redirects=True)
                
                                        
                                        
                                          
                open('NSE25Share_Chart.rtf', 'wb').write(r.content)
                

                import csv
                #open a csv file with append, so old data will not be erased
                with open("NSE25Share-Index.csv", "a", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Name",  "CurrentPrice", "PreviousPrice", "Change", "LowestPrice", "HighestPrice"])
                    Name=name
                    CurrentPrice= Currentprice
                    PreviousPrice=previousPrice
                    Change=name_box4.text
                    LowestPrice=sharesIssued1.text
                    HighestPrice=sharesIssued2.text
                    
                    writer.writerow([Name,  CurrentPrice, PreviousPrice, Change, LowestPrice, HighestPrice])
                print("\n")
                print("********************")
                main()
                    
        if choice =="3": 
            quote_page = "https://live.mystocks.co.ke/stock=%255EN25I"
            page = urllib.request.urlopen(quote_page)
            soup = BeautifulSoup(page, "lxml")
            news=soup.find("div", attrs={"id": "newsJson"})
            print(news.text)
            
        import csv
        #open a csv file with append, so old data will not be erased
        with open("BreakingNews.csv", "a", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Breaking_News1"])
            Breaking_News1=news.text
            writer.writerow([Breaking_News1])
        print("\n")
        print("********************")
        main()


if __name__ == "__main__":
    main()






                


    

    

