*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  timo
    Set Password  timo12345
    Set Password Confirmation  timo12345
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  tt
    Set Password  wordpass
    Set Password Confirmation  wordpass
    Click Button  Register
    Register Should Fail With Message  Username has to be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  timon
    Set Password  pass
    Set Password Confirmation  pass
    Click Button  Register
    Register Should Fail With Message  Password has to be at least 8 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
# ...

Register With Nonmatching Password And Password Confirmation
    Set Username  timo1
    Set Password  timo12345
    Set Password Confirmation  1
    Click Button  Register
    Register Should Fail With Message  User already exists

Register With Username That Is Already In Use
    Set Username  timo
    Set Password  timo12345
    Set Password Confirmation  timo12345
    Click Button  Register
    Register Should Fail With Message  User already exists

*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
