*** Settings ***
| Documentation | A global nav model menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${F PERFORMANCE} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| F Sport Performance Link |
| |	Verify Element Is On Page And Click On It | ${F SPORT ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${F SPORT NAME}    | ${F SPORT URL} | 

| LFA Model |
| |	Verify Element Is On Page And Click On It | ${LFA ELEMENT}     | 
| |	Verify Opened Page Matches Element        | ${LFA NAME}        | ${LFA URL} | 

| RCF Model (2nd link) |
| |	Verify Element Is On Page And Click On It | ${RCF-2 ELEMENT}   | 
| |	Verify Opened Page Matches Element        | ${RCF NAME}        | ${RCF URL} | 