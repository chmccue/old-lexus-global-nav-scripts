*** Settings ***
| Documentation | A global nav model menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${FUTURE} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| LF-C2 Model |
| |	Verify Element Is On Page And Click On It | ${LFC2 ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${LFC2 NAME}    | ${LFC2 URL} | 

| LF-LC Model |
| |	Verify Element Is On Page And Click On It | ${LFLC ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${LFLC NAME}    | ${LFLC URL} |

#| The Next F Section | 
#| |	Verify Element Is On Page And Click On It | ${THE NEXT F ELEMENT} | 
#| |	Verify Opened Page Matches Element        | ${THE NEXT F NAME}    | ${THE NEXT F URL} |