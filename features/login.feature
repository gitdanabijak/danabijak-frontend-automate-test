Feature: Login Page

    Scenario: User can login
        Given open browser
        When open danabijak login site
        Then user input email
        And user input password
        And user click login