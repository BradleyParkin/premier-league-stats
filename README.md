# Premier Leauge Data Automation

Premier Leauge Data Automation is a Python automation application that runs in the Code Institute most terminal on Heroku.

Users can enter their own set of data, which is how many games a team has won and lost. This will automatically add up the total games played, and will also then show the user the win and loss percentage for each team.

[Here is the live version of my project](https://premier-leauge-data-automation.herokuapp.com/)

![Responesive Image](/images/python-responsive.png)

# How to use and features

The user will enter the data of games lost for the 5 teams shown on the terminal, Arsenal, Man City, Newcastle, Tottenham Hotspur and Man United in that order. 

![games lost](/images/games-lost.png)

The user will enter the data of games won for the 5 teams shown on the terminal, Arsenal, Man City, Newcastle, Tottenham Hotspur and Man United in that order.

![games won](/images/games-won.png)

Once the user has entered both data sets, the terminal will print out the win and loss percentage of the games data the user has just entered. It will also update the google docs spreadsheet. You can find that here [Premier Leauge Data Automation](https://docs.google.com/spreadsheets/d/1NixGI6ijamkOwq2-ysSxNphr1lbLTwgt0pzWUn69NHk/edit?usp=sharing)

![games updated](/images/games-updated.png)

# Testing

I have manually tested the project by doing the follow:

* I have passed the code through the [CI Python Linter](https://pep8ci.herokuapp.com/#) and can confirm there are no issues.
* Given invalid inputs, strings when numbers are expected and if a number less than 0 is entered into the field it will throw an error.
* Tested in my local terminal and the Code Institute Heroku terminal.

# Bugs

Solved Bugs

* When i wrote the project, when i was entering numbers i was getting the str and int error, this was becuase i had not added the (int).

Validator Testing

* PEPB
    * No errors were were returned from testing for PEPB8(Code Institute's own)

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

* How is it deployed
    * You can clone this repositry
    * Create a new Heroku app
    * Set the build backs to Python and NodeJS in that order
    * Link the Heroku app to the repositry
    * Click Deploy

# Credits

* Code Institute for the deployment terminal.
* Used the Love Sandwiches project to base my code and functinality from that. 
* Tutor/Online Tutor for help on validating inputs

