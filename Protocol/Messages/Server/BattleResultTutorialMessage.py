from ByteStream.Writer import Writer
import random

class BattleResultTutorialMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.db = db

    def encode(self):
        self.writeVInt(1) # Battle End Gamemode
        self.writeVInt(self.player.battle_result) # Result (Victory, Defeat, Draw)

        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        brawler_level = self.player.brawlers_level[str(self.player.home_brawler)] + 1
        brawler_high_trophies = self.player.brawlers_high_trophies[str(self.player.home_brawler)]

        self.player.tutorial += 1
        self.db.update_player_account(self.player.token, 'Tutorial', self.player.tutorial)       

        self.writeVInt(0) # Tokens Gained
        self.writeVInt(0) # Trophies Result
        self.writeVInt(0) # Power Play Points Gained
        self.writeVInt(0) # Doubled Tokens
        self.writeVInt(0) # Double Token Event
        self.writeVInt(0) # Token Doubler Remaining
        self.writeVInt(0) # Robo Rumble/Boss Fight/Super City Rampage Level Passed
        self.writeVInt(0) # Epic Win Power Play Points Gained
        self.writeVInt(0) # Championship Level Passed
        self.writeVInt(0) # Challenge Reward Type (0 = Star Points, 1 = Star Tokens)
        self.writeVInt(0) # Challenge Reward Ammount
        self.writeVInt(0) # Championship Losses Left
        self.writeVInt(0) # Championship Maximun Losses
        self.writeVInt(0) # Coin Shower Event
        self.writeVInt(0) # Underdog Trophies
        self.writeVInt(0) # Battle Result Type ((-16)-(-1) = Power Play Battle End, 0-15 = Practice and Championship Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End, 64-79 = Championship Battle End)
        self.writeVInt(-64) # Championship Challenge Type
        self.writeVInt(0) # Championship Cleared
        
        self.writeVInt(6) # Players
        for x in range(1):
            self.writeByte(1) # Player Team 
            self.writeDataReference(16, self.player.home_brawler) # BrawlerID
            self.writeDataReference(29, self.player.selected_skins[str(self.player.home_brawler)]) # SkinID
            self.writeVInt(brawler_trophies) # Trophies
            self.writeVInt(0) # Power Play Trophies
            self.writeVInt(brawler_level) # PowerLevel
            self.writeBoolean(True) # Player HighID and LowID Array
            if True:
                self.writeLong(self.player.ID)
            self.writeString(self.player.name) # PlayerName
            self.writeVInt(self.player.exp_points)
            self.writeVInt(28000000) # PlayerThumbnail
            self.writeVInt(43000000) # NameColor
            self.writeNullVInt() 

            self.writeByte(0) # Player Team
            self.writeDataReference(16, self.player.bot1) # BrawlerID
            self.writeVInt(0) # SkinID
            self.writeVInt(0) # Trophies
            self.writeVInt(0) # Power Play Trophies
            self.writeVInt(10) # PowerLevel
            self.writeBoolean(False) # Player HighID and LowID Array
            self.writeString(self.player.bot1_n) # PlayerName
            self.writeVInt(0) 
            self.writeVInt(28000000) # PlayerThumbnail
            self.writeVInt(43000000) # NameColor
            self.writeNullVInt() 

            self.writeByte(0) # Player Team
            self.writeDataReference(16, self.player.bot2) # BrawlerID
            self.writeVInt(0) # SkinID
            self.writeVInt(0) # Trophies
            self.writeVInt(0) # Power Play Trophies
            self.writeVInt(10) # PowerLevel
            self.writeBoolean(False) # Player HighID and LowID Array
            self.writeString(self.player.bot2_n) # PlayerName
            self.writeVInt(0) 
            self.writeVInt(28000000) # PlayerThumbnail
            self.writeVInt(43000000) # NameColor
            self.writeNullVInt() 

            self.writeByte(2) # Player Team
            self.writeDataReference(16, self.player.bot3) # BrawlerID
            self.writeVInt(0) # SkinID
            self.writeVInt(0) # Trophies
            self.writeVInt(0) # Power Play Trophies
            self.writeVInt(10) # PowerLevel
            self.writeBoolean(False) # Player HighID and LowID Array
            self.writeString(self.player.bot3_n) # PlayerName
            self.writeVInt(0) 
            self.writeVInt(28000000) # PlayerThumbnail
            self.writeVInt(43000000) # NameColor
            self.writeNullVInt() 

            self.writeByte(2) # Player Team
            self.writeDataReference(16, self.player.bot4) # BrawlerID
            self.writeVInt(0) # SkinID
            self.writeVInt(0) # Trophies
            self.writeVInt(0) # Power Play Trophies
            self.writeVInt(10) # PowerLevel
            self.writeBoolean(False) # Player HighID and LowID Array
            self.writeString(self.player.bot4_n) # PlayerName
            self.writeVInt(0) 
            self.writeVInt(28000000) # PlayerThumbnail
            self.writeVInt(43000000) # NameColor
            self.writeNullVInt() 

            self.writeByte(2) # Player Team
            self.writeDataReference(16, self.player.bot5) # BrawlerID
            self.writeVInt(0) # SkinID
            self.writeVInt(0) # Trophies
            self.writeVInt(0) # Power Play Trophies
            self.writeVInt(10) # PowerLevel
            self.writeBoolean(False) # Player HighID and LowID Array
            self.writeString(self.player.bot5_n) # PlayerName
            self.writeVInt(0) 
            self.writeVInt(28000000) # PlayerThumbnail
            self.writeVInt(43000000) # NameColor
            self.writeNullVInt() 
      
        self.writeVInt(2)  # XpEntry
        for x in range(1):
            self.writeVInt(0) # Normal Experience ID
            self.writeVInt(0) # Normal Experience Gained
            self.writeVInt(8) # Star Player Experience ID
            self.writeVInt(0) # Star Player Experience Gained

        self.writeVInt(0) # Rank Up and Level Up Bonus Array

        self.writeVInt(2)  # LogicMilestoneProgress
        for x in range(1):
            self.writeVInt(1) # Trophy Bar ID
            self.writeVInt(brawler_trophies) # Brawler Trophies
            self.writeVInt(brawler_high_trophies) # Brawler Trophies for Rank
            self.writeVInt(5) # Experience ID
            self.writeVInt(self.player.exp_points) # Player XP
            self.writeVInt(self.player.exp_points) # Player XP for new Level
        
        self.writeDataReference(28, 0)
        self.writeBool(False)  # PlayAgainStatus

        self.writeBool(False)  # LogicQuests