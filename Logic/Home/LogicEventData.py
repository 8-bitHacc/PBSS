import json

class LogicEventData:
    events = json.loads(open("events.json", 'r').read())

    def encode(self):
        events = json.loads(open("events.json", 'r').read())

        # Event Slots IDs Array
        self.writeVInt(len(events))  # Count
        for x in range(len(events)):
            self.writeVInt(x)
        # Event Slots IDs Array End

        self.writeVInt(len(events))  # Events Count
        for event in events:
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(events.index(event) + 1)  # EventType
            self.writeVInt(event['Ended'])  # EventsBeginCountdown
            self.writeVInt(event['Timer'])  # Timer

            self.writeVInt(0)  # Tokens from New Event
            self.writeDataReference(15, event['ID'])  # MapID

            self.writeVInt(-64)  # GameModeVariation
            self.writeVInt(event['Status'])  # State

            self.writeString()
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
            self.writeBoolean(False)  # Map Maker Map Structure Array
            self.writeVInt(0)
            self.writeBoolean(False)  # Power League Data Array
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)  # ChronosTextEntry
            self.writeVInt(-64)
            self.writeBoolean(False)

        self.writeVInt(0)  # Coming Up Events Count
        for x in range(0):
            pass
