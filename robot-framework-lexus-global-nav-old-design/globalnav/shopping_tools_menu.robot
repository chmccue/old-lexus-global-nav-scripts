*** Settings ***
| Documentation | A global nav menu section test case. |
| Resource      | resources/resource_keywords.robot |
| Resource      | resources/resource_variables.txt |
| Resource      | resources/global_variables.robot | 
| Test Setup    | Setup Commands, Click On Menu Dropdown | ${SHOPPING TOOLS} | 
| Test Teardown | Teardown Commands |

*** Test Cases ***
| Financial Services Link |
| |	Verify Element Is On Page And Click On It         | ${FINANCIAL SERVICES ELEMENT} | 
| | Switch Window, Verify Opened Page Matches Element | ${FINANCIAL SERVICES NAME}   | ${FINANCIAL SERVICES URL} |

| Accessories Link | 
| | Verify Element Is On Page And Click On It         | ${ACCESSORIES ELEMENT} | 
| | Verify Opened Page Matches Element                | ${ACCESSORIES NAME}    | ${ACCESSORIES URL} | 

| Special Offers Link |
| |	Verify Element Is On Page And Click On It         | ${SPECIAL OFFERS ELEMENT} | 
| | Switch Window, Verify Opened Page Matches Element | ${SPECIAL OFFERS NAME}    | ${SPECIAL OFFERS URL} |

| Sign Up Link |
| | [Tags] | High | 
| |	Verify Element Is On Page And Click On It         | ${SIGN UP ELEMENT} | 
| | Switch alt Window                                 | ${SIGN UP URL}     |
| |	Verify Sign Up Page | 

*** Keywords ***
| Verify Sign Up Page | 
| | Wait Until Element Is Visible | css=header.lead-form-header[style='background-image'] | 
| | Wait Until Element Is Visible | css=input#firstName | 
| | Wait Until Element Is Visible | css=input#lastName | 

