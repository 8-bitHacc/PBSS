from ByteStream.Reader import Reader
from Protocol.Messages.Server.TeamMessage import TeamMessage
from Protocol.Messages.Server.TeamGameStartingMessage import TeamGameStartingMessage

class TeamSetMemberReadyMessage(Reader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player
    
    def decode(self):
        self.room_type = 0
    
    def process(self, db):
        if (self.player.isReady == 0):
            self.player.isReady = 1
        else:
            self.player.isReady = 0
        
        TeamMessage(self.client, self.player, self.room_type).send()
        TeamGameStartingMessage(self.client, self.player).send()
