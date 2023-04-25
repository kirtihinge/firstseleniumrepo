# import time
#
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
#
# from behave import *
# from selenium import webdriver
# from POM import loginpom
#
#
# @given(u'open chrome browser')
# def openbrowser(context):
#     context.driver = webdriver.Chrome(executable_path="C:\selenium driver\chromedriver_win32\chromedriver.exe")
#     # raise NotImplementedError(u'STEP: Given open chrome browser')
#     time.sleep(3)
#
# @when(u'Enter url')
# def enterURL(context):
#     context.driver.get("https://demo.guru99.com/v4/")
#     time.sleep(3)
#
# # @when(u'Enter username "{ur}" and password "{password}"')
# # def step_impl(context,un,password):
# #     context.driver.find_element(By.NAME,"uid").send_keys(ur)
# #     context.driver.find_element(By.NAME,"password").send_keys(password)
# #     time.sleep(3)
#
# @when(u'Enter username and password')
# def step_impl(context):
#     context.driver.find_element(By.NAME, "uid").send_keys(loginpom.username)
#     context.driver.find_element(By.NAME, "password").send_keys(loginpom.password)
#     time.sleep(3)
#
#
# @when(u'Click on Login button')
# def step_impl(context):
#     context.driver.find_element(By.NAME, "btnLogin").click()
#     time.sleep(3)
#
#
# @when(u'click on Edit Customer')
# def step_impl(context):
#     context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Edit Customer').click()
#     time.sleep(3)
#
#
# @when(u'Enter Customer id "{cusid}"')
# def step_impl(context, cusid):
#     context.driver.find_element(By.NAME, 'cusid').send_keys(cusid)
#
#
# @when(u'Click on submit button')
# def step_impl(context):
#     context.driver.find_element(By.NAME, 'AccSubmit').click()
#
#
# # @then(u'login page should be displayed')
# # def checkloginpage(context):
# #     title=context.driver.title
# #     assert title=="Guru99 Bank Home Page"
# #     # raise NotImplementedError(u'STEP: Then login page should be displayed')
# #
# # @then(u'home page should be displayed')
# # def step_impl(context):
# #     title=context.driver.title
# #     assert title=="Guru99 Bank Manager HomePage"
#
# @then(u'Edit account page should be displayed')
# def step_impl(context):
#     alert = Alert(context.driver)
#
#     # get alert text
#     errmsg = alert.text
#
#     # accept the alert
#     alert.accept()
#     time.sleep(5)
#     assert errmsg == "Customer does not exist!!"
