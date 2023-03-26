from ByteStream.Reader import Reader

class AnalyticEventMessage (Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Type = self.readString()
        self.Event = self.readString()

    def process(self, db):
        print("" + self.Type + " " + self.Event)
        if self.Event == '{"step":"click_to_end","step_id":"18"}':
            self.player.tutorial += 1
            db.update_player_account(self.player.token, 'Tutorial', self.player.tutorial)