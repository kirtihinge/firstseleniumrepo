# import time
#
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
#
# from behave import *
# from selenium import webdriver
#
#
# # @given(u'open chrome browser')
# # def openbrowser(context):
# #     context.driver = webdriver.Chrome(executable_path="C:\selenium driver\chromedriver_win32\chromedriver.exe")
# #     # raise NotImplementedError(u'STEP: Given open chrome browser')
#
#
# # @when(u'Enter url')
# # def enterurl(context):
# #     context.driver.get("https://demo.guru99.com/v4/")
# #     # raise NotImplementedError(u'STEP: When Enter url')
# #
# #
# # @when(u'Enter username "{un}" and password "{password}"')
# # def step_impl(context, un, password):
# #     context.driver.find_element(By.NAME, "uid").send_keys(un)
# #     context.driver.find_element(By.NAME, "password").send_keys(password)
# #     time.sleep(3)
# #
# #
# # @when(u'Click on Login button')
# # def step_impl(context):
# #     context.driver.find_element(By.NAME, "btnLogin").click()
# #     time.sleep(3)
#
#
# @when(u'click on Edit Account')
# def step_impl(context):
#     context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Edit Account').click()
#     time.sleep(3)
#
# @when(u'Enter account no "{accountno}"')
# def step_impl(context, accountno):
#     context.driver.find_element(By.NAME, 'accountno').send_keys(accountno)
#     time.sleep(3)
#
# @when(u'Click on submit')
# def step_impl(context):
#     context.driver.find_element(By.NAME, 'AccSubmit').click()
#
#
# @then(u'check edit account page')
# def step_impl(context):
#     alert = Alert(context.driver)
#
#     # get alert text
#     errmsg = alert.text
#
#     # accept the alert
#     alert.accept()
#     time.sleep(5)
#     assert errmsg == "Account does not exist"
