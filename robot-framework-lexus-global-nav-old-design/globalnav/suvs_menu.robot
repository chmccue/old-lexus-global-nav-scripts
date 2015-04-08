*** Settings ***
| Documentation | A global nav model menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${SUVS} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| GX Model |
| |	Verify Element Is On Page And Click On It | ${GX ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${GX NAME}    | ${GX URL} | 

| LX Model |
| |	Verify Element Is On Page And Click On It | ${LX ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${LX NAME}    | ${LX URL} |

| NX Model |
| |	Verify Element Is On Page And Click On It | ${NX ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${NX NAME}    | ${NX URL} | 

| RX Model |
| |	Verify Element Is On Page And Click On It | ${RX ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${RX NAME}    | ${RX URL} | 