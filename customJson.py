import json
from json import JSONEncoder
from event import Event
from datetime import datetime

class DictionaryEncoder(JSONEncoder):
    def default(self, o):
        if type(o) is Event:
            eventNameandTime = {}
            eventNameandTime["name"] = o.name
            eventNameandTime["time"] = o.time
            return {"Event" : eventNameandTime}
        if type(o) is datetime:
            return str(o)

        return JSONEncoder.default(self, o)