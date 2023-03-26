import json

class LogicEventData:
    events = json.loads(open("events.json", 'r').read())

    def encode(self):
        eventdata = json.loads(open("events.json", 'r').read())
        events = eventdata['ActiveEvents']
        comingevents = eventdata['ComingUpEvents']

        self.writeVInt(16) # Event Slots Count
        for x in range(16):
            self.writeVInt(x)

        self.writeVInt(len(events))

        for event in events:
            self.writeVInt(0)
            self.writeVInt(event['EventIndex'])
            self.writeVInt(event['Ended'])
            self.writeVInt(event['Timer'])

            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])

            self.writeVInt(event['Status'])

            self.writeString(event['TextEntry'])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)


        self.writeVInt(len(comingevents)) # Coming Up Events

        for event in comingevents:
            self.writeVInt(0)
            self.writeVInt(event['EventIndex'])
            self.writeVInt(event['Ended'])
            self.writeVInt(event['Timer'])

            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])

            self.writeVInt(event['Status'])

            self.writeString(event['TextEntry'])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)