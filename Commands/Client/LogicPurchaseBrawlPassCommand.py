from ByteStream.Reader import Reader

class LogicPurchaseBrawlPassCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        print(f'First VInt: {self.readVInt()}')
        self.PurchaseType = self.readVInt()
        print(self.PurchaseType)
        print(f'LogicLong: {self.readLogicLong()}')

    def process(self, db):
        self.player.bp_activated = True
        db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)