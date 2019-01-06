# Wildlife Quiz

Wildlife Quiz is a quick and easy online guessing game for one person that requires nothing more than the ability to spell and some knowledge about animals. It was written in Python using the Flask framework. It tests your knowledge in fun and entertaining way, not being too challenging.
 
## UX

When creating this project I was greatly influenced by Clarissa Peterson's [Learning Responsive Web Design](http://shop.oreilly.com/product/0636920029199.do). Some methods (e.g. start with the design for the smallest screen size, use "rem" units, minification) were directly taken from her book. I wanted to make the project mobile-first and responsive. There were several break points used and most of the functionality was set up using the default layout
for devices with a width of max 575 pixels. It was designed with simplicity in mind, meant to be easy to navigate and give user simple information to process. It's a casual entertainment for casual gamers hence its trivial look. I've tried to keep it close to modern trends in apps design. My goal was to create a user-friendly web application and I wanted to make it obvious, how to use available functionalities.

### Users Stories:

To make things easier, I've created User Stories. Here are some examples:
- As a user, I want to able create a game using unique username. 
- As a user, I want to check if I've chosen correct letter.
- As a user, I want to check my score.
- As a user, I want to compare my score with other players.
- As a user, I want help when I'm stuck.

### Wireframes

Examples of wireframes I've used for this project:
- [Early idea](https://github.com/chookmook29/guessing_game/blob/master/wireframes/mockup1.png)
- [Early tablet screen layout](https://github.com/chookmook29/guessing_game/blob/master/wireframes/mockup2.png)
- [More compact mobile first layout](https://github.com/chookmook29/guessing_game/blob/master/wireframes/mockup3.png)
- [Just before project's development started](https://github.com/chookmook29/guessing_game/blob/master/wireframes/mockup4.png)

Some concepts of the design and some features changed over time in the development process.

## Features
 
### Existing Features

- Menu - allows users to check score, rules and quit, by having them click on list of links.
- Main screen - allows users to play game, see remaining attempts left, and all letter used, and most recent letter.
- Set of buttons representing all letters of alphabet - allows users to chose letter, by pressing button of their choice.
- Space below letters and main info - allows users to check hint, by hovering over a hint word.

### Features Left to Implement

- I would like to make onmouseover event in JavaScript that triggers loss of player's remaining "attempts" by one each time, however this would require a lot of additional work. 

## Technologies Used

- HTML and CSS
    - project uses **HTML** and **CSS** to build webpages.
- [Tidy](http://www.html-tidy.org/)
    - Used to fix markup errors.
- [Bootstrap](https://getbootstrap.com/)
    - The project uses some **Bootstrap** elements for more responsive layout.
- [Python](https://www.python.org/)
    - Back-end was written in **Python** .
    - **vnev** library was used in development of the project.
    - **random** module was used with dictionaries.
- [Flask](http://flask.pocoo.org/)
    - The project was built **flask** microframework due to its simplicity.
    - **flask.session** was used to store all variables values. 
- [Jinja2](https://jinja.pocoo.org/)
    - Used for creating templates.
- [unit-test](https://docs.python.org/3/library/unittest.html)
    - Used for automated testing.
- [JSON](https://www.json.org/)
    - **JSON** was used to keep data in separate file.
- [AWS S3](https://aws.amazon.com/s3/)
    - Used to store large static media files.
- [Balsamiq](https://balsamiq.com/)
    - Before development started, **Balsamiq** was used for wireframes.
- [GitHub]((https://www.github.com/)
    - Used for version control and backup.


## Testing

When writing backend code I used unittest before adding new functionalities. I have also manually tested views to see if scenarios from user stories are giving desirable results.
The project has been tested on various browsers, including Firefox, Chrome, Opera, and Safari. 
All tests can be found in test.py file.

###Automated tests for code logic:

- test_correct(self) - testing most important feature of the game, when guess is correct, it creates new hidden word with guess displayed
- test_wrong(self) - tests effects of a wrong guess
- test_search_through(self) - testing checks for letter in a random word
- test_username_length - defensive design testing
- test_dictionary - checks if program picks up correct value of a key
- test_delete_dict_element(self) - testing deletion of a dictionary element
- test_empty_dict(self) - test of important feature preventing NoneType variable creation
    
###Automated tests for deployed version:

- test_index(self) - testing GET request of a index.html template and a response code 
- test_data_post(self) - testing POST request of a index.html template and a response code 
- test_initial_word(self)- testing GET request of game.html
- test_rules(self) - testing if rules.html template is deployed with few variables
- test_final(self) - similar to test_rules(self), different template

### Manual testing during developement:

- testing game view:
    - Submit username and start the actual game, the game page will load. 
    - Verify that score is 0, guess is question mark and there are no letters shown as used, attempts set to 8.
    - Verify that there is a message with current username displayed, above mentioned before.
    - Press button with an incorrect letter, to verify that the page will be reloaded, attempts deducted and word on display won't change.
    - Use all your attempts down to zero, so final score will be displayed and you'll be able to go back to initial page.
    - Try to hover over hint section so image of a corresponding animal will be displayed.
    - Hover over menu in top right corner, every option will redirect you to other subpages.
    - Try to press button with a correct letter. Word should now include letter you just guessed(or multiple letters if they duplicate in given word).
    - Try to press button with a last remaining correct letter. New word should appear and points should be added to the overall score in menu at the top right corner of the page.
    - When all words are guessed, the page should be redirected to the final score view.
- testing score view:
    - It should display user's points or final points if it's final score view


### User testing:

Webpage was also tested by group of users using similar scenarios as mentioned in manual testing. Feedback helped with further development.

### Known issues:

Touchscreens don't support hover effects on game's hint. 

## Deployment

The application is deployed at [Wildlife Quiz](https://test-my-app-ok.herokuapp.com/).

In order to deploy, following changes has been made:
- Set 'debug' value in run.py file to False
- Added requirements.txt and Procfile, as required by heroku
- Set Heroku Config Vars:
    - IP to 0.0.0.0
    - PORT to 5000

To run it locally:
- Install python 3
- Install virtualenv
- Create virtual environment inside directory of this webpage
- Activate virtual environment
    - source venv/bin/activate
- Install flask packages using pip with virtual environment active
- Install flask-sessions packages
- Start the web server with commands:
    - export FLASK_APP=run.py
    - flask run
- Type http://127.0.0.1:5000 address in your browser window


## Credits

### Content

- Images where taken from [Shutterstock.com](https://www.shutterstock.com/)
- Font was taken [FontSquirrel.com](https://www.fontsquirrel.com/)

### Media

- The photos used in this site were obtained from [Shutterstock.com](https://www.shutterstock.com/)

### Acknowledgements

- Big thank you to my mentor [Antonija Šimić](https://github.com/tonkec/)
