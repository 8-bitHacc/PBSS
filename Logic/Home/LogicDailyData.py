from datetime import datetime
from Logic.Home.LogicShopData import LogicShopData
from Logic.Home.ForcedDrops import ForcedDrops

class LogicDailyData:

    def encode(self):

        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        self.writeVInt(time_stamp)

        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.high_trophies)
        self.writeVInt(self.player.high_trophies)

        self.writeVInt(95)
        self.writeVInt(self.player.exp_points)
        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        # Array
        self.writeVInt(0)

        # Selected Skins
        self.writeVInt(len(self.player.selected_skins))
        for x in self.player.selected_skins:
            self.writeDataReference(29, self.player.selected_skins[x])

        # Skin Selected For Random Skin
        self.writeVInt(0)
        for x in range(0):
            self.writeDataReference(29, 0)

        # Current Random Skin
        self.writeVInt(0)
        for i in range(0):
            self.writeDataReference(29, 0)  # SkinID

        # Selected Group Skin
        self.writeVInt(1)  # Skin Count
        for i in range(1):
            self.writeVInt(1)  # Group Index
            self.writeDataReference(29, 18)  # SkinID

        # Unlocked Skin
        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)

        # Unlocked Skin Purchase Option
        self.writeVInt(1)
        for i in range(1):
            self.writeDataReference(29, 357)  # SkinID

        # New Item
        self.writeVInt(0)
        for i in range(0):
            self.writeDataReference(23, 0)  # ItemID

        self.writeVInt(0)  # Leaderboard Region | 0 = Global, 1 = Asia
        self.writeVInt(self.player.high_trophies)  # Trophy Road Highest Trophies
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(self.player.token_doubler)  # Tokens Doubler
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        ForcedDrops.encode(self)

        self.writeByte(4)  # Shop Token Doubler
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(0)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change

        LogicShopData.encodeShopOffers(self)

        self.writeVInt(0)  # AdStatus

        self.writeVInt(200)  # Available tokens from battles
        self.writeVInt(-64)  # Timer for new tokens

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(16, self.player.home_brawler)
        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)

        self.writeVInt(1) # Home Events Array
        for x in range(1):
            self.writeInt(4) # ID
            self.writeInt(self.player.TrophiesAnimation)

        self.writeVInt(0) # CoolDownEntry

        self.writeVInt(1)  # BrawlPassSeasonData
        for i in range(1):
            self.writeVInt(8) # Current Season
            self.writeVInt(0) # Pass Tokens
            self.writeBoolean(self.player.bp_activated)
            self.writeVInt(0) # Pass Progress

            self.writeByte(2)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(511)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVInt(0) # ProLeagueSeasonData

        self.writeBoolean(True) # LogicQuests
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(1 + 1)  # Vanity Count
        for i in range(1):
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in range(1):
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)


        self.writeBoolean(False)

        self.writeInt(0)




