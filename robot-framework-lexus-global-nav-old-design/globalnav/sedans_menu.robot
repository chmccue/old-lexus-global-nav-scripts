*** Settings ***
| Documentation | A global nav model menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${SEDANS} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| IS Model |
| |	Verify Element Is On Page And Click On It | ${IS ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${IS NAME}    | ${IS URL} |

| ES Model |
| |	Verify Element Is On Page And Click On It | ${ES ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${ES NAME}    | ${ES URL} |

| GS Model |
| |	Verify Element Is On Page And Click On It | ${GS ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${GS NAME}    | ${GS URL} |

| LS Model |
| |	Verify Element Is On Page And Click On It | ${LS ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${LS NAME}    | ${LS URL} |
