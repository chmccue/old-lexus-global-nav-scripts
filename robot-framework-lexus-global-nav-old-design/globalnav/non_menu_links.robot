*** Settings ***
| Documentation | A global nav test case for non menu links in the nav. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| Lexus Logo |
| |	Verify Element Is On Page And Click On It | ${LEXUS LOGO ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${LEXUS LOGO NAME}    | ${LEXUS LOGO URL} |

| Build Your Lexus Link |
| | [Tags] | simpletest | 
| |	Verify Element Is On Page And Click On It | ${BYL ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${BYL NAME}    | ${BYL URL} |

| Find A Dealer Link |
| | [Tags] | simpletest | 
| |	Verify Element Is On Page And Click On It | ${FIND A DEALER ELEMENT} | 
| |	Verify Opened Page Matches Element        | ${FIND A DEALER NAME}    | ${FIND A DEALER URL} |
