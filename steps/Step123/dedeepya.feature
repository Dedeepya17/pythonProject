Feature: User login
  Scenario Outline: Successful User login with different data
    Given The user is on the login page
    When They enter  "<First Name>" and  "<email>"
    When  enter "<Last Name>"
    And Confirm the password "<confirmpwd>"
    And Click the "checkbox1","checkbox2"
    Then click the login button
    Then registration succefull,close the browser
    Examples:
      | First Name | email | Last Name | password | confirmpwd |
      |shymala    |symala17@gmail.com| Russum|    1234567 | 1234567|



























