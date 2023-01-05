["BABUK","cuba","DAIXIN ","ragnar_Locker","RANSOMEXX","RANSOM HOUSE","Mallox"]
import schedule
import time
from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import pymongo
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


links=[]
'''d=["http://woqjumaahi662ka26jzxyx7fznbp4kg3bsjar4b52tqkxgm2pylcjlad.onion/","http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/HackTown.html","http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion"]
status=[]
urgent=[]'''

def scrap0():
    try:
    



        with TorBrowserDriver("/home/linux/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://woqjumaahi662ka26jzxyx7fznbp4kg3bsjar4b52tqkxgm2pylcjlad.onion/')
    
            data = driver.page_source
            alldata = "".join(data)
    #print(alldata)
            soup = BeautifulSoup(alldata,'html.parser')
            head = soup.find_all('h2',class_="post-title")
            head1 = soup.find_all('span')
    #link= soup.find_all('a')
            date=driver.find_elements(By.XPATH,'/html/body/div/div[3]/section/div/a')
            heading=[]
            print(len(links))
        
            Date=[]
            about=[]
            for i in date:
                links.append(i.get_attribute('href'))
            for i in head1:
                Date.append(i.text)
            for i in head:
                heading.append(i.text)
            for o in links:
                driver.get(o)
                ta=driver.page_source
                aldata="".join(ta)
                soup=BeautifulSoup('aldata','html.parser')
                di=driver.find_elements(By.XPATH,'/html/body/div/div[3]/div[1]/div[3]')
                tem=''
                for i in di:
                    tem+=str(i.text)
                about.append(tem)
            
        
        print(len(about))
    
        print(links)
        print(heading)
        print(Date)
        print(len(links))
        links.clear()
        return "runnned"
    except:
        print("driver error")
def scrap1():
    try:
    




        with TorBrowserDriver("/home/linux/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/HackTown.html')
            time.sleep(5.9)
            data = driver.page_source
            alldata = "".join(data)
    #print(alldata)
            soup = BeautifulSoup(alldata,'html.parser')
    #head = soup.find_all('h5')
    
    #head1 = soup.find_all('div',class_="col-auto published")
            link= soup.find_all('p')
            linke= soup.find_all('a')
            date=driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div/font/div/center/a')
            title=[]
        #links=["https://geeksadvice.com/remove-mallox-ransomware-virus/"]
    
            '''Body=[]
    
            #heading=["Remove MALLOX Ransomware Virus (DECRYPT .mallox FILES"]
        tem=''
        for i in range(3,len(link)-26):
            tem+=link[i].text
        Body.append(tem)'''
        

            for i in range(len(date)):
                if i%2==0:
                    x=date[i].get_attribute("href")
                    links.append(x)
            print(len(links))
            headi1=[]
            bdy=[]
            for o in links:
                driver.get(o)
                time.sleep(5.9)
                ta=driver.page_source
        
                aldata="".join(ta)
                soup=BeautifulSoup('aldata','html.parser')
                date=driver.find_elements(By.XPATH,'//*[@id="rules"]')
                date1=driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[2]/div/div/center/font/b')
        
        
        #print(lo)
                for i in date1:
                    headi1.append(i.text)
                tem=''
                for i in date:
                    tem+=i.text
                bdy.append(tem)
            
          
        print(len(bdy))
        print(headi1)
        createdAt=[]
        createdby=["prince","prince","prince","prince","prince","prince","prince","prince","prince","prince"]
        for i in range(9):
            createdAt.append("28-12-2022")
        return "runnned"
        links.clear()
    except:
        print("driver error")
def scrap2():
    try:
        with TorBrowserDriver("/home/linux/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
            driver.get('http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion')
            time.sleep(5.9)
            data = driver.page_source
            alldata = "".join(data)
    #print(alldata)
            soup = BeautifulSoup(alldata,'html.parser')
            head = soup.find_all('h5')
    
            head1 = soup.find_all('div',class_="col-auto published")
            link= soup.find_all('a')
            linke= soup.find_all('em')
            date=driver.find_elements(By.XPATH,'/html/body/div/div[3]/section/div/a')
            heading=[]
            
            Date=[]
            Body=[]
            heading=[]
            for i in head1:
                u=i.text
                uuu=u.strip('\n        ')
                Date.append(uuu)
            for i in range(4,len(head)-3):
                heading.append(head[i].text)
            for i in range(4,len(link)):
                x=link[i].get("href")
                u="http://nq4zyac4ukl4tykmidbzgdlvaboqeqsemkp4t35bzvjeve6zm2lqcjid.onion"+x
                links.append(u)
            for o in links:
                driver.get(o)
                time.sleep(5.9)
                data = driver.page_source
                alldata = "".join(data)
    #print(alldata)
                soup = BeautifulSoup(alldata,'html.parser')
                linke= soup.find_all('div',class_="container py-5 content-info")
                body=driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/p')
        
        
                tem=''
                for i in linke:
                    tem=i.text
                Body.append(tem)
            createddate=["26-12-2022"]*6
        print(Body)
        print(heading)
        links.clear()
    except:
        print("driver error")


client =pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db =client['prince']
collection =db['prince1']
def getfunction(func,status):
    if status=="null":
        if func=="f0":
            scrap0()
            collection.update_one({"name":'f0'},{'$set':{"urgent":False,"status":"done"}})
        elif func=="fun1":
            scrap1()
            collection.update_one({"name":'f1'},{'$set':{"urgent":False,"status":"done"}})
        else:
            scrap2()
            collection.update_one({"name":'f2'},{'$set':{"urgent":False,"status":"done"}})
print(len(links))
def run():
    pass
    if len(links)==0:
        if collection.count_documents({'urgent':True})>0:
            urgent1=collection.find({"urgent":True},{'_id':0,"name":1,"status":1,"urgent":1})
            for i in urgent1:
                site=[]
                for j,k in i.items():
                    if j=="name":
                        site.append(j)
                getfunction(site[0],"null")
        for item in collection.find({"status":"null"},{'_id':0,"name":1,"status":1,"urgent":1})   
            if collection.count_documents({'urgent':True})>0:
                urgent1=collection.find({"urgent":True},{'_id':0,"name":1,"status":1,"urgent":1})
                for i in urgent1:
                    site=[]
                    for j,k in i.items():
                        if j=="name":
                           site.append(j)
                    getfunction(site[0],"null")
            else:
                site=[]
                status=[]
                for j,k in item.items():
                    if i=="name":
                       site.append(j)
                    elif i=="status":
                        status.append(j)
                getfunction(site[0],status[0])   

        


 
	
schedule.every(5).minutes.do(run)



        


'''if len(links)==0:
    for i in range(2):
        if urgent[i]==1:
            if i==0:
                   
                schedule.every(1).minutes.do(scrap0)
                
                

            else:
                
                schedule.every(1).minutes.do(scrap1)
    for j in range(2):
        if status[j]==1:
            if j==0:
                schedule.every(1).minutes.do(scrap0)
            else:
                schedule.every(1).minutes.do(scrap1)'''

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
            
             

    






    
    
