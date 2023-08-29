Feature :login
  Scenario Outline :successful user login with different data
  Given the user is on the login page
  When load the url
  When enter <Username> and <password>
  And click on login button
  Then login should be successful
    Examples:
      | Username | password |
      |symala   |1234567   |

