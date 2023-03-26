from ByteStream.Writer import Writer
import random

class BattleResult2Message(Writer):

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
        old_tr = self.player.trophies


        if 0 <= brawler_trophies <= 49:
            win_val = 8
            lose_val = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8
                lose_val = -1

            if 100 <= brawler_trophies <= 199:
                win_val = 8
                lose_val = -2

            if 200 <= brawler_trophies <= 299:
                win_val = 8
                lose_val = -3

            if 300 <= brawler_trophies <= 399:
                win_val = 8
                lose_val = -4

            if 400 <= brawler_trophies <= 499:
                win_val = 8
                lose_val = -5

            if 500 <= brawler_trophies <= 599:
                win_val = 8
                lose_val = -6

            if 600 <= brawler_trophies <= 699:
                win_val = 8
                lose_val = -7

            if 700 <= brawler_trophies <= 799:
                win_val = 8
                lose_val = -8

            if 800 <= brawler_trophies <= 899:
                win_val = 7
                lose_val = -9

            if 900 <= brawler_trophies <= 999:
                win_val = 6
                lose_val = -10

            if 1000 <= brawler_trophies <= 1099:
                win_val = 5
                lose_val = -11

            if 1100 <= brawler_trophies <= 1199:
                win_val = 4
                lose_val = -12

            if brawler_trophies >= 1200:
                win_val = 3
                lose_val = -12

        if self.player.battle_result == 0:
            new_trophies = old_tr + win_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + win_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + win_val
            TrophiesResult = win_val
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)

            self.player.TrophiesAnimation = win_val
        else:
            new_trophies = old_tr + lose_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + lose_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + lose_val
            TrophiesResult = lose_val
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)


        self.writeVInt(0) # Tokens Gained
        self.writeVInt(TrophiesResult) # Trophies Result
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
        self.writeVInt(16) # Battle Result Type ((-16)-(-1) = Power Play Battle End, 0-15 = Practice and Championship Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End, 64-79 = Championship Battle End)
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