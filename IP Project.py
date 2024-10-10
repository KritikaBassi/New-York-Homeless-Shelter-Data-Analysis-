
import matplotlib.pyplot as plt
import tkinter.ttk as ttk
from tkinter import *
import pandas as pd
import numpy as np
import csv
import time
import datetime


def main():
    login()

print('_' * 60)
print()
print('░█░░░▄▀▀▀▄░░▄▀▀▀░░░▀█▀░█▄░░█░')
print('░█░░░█   █░░█  ▄░░░░█░░█░▀▄█░')
print('░█▄▄░▀▄▄▄▀░░▀▄▄▄▀▄░▄█▄░█░░░█░')
print('_' * 60)

#login

def login():
    while True:
        print()
        username="name"
        password="pass"
        answer1=input("Enter username : ")
        answer2=input("Enter password : ")

        if answer1==username and answer2==password:
            print()
            print("Welcome - Access Granted")
            print()
            print()
            print("About...")
            print()
            print("*************************************************************************************************")
            print()
            print("How many people spend each night in a New York City homeless shelter? It seems like a simple question, but getting the answer is pretty complicated.")
            print("This dataset includes the daily number of families and individuals residing in the Department of Homeless Services (DHS)")
            print()
            print()
            print("What can I do?")
            print()
            print("***Data processing and organization.")
            print("The pandas package is a flexible and intuitive tool that allows researchers to work with all sorts of data such as text data, comma-separated data or Excel-style spreadsheets.")
            print("Data like these can be stored in '.csv' and pandas makes it easy to perform operations on both row- and column- labeled data.")
            print()
            print("***Data analysis.")
            print("Using pandas I can also perform a wide variety of statistics for data analysis.")
            print()
            print("***Data visualization.")
            print("The module matplotlib.pyplot in the Matplotlib package can create all sorts of plots.")
            print("Matplotlib which creates beautiful statistical graphics.")
            print()
            print("*************************************************************************************************")
            print()
            print("Press any key to continue...")
            wait = input()
            menu()

        else:
            answer1!=username and answer2!=password
            print("Incorrect")
            print("Please Try again...")

            print()

csv_file = ("/Users/Kritikabassi/Desktop/Python Programs Class 12/DHS_Daily_Report Updated.csv")
df = pd.read_csv("/Users/Kritikabassi/Desktop/Python Programs Class 12/DHS_Daily_Report Updated.csv")

#menu

def menu():
    while True:
        print('░█▄░▄█░▄▀▀▄░░▀█▀░█▄ ░█░░░░░░█▄░▄█░█▀▀░█▄ ░█░█░░░█░')
        print('░█ ▀ █░█▄▄█░░░█░░█░▀▄█░░░░░░█ ▀ █░█▀░░█░▀▄█░█░░░█░')
        print('░█░░░█░█░░█░░▄█▄░█░░░█░░░░░░█░░░█░█▄▄░█░░░█░▀▄▄▄▀░')
        print()
        print('_'*76)
        print()
        print("****************************************************")
        print()
        print('1. Analytics Pane\n')
        print('2. Visualize the data\n')
        print('3. Export data\n')
        print('4. Dataset Information\n')
        print('00.Exit\n')

        choice = int(input('Enter your option : '))

        if choice == 1:
            data_analysis_menu()
            wait = input()

        if choice == 2:
            graph()
            wait = input()

        if choice == 3:
            export_menu()
            wait = input()

        if choice == 4:
            print()
            print("NYC Department of Homeless Services Daily Report")
            print("********************************************************************************************")
            print('Agency    :   Department of Homeless Services (DHS)')
            print("----------------------------------")
            print('Licensing and Attribution')
            print('License        :   The license for this dataset is unspecified')
            print('Source Link    :   http://www.nyc.gov/html/dhs/downloads/pdf/dailyreport.pdf')
            print('Source Link    :   https://data.world/ian/nyc-department-of-homeless-services-daily-report')
            print()
            wait = input()
            

        if choice == 00:
            print()
            print("""
        MADE BY

   Roll No : Names

        09 : Ayushi Chaudhary
        19 : Kritika Bassi
        22 : Mohammed Junaid
    
   CLASS - XII A
                         """)
            wait = input()
            quit()
            

        
            
#data_analysis_menu

def data_analysis_menu():
    while True:
        csv_file = ("/Users/Kritikabassi/Desktop/Python Programs Class 12/DHS_Daily_Report Updated.csv")
        df = pd.read_csv("/Users/Kritikabassi/Desktop/Python Programs Class 12/DHS_Daily_Report Updated.csv")
        
        print()
        print('░▄▀▀▄░█▄ ░█░▄▀▀▄░█░░░█░░░█░▀▀█▀▀░▀█▀░▄▀▀▄░▄▀▀▀▄░░░░░░█▄░▄█░█▀▀░█▄ ░█░█░░░█░')
        print('░█▄▄█░█░▀▄█░█▄▄█░█░░░▀▄▄▄▀░░░█░░░░█░░█░░░░░▀▀▀▄░░░░░░█ ▀ █░█▀░░█░▀▄█░█░░░█░')
        print('░█░░█░█░░░█░█░░█░█▄▄░░░█░░░░░█░░░▄█▄░▀▄▄▀░▀▄▄▄▀░░░░░░█░░░█░█▄▄░█░░░█░▀▄▄▄▀░')
        print('\n\nData Analysis Menu')
        print('_'*76)
        print()
        print('1. Show Whole DataFrame\n')
        print('2. Show Columns\n')
        print('3. Show Top Rows\n')
        print('4. Show Bottom Rows\n')
        print('5. Show Specific Column\n')
        print('6. Data Summery\n')
        print('7. Add a New Row\n')
        print('8. Filter data\n')
        print('9. Delete a Record\n')
        print('00. Exit(Move to main menu)\n')
        ch = int(input('Enter your choice:'))
        print()
        if ch == 1:
            print()
            print('1. In Brief\n')
            print()
            print('2. In Detail\n')
            print()
            showordata = int(input('Option : '))
            if showordata == 1:
                print(df)
                wait = input()

            if showordata == 2:
                root = Tk()
                root.title("Python - Import CSV File To Tkinter Table")
                width = 700
                height = 500
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                root.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root.resizable(0, 0)  
                TableMargin = Frame(root, width=500)
                TableMargin.pack(side=TOP)
                scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
                scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
                tree = ttk.Treeview(TableMargin, columns=("Date_of_Census", "Total_Adults_in_Shelter", "Total_Children_in_Shelter", "Total_Individuals_in_Shelter", "Single_Adult_Men_in_Shelter", "Single_Adult_Women_in_Shelter", "Total_Single_Adults_in_Shelter", "Families_with_Children_in_Shelter", "Adult_Families_in_Shelter", "Individuals_in_Adult_Families_in_Shelter"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
                scrollbary.config(command=tree.yview)
                scrollbary.pack(side=RIGHT, fill=Y)
                scrollbarx.config(command=tree.xview)
                scrollbarx.pack(side=BOTTOM, fill=X)
                tree.heading('Date_of_Census', text="Date_of_Census", anchor=W)
                tree.heading('Total_Adults_in_Shelter', text="Total_Adults_in_Shelter", anchor=W)
                tree.heading('Total_Children_in_Shelter', text="Total_Children_in_Shelter", anchor=W)
                tree.heading('Total_Individuals_in_Shelter', text="Total_Individuals_in_Shelter", anchor=W)
                tree.heading('Single_Adult_Men_in_Shelter', text="Single_Adult_Men_in_Shelter", anchor=W)
                tree.heading('Single_Adult_Women_in_Shelter', text="Single_Adult_Women_in_Shelter", anchor=W)
                tree.heading('Total_Single_Adults_in_Shelter', text="Total_Single_Adults_in_Shelter", anchor=W)
                tree.heading('Families_with_Children_in_Shelter', text="Families_with_Children_in_Shelter", anchor=W)
                tree.heading('Adult_Families_in_Shelter', text="Adult_Families_in_Shelter", anchor=W)
                tree.heading('Individuals_in_Adult_Families_in_Shelter', text="Individuals_in_Adult_Families_in_Shelter", anchor=W)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=200)
                tree.column('#2', stretch=NO, minwidth=0, width=200)
                tree.column('#4', stretch=NO, minwidth=0, width=300)
                tree.column('#5', stretch=NO, minwidth=0, width=300)
                tree.column('#6', stretch=NO, minwidth=0, width=300)
                tree.column('#7', stretch=NO, minwidth=0, width=300)
                tree.column('#8', stretch=NO, minwidth=0, width=300)
                tree.column('#9', stretch=NO, minwidth=0, width=300)
                tree.column('#10', stretch=NO, minwidth=0, width=300)
                tree.pack()
                         
                with open("/Users/Kritikabassi/Desktop/DHS_Daily_Report Updated.csv") as f:
                    reader = csv.DictReader(f, delimiter=',')
                    for row in reader:
                        Date_of_Census = row['Date of Census']
                        Total_Children_in_Shelter = row['Total Children in Shelter']
                        Total_Adults_in_Shelter = row['Total Adults in Shelter']
                        Total_Individuals_in_Shelter = row['Total Individuals in Shelter']
                        Single_Adult_Men_in_Shelter = row['Single Adult Men in Shelter']
                        Single_Adult_Women_in_Shelter = row['Single Adult Women in Shelter']
                        Total_Single_Adults_in_Shelter = row['Total Single Adults in Shelter']
                        Families_with_Children_in_Shelter = row['Families with Children in Shelter']
                        Adult_Families_in_Shelter = row['Adult Families in Shelter']
                        Individuals_in_Adult_Families_in_Shelter = row['Individuals in Adult Families in Shelter']
                        tree.insert("", 0, values=(Date_of_Census, Total_Adults_in_Shelter, Total_Children_in_Shelter, Total_Individuals_in_Shelter, Single_Adult_Men_in_Shelter, Single_Adult_Women_in_Shelter, Total_Single_Adults_in_Shelter, Families_with_Children_in_Shelter, Adult_Families_in_Shelter, Individuals_in_Adult_Families_in_Shelter))

                if __name__ == '__main__':
                    root.mainloop()
                    wait = input()
        
        if ch == 2:
            print(df.columns)
            wait = input()

        
        if ch == 3:
            n = int(input('Enter Total rows you want to show :'))
            print(df.head(n))
            wait = input()
        
        if ch == 4:
            n = int(input('Enter Total rows you want to show :'))
            print(df.tail(n))
            wait = input()
        
        if ch == 5:
            print(df.columns)
            col_name = input('Enter Column Name that You want to print : ')
            print(df[col_name])
            wait = input()
        
        if ch == 6:
            print(df.describe())
            print("\n\n\nPress any key to continue....")
            wait=input()

        if ch == 7:
            a = input('Date of Census : ')
            b = int(input('Total Adults in Shelter : '))
            c = int(input('Total Children in Shelter : '))
            d = int(input('Total Individuals in Shelter : '))
            e = int(input('Single Adult Men in Shelter : '))
            f = int(input('Single Adult Women in Shelter : '))
            g = int(input('Total Single Adults in Shelter : '))
            h = int(input('Families with Children in Shelter : '))
            i = int(input('Adult Families in Shelter : '))
            j = int(input('Individuals in Adult Families in Shelter : '))

            data={'Date of Census':a,'Total Adults in Shelte':b,'Total Children in Shelter':c,'Total Individuals in Shelter':d,'Single Adult Men in Shelter':e,'Single Adult Women in Shelter':f,'Total Single Adults in Shelter':g,'Families with Children in Shelter':h,'Adult Families in Shelter':i,'Individuals in Adult Families in Shelter':j}
            df = df.append(data,ignore_index=True)
            print(df)
            wait = input()

        if ch == 8:
            print()
            print('Example : 12-31-2019,  month-date-year')
            print()
            fromdate = input('From Date : ')
            print()
            tilldate = input('Till Date : ')
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            newdf = (df['Date of Census'] > fromdate) & (df['Date of Census'] <= tilldate )
            newdf = df.loc[newdf]
            print(newdf)



            wait = input()

        if ch == 9:
            print(df)
            print()
            index_no =int(input('Enter the Index Number that You want to delete :'))
            df = df.drop(df.index[index_no])
            print(df)
            print('\n\n\n Press any key to continue....')
            wait = input()

            
        if ch == 00:
            break
        


#graphs
        
def graph():
    while True:
        print()
        print('░▄▀▀▀░░░█▀▀▄░▄▀▀▄░█▀▀▄░█░░█░░░░░░█▄░▄█░█▀▀░█▄ ░█░█░░░█░')
        print('░█  ▄░░░█▄▄▀░█▄▄█░█▄▄▀░█▄▄█░░░░░░█ ▀ █░█▀░░█░▀▄█░█░░░█░')
        print('░▀▄▄▄▀▄░█░ █░█░░█░█░░░░█░░█░░░░░░█░░░█░█▄▄░█░░░█░▀▄▄▄▀░')
        print('\nGRAPH MENU ')
        print('_'*76)
        print()
        print('1. Graph for 2018\n')
        print('2. Graph for 2019\n')
        print('3. Graph for 2020\n')
        print('4. Graph for 2021\n')
        print('5. Graph By User Condition\n')
        print('6. Summary Graph\n')
        print('00. Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:' ))
        print()
        
    #1. Graph for 2018
        
        if ch==1:
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            d1= df.loc[(df['Date of Census']>='01-Jan-2018') & (df['Date of Census']<='31-Dec-2018')]
        
            a=d1.loc[(d1['Date of Census']>='01-Jan-2018') & (df['Date of Census']<='31-1-2018')]
            a1=a['Total Adults in Shelter'].mean()
            a2=a['Total Children in Shelter'].mean()
            a3=a['Total Individuals in Shelter'].mean()
            a4=a['Single Adult Men in Shelter'].mean()
            a5=a['Single Adult Women in Shelter'].mean()
            a6=a['Total Single Adults in Shelter'].mean()
            a7=a['Families with Children in Shelter'].mean()
            a8=a['Adult Families in Shelter'].mean()
            a9=a['Individuals in Adult Families in Shelter'].mean()

            b=d1.loc[(d1['Date of Census']>='01-Feb-2018') & (df['Date of Census']<='28-Feb-2018')]
            b1=b['Total Adults in Shelter'].mean()
            b2=b['Total Children in Shelter'].mean()
            b3=b['Total Individuals in Shelter'].mean()
            b4=b['Single Adult Men in Shelter'].mean()
            b5=b['Single Adult Women in Shelter'].mean()
            b6=b['Total Single Adults in Shelter'].mean()
            b7=b['Families with Children in Shelter'].mean()
            b8=b['Adult Families in Shelter'].mean()
            b9=b['Individuals in Adult Families in Shelter'].mean()
        
            c=d1.loc[(d1['Date of Census']>='01-Mar-2018') & (df['Date of Census']<='31-Mar-2018')]
            c1=c['Total Adults in Shelter'].mean()
            c2=c['Total Children in Shelter'].mean()
            c3=c['Total Individuals in Shelter'].mean()
            c4=c['Single Adult Men in Shelter'].mean()
            c5=c['Single Adult Women in Shelter'].mean()
            c6=c['Total Single Adults in Shelter'].mean()
            c7=c['Families with Children in Shelter'].mean()
            c8=c['Adult Families in Shelter'].mean()
            c9=c['Individuals in Adult Families in Shelter'].mean()
        
        
            z=d1.loc[(d1['Date of Census']>='01-Apr-2018') & (df['Date of Census']<='30-Apr-2018')]
            z1=z['Total Adults in Shelter'].mean()
            z2=z['Total Children in Shelter'].mean()
            z3=z['Total Individuals in Shelter'].mean()
            z4=z['Single Adult Men in Shelter'].mean()
            z5=z['Single Adult Women in Shelter'].mean()
            z6=z['Total Single Adults in Shelter'].mean()
            z7=z['Families with Children in Shelter'].mean()
            z8=z['Adult Families in Shelter'].mean()
            z9=z['Individuals in Adult Families in Shelter'].mean()
        
            e=d1.loc[(d1['Date of Census']>='01-May-2018') & (df['Date of Census']<='31-May-2018')]
            e1=e['Total Adults in Shelter'].mean()
            e2=e['Total Children in Shelter'].mean()
            e3=e['Total Individuals in Shelter'].mean()
            e4=e['Single Adult Men in Shelter'].mean()
            e5=e['Single Adult Women in Shelter'].mean()
            e6=e['Total Single Adults in Shelter'].mean()
            e7=e['Families with Children in Shelter'].mean()
            e8=e['Adult Families in Shelter'].mean()
            e9=e['Individuals in Adult Families in Shelter'].mean()

            f=d1.loc[(d1['Date of Census']>='01-Jun-2018') & (df['Date of Census']<='30-Jun-2018')]
            f1=f['Total Adults in Shelter'].mean()
            f2=f['Total Children in Shelter'].mean()
            f3=f['Total Individuals in Shelter'].mean()
            f4=f['Single Adult Men in Shelter'].mean()
            f5=f['Single Adult Women in Shelter'].mean()
            f6=f['Total Single Adults in Shelter'].mean()
            f7=f['Families with Children in Shelter'].mean()
            f8=f['Adult Families in Shelter'].mean()
            f9=f['Individuals in Adult Families in Shelter'].mean()
        
            g=d1.loc[(d1['Date of Census']>='01-Jul-2018') & (df['Date of Census']<='31-Jul-2018')]
            g1=g['Total Adults in Shelter'].mean()
            g2=g['Total Children in Shelter'].mean()
            g3=g['Total Individuals in Shelter'].mean()
            g4=g['Single Adult Men in Shelter'].mean()
            g5=g['Single Adult Women in Shelter'].mean()
            g6=g['Total Single Adults in Shelter'].mean()
            g7=g['Families with Children in Shelter'].mean()
            g8=g['Adult Families in Shelter'].mean()
            g9=g['Individuals in Adult Families in Shelter'].mean()

            h=d1.loc[(d1['Date of Census']>='01-Aug-2018') & (df['Date of Census']<='31-Aug-2018')]
            h1=h['Total Adults in Shelter'].mean()
            h2=h['Total Children in Shelter'].mean()
            h3=h['Total Individuals in Shelter'].mean()
            h4=h['Single Adult Men in Shelter'].mean()
            h5=h['Single Adult Women in Shelter'].mean()
            h6=h['Total Single Adults in Shelter'].mean()
            h7=h['Families with Children in Shelter'].mean()
            h8=h['Adult Families in Shelter'].mean()
            h9=h['Individuals in Adult Families in Shelter'].mean()
        
            i=d1.loc[(d1['Date of Census']>='01-Sep-2018') & (df['Date of Census']<='30-Sep-2018')]
            i1=i['Total Adults in Shelter'].mean()
            i2=i['Total Children in Shelter'].mean()
            i3=i['Total Individuals in Shelter'].mean()
            i4=i['Single Adult Men in Shelter'].mean()
            i5=i['Single Adult Women in Shelter'].mean()
            i6=i['Total Single Adults in Shelter'].mean()
            i7=i['Families with Children in Shelter'].mean()
            i8=i['Adult Families in Shelter'].mean()
            i9=i['Individuals in Adult Families in Shelter'].mean()

            j=d1.loc[(d1['Date of Census']>='01-Oct-2018') & (df['Date of Census']<='31-Oct-2018')]
            j1=j['Total Adults in Shelter'].mean()
            j2=j['Total Children in Shelter'].mean()
            j3=j['Total Individuals in Shelter'].mean()
            j4=j['Single Adult Men in Shelter'].mean()
            j5=j['Single Adult Women in Shelter'].mean()
            j6=j['Total Single Adults in Shelter'].mean()
            j7=j['Families with Children in Shelter'].mean()
            j8=j['Adult Families in Shelter'].mean()
            j9=j['Individuals in Adult Families in Shelter'].mean()
        
            k=d1.loc[(d1['Date of Census']>='01-Nov-2018') & (df['Date of Census']<='30-Nov-2018')]
            k1=k['Total Adults in Shelter'].mean()
            k2=k['Total Children in Shelter'].mean()
            k3=k['Total Individuals in Shelter'].mean()
            k4=k['Single Adult Men in Shelter'].mean()
            k5=k['Single Adult Women in Shelter'].mean()
            k6=k['Total Single Adults in Shelter'].mean()
            k7=k['Families with Children in Shelter'].mean()
            k8=k['Adult Families in Shelter'].mean()
            k9=k['Individuals in Adult Families in Shelter'].mean()
            
            l=d1.loc[(d1['Date of Census']>='01-Dec-2018') & (df['Date of Census']<='31-Dec-2018')]
            l1=l['Total Adults in Shelter'].mean()
            l2=l['Total Children in Shelter'].mean()
            l3=l['Total Individuals in Shelter'].mean()
            l4=l['Single Adult Men in Shelter'].mean()
            l5=l['Single Adult Women in Shelter'].mean()
            l6=l['Total Single Adults in Shelter'].mean()
            l7=l['Families with Children in Shelter'].mean()
            l8=l['Adult Families in Shelter'].mean()
            l9=l['Individuals in Adult Families in Shelter'].mean()
   
            x=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
            y1=[a1,b1,c1,z1,e1,f1,g1,h1,i1,j1,k1,l1]
            y2=[a2,b2,c2,z2,e2,f2,g2,h2,i2,j2,k2,l2]
            y3=[a3,b3,c3,z3,e3,f3,g3,h3,i3,j3,k3,l3]
            y4=[a4,b4,c4,z4,e4,f4,g4,h4,i4,j4,k4,l4]
            y5=[a5,b5,c5,z5,e5,f5,g5,h5,i5,j5,k5,l5]
            y6=[a6,b6,c6,z6,e6,f6,g6,h6,i6,j6,k6,l6]
            y7=[a7,b7,c7,z7,e7,f7,g7,h7,i7,j7,k7,l7]
            y8=[a8,b8,c8,z8,e8,f8,g8,h8,i8,j8,k8,l8]
            y9=[a9,b9,c9,z9,e9,f9,g9,h9,i9,j9,k9,l9]
            plt.ylabel('Number of People in NYC Homeless Shelters in 2018')
            plt.title('2018')
            plt.grid(True)
            print('1. Line Graph\n')
            print('2. Bar Graph\n')
            print()
            
            z=input("Enter your choice : ")
            print()
            print('*****************************************')

        #Line Graph for year 2018

            if z == '1' :
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column : ")
                if n=='1':
                    plt.plot(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.plot(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.plot(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.plot(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.plot(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.plot(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.plot(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.plot(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.plot(x,y9,label='Individuals in Adult Families in Shelter')

        #Bar Graph for year 2018
                    
            if z == '2':
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column:")
                if n=='1':
                    plt.bar(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.bar(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.bar(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.bar(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.bar(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.bar(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.bar(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.bar(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.bar(x,y9,label='Individuals in Adult Families in Shelter')
                
            plt.legend()
            plt.show()
            wait = input()

        #2. Graph for 2019

        if ch==2:
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            d1= df.loc[(df['Date of Census']>='01-Jan-2019') & (df['Date of Census']<='31-Dec-2019')]
        
            a=d1.loc[(d1['Date of Census']>='01-Jan-2019') & (df['Date of Census']<='31-1-2019')]
            a1=a['Total Adults in Shelter'].mean()
            a2=a['Total Children in Shelter'].mean()
            a3=a['Total Individuals in Shelter'].mean()
            a4=a['Single Adult Men in Shelter'].mean()
            a5=a['Single Adult Women in Shelter'].mean()
            a6=a['Total Single Adults in Shelter'].mean()
            a7=a['Families with Children in Shelter'].mean()
            a8=a['Adult Families in Shelter'].mean()
            a9=a['Individuals in Adult Families in Shelter'].mean()

            b=d1.loc[(d1['Date of Census']>='01-Feb-2019') & (df['Date of Census']<='28-Feb-2019')]
            b1=b['Total Adults in Shelter'].mean()
            b2=b['Total Children in Shelter'].mean()
            b3=b['Total Individuals in Shelter'].mean()
            b4=b['Single Adult Men in Shelter'].mean()
            b5=b['Single Adult Women in Shelter'].mean()
            b6=b['Total Single Adults in Shelter'].mean()
            b7=b['Families with Children in Shelter'].mean()
            b8=b['Adult Families in Shelter'].mean()
            b9=b['Individuals in Adult Families in Shelter'].mean()
        
            c=d1.loc[(d1['Date of Census']>='01-Mar-2019') & (df['Date of Census']<='31-Mar-2019')]
            c1=c['Total Adults in Shelter'].mean()
            c2=c['Total Children in Shelter'].mean()
            c3=c['Total Individuals in Shelter'].mean()
            c4=c['Single Adult Men in Shelter'].mean()
            c5=c['Single Adult Women in Shelter'].mean()
            c6=c['Total Single Adults in Shelter'].mean()
            c7=c['Families with Children in Shelter'].mean()
            c8=c['Adult Families in Shelter'].mean()
            c9=c['Individuals in Adult Families in Shelter'].mean()
        
        
            z=d1.loc[(d1['Date of Census']>='01-Apr-2019') & (df['Date of Census']<='30-Apr-2019')]
            z1=z['Total Adults in Shelter'].mean()
            z2=z['Total Children in Shelter'].mean()
            z3=z['Total Individuals in Shelter'].mean()
            z4=z['Single Adult Men in Shelter'].mean()
            z5=z['Single Adult Women in Shelter'].mean()
            z6=z['Total Single Adults in Shelter'].mean()
            z7=z['Families with Children in Shelter'].mean()
            z8=z['Adult Families in Shelter'].mean()
            z9=z['Individuals in Adult Families in Shelter'].mean()
        

            e=d1.loc[(d1['Date of Census']>='01-May-2019') & (df['Date of Census']<='31-May-2019')]
            e1=e['Total Adults in Shelter'].mean()
            e2=e['Total Children in Shelter'].mean()
            e3=e['Total Individuals in Shelter'].mean()
            e4=e['Single Adult Men in Shelter'].mean()
            e5=e['Single Adult Women in Shelter'].mean()
            e6=e['Total Single Adults in Shelter'].mean()
            e7=e['Families with Children in Shelter'].mean()
            e8=e['Adult Families in Shelter'].mean()
            e9=e['Individuals in Adult Families in Shelter'].mean()

            f=d1.loc[(d1['Date of Census']>='01-Jun-2019') & (df['Date of Census']<='30-Jun-2019')]
            f1=f['Total Adults in Shelter'].mean()
            f2=f['Total Children in Shelter'].mean()
            f3=f['Total Individuals in Shelter'].mean()
            f4=f['Single Adult Men in Shelter'].mean()
            f5=f['Single Adult Women in Shelter'].mean()
            f6=f['Total Single Adults in Shelter'].mean()
            f7=f['Families with Children in Shelter'].mean()
            f8=f['Adult Families in Shelter'].mean()
            f9=f['Individuals in Adult Families in Shelter'].mean()
        
            g=d1.loc[(d1['Date of Census']>='01-Jul-2019') & (df['Date of Census']<='31-Jul-2019')]
            g1=g['Total Adults in Shelter'].mean()
            g2=g['Total Children in Shelter'].mean()
            g3=g['Total Individuals in Shelter'].mean()
            g4=g['Single Adult Men in Shelter'].mean()
            g5=g['Single Adult Women in Shelter'].mean()
            g6=g['Total Single Adults in Shelter'].mean()
            g7=g['Families with Children in Shelter'].mean()
            g8=g['Adult Families in Shelter'].mean()
            g9=g['Individuals in Adult Families in Shelter'].mean()

            h=d1.loc[(d1['Date of Census']>='01-Aug-2019') & (df['Date of Census']<='31-Aug-2019')]
            h1=h['Total Adults in Shelter'].mean()
            h2=h['Total Children in Shelter'].mean()
            h3=h['Total Individuals in Shelter'].mean()
            h4=h['Single Adult Men in Shelter'].mean()
            h5=h['Single Adult Women in Shelter'].mean()
            h6=h['Total Single Adults in Shelter'].mean()
            h7=h['Families with Children in Shelter'].mean()
            h8=h['Adult Families in Shelter'].mean()
            h9=h['Individuals in Adult Families in Shelter'].mean()
        
            i=d1.loc[(d1['Date of Census']>='01-Sep-2019') & (df['Date of Census']<='30-Sep-2019')]
            i1=i['Total Adults in Shelter'].mean()
            i2=i['Total Children in Shelter'].mean()
            i3=i['Total Individuals in Shelter'].mean()
            i4=i['Single Adult Men in Shelter'].mean()
            i5=i['Single Adult Women in Shelter'].mean()
            i6=i['Total Single Adults in Shelter'].mean()
            i7=i['Families with Children in Shelter'].mean()
            i8=i['Adult Families in Shelter'].mean()
            i9=i['Individuals in Adult Families in Shelter'].mean()

            j=d1.loc[(d1['Date of Census']>='01-Oct-2019') & (df['Date of Census']<='31-Oct-2019')]
            j1=j['Total Adults in Shelter'].mean()
            j2=j['Total Children in Shelter'].mean()
            j3=j['Total Individuals in Shelter'].mean()
            j4=j['Single Adult Men in Shelter'].mean()
            j5=j['Single Adult Women in Shelter'].mean()
            j6=j['Total Single Adults in Shelter'].mean()
            j7=j['Families with Children in Shelter'].mean()
            j8=j['Adult Families in Shelter'].mean()
            j9=j['Individuals in Adult Families in Shelter'].mean()
        
            k=d1.loc[(d1['Date of Census']>='01-Nov-2019') & (df['Date of Census']<='30-Nov-2019')]
            k1=k['Total Adults in Shelter'].mean()
            k2=k['Total Children in Shelter'].mean()
            k3=k['Total Individuals in Shelter'].mean()
            k4=k['Single Adult Men in Shelter'].mean()
            k5=k['Single Adult Women in Shelter'].mean()
            k6=k['Total Single Adults in Shelter'].mean()
            k7=k['Families with Children in Shelter'].mean()
            k8=k['Adult Families in Shelter'].mean()
            k9=k['Individuals in Adult Families in Shelter'].mean()
        
            l=d1.loc[(d1['Date of Census']>='01-Dec-2019') & (df['Date of Census']<='31-Dec-2019')]
            l1=l['Total Adults in Shelter'].mean()
            l2=l['Total Children in Shelter'].mean()
            l3=l['Total Individuals in Shelter'].mean()
            l4=l['Single Adult Men in Shelter'].mean()
            l5=l['Single Adult Women in Shelter'].mean()
            l6=l['Total Single Adults in Shelter'].mean()
            l7=l['Families with Children in Shelter'].mean()
            l8=l['Adult Families in Shelter'].mean()
            l9=l['Individuals in Adult Families in Shelter'].mean()
       
            x=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
            y1=[a1,b1,c1,z1,e1,f1,g1,h1,i1,j1,k1,l1]
            y2=[a2,b2,c2,z2,e2,f2,g2,h2,i2,j2,k2,l2]
            y3=[a3,b3,c3,z3,e3,f3,g3,h3,i3,j3,k3,l3]
            y4=[a4,b4,c4,z4,e4,f4,g4,h4,i4,j4,k4,l4]
            y5=[a5,b5,c5,z5,e5,f5,g5,h5,i5,j5,k5,l5]
            y6=[a6,b6,c6,z6,e6,f6,g6,h6,i6,j6,k6,l6]
            y7=[a7,b7,c7,z7,e7,f7,g7,h7,i7,j7,k7,l7]
            y8=[a8,b8,c8,z8,e8,f8,g8,h8,i8,j8,k8,l8]
            y9=[a9,b9,c9,z9,e9,f9,g9,h9,i9,j9,k9,l9]
            plt.ylabel('Number of People in NYC Homeless Shelters in 2019')
            plt.title('2019')
            plt.grid(True)
            print('1. Line Graph\n')
            print('2. Bar Graph\n')
            print()
            
            z=input("Enter your choice : ")
            print()
            print('*****************************************')

        #Line Graph for year 2019

            if z == '1' :
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column : ")
                if n=='1':
                    plt.plot(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.plot(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.plot(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.plot(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.plot(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.plot(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.plot(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.plot(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.plot(x,y9,label='Individuals in Adult Families in Shelter')
                    
        #Bar Graph for year 2019
                    
            if z == '2':
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column:")
                if n=='1':
                    plt.bar(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.bar(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.bar(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.bar(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.bar(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.bar(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.bar(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.bar(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.bar(x,y9,label='Individuals in Adult Families in Shelter')
                
            plt.legend()
            plt.show()
            wait = input()

        #3. Graph for 2020
            
        if ch==3:
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            d1= df.loc[(df['Date of Census']>='01-Jan-2020') & (df['Date of Census']<='31-Dec-2020')]
            
            a=d1.loc[(d1['Date of Census']>='01-Jan-2020') & (df['Date of Census']<='31-1-2020')]
            a1=a['Total Adults in Shelter'].mean()
            a2=a['Total Children in Shelter'].mean()
            a3=a['Total Individuals in Shelter'].mean()
            a4=a['Single Adult Men in Shelter'].mean()
            a5=a['Single Adult Women in Shelter'].mean()
            a6=a['Total Single Adults in Shelter'].mean()
            a7=a['Families with Children in Shelter'].mean()
            a8=a['Adult Families in Shelter'].mean()
            a9=a['Individuals in Adult Families in Shelter'].mean()

            b=d1.loc[(d1['Date of Census']>='01-Feb-2020') & (df['Date of Census']<='28-Feb-2020')]
            b1=b['Total Adults in Shelter'].mean()
            b2=b['Total Children in Shelter'].mean()
            b3=b['Total Individuals in Shelter'].mean()
            b4=b['Single Adult Men in Shelter'].mean()
            b5=b['Single Adult Women in Shelter'].mean()
            b6=b['Total Single Adults in Shelter'].mean()
            b7=b['Families with Children in Shelter'].mean()
            b8=b['Adult Families in Shelter'].mean()
            b9=b['Individuals in Adult Families in Shelter'].mean()
        
            c=d1.loc[(d1['Date of Census']>='01-Mar-2020') & (df['Date of Census']<='31-Mar-2020')]
            c1=c['Total Adults in Shelter'].mean()
            c2=c['Total Children in Shelter'].mean()
            c3=c['Total Individuals in Shelter'].mean()
            c4=c['Single Adult Men in Shelter'].mean()
            c5=c['Single Adult Women in Shelter'].mean()
            c6=c['Total Single Adults in Shelter'].mean()
            c7=c['Families with Children in Shelter'].mean()
            c8=c['Adult Families in Shelter'].mean()
            c9=c['Individuals in Adult Families in Shelter'].mean()
        
        
            z=d1.loc[(d1['Date of Census']>='01-Apr-2020') & (df['Date of Census']<='30-Apr-2020')]
            z1=z['Total Adults in Shelter'].mean()
            z2=z['Total Children in Shelter'].mean()
            z3=z['Total Individuals in Shelter'].mean()
            z4=z['Single Adult Men in Shelter'].mean()
            z5=z['Single Adult Women in Shelter'].mean()
            z6=z['Total Single Adults in Shelter'].mean()
            z7=z['Families with Children in Shelter'].mean()
            z8=z['Adult Families in Shelter'].mean()
            z9=z['Individuals in Adult Families in Shelter'].mean()
        

            e=d1.loc[(d1['Date of Census']>='01-May-2020') & (df['Date of Census']<='31-May-2020')]
            e1=e['Total Adults in Shelter'].mean()
            e2=e['Total Children in Shelter'].mean()
            e3=e['Total Individuals in Shelter'].mean()
            e4=e['Single Adult Men in Shelter'].mean()
            e5=e['Single Adult Women in Shelter'].mean()
            e6=e['Total Single Adults in Shelter'].mean()
            e7=e['Families with Children in Shelter'].mean()
            e8=e['Adult Families in Shelter'].mean()
            e9=e['Individuals in Adult Families in Shelter'].mean()

            f=d1.loc[(d1['Date of Census']>='01-Jun-2020') & (df['Date of Census']<='30-Jun-2020')]
            f1=f['Total Adults in Shelter'].mean()
            f2=f['Total Children in Shelter'].mean()
            f3=f['Total Individuals in Shelter'].mean()
            f4=f['Single Adult Men in Shelter'].mean()
            f5=f['Single Adult Women in Shelter'].mean()
            f6=f['Total Single Adults in Shelter'].mean()
            f7=f['Families with Children in Shelter'].mean()
            f8=f['Adult Families in Shelter'].mean()
            f9=f['Individuals in Adult Families in Shelter'].mean()
        
            g=d1.loc[(d1['Date of Census']>='01-Jul-2020') & (df['Date of Census']<='31-Jul-2020')]
            g1=g['Total Adults in Shelter'].mean()
            g2=g['Total Children in Shelter'].mean()
            g3=g['Total Individuals in Shelter'].mean()
            g4=g['Single Adult Men in Shelter'].mean()
            g5=g['Single Adult Women in Shelter'].mean()
            g6=g['Total Single Adults in Shelter'].mean()
            g7=g['Families with Children in Shelter'].mean()
            g8=g['Adult Families in Shelter'].mean()
            g9=g['Individuals in Adult Families in Shelter'].mean()

            h=d1.loc[(d1['Date of Census']>='01-Aug-2020') & (df['Date of Census']<='31-Aug-2020')]
            h1=h['Total Adults in Shelter'].mean()
            h2=h['Total Children in Shelter'].mean()
            h3=h['Total Individuals in Shelter'].mean()
            h4=h['Single Adult Men in Shelter'].mean()
            h5=h['Single Adult Women in Shelter'].mean()
            h6=h['Total Single Adults in Shelter'].mean()
            h7=h['Families with Children in Shelter'].mean()
            h8=h['Adult Families in Shelter'].mean()
            h9=h['Individuals in Adult Families in Shelter'].mean()
        
            i=d1.loc[(d1['Date of Census']>='01-Sep-2020') & (df['Date of Census']<='30-Sep-2020')]
            i1=i['Total Adults in Shelter'].mean()
            i2=i['Total Children in Shelter'].mean()
            i3=i['Total Individuals in Shelter'].mean()
            i4=i['Single Adult Men in Shelter'].mean()
            i5=i['Single Adult Women in Shelter'].mean()
            i6=i['Total Single Adults in Shelter'].mean()
            i7=i['Families with Children in Shelter'].mean()
            i8=i['Adult Families in Shelter'].mean()
            i9=i['Individuals in Adult Families in Shelter'].mean()

            j=d1.loc[(d1['Date of Census']>='01-Oct-2020') & (df['Date of Census']<='31-Oct-2020')]
            j1=j['Total Adults in Shelter'].mean()
            j2=j['Total Children in Shelter'].mean()
            j3=j['Total Individuals in Shelter'].mean()
            j4=j['Single Adult Men in Shelter'].mean()
            j5=j['Single Adult Women in Shelter'].mean()
            j6=j['Total Single Adults in Shelter'].mean()
            j7=j['Families with Children in Shelter'].mean()
            j8=j['Adult Families in Shelter'].mean()
            j9=j['Individuals in Adult Families in Shelter'].mean()
        
            k=d1.loc[(d1['Date of Census']>='01-Nov-2020') & (df['Date of Census']<='30-Nov-2020')]
            k1=k['Total Adults in Shelter'].mean()
            k2=k['Total Children in Shelter'].mean()
            k3=k['Total Individuals in Shelter'].mean()
            k4=k['Single Adult Men in Shelter'].mean()
            k5=k['Single Adult Women in Shelter'].mean()
            k6=k['Total Single Adults in Shelter'].mean()
            k7=k['Families with Children in Shelter'].mean()
            k8=k['Adult Families in Shelter'].mean()
            k9=k['Individuals in Adult Families in Shelter'].mean()
        
            l=d1.loc[(d1['Date of Census']>='01-Dec-2020') & (df['Date of Census']<='31-Dec-2020')]
            l1=l['Total Adults in Shelter'].mean()
            l2=l['Total Children in Shelter'].mean()
            l3=l['Total Individuals in Shelter'].mean()
            l4=l['Single Adult Men in Shelter'].mean()
            l5=l['Single Adult Women in Shelter'].mean()
            l6=l['Total Single Adults in Shelter'].mean()
            l7=l['Families with Children in Shelter'].mean()
            l8=l['Adult Families in Shelter'].mean()
            l9=l['Individuals in Adult Families in Shelter'].mean()
   
            x=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
            y1=[a1,b1,c1,z1,e1,f1,g1,h1,i1,j1,k1,l1]
            y2=[a2,b2,c2,z2,e2,f2,g2,h2,i2,j2,k2,l2]
            y3=[a3,b3,c3,z3,e3,f3,g3,h3,i3,j3,k3,l3]
            y4=[a4,b4,c4,z4,e4,f4,g4,h4,i4,j4,k4,l4]
            y5=[a5,b5,c5,z5,e5,f5,g5,h5,i5,j5,k5,l5]
            y6=[a6,b6,c6,z6,e6,f6,g6,h6,i6,j6,k6,l6]
            y7=[a7,b7,c7,z7,e7,f7,g7,h7,i7,j7,k7,l7]
            y8=[a8,b8,c8,z8,e8,f8,g8,h8,i8,j8,k8,l8]
            y9=[a9,b9,c9,z9,e9,f9,g9,h9,i9,j9,k9,l9]
            plt.ylabel('Number of People in NYC Homeless Shelters in 2020')
            plt.title('2020')
            plt.grid(True)
            print('1. Line Graph\n')
            print('2. Bar Graph\n')
            print()
            
            z=input("Enter your choice : ")
            print()
            print('*****************************************')

        #Line Graph for year 2020

            if z == '1' :
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column : ")
                if n=='1':
                    plt.plot(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.plot(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.plot(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.plot(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.plot(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.plot(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.plot(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.plot(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.plot(x,y9,label='Individuals in Adult Families in Shelter')
                    
        #Bar Graph for year 2020
                    
            if z == '2':
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column:")
                if n=='1':
                    plt.bar(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.bar(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.bar(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.bar(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.bar(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.bar(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.bar(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.bar(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.bar(x,y9,label='Individuals in Adult Families in Shelter')
                
            plt.legend()
            plt.show()
            wait = input()

        #4. Graph for 2021

        if ch==4:
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            d1= df.loc[(df['Date of Census']>='01-Jan-2021') & (df['Date of Census']<='31-Dec-2021')]
        
            a=d1.loc[(d1['Date of Census']>='01-Jan-2021') & (df['Date of Census']<='31-1-2021')]
        
            a1=a['Total Adults in Shelter'].mean()
            a2=a['Total Children in Shelter'].mean()
            a3=a['Total Individuals in Shelter'].mean()
            a4=a['Single Adult Men in Shelter'].mean()
            a5=a['Single Adult Women in Shelter'].mean()
            a6=a['Total Single Adults in Shelter'].mean()
            a7=a['Families with Children in Shelter'].mean()
            a8=a['Adult Families in Shelter'].mean()
            a9=a['Individuals in Adult Families in Shelter'].mean()

            b=d1.loc[(d1['Date of Census']>='01-Feb-2021') & (df['Date of Census']<='28-Feb-2021')]
            b1=b['Total Adults in Shelter'].mean()
            b2=b['Total Children in Shelter'].mean()
            b3=b['Total Individuals in Shelter'].mean()
            b4=b['Single Adult Men in Shelter'].mean()
            b5=b['Single Adult Women in Shelter'].mean()
            b6=b['Total Single Adults in Shelter'].mean()
            b7=b['Families with Children in Shelter'].mean()
            b8=b['Adult Families in Shelter'].mean()
            b9=b['Individuals in Adult Families in Shelter'].mean()
        
            c=d1.loc[(d1['Date of Census']>='01-Mar-2021') & (df['Date of Census']<='31-Mar-2021')]
            c1=c['Total Adults in Shelter'].mean()
            c2=c['Total Children in Shelter'].mean()
            c3=c['Total Individuals in Shelter'].mean()
            c4=c['Single Adult Men in Shelter'].mean()
            c5=c['Single Adult Women in Shelter'].mean()
            c6=c['Total Single Adults in Shelter'].mean()
            c7=c['Families with Children in Shelter'].mean()
            c8=c['Adult Families in Shelter'].mean()
            c9=c['Individuals in Adult Families in Shelter'].mean()
        
            z=d1.loc[(d1['Date of Census']>='01-Apr-2021') & (df['Date of Census']<='30-Apr-2021')]
            z1=z['Total Adults in Shelter'].mean()
            z2=z['Total Children in Shelter'].mean()
            z3=z['Total Individuals in Shelter'].mean()
            z4=z['Single Adult Men in Shelter'].mean()
            z5=z['Single Adult Women in Shelter'].mean()
            z6=z['Total Single Adults in Shelter'].mean()
            z7=z['Families with Children in Shelter'].mean()
            z8=z['Adult Families in Shelter'].mean()
            z9=z['Individuals in Adult Families in Shelter'].mean()
        

            e=d1.loc[(d1['Date of Census']>='01-May-2021') & (df['Date of Census']<='31-May-2021')]
            e1=e['Total Adults in Shelter'].mean()
            e2=e['Total Children in Shelter'].mean()
            e3=e['Total Individuals in Shelter'].mean()
            e4=e['Single Adult Men in Shelter'].mean()
            e5=e['Single Adult Women in Shelter'].mean()
            e6=e['Total Single Adults in Shelter'].mean()
            e7=e['Families with Children in Shelter'].mean()
            e8=e['Adult Families in Shelter'].mean()
            e9=e['Individuals in Adult Families in Shelter'].mean()

            f=d1.loc[(d1['Date of Census']>='01-Jun-2021') & (df['Date of Census']<='30-June-2021')]
            f1=f['Total Adults in Shelter'].mean()
            f2=f['Total Children in Shelter'].mean()
            f3=f['Total Individuals in Shelter'].mean()
            f4=f['Single Adult Men in Shelter'].mean()
            f5=f['Single Adult Women in Shelter'].mean()
            f6=f['Total Single Adults in Shelter'].mean()
            f7=f['Families with Children in Shelter'].mean()
            f8=f['Adult Families in Shelter'].mean()
            f9=f['Individuals in Adult Families in Shelter'].mean()
        
            g=d1.loc[(d1['Date of Census']>='01-Jul-2021') & (df['Date of Census']<='31-Jul-2021')]
            g1=g['Total Adults in Shelter'].mean()
            g2=g['Total Children in Shelter'].mean()
            g3=g['Total Individuals in Shelter'].mean()
            g4=g['Single Adult Men in Shelter'].mean()
            g5=g['Single Adult Women in Shelter'].mean()
            g6=g['Total Single Adults in Shelter'].mean()
            g7=g['Families with Children in Shelter'].mean()
            g8=g['Adult Families in Shelter'].mean()
            g9=g['Individuals in Adult Families in Shelter'].mean()

            h=d1.loc[(d1['Date of Census']>='01-Aug-2021') & (df['Date of Census']<='31-Aug-2021')]
            h1=h['Total Adults in Shelter'].mean()
            h2=h['Total Children in Shelter'].mean()
            h3=h['Total Individuals in Shelter'].mean()
            h4=h['Single Adult Men in Shelter'].mean()
            h5=h['Single Adult Women in Shelter'].mean()
            h6=h['Total Single Adults in Shelter'].mean()
            h7=h['Families with Children in Shelter'].mean()
            h8=h['Adult Families in Shelter'].mean()
            h9=h['Individuals in Adult Families in Shelter'].mean()
        
            i=d1.loc[(d1['Date of Census']>='01-Sep-2021') & (df['Date of Census']<='30-Sep-2021')]
            i1=i['Total Adults in Shelter'].mean()
            i2=i['Total Children in Shelter'].mean()
            i3=i['Total Individuals in Shelter'].mean()
            i4=i['Single Adult Men in Shelter'].mean()
            i5=i['Single Adult Women in Shelter'].mean()
            i6=i['Total Single Adults in Shelter'].mean()
            i7=i['Families with Children in Shelter'].mean()
            i8=i['Adult Families in Shelter'].mean()
            i9=i['Individuals in Adult Families in Shelter'].mean()

            j=d1.loc[(d1['Date of Census']>='01-Oct-2021') & (df['Date of Census']<='31-Oct-2021')]
            j1=j['Total Adults in Shelter'].mean()
            j2=j['Total Children in Shelter'].mean()
            j3=j['Total Individuals in Shelter'].mean()
            j4=j['Single Adult Men in Shelter'].mean()
            j5=j['Single Adult Women in Shelter'].mean()
            j6=j['Total Single Adults in Shelter'].mean()
            j7=j['Families with Children in Shelter'].mean()
            j8=j['Adult Families in Shelter'].mean()
            j9=j['Individuals in Adult Families in Shelter'].mean()
        
            k=d1.loc[(d1['Date of Census']>='01-Nov-2021') & (df['Date of Census']<='30-Nov-2021')]
            k1=k['Total Adults in Shelter'].mean()
            k2=k['Total Children in Shelter'].mean()
            k3=k['Total Individuals in Shelter'].mean()
            k4=k['Single Adult Men in Shelter'].mean()
            k5=k['Single Adult Women in Shelter'].mean()
            k6=k['Total Single Adults in Shelter'].mean()
            k7=k['Families with Children in Shelter'].mean()
            k8=k['Adult Families in Shelter'].mean()
            k9=k['Individuals in Adult Families in Shelter'].mean()
        
            l=d1.loc[(d1['Date of Census']>='01-Dec-2021') & (df['Date of Census']<='31-Dec-2021')]
            l1=l['Total Adults in Shelter'].mean()
            l2=l['Total Children in Shelter'].mean()
            l3=l['Total Individuals in Shelter'].mean()
            l4=l['Single Adult Men in Shelter'].mean()
            l5=l['Single Adult Women in Shelter'].mean()
            l6=l['Total Single Adults in Shelter'].mean()
            l7=l['Families with Children in Shelter'].mean()
            l8=l['Adult Families in Shelter'].mean()
            l9=l['Individuals in Adult Families in Shelter'].mean()
   
            x=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
            y1=[a1,b1,c1,z1,e1,f1,g1,h1,i1,j1,k1,l1]
            y2=[a2,b2,c2,z2,e2,f2,g2,h2,i2,j2,k2,l2]
            y3=[a3,b3,c3,z3,e3,f3,g3,h3,i3,j3,k3,l3]
            y4=[a4,b4,c4,z4,e4,f4,g4,h4,i4,j4,k4,l4]
            y5=[a5,b5,c5,z5,e5,f5,g5,h5,i5,j5,k5,l5]
            y6=[a6,b6,c6,z6,e6,f6,g6,h6,i6,j6,k6,l6]
            y7=[a7,b7,c7,z7,e7,f7,g7,h7,i7,j7,k7,l7]
            y8=[a8,b8,c8,z8,e8,f8,g8,h8,i8,j8,k8,l8]
            y9=[a9,b9,c9,z9,e9,f9,g9,h9,i9,j9,k9,l9]
            plt.ylabel('Number of People in NYC Homeless Shelters in 2021')
            plt.title('2021')
            plt.grid(True)
            print('1. Line Graph\n')
            print('2. Bar Graph\n')
            print()
            
            z=input("Enter your choice : ")
            print()
            print('*****************************************')

        #Line Graph for year 2021

            if z == '1' :
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column : ")
                if n=='1':
                    plt.plot(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.plot(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.plot(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.plot(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.plot(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.plot(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.plot(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.plot(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.plot(x,y9,label='Individuals in Adult Families in Shelter')
                    
        #Bar Graph for year 2021
                    
            if z == '2':
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column:")
                if n=='1':
                    plt.bar(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.bar(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.bar(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.bar(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.bar(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.bar(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.bar(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.bar(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.bar(x,y9,label='Individuals in Adult Families in Shelter')
                
            plt.legend()
            plt.show()
            wait = input()

        #5. Graph By User Condition

        if ch==5:
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            fromdate = input('From Date : ')
            print()
            tilldate = input('Till Date : ')
        
            d1= df.loc[(df['Date of Census']>=fromdate) & (df['Date of Census']<=tilldate)]
            print(d1)
        
            a1=d1['Total Adults in Shelter'].mean()
            a2=d1['Total Children in Shelter'].mean()
            a3=d1['Total Individuals in Shelter'].mean()
            a4=d1['Single Adult Men in Shelter'].mean()
            a5=d1['Single Adult Women in Shelter'].mean()
            a6=d1['Total Single Adults in Shelter'].mean()
            a7=d1['Families with Children in Shelter'].mean()
            a8=d1['Adult Families in Shelter'].mean()
            a9=d1['Individuals in Adult Families in Shelter'].mean()

            x=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
            z=('Total Adults in Shelter','Total Children in Shelter','Total Individuals in Shelter','Single Adult Men in Shelter','Single Adult Women in Shelter','Total Single Adults in Shelter','Families with Children in Shelter','Adult Families in Shelter','Individuals in Adult Families in Shelter')
            xpos=np.arange(len(z))
            plt.xlabel('Columns')
            plt.ylabel('Numbers')
            plt.title('Graph By User Condition')
            plt.xticks(xpos,z)
            plt.grid(True)
            plt.plot(x)
            plt.show()
            wait = input()

        #6. Summary Graph

        if ch==6:
            df['Date of Census'] = pd.to_datetime(df['Date of Census'])
            df1= df.loc[(df['Date of Census']>='01-Jan-2018') & (df['Date of Census']<='31-Dec-2018')]
            a1=df1['Total Adults in Shelter'].mean()
            a2=df1['Total Children in Shelter'].mean()
            a3=df1['Total Individuals in Shelter'].mean()
            a4=df1['Single Adult Men in Shelter'].mean()
            a5=df1['Single Adult Women in Shelter'].mean()
            a6=df1['Total Single Adults in Shelter'].mean()
            a7=df1['Families with Children in Shelter'].mean()
            a8=df1['Adult Families in Shelter'].mean()
            a9=df1['Individuals in Adult Families in Shelter'].mean()

            df2= df.loc[(df['Date of Census']>='01-Jan-2019') & (df['Date of Census']<='31-Dec-2019')]
            b1=df2['Total Adults in Shelter'].mean()
            b2=df2['Total Children in Shelter'].mean()
            b3=df2['Total Individuals in Shelter'].mean()
            b4=df2['Single Adult Men in Shelter'].mean()
            b5=df2['Single Adult Women in Shelter'].mean()
            b6=df2['Total Single Adults in Shelter'].mean()
            b7=df2['Families with Children in Shelter'].mean()
            b8=df2['Adult Families in Shelter'].mean()
            b9=df2['Individuals in Adult Families in Shelter'].mean()

            df3= df.loc[(df['Date of Census']>='01-Jan-2020') & (df['Date of Census']<='31-Dec-2020')]
            c1=df3['Total Adults in Shelter'].mean()
            c2=df3['Total Children in Shelter'].mean()
            c3=df3['Total Individuals in Shelter'].mean()
            c4=df3['Single Adult Men in Shelter'].mean()
            c5=df3['Single Adult Women in Shelter'].mean()
            c6=df3['Total Single Adults in Shelter'].mean()
            c7=df3['Families with Children in Shelter'].mean()
            c8=df3['Adult Families in Shelter'].mean()
            c9=df3['Individuals in Adult Families in Shelter'].mean()

            df4= df.loc[(df['Date of Census']>='01-Jan-2021') & (df['Date of Census']<='31-Dec-2021')]
            d1=df4['Total Adults in Shelter'].mean()
            d2=df4['Total Children in Shelter'].mean()
            d3=df4['Total Individuals in Shelter'].mean()
            d4=df4['Single Adult Men in Shelter'].mean()
            d5=df4['Single Adult Women in Shelter'].mean()
            d6=df4['Total Single Adults in Shelter'].mean()
            d7=df4['Families with Children in Shelter'].mean()
            d8=df4['Adult Families in Shelter'].mean()
            d9=df4['Individuals in Adult Families in Shelter'].mean()

            x=['2018','2019','2020','2021']
            y1=[a1,b1,c1,d1]
            y2=[a2,b2,c2,d2]
            y3=[a3,b3,c3,d3]
            y4=[a4,b4,c4,d4]
            y5=[a5,b5,c5,d5]
            y6=[a6,b6,c6,d6]
            y7=[a7,b7,c7,d7]
            y8=[a8,b8,c8,d8]
            y9=[a9,b9,c9,d9]
            z=('2018','2019','2020','2021')
            xpos=np.arange(len(z))
            plt.xlabel('Years')
            plt.ylabel('Numbers')
            plt.xticks(xpos,z)
            plt.title('Summary Graph')
            plt.grid(True)
            print('1. Line Graph\n')
            print('2. Bar Graph\n')
            print()
            
            z=input("Enter your choice : ")
            print()
            print('*****************************************')

        #Line Graph for Summary

            if z == '1' :
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column : ")
                if n=='1':
                    plt.plot(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.plot(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.plot(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.plot(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.plot(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.plot(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.plot(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.plot(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.plot(x,y9,label='Individuals in Adult Families in Shelter')

        #Bar Graph for Summary
                    
            if z == '2':
                print('''
1.Total Adults,            2.Total Children,       3.Total Individuals ,
4.Single Adult Men,        5.Single Adult Women,   6.Total Single Adults ,
7.Families with Children,  8.Adult Families,       9.Individuals in Adult Families  ''')
                print()
                print('*****************************************')
                
                n=input("For which column:")
                if n=='1':
                    plt.bar(x,y1,label='Total Adults in Shelter')
                if n=='2':
                    plt.bar(x,y2,label='Total Children in Shelter')
                if n=='3':
                    plt.bar(x,y3,label='Total Individuals in Shelter')
                if n=='4':
                    plt.bar(x,y4,label='Single Adult Men in Shelter')
                if n=='5':
                    plt.bar(x,y5,label='Single Adult Women in Shelter')
                if n=='6':
                    plt.bar(x,y6,label='Total Single Adults in Shelter')
                if n=='7':
                    plt.bar(x,y7,label='Families with Children in Shelter')
                if n=='8':
                    plt.bar(x,y8,label='Adult Families in Shelter')
                if n=='9':
                    plt.bar(x,y9,label='Individuals in Adult Families in Shelter')
                
            plt.legend()
            plt.show()
            wait = input()

        if ch==00:
            break


#export
            
def export_menu():
    while True:
        print()
        print('░█▀▀░▀▄░░▄▀░█▀▀▄░▄▀▀▄░█▀▀▄░▀▀█▀▀░░░░░░█▄░▄█░█▀▀░█▄░░█░█░░░█░')
        print('░█▀░░░░██░░░█▄▄▀░█░░█░█▄▄▀░░░█░░░░░░░░█ ▀ █░█▀░░█░▀▄█░█░░░█░')
        print('░█▄▄░▄▀░░▀▄░█░░░░▀▄▄▀░█░ █░░░█░░░░░░░░█░░░█░█▄▄░█░░░█░▀▄▄▄▀░')
        print('\n\nEXPORT MENU ')
        print('_'*76)
        print()
        print('1. CSV File\n')
        print('2. Excel File\n')
        print('00. Exit (Move to main menu)')
        print()
        ch = int(input('Enter your Choice : '))
        
        if ch==1:
            df.to_csv("/Users/Kritikabassi/Desktop/Python Programs Class 12/DHS_Daily_Report Updated.csv")
            print('\n\nCheck your new file "newPassport.csv" on C:Drive.....')        
            wait = input()
            
        if ch == 2:
            df.to_excel("/Users/Kritikabassi/Desktop/Python Programs Class 12/DHS_Daily_Report Updated.csv")
            print('\n\nCheck your new file "newPassport.xlsx" on C:Drive.....')
            wait = input()

        if ch == 00:
            break
    

main()
