import time
import os
import datetime
import webbrowser
import pandas as pd

JP="      ## ########  \n      ## ##     ## \n      ## ##     ## \n      ## ########  \n##    ## ##        \n##    ## ##        \n ######  ##        " #My beautiful art xd
print("Loading csv...")
csv = pd.read_csv('classes.csv')
os.system('cls')
print("Zoomer by\n\n"+JP+"\n\nStatus: Running")
#monday 0 sunday 6
print("Started day:", datetime.date.today().weekday()) 
print("Started hour: "+time.strftime("%H:%M", time.localtime()))

dots=1
while True:
    print("Checking for classes "+("#"+str(dots)),end ="\r")
    dots=dots+1
    today=datetime.date.today().weekday()
    hour=time.strftime("%H:%M", time.localtime())
    for i in csv['time']:
        if i == hour:
            row = csv.loc[csv['time'] == i]
            day = str(row.iloc[0,1])
            link = str(row.iloc[0,2])
            days=day.split(',')
            for j in days:
                if str(j)==str(today):
                    print("")
                    print("Starting zoom...")
                    webbrowser.open(str(row.iloc[0,3]))
                    time.sleep(15)
                    webbrowser.open(link)
                    time.sleep(5)
                    exit()
                    print("")
                    #If you want to be all day joining remove the exit()
            #time.sleep(60*60)
    time.sleep(59)
