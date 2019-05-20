*** Settings ***
Library           SeleniumLibrary
Library           Process
Library           Screenshot
Library           Collections
Library           String
Library           OperatingSystem
Library           XML
Library           selenium_extensions.selenium_extensions.SeleniumExtensions    WITH NAME    SL
# Page objcets
Library           sign_in.sign_in.SignIn    WITH NAME    SignIn
# Variable files
Variables         variable_file/common_variables.py    test