*** Settings ***
Resource    ../../../shared_resources/shared_resource.robot

*** Keywords ***
Sign In TO Booking.com
    SignIn.Sign In To Booking    ${USERNAME}    ${PASSWORD}