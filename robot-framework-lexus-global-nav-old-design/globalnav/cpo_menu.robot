*** Settings ***
| Documentation | A global nav menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${CPO} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| Vehicle Search Link |
| |	Verify Element Is On Page And Click On It  | ${VEHICLE SEARCH ELEMENT} | 
| |	Verify Opened Page Matches Element         | ${VEHICLE SEARCH NAME}    | ${VEHICLE SEARCH URL} |

| CPO Overview Link |
| |	Verify Element Is On Page And Click On It  | ${CPO OVERVIEW ELEMENT} | 
| |	Verify Opened Page Matches Element         | ${CPO OVERVIEW NAME}    | ${CPO OVERVIEW URL} |

| Vehicle Library Link |
| |	Verify Element Is On Page And Click On It  | ${VEHICLE LIBRARY ELEMENT} | 
| |	Verify Opened Page Matches Element         | ${VEHICLE LIBRARY NAME}    | ${VEHICLE LIBRARY URL} |
