# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sqlite3
# from rasa_core_sdk import Action
# from rasa_core_sdk.events import SlotSet
#from database_connection import DataUpdate


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_fallback")

        return []





class ActionFormSubmit(Action):
    
    def name(self) -> Text:
        return "action_form_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
                   
        
        sqliteConnection = sqlite3.connect('ucmas.db')
        cursor = sqliteConnection.cursor()

        name= tracker.get_slot("PERSON")
        age=tracker.get_slot("DATE")
        contact=tracker.get_slot("CARDINAL")
            
            
        cursor.execute('CREATE TABLE IF NOT EXISTS customer_contact(name Char(30), age int(5), contact int(15));')

        sqlite_insert_Query ='insert into customer_contact(name,age,contact) values("{0}","{1}","{2}");'.format(name,age,contact)
        cursor.execute(sqlite_insert_Query)
        
        cursor.close()
        sqliteConnection.commit()

        # except sqlite3.Error as error:
        #     print("Error while connecting to sqlite", error)
        # finally:
        #     if sqliteConnection:
        #         sqliteConnection.close()
    
        dispatcher.utter_message(text="Child name is " + str(tracker.get_slot("PERSON")) + ", age is " + tracker.get_slot("DATE") +" and contact no is " + tracker.get_slot("CARDINAL") + ".\n U can go ahead with admission by filling the form and paying the fees at our office")
        
        
        return []

class Actionagechecking(Action):

    def name(self) -> Text:
        return "action_age_checking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            
            
            age1= next(tracker.get_latest_entity_values("DATE"),None)

            # checking the age of a child

            if int(age1) >= 5 and int(age1) <= 13 :
                dispatcher.utter_message(text="Age of the Child is appropriate of the admission. you can go ahead with admission if interested")
            else:
                dispatcher.utter_message(text="Sorry, your child cannot go ahead with admission as the age limit is between 4 to 13 years")

      

            return []



# class ActionContactForm(Action):
#     def name(self) -> Text:
#         return "contact_form"

    #this method will initiate the form 
    # conversation message from domain file...
    # sequence is important..In stories active_loop: contact_form
    #will inititate this below method
    
    # @staticmethod
    # def required_slots(tracker: Tracker) -> List[Text]:
    #      return["name","age","contact_no"]

    
    #this method will be call when in stories
    # active_loop: null is called
    
    # def submit(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    #         dispatcher.utter_message(template="utter_submit",
    #                                  name=tracker.getslot('name'),
    #                                  age=tracker.getslot('age'),
    #                                  contact_no=tracker.getslot('contact_no')
    #                                  )                                  
    #         return()

    
    # Slot and Entity Mapping with Intent
    
    # def slot_mappings(self) -> Dict[Text, Union[Dict,List[Dict]]]:
    #     return {"name": self.from_entity(entity="name",intent="child_name"),
    #             "age" : self.from_entity(entity="age", intent="child_age"),
    #             "contact_no": self.from_entity(entity="contact_no",intent="contact_number")
    #             }
