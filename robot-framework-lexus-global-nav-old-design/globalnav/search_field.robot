*** Settings ***
| Documentation | Test cases for checking the Lexus Search Field. | 
| Resource      | resources/resource_variables.txt | 
| Resource      | resources/global_variables.robot | 
| Resource      | resources/resource_keywords.robot | 
| Test Setup    | Setup Commands | 
| Test Teardown | Teardown Commands | 

*** Test Cases ***
| 1 word valid search |
| | Verify Element Is On Page And Click On It | ${SEARCH FIELD ELEMENT} | 
| | Input and Submit Search Words, Verify Opened Search Page | ${1 SEARCH WORD} | 

| multiple word valid search |
| | Verify Element Is On Page And Click On It | ${SEARCH FIELD ELEMENT} | 
| | Input and Submit Search Words, Verify Opened Search Page | ${MULTIPLE WORDS} | 

| 2 word valid search |
| | Verify Element Is On Page And Click On It | ${SEARCH FIELD ELEMENT} | 
| | Input and Submit Search Words, Verify Opened Search Page | ${2 SEARCH WORDS} |  

| text too long valid search |
| | Verify Element Is On Page And Click On It | ${SEARCH FIELD ELEMENT} | 
| | Input and Submit Search Words, Verify Search Contains Part Of Search Words | ${TOO LONG SEARCH} | 

| press search button without search words | 
| | Verify Element Is On Page And Click On It | ${SEARCH FIELD ELEMENT} | 
| | Press Search Button Without Search Words, Verify Nothing Happens | 
