*** Settings ***
Resource          resources/sign_in_resource.robot
Suite Teardown    Close All Browsers

*** Test Cases ***
Start Login
    [Tags]  sign_in
    Sign In TO Booking.com