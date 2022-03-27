*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kikka
    Set Password  kikka123
    Set Password Confirmation  kikka123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ki
    Set Password  kikka123
    Set Password Confirmation  kikka123
    Submit Credentials
    Register Should Fail With Message  Username or password too short

Register With Valid Username And Too Short Password
    Set Username  kikka
    Set Password  ki5
    Set Password Confirmation  ki5
    Submit Credentials
    Register Should Fail With Message  Username or password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kikka
    Set Password  kikka123
    Set Password Confirmation  kikka124
    Submit Credentials
    Register Should Fail With Message  Nonmatching passwords

Login After Successful Registration
    Set Username  kikka
    Set Password  kikka123
    Set Password Confirmation  kikka123
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Main Page Should Be Open
    Submit Logout
    Login Page Should Be Open
    Set Username  kikka
    Set Password  kikka123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kikka
    Set Password  ki5
    Set Password Confirmation  ki5
    Submit Credentials
    Register Should Fail With Message  Username or password too short
    Go To Login Page
    Login Page Should Be Open
    Set Username  kikka
    Set Password  ki5
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User  kukka  kukka123
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Submit Logout
    Click Button  Logout

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}