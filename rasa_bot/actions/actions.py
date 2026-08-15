# rasa_bot/actions/actions.py
#
# Custom action server for the Visit Nepal chatbot.
# Rasa will call these actions when a user triggers a flow
# that requires server-side logic (e.g., looking up live data).
#
# To add a custom action:
#   1. Subclass rasa_sdk.Action
#   2. Implement name() and run()
#   3. Register it in domain.yml under `actions:`
#   4. Start the action server: rasa run actions
#
# Example:
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
# class ActionGetHotelPrices(Action):
#     def name(self) -> Text:
#         return "action_get_hotel_prices"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Rooms start from NPR 4,000 per night.")
#         return []
