# a= 10
# b= 20
# c="hello"
# print(a,b)
# ad= ("{}".format(a)+c)
# print(ad)
#bc=["hello",12,343,6565,"testing","dddd","oooo","qqqq"]
# bc[1]="jjjjj"
# print(bc)
# bc.append("uuuuuu")
# print(bc)
# bc.insert(6,c)
# print(bc)

# fruits=["apple", "banana", "cherry", "date", "elderberry"]
# print("First Fruit",fruits[0])
# print("Last Fruit",fruits[-1])
# print("Fruits from index 1 to 2",fruits[3:5])
# person=("king",25,5.9)
# print(person[2])
# print(type(bc))
# bc.append("helloking")
# print(bc)


##############################

# a=[]
# for x in range(6):
#     a.append(x)
# print(a)
# print(sum(a))

#############################
# a=15
# b=0
# while a > 3:
#     for x in range(8):
#         b=b+1
#         if b > 5:
#             a=1 
#             break
#         else:
#             print(b)

# print("completed")

####################################
# a="Hello"
# if a=="Hello":
#     print("Hello there!")
#     print("How can I assist you today?")
# else:
#     print("Greetings!")
#     print("Program has completed.")

###############################
# def uservalue():
#     value= float(input("enter number"))
#     user=value
#     if user >5 and user < 11:
#         print("Good Morning")
#     elif user >12 and user < 17:
#         print("Good Afternoon")
#     elif user >18 and user < 21:
#         print("Good Evening")
#     else:
#         print("Good Night")
#     print("Greeting code has completed.")
# uservalue()

########################################################
# a= 10
# b=["ADD" , "SUB", "MUL", "Div"]
# while  a <100 :
#     value1=input("enter the value for 1 : ")
#     if not value1.replace(".","",1).isdigit():
#         print("Enter correct value for value1")
#         continue
#     value1=float(value1)

#     value2= input("enter the value for 2 : ")
#     if not value2.replace(".","",1).isdigit():
#         print("Enter correct value for value2")
#         continue
#     value2=float(value2)

#     print("Enter the opction , Add , Sub, Mul, Div")
#     opction = input(("enter the opction : ")).upper()
#     if opction not in b:
#         print("enter correct opction ")
#         continue
    

#     if opction=="ADD":
#         addvalue=value1+value2
#         print("add value=:",addvalue)
#     elif opction =="SUB":
#         sub =value1-value2
#         print("sub value =",sub)
#     elif opction == "MUL":
#         mul= value1*value2
#         print("mul value =",mul)
#     elif opction == "DIV":
#         if value2 %2==0:
#             print("can not able devide the number ")
#         else:
#             div=value1%value2
#             print("div value=",div)


#     a=11100
#     break
#################################################################
# class BasicCalculator:
#     a=10
#     b=5
#     def Addition(self,):
#         Addition1=self.a+self.b
#         print(Addition1)
#     def Subtraction(self):
#         Subtraction1= self.a-self.b
#         print(Subtraction1)
#     def Multiplication(self):
#         Multiplication1= self.a*self.b
#         print(Multiplication1)
#     def Division(self):
#         Division1= self.a%self.b
#         print(Division1)
        
# basic=BasicCalculator()
# basic.Addition()
# basic.Subtraction()
# basic.Division()
# basic.Multiplication()
#####################################################       
# class GreetUser:
#     def __init__(self,username):
#         self.username=username
#     def fun(self):
#         print("hello",self.username,"Welcome to the Python course")
# gree=GreetUser("John")
# gree.fun()

# def CalculateAverage(num1,num2,num3):
#     num4= num1+num2+num3
#     return num4 / 3
# print(CalculateAverage(10,20,30))

# with open ("C:/Users/ganes/OneDrive/Desktop/RedantPython1/file1.txt") as data1:
#     # print("file open")
#     # data2=data1.readlines()
#     # for x in data2:
#     #     print(x)
#     #########################################
#     #print(data1.read())
#     print(data1.readline())
##############################################################
#from logging import exception


#file1=open("C:/Users/ganes/OneDrive/Desktop/RedantPython1/file1.txt","r")
# line=file1.readline()
# print(line)
# while   file1 !="":
#     print(file1.readline())
#     line=file1.readline()
# #########################################
# t=0
# for x in file1:
#     print(x)
#     t=t+1
# print(t)
# file1=open("C:/Users/ganes/OneDrive/Desktop/RedantPython1/file1.txt","r")
# t=0
# file2=file1.readline()
# while file2!="":
#     t=t+1
#     print(file2)
#     file2=file1.readline()
# print("Total number of lines:",t)
# f=file1.read()
# print(len(f))

#################################################
# ItemsInCart = 0
# def add_to_cart (items_to_add):
#     if items_to_add <0:
#         raise exception ("Cannot add a negative number of items")
# add_to_cart(-1)
##########################################
# ItemsInCart = 0
# def add_to_cart (items_to_add):
#     try:

#         if items_to_add <0:
#             a= items_to_add+items_to_add
#             print(a)
    
#     except Exception as e:
#         print("error occess")
#         print("Error:", e)

   
#     finally:
#         print("last line in this code ")
# add_to_cart("Hello")
##############################################
# person=("Rahul", 25, 5.9)
# try:
#     print(person[1])
#     person[1]="hello"
# except exception as e:
#     print(e)
# finally:
#     print(person,"No change")
#################################################
# import time
# from selenium import webdriver
# d=webdriver.Chrome()
# d.get("https://www.google.co.in/")
# print(d.title)
# print(d.current_url)
# a=d.current_url
# assert "golgl" in a ,"issue "
# time.sleep(2)
# d.quit()
######################################################
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
driver = webdriver.Chrome()
driver.implicitly_wait(5)
wait =WebDriverWait(driver,5)
driver.maximize_window()
url= "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.find_element(By.CLASS_NAME,"form-control").send_keys("hello")
driver.find_element(By.NAME,"email").send_keys("ganesh.com")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.ID,"exampleFormControlSelect1").click()
driver.find_element(By.XPATH,'(//input[@class="form-control"])[2]').send_keys("22-4-1998")
driver.find_element(By.XPATH,'//*[@id="exampleFormControlSelect1"]/option[1]').click()
driver.find_element(By.XPATH,'//input[@name="bday"]').click()
driver.find_element(By.XPATH,'//input[@value="Submit"]').click()
d=wait.until(ES.visibility_of_element_located((By.XPATH,"/html/body/app-root/form-comp/div/div[2]/div"))).text
print(d)
time.sleep(2)
##########################################################
 
# import time
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium .webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ES

# driver1=webdriver.Chrome()
# wait = WebDriverWait(driver1,5)
# driver1.maximize_window()
# driver1.implicitly_wait(10)
# driver1.get("https://rahulshettyacademy.com/client")
# driver1.find_element(By.PARTIAL_LINK_TEXT,"Register here").click()
# driver1.find_element(By.ID,"firstName").send_keys("Ganesh")
# driver1.find_element(By.ID,"lastName").send_keys("testing")
# driver1.find_element(By.XPATH,"/html/body/app-root/app-register/div[1]/section[2]/div/div[2]/form/div[2]/div[1]/input").send_keys("Ganesh@gmail.com")
# d=Select(driver1.find_element(By.XPATH,'//select[@formcontrolname="occupation"]'))
# d.select_by_visible_text("Scientist")
# driver1.find_element(By.XPATH,'//input[@value="Male"]').click()
# driver1.find_element(By.XPATH,'//input[@id="userPassword"]').send_keys("Password@1")
# driver1.find_element(By.XPATH,'//input[@type="checkbox"]').click()
# driver1.find_element(By.ID,"userMobile").send_keys("9999999887")
# driver1.find_element(By.ID,"confirmPassword").send_keys("Password@1")
# driver1.find_element(By.ID,"login").click()
# d1=wait.until(ES.presence_of_element_located(((By.XPATH,'//*[@id="toast-container"]/div/div'))))
# d2=d1.text

# print(d2)

# if "User already exisits with this Email Id" in d2 or "User already exists with this Email Id" in d2:
#     login_link = driver1.find_element(By.CSS_SELECTOR, "a[href*='login']")
#     login_link.click()
#     print("Clicked on login link")



# print("Completed")
# time.sleep(2)
# driver1.quit


######################################################################################################################################

# from selenium import webdriver
# import time
# from selenium .webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver2=webdriver.Chrome()
# driver2.implicitly_wait(5)
# wait_time= WebDriverWait(driver2,5)
# driver2.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver2.find_element(By.ID,"autosuggest").send_keys("ind")
# value1=wait_time.until(EC.presence_of_all_elements_located((By.XPATH,'//li[@class="ui-menu-item"]')))
# for x in value1:
#     print(x.text)
#     if x.text=="India":
#         x.click()
#         break

# print("--------------------------------------------")
# text1=wait_time.until(EC.presence_of_element_located((By.ID,"autosuggest"))).get_attribute("value")
# print(text1)
# assert "Ind" in text1
# driver2.find_element(By.ID,"ctl00_mainContent_ddl_originStation1_CTXT").clear()
# driver2.find_element(By.ID,"ctl00_mainContent_ddl_originStation1_CTXT").send_keys("Po")
# value2=wait_time.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="dropdownGroup1"]/div/ul/li/a')))
# for x1 in value2:
#     print(x1.text.strip())
#     if x1.text=="Pondicherry (PNY)":
#         x1.click()
# print("--------------------------------------------")
# driver2.find_element(By.ID,"ctl00_mainContent_ddl_destinationStation1_CTXT").click()
# value3=driver2.find_elements(By.XPATH,'//*[@id="dropdownGroup1"]/div/ul/li/a')
# for x3 in value3:
#     print(x3.text)
#     if x3.text == "Kochi (COK)":
#         x3.click()
#         break

# value4=driver2.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr/td/a')
# for x4 in value4:
#     print(x4.text)
#     if x4.text=="10":
#         x4.click()
#         break

# driver2.find_element(By.XPATH,'//*[@id="ctl00_mainContent_btn_FindFlights"]').click()
# time.sleep(5)
  
##########
# value5= driver2.find_elements(By.XPATH,'//*[@id="divpaxOptions"]/div/div/label')
# for x5 in value5:
#     if x5.text =="Adult":


# //*[@id="hrefIncAdt"]

# /html/body/form/div[4]/div[2]/div/div[5]/div[2]/div[2]/div[2]/div[3]/div/div[6]/div[3]/div[1]/div[2]/span[3]  
# //*[@id="divpaxOptions"]/div/div/div/span[3]

############################################################

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver3=webdriver.Chrome()
# driver3.get("https://rahulshettyacademy.com/AutomationPractice/")
# v1=driver3.find_elements(By.XPATH,'//*[@id="checkbox-example"]/fieldset/label/input')
# for x in v1:
#     R=x.get_attribute("value")
#     print(R)
#     if R =="option2":
#         x.click()
#         break
# v2=Select(driver3.find_element(By.XPATH,'//select[@id="dropdown-class-example"]'))
# v2.select_by_visible_text("Option2")
# time.sleep(2)
#########################################################################
# from selenium import webdriver
# from selenium .webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver4 = webdriver.Chrome()
# driver4.implicitly_wait(5)
# driver4.get("https://rahulshettyacademy.com/AutomationPractice/")
# d4=driver4.find_elements(By.XPATH,'//div[@id="radio-btn-example"]//fieldset//label//input')
# for x4 in d4:
#     if x4.get_attribute("value")=="radio2":
#         x4.click()
#         value1=x4
        
# assert value1.is_selected()
# print("correct")
#########################################################################################
# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #from selenium.webdriver.common.alert import Alert
# from selenium .webdriver.support import expected_conditions as EC
# value1="Testing"
# driver5= webdriver.Chrome()
# driver5.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver5.maximize_window()
# a1=driver5.find_element(By.XPATH,'//input[@name="show-hide"]') 
# assert a1.is_displayed()
# driver5.find_element(By.ID,"hide-textbox").click()
# time.sleep(1)
# assert not driver5.find_element(By.XPATH,'//input[@name="show-hide"]') .is_displayed()
# driver5.find_element(By.ID,"name").send_keys(value1)
# driver5.find_element(By.ID,"alertbtn").click()
# time.sleep(2)
# al=driver5.switch_to.alert
# print(al.text)
# al1=al.text
# assert value1 in al1
# al.accept()
# time.sleep(2)
##################################################################
# from selenium import webdriver
# from selenium .webdriver.common.by import By
# import time
# driver5 = webdriver.Chrome()
# value1="Testing"
# driver5.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver5.maximize_window()
# a1=driver5.find_element(By.XPATH,'//input[@name="show-hide"]') 
# assert a1.is_displayed()
# driver5.find_element(By.ID,"hide-textbox").click()
# time.sleep(1)
# assert not driver5.find_element(By.XPATH,'//input[@name="show-hide"]') .is_displayed()
# driver5.find_element(By.ID,"name").send_keys(value1)
# driver5.find_element(By.ID,"confirmbtn").click()
# time.sleep(2)
# al=driver5.switch_to.alert
# print(al.text)
# al1=al.text
# assert value1 in al1
# al.dismiss()
# time.sleep(2)
##################################################################################################//*[@id="productCartTables"]/tbody/tr[1]/td[5]/p
# data="rahulshettyacademy"
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ES
# total=0
# driver6=webdriver.Chrome()
# driver6.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver6.maximize_window()
# driver6.implicitly_wait(5)
# driver6.find_element(By.XPATH,'//input[@class="search-keyword"]').send_keys("ap")
# time.sleep(5)
# d6=driver6.find_elements(By.XPATH,'//div[@class="product"]')
# for i in d6:
#     p1= i.find_element(By.XPATH,'.//h4').text
#     print(p1)

#     if "Apple - 1 Kg" in p1 or "Grapes - 1 Kg" in p1:
#         p2=i.find_element(By.XPATH,'.//div//button')
#         p2.click()

  
        
# driver6.find_element(By.XPATH,'//a[@class="cart-icon"]').click()
# driver6.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
# driver6.find_element(By.XPATH,'//input[@class="promoCode"]').send_keys(data)
# driver6.find_element(By.XPATH,'//button[@class="promoBtn"]').click()
# value1=driver6.find_elements(By.XPATH,'//table[@id="productCartTables"]//tbody//tr//td[5]//p')
# timerwait=WebDriverWait(driver6,15)
# code=timerwait.until(ES.presence_of_element_located((By.XPATH,'//span[@class="promoInfo"]')))
# print(code.text)
# for x in value1:
#     value2=x.text
#     value3=int(value2)
#     total=total+value3
# print(total)     
# dl6=driver6.find_element(By.XPATH,'//span[@class="discountAmt"]').text
# print(dl6)
# dl6=float(dl6)
# print(type(dl6))
# print(type(total))
# assert dl6 < total,"value not match "
# time.sleep(2)
######################################################################################### 
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver7= webdriver.Chrome()
# data_From_List=["Brocolli - 1 Kg","Cauliflower - 1 Kg","Cucumber - 1 Kg","Carrot - 1 Kg","Capsicum","Corn - 1 Kg","Cashews - 1 Kg",]
# list=[]
# driver7.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver7.find_element(By.XPATH,'//input[@class="search-keyword"]').send_keys("c")
# time.sleep(2)
# data = driver7.find_elements(By.XPATH,'//div[@class="products"]//div/h4')
# for x in data:
#     list.append(x.text)
# print(list)
# assert data_From_List == list
# print("completed")
########################################################################
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# import time
# driver8=webdriver.Chrome()
# driver8.implicitly_wait(5)
# driver8.maximize_window()
# driver8.get("https://rahulshettyacademy.com/AutomationPractice/")
# actions=ActionChains(driver8)
# actions.double_click(driver8.find_element(By.ID,"checkBoxOption1")).perform()
# time.sleep(2)
# driver8.find_element(By.XPATH,'//input[@id="name"]').send_keys("hello")
# time.sleep(2)
# actions.move_to_element(driver8.find_element(By.ID,"mousehover")).perform()
# time.sleep(1)
# #actions.context_click(driver8.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[2]")).click().perform()
# actions.move_to_element(driver8.find_element(By.LINK_TEXT,"Reload")).click().perform()
# time.sleep(1)
#############################################################################
# from selenium import webdriver
# from selenium .webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# import time
# driver9= webdriver.Chrome()
# driver9.implicitly_wait(10)
# driver9.get("https://the-internet.herokuapp.com/windows")
# print(driver9.find_element(By.TAG_NAME,"h3").text)
# driver9.find_element(By.XPATH,'//*[@id="content"]/div/a').click()
# handles= driver9.window_handles
# time.sleep(3)
# driver9.switch_to.window(handles[1])
# text1=driver9.find_element(By.TAG_NAME,"h3").text
# print(text1)
# driver9.switch_to.window(handles[0])
# print(driver9.find_element(By.TAG_NAME,"h3").text)
# time.sleep(2)
############################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as Ex
# import time
# driver10= webdriver.Chrome()
# wait_time=WebDriverWait(driver10,7)
# driver10.implicitly_wait(5)
# driver10.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver10.maximize_window()
# driver10.switch_to.frame("courses-iframe")
# print(driver10.find_element(By.XPATH,'/html/body/div/header/div[2]/div/div/div[1]/ul/li').text)
# driver10.find_element(By.XPATH,"/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[5]/a").click() 
# print(wait_time.until(Ex.presence_of_element_located((By.XPATH,"/html/body/div/section[1]/div/div/h1"))).text)
# driver10.switch_to.default_content()
# driver10.find_element(By.XPATH,'//input[@id="name"]').send_keys("hello")
# time.sleep(2)
##########################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium .webdriver.support.wait import WebDriverWait
# from selenium .webdriver.support import expected_conditions as EX
# import time
# driver11= webdriver.Chrome()
# driver11.implicitly_wait(10)
# wait=WebDriverWait(driver11,10)
# driver11.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver11.maximize_window()
# driver11.switch_to.frame("courses-iframe")
# print(driver11.find_element(By.XPATH,'/html/body/div/header/div[2]/div/div/div[1]/ul/li').text)
# driver11.execute_script("window.scroll(0,window.document.body.scrollHeight)")
# driver11.find_element(By.XPATH,"/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[5]/a").click() 
# print(wait.until(EX.presence_of_element_located((By.XPATH,"/html/body/div/section[1]/div/div/h1"))).text)
# driver11.switch_to.default_content()
# driver11.find_element(By.XPATH,'//input[@id="name"]').send_keys("hello")
# driver11.get_screenshot_as_file("savetestfile.png")
# time.sleep(2)
##########################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium .webdriver.support.wait import WebDriverWait
# from selenium .webdriver.support import expected_conditions as EX
# import time
# options1=webdriver.ChromeOptions()
# options1.add_argument("headless")
# value=[]
# driver12= webdriver.Chrome(options=options1)
# wait=WebDriverWait(driver12,10)
# driver12.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver12.find_element(By.XPATH,'//div[@class="cart"]//a[2]').click()
# handles=driver12.window_handles
# driver12.switch_to.window(handles[1])
# wait.until(EX.presence_of_element_located((By.XPATH,"//th[@aria-label='Veg/fruit name: activate to sort column ascending']"))).click()
# data=driver12.find_elements(By.XPATH,'//*[@id="root"]/div/div[1]/div/div/div/div/table/tbody/tr/td[1]')
# for x in data:
#     value.append(x.text)
# print(value)
# value.sort()
# print(value)
# time.sleep(2)
##################################################################################
# import openpyxl
# open1=openpyxl.load_workbook("C:\\Users\\ganes\\Downloads\\openxl.xlsx")
# sheet=open1.active
# print(sheet.max_column)
# print(sheet.max_row)
# for x in range(1,sheet.max_row+1):
#     for y in range(1,sheet.max_column+1):
#         if sheet.cell(row=x,column=1).value==2:
#            print(sheet.cell(row=x,column=y).value)
###############################################################
# from selenium import webdriver
# from selenium .webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium .webdriver.support import expected_conditions as EC
# driver13= webdriver.Chrome()
# driver13.implicitly_wait(5)
# driver13.get("rahulshettyacademy.com/upload-download-test/index.html")
# driver13.find_element(By.ID,"downloadButton").click()
# driver13.find_element(By.ID,"fileinput").send_keys()












