*** Settings ***
| Documentation | A global nav model menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${HYBRIDS} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| CTh Model |
| |	Verify Element Is On Page And Click On It | ${CTH ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${CTH NAME}    | ${CTH URL} | 

| ESh Model |
| |	Verify Element Is On Page And Click On It | ${ESH ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${ESH NAME}    | ${ESH URL} |

| GSh Model |
| |	Verify Element Is On Page And Click On It | ${GSH ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${GSH NAME}    | ${GSH URL} |

| LSh Model |
| |	Verify Element Is On Page And Click On It | ${LSH ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${LSH NAME}    | ${LSH URL} |

| NXh Model |
| |	Verify Element Is On Page And Click On It | ${NXH ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${NXH NAME}    | ${NXH URL} |

| RXh Model |
| |	Verify Element Is On Page And Click On It | ${RXH ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${RXH NAME}    | ${RXH URL} |