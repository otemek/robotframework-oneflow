*** Settings ***
Documentation       Sample suite to skip all tests after parent setup fail

Library             OneFlow

Suite Setup         Fail    parent setup failing ++++


*** Test Cases ***
Should Be Skipped First
    Pass Execution    Should be skipped because parent setup failed

Should Be Skipped Second
    No Operation

Should Be Skipped Third
    Fail    Should be skipped becasue parent setup is failed
