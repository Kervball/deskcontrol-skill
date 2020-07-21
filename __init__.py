from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder 
from os.path import dirname, abspath
from .light import set, off

class Deskcontrol(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("colorChangeIntent").require("location").require("color"))
    def handle_turn_on_lights_intent(self, message):
        if message.data["location"].upper() == "FRONT LIGHTS":
            light.set(message.data["location"].upper(), message.data['color'])

        if message.data["location"].upper() == "BACK LIGHTS":
            light.set(message.data["location"].upper(), message.data['color'])

        if message.data["location"].upper() == "BOTH LIGHTS":
            light.set(message.data["location"].upper(), message.data['color'])

        self.speak_dialog('deskcontrol')

    @intent_handler(IntentBuilder("").require('powerOff').require('location'))
    def handle_turn_off_lights_intent(self, message):
        light.off(message.data['location'].upper())
        self.speak_dialog('deskcontrol')

def create_skill():
    return Deskcontrol()

