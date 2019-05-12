Feature: List Conferences
In order to see all existing conferences,
As a user,
I want to list all the conferences.

Background: There are 2 conferences
  Scenario: List all
    When I list conferences
    Then I'm viewing a list containing
      | name      |
      | West      |
      | East      |
    And The list contains 2 conferences
