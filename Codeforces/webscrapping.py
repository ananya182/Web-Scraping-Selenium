from selenium import webdriver
import os
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
n=input("Contest number??")
driver.get("https://codeforces.com/contest/{}".format(n))
text=driver.find_element_by_class_name("problems").text
l=text.split('\n')
l=l[1:]
probs=len(l)//5
x=[]
for i in range(0,len(l),5):
    x.append(l[i])
os.mkdir(n)
for i in x:
    os.mkdir("{}/{}".format(n,i))
    driver.get("https://codeforces.com/contest/{}/problem/{}".format(n,i))
    driver.save_screenshot("{}/{}/problem.png".format(n,i))
    inp=driver.find_element_by_class_name("input").text
    out=driver.find_element_by_class_name("output").text
    l=inp.split("\n")[3:]
    m=out.split("\n")[2:]
    factor=max(len(l),len(m))//min(len(l),len(m))
    c1=1
    c2=1
    for j in range(0,len(l),factor):
        f=open("{}/{}/input{}.txt".format(n,i,c1),"w")
        f.writelines(l[j:j+factor])
        f.close()
        c1+=1
    for k in m:
        g=open("{}/{}/output{}.txt".format(n,i,c2),"w")
        g.write(k)
        g.close()
        c2+=1
        
    
        
        
        

