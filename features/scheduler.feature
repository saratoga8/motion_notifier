Feature: Scheduling motions detection
  It gives the ability to user to plan some actions for the running agent
  E.g. to run detections every day from 9 AM till 6 PM

  Scenario Outline: <action>ing the motion detections at scheduled time
    When user schedules detections <action>
    Then scheduled detections <action>ed at time

    Examples:
      | action |
      | start  |
      | stop   |

  Scenario: Ability of one time action(E.g. to stop detections in one hour)
    When user schedules to stop detections one time
    Then detections stopped at the scheduled time

  Scenario: Getting info about currently running scheduling
    When user schedules detections start
    And user schedules to stop detections one time
    And user asks for running scheduling
    Then user gets the running scheduling

