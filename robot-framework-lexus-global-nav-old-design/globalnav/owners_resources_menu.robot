*** Settings ***
| Documentation | A global nav menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${OWNER'S RESOURCES} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| My Lexus Link |
| |	Verify Element Is On Page And Click On It         | ${MY LEXUS ELEMENT} |  
| |	Switch Window, Verify Opened Page Matches Element | ${MY LEXUS NAME}    | ${MY LEXUS URL} |

| Owner Benefits Link |
| |	Verify Element Is On Page And Click On It         | ${OWNER BENEFITS ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${OWNER BENEFITS NAME}    | ${OWNER BENEFITS URL} |

| Pay My Bill Link |
| |	Verify Element Is On Page And Click On It         | ${PAY MY BILL ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${PAY MY BILL NAME}    | ${PAY MY BILL URL} |

| Lexus Enform Link |
| |	Verify Element Is On Page And Click On It         | ${LEXUS ENFORM ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${LEXUS ENFORM NAME}    | ${LEXUS ENFORM URL} |

| Scheduled Maintenance Link |
| |	Verify Element Is On Page And Click On It         | ${SCHEDULED MAINT ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${SCHEDULED MAINT NAME}    | ${SCHEDULED MAINT URL} |

| FAQ Link |
| |	Verify Element Is On Page And Click On It         | ${FAQ ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${FAQ NAME}    | ${FAQ URL} |

| Lexus Magazine Link |
| |	Verify Element Is On Page And Click On It         | ${LEXUS MAGAZINE ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${LEXUS MAGAZINE NAME}    | ${LEXUS MAGAZINE URL} |

| Lexus Navigation Link |
| |	Verify Element Is On Page And Click On It         | ${LEXUS NAVIGATION ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${LEXUS NAVIGATION NAME}    | ${LEXUS NAVIGATION URL} |

| Safety Recalls & Service Campaigns Link |
| |	Verify Element Is On Page And Click On It         | ${RECALLS ELEMENT} | 
| |	Switch Window, Verify Opened Page Matches Element | ${RECALLS NAME}    | ${RECALLS URL} |
