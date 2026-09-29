import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
pro=input("Enter the project title")
while True:
 print("-----------------------------------------------------------")
 print(" ", pro," ")
 print("-----------------------------------------------------------")
 mainmenu='''1. Read CSV/ Excel File
   \n2. Manipulation
   \n3. Analysis
   \n4. Visualisation
   \n5. Exit'''
 print(mainmenu)
 ch=int(input("Enter your choice"))
 if ch==1:
   print('''1. Read CSV File to create and Display DataFrame\
       \n2. Read Excel File to create and Display DataFrame\
       \n3. Press enter to go back''')
   ch1=int(input("Enter your choice"))
   if ch1==1:
      df=pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\Football management.csv")
      print(df)
      print("File Reterived Sucessfully!!!!")
   elif ch1==2:
     df=pd.read_excel("C:\\Users\\User\\OneDrive\\Desktop\\Football management.xlsx")
     print(df)
     print("File Reterived Sucessfully!!!!")
   elif ch1==3:
    pass
 elif ch==2:
  print('''\n 1.Insert a row\n
        2. Delete a row\n
        3. Enter to go back''')
  mch=int(input("Enter your choice"))
  if mch==1:
    col=df.columns
    print(col)
    print(df.head(1))
    j=0
    ninsert={}
    for i in col:
       print("Enter ", col[j], " value")
       nval=input()
       ninsert[col[j]]=nval
       j=j+1
       print(ninsert)
    df = df.append(ninsert, ignore_index=True)
    print("New row inserted")
    print(df)
  elif mch==2: 
    n=int(input("Enter The Row No To Be Deleted"))
    print(df.drop(n))
  elif mch==3:
    pass
 elif ch==3:
  print("Data Frame Analysis")
  menu=''' 1. Top record
        \n 2. Bottom Records
        \n 3. To print particular column
        \n 4. To print multiple columns
        \n 5. To display complete statitics of the dataframe
        \n Press enter to go back'''
  print(menu)
  ch3=int(input("Enter your choice"))
  if ch3==1:
      n=int(input("Enter the number of records to be displayed"))
      print("Top ", n," records from the dataframe")
      print(df.head(n))
  elif ch3==2:
      n=int(input("Enter the number of records to be displayed"))
      print("Bottom ", n," records from the dataframe")
      print(df.tail(n))
  elif ch3==3:
      print("Name of the columns\n",df.columns)
      co=input("Enter the column name to be displayed")
      print(df[[co]])
  elif ch3==4:
      print("Name of the columns\n",df.columns)
      co=eval(input("Enter the column names as list in square bracket"))
      print(df[co])
  elif ch3==5:
      print("Complete Statistics")
      print(df.describe())
  else:
       print("Invalid choice")
 elif ch==4:
       df=pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\Football management.csv")
       print("Data Visualisation of pandas data frame")
       menu=''' 1. To display histogram of all numeric columns
           \n 2. To display the line chart for each room number against room rate
           \n 3. To display BAR chart of duration AGAINST roomrate
           \n 4. press enter to go back'''
       print(menu)
       ch4=int(input("Enter your choice"))
       if ch4==1: 
           df.hist()
           plt.show()
       elif ch4==2:
           df.plot(x="Tno",y=['Total Wins',"UCL Titles"],kind='line',color=["red","green"])
           plt.xlabel("Team No.")
           plt.ylabel("no  of wins")
           plt.show()
       elif ch4==3:
           df.plot(x='Tno',y=['Total Wins',"TAge"],kind='bar')
           plt.xlabel("Team Number")
           plt.ylabel("total no of wins/no of years of play")
           plt.show()
       elif ch4==4:
           pass
       else:
           break
 else:
    break
con=input("DO YOU WANT TO CONTINUE")
if con=='n'or con=='N':
   sys.exit()

