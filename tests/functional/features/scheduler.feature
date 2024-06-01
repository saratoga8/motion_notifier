Feature: Scheduling actions
  It gives the ability to user to plan some actions for the running agent
  E.g. to run detections every day from 9 AM till 6 PM

  Scenario: Scheduling recurrent actions
    When user schedules a recurrent action
    Then the scheduled action happened recurrently

  Scenario: Ability of one time action(E.g. to stop detections in one hour)
    When user schedules an one time action
    Then the scheduled action happened one time only

  Scenario: Getting info about currently running scheduling
    When user schedules a recurrent action
    And user schedules an one time action
    And user asks for running scheduling
    Then user gets the running scheduling

  Scenario: Stopping currently running scheduler
    When user schedules a recurrent action
    And user stops the scheduler
    Then the scheduler doesn't run

