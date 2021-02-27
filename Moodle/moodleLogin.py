from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
u=input("enter username")
pwd=input("enter password")
text=driver.find_element_by_id("login").text
l=text.split('\n')
p=l[3].split()[1]
if p=="add":
    ans=int(l[3].split()[2]) + int(l[3].split()[4])
elif p=="subtract":
    ans=int(l[3].split()[2]) - int(l[3].split()[4])
else:
    if l[3].split()[2]=="first":
        ans=int(l[3].split()[4])
    else:
        ans=int(l[3].split()[6])
username=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
cap=driver.find_element_by_id("valuepkg3")
username.send_keys(u)
password.send_keys(pwd)
cap.send_keys(ans)
submit=driver.find_element_by_id("loginbtn").click()



    

