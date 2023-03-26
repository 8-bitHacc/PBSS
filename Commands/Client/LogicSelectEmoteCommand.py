from ByteStream.Reader import Reader
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Characters import Characters

class LogicSelectEmoteCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.EmoteID = self.readDataReference()[1]


    def process(self, db):
        self.player.selected_pins = self.EmoteID
        db.update_player_account(self.player.token, 'SelectedPins', self.player.selected_pins)