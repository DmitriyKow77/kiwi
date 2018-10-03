# Created by dmitriy at 10/3/18
Feature: Bitly qa task

  Scenario Outline: Shorten link by bit ly and check it opens initial link
    Given I am at bitly home page
    When I shorten url "<url>"
    And I check url is shorten
    Then I go to shorten url
    And I check opens initial url

  Examples: sample urls
    |url|
    |https://www.petmd.com/sites/default/files/petmd-kitten-facts.jpg |
    |https://behave.readthedocs.io/en/latest/                         |

