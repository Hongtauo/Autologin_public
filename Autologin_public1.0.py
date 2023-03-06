import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#读取文件中的网址
def ReadSetting(Username,Password,Adress):
    # 获取绝对路径
    path=os.getcwd()
    #path=os.path.realpath(os.path.dirname(sys.executable))
    file = open(path+"\\Setting.txt",'r',encoding='utf-8')
    lines = file.readlines()
    for lines in lines:
        if "Username=" in lines:
            Username=lines[len("Username="):]
        if "Password=" in lines:
            Password=lines[len("Password="):]
        if "Adress=" in lines:
            Adress=lines[len("Adress="):]
    return Username,Password,Adress
            
def AutoOption(driver,Username,Password):

    inputUsername = driver.find_element(By.XPATH, '//*[@id="username"]')
    inputUsername.send_keys(Username)
    
    #输入密码(出现异常按F12检查元素，删除遮挡的隐藏元素，找到真正的输入框）
    time.sleep(2)
    pwd = driver.find_element(By.ID, 'pwd')
    ActionChains(driver).send_keys_to_element(pwd,Password).perform()

    clickButton = driver.find_element(By.XPATH,'//*[@id="selectDisname"]')
    clickButton.click()
    
    time.sleep(2)
    clickButton = driver.find_element(By.XPATH,'//*[@id="_service_1"]')
    clickButton.click()

    time.sleep(2)
    clickButton = driver.find_element(By.XPATH,'//*[@id="loginLink_div"]')
    clickButton.click()

    time.sleep(2)
    #driver.quit()

#将网址载入脚本中
def Load(Username,Password,Adress):
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=option)

    driver.get(Adress)
    AutoOption(driver,Username,Password)
def top():
    Username='null'
    Password='null'
    Adress='nul'
    Username,Password,Adress=ReadSetting(Username,Password,Adress)
    Load(Username,Password,Adress)

top()
