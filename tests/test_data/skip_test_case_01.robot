*** Settings ***
Documentation       Sample test suite for OneFlow library

Library             OneFlow


*** Test Cases ***
First Should Pass
    No Operation

This Should Fail
    Fail    Becasue I said so

This Should Be Skipped
    Pass Execution    Should be skipped

This Should Also Be Skipped
    Pass Execution    Also should be skipped
