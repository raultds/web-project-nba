Feature: Register all_star
  In order to create my all_star
  As a user
  I want to register an all_star

  Background: There are registered users and an all_star by one of them
    Given Exists a user "prova" with password "nba123456789"

  Scenario: Register all_star
    Given I login as user "prova" with password "nba123456789"
    When I register an all_star
      | player1 |
      | Pau Gasol |
    Then I'm viewing the details page for restaurant by "prova"
    And there is 1 all_star