Feature: Homepage presence

    Scenario: User can see TKB90
        Given open browser
        When open danabijak site
        Then user can see tkb90 info
        And close browser

    Scenario: User can access login page
        Given open browser
        When open danabijak site
        Then user can click login button
        And close browser

    Scenario: User can access register page
        Given open browser
        When open danabijak site
        Then user can click register button
        And close browser