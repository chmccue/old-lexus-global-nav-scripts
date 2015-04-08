*** Settings ***
| Documentation | A global nav model menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${COUPES} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| ISC Model |
| |	Verify Element Is On Page And Click On It | ${ISC ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${ISC NAME}    | ${ISC URL} | 

| RC Model |
| |	Verify Element Is On Page And Click On It | ${RC ELEMENT}  | 
| |	Verify Opened Page Matches Element        | ${RC NAME}     | ${RC URL} | 

| RCF Model |
| |	Verify Element Is On Page And Click On It | ${RCF ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${RCF NAME}    | ${RCF URL} | 