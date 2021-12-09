# Version
Compatible with Rasa Open Source version 2.8.15

# Rasa for Beginners wellness-check-bot
This assistant is based on the [Rasa for Beginners wellness-check-bot](https://github.com/RasaHQ/rasa-for-beginners), which is a project for the Rasa for Beginners course from Udemy.

It uses a form to collect a user's daily health information and saves it to a local csv file.

## Running the assistant

1. If you are using the pre-prepared Gitpod workspace image, enter the preset venv environment:

``source venv/bin/activate``

2. Run the action server on a new terminal window:

``rasa run actions``

3. Return to the first terminal window and start the assistant on the command line:

``rasa shell``
