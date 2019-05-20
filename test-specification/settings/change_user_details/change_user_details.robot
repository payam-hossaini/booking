*** Settings ***
Resource          resources/change_user_details_resource.robot
# Suite Teardown    Close All Browsers

*** Test Cases ***
Start Login
    [Tags]  login
    Sign In TO Booking.com