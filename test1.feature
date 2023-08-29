Feature: search
  Scenario Outline: textbox is present in search box
    Given :open the browser
    When :load url
    Then :verify textbox is present
    And :search for <item>
    And :close the browser
    Examples:
      | item  |
       |cars  |

