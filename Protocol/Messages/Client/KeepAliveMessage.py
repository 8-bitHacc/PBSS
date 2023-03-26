from ByteStream.Reader import Reader
from Protocol.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage
from Protocol.Messages.Server.LobbyInfoMessage import LobbyInfoMessage
from Utils.Helpers import Helpers

class KeepAliveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self, db):
        KeepAliveOkMessage(self.client, self.player).send()
        LobbyInfoMessage(self.client, self.player, Helpers.connected_clients['ClientsCount']).send()
