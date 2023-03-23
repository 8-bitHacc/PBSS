from Logic.Home.LogicDailyData import LogicDailyData
from Logic.Home.LogicConfData import LogicConfData

class LogicClientHome:

    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(self.player.ID)  # PlayerID

        self.writeVInt(0) # Notification Factory
        for x in range(0):
            pass

        self.writeVInt(-64)  # VideoAdStarted
        self.writeBoolean(False)
        self.writeVInt(0)  # GatchaDrop
        self.writeVInt(0)  # FriendlyStarPower
