Feature: five finger
#  Scenario Outline: to check admin page
#    Given open chrome browser
#    When enter url
#    And enter username "<username>" and password "<password>"
#    And click on login button
#    Then Login page should be displayed
#    Examples: Credential
#      | username   | password |
#      | kirtihinge | prutha20 |
#      | kirtihige  | prutha8  |

#  Scenario: to check admin page
#    Given open chrome browser
#    When enter url
#    And enter username and password
#    And click on login button
#    Then Login page should be displayed

   Scenario Outline: to check admin page
    Given open chrome browser
    When enter url
    And enter username and password with "<roll>"
    And click on login button state"<status>"
    Then home page should be displayed
    Examples: Credential
      | roll     | status |
      | Manager  | E6     |
      | Manager1 | E7     |