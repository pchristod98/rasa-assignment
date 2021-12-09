from typing import Any, Text, Dict, List, Union, Optional
from dotenv import load_dotenv

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

import csv
import os

load_dotenv()

airtable_api_key=os.getenv("AIRTABLE_API_KEY")
base_id=os.getenv("BASE_ID")
table_name=os.getenv("TABLE_NAME")

def create_health_log(confirm_exercise, exercise, sleep, diet, stress, goal):
    header = ['confirm_exercise', 'exercise', 'sleep', 'diet', 'stress', 'goal']
    data = [confirm_exercise, exercise, sleep, diet, stress, goal]

    with open('user_response.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerow(data)

class ValidateHealthForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_health_form"

    async def validate_confirm_exercise(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value:
            return {"confirm_exercise": True}
        else:
            return {"exercise": "None", "confirm_exercise": False }

class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        confirm_exercise = tracker.get_slot("confirm_exercise")
        exercise = tracker.get_slot("exercise")
        sleep = tracker.get_slot("sleep")
        stress = tracker.get_slot("stress")
        diet = tracker.get_slot("diet")
        goal = tracker.get_slot("goal")

        response = create_health_log(
                confirm_exercise=confirm_exercise,
                exercise=exercise,
                sleep=sleep,
                stress=stress,
                diet=diet,
                goal=goal
            )

        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return []

