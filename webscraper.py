import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl



def get_data(url):
    # returns the data in the form of 2d list

    # define user agent
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
    # specify the url
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    all_data = []   # define list to store list of all rows
    head = []       # define list to store header row
    data = (soup.find_all('th'))     # header cells
    for i in data:
        head.append(i.text)         # data in header cells
    all_data.append(head)

    # all_data list has the heading row
    # adding remaining rows

    cells = soup.find_all('td', attrs={'align':"center"})   #all the cells

    n = len(cells)
    for i in range(0, n, 7):                                # no. of columns is 7
        row = []                                            # each row
        for j in range(i, i+7):
            row.append(cells[j].text)
        all_data.append(row)                                # row appended in all_data
    return(all_data)


def dataframe(all_data):
    # creates pandas dataframe using 2d list

    df = pd.DataFrame(all_data[1:], columns=all_data[0])
    return(df)


def export_to_excel(df):
    # exports the given dataframe to an excel at the specified location

    df.to_excel(r'Bulk_deals.xlsx', index=False)
    print("Excel file created with name Bulk_deals ")


url = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx?expandable=3'
all_data = get_data(url)          # getting the 2d list
df = dataframe(all_data)       # feeding the 2d list received to create dataframe
export_to_excel(df)            # exporting the dataframe
ans=pd.read_excel("Bulk_deals.xlsx")
print(ans)