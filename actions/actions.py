# # # This files contains your custom actions which can be used to run
# # # custom Python code.
# # #
# # # See this guide on how to implement these action:
# # # https://rasa.com/docs/rasa/custom-actions

# from custom_connector import get_custom_webhook_app

# # Initialize the custom webhook app
# custom_app = get_custom_webhook_app()

# # ... other action definitions or imports

# # Start the Rasa action server with the custom webhook app
# if __name__ == "__main__":
#     custom_app.run(host="0.0.0.0", port=5055)  # Customize the host and port



# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# 
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class FallbackAction(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Your fallback logic here
#         dispatcher.utter_message("I'm sorry, I didn't understand that.")
#         return []
