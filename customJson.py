import json
from json import JSONEncoder, JSONDecoder
from event import Event
from datetime import datetime

class DictionaryEncoder(JSONEncoder):
    def default(self, o):
        if type(o) is Event:
            if not o.googleCalendar:
                eventNameandTime = {}
                eventNameandTime["name"] = o.name
                eventNameandTime["time"] = o.time
                return {"Event": eventNameandTime}
            return None


        return JSONEncoder.default(self, o)



class DictionaryDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):

        JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)
    def object_hook(self, dct):
        #check if contains Event keyword
        if "Event" in dct:
            return Event(dct["Event"]["name"], dct["Event"]["time"], None, None, googleCalendar=False)
        else:
            return dct
