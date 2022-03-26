*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kukko  kukko123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kustaa  kustaa1234
    Output Should Contain  User with username kustaa already exists

Register With Too Short Username And Valid Password
    Input Credentials  ku  kusti12345
    Output Should Contain  Username or password too short

Register With Valid Username And Too Short Password
    Input Credentials  kusti  kust123
    Output Should Contain  Username or password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kusti  kustikusti
    Output Should Contain  Invalid password

*** Keywords ***
Create User And Input New Command
    Create User  kustaa  kustaa1234
    Input New Command