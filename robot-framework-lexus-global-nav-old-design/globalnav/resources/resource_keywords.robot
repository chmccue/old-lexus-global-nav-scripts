*** Settings ***
| Library | Selenium2Library |
| Library |	BuiltIn          |

*** Keywords ***

# Setup and Teardown Commands************
| Setup Commands | 
| | Set Selenium Speed | ${TEST SPEED} |
| | Open Browser | ${BASE URL} | ${BROWSER} |
| | Maximize Browser Window |

| Setup Commands, Click On Menu Dropdown | [Arguments] | ${MENU ELEMENT} | 
| | Set Selenium Speed | ${TEST SPEED} |
| | Open Browser | ${BASE URL} | ${BROWSER} |
| | Maximize Browser Window |
| | Verify Element Is On Page And Click On It | ${MENU ELEMENT} | 

| Teardown Commands |
| | Close Browser |

# ***************************************

| Switch alt Window | [Arguments] | ${MENU URL} |
| | Sleep           | 5 |
| | Select Window   | url=${MENU URL} |

| Assert Link Title | [Arguments] | ${MENU NAME} |
| |	${Current page} | Get Title |
| |	Should Contain | ${Current page} | ${MENU NAME} |

# ***************************************

| Verify Element Is On Page And Click On It | [Arguments] | ${MENU ELEMENT} |
| |	Wait Until Element Is Visible                         | ${MENU ELEMENT} |
| | Click Element                                         | ${MENU ELEMENT} |

| Verify Opened Page Matches Element | [Arguments] | ${MENU NAME} | ${MENU URL} | 
| | Assert Link Title       | ${MENU NAME} | 
| | Location Should Contain | ${MENU URL}  | 

| Switch Window, Verify Opened Page Matches Element | [Arguments] | ${MENU NAME} | ${MENU URL} | 
| | Sleep                   | ${WAIT TIME}       | 
| | Select Window           | title=${MENU NAME} | 
| | Assert Link Title       | ${MENU NAME}       | 
| | Location Should Contain | ${MENU URL}        | 

# Search page/results keywords***********

| Input and Submit Search Words, Verify Opened Search Page | [Arguments] | ${Search word} | 
| | Input Text | id=nav_search_field | ${Search word} | 
| | Click Button | css=input.inputActivate[type=submit] | 
| | Wait Until Element Is Visible | css=img[title='Search results title'] | 
| | ${Linked page search word} | Get Value | id=qt | 
| | Should Be Equal | ${Linked page search word} | ${Search word} | 

| Input and Submit Search Words, Verify Search Contains Part Of Search Words | [Arguments] | ${Search word} | 
| | Input Text | id=nav_search_field | ${Search word} | 
| | Click Button | css=input.inputActivate[type=submit] | 
| | Wait Until Element Is Visible | css=img[title='Search results title'] | 
| | ${Linked page search word} | Get Value | id=qt | 
| | Should Contain | ${Search word} | ${Linked page search word} | 

| Press Search Button Without Search Words, Verify Nothing Happens | 
| | Click Button | css=input.inputActivate[type=submit] | 
| | Sleep | ${WAIT TIME} | 
| | Page Should Not Contain Element | css=img[title='Search results title'] | 