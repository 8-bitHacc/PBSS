from datetime import datetime
from Logic.Home.LogicEventData import LogicEventData
from Logic.Home.LogicShopData import LogicShopData

class LogicConfData:

    def encode(self):
        self.writeVInt(0) # Timestamp

        LogicEventData.encode(self)

        self.writeIntList([8, 20, 35, 75, 140, 290, 480, 800, 1250])  # Brawler Upgrade Cost
        self.writeIntList([4, 20, 50, 140, 280])  # Shop Coins Price
        self.writeIntList([4, 150, 400, 1200, 2600])  # Shop Coins Amount

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0)  # Release Entry

        self.writeVInt(1)  # IntValueEntry
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000000 + self.player.theme_id) # Theme ID

        self.writeVInt(0)  # Timed Int Value Entry

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
