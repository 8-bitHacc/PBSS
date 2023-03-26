from ByteStream.Writer import Writer

class BattleResultMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.db = db

    def encode(self):
        self.writeVInt(2) # Battle End Gamemode
        self.writeVInt(self.player.rank) # Rank

        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        brawler_level = self.player.brawlers_level[str(self.player.home_brawler)] + 1
        brawler_high_trophies = self.player.brawlers_high_trophies[str(self.player.home_brawler)]
        old_tr = self.player.trophies


        if 0 <= brawler_trophies <= 49:
            rank_1_val = 10
            rank_2_val = 8
            rank_3_val = 7
            rank_4_val = 6
            rank_5_val = 4
            rank_6_val = 2
            rank_7_val = 2
            rank_8_val = 1
            rank_9_val = 0
            rank_10_val = 0
        else:
            if 50 <= brawler_trophies <= 99:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 2
                rank_7_val = 2
                rank_8_val = 0
                rank_9_val = -1
                rank_10_val = -2

            if 100 <= brawler_trophies <= 199:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -1
                rank_9_val = -2
                rank_10_val = -2

            if 200 <= brawler_trophies <= 299:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 3
                rank_6_val = 1
                rank_7_val = 0
                rank_8_val = -2
                rank_9_val = -3
                rank_10_val = -3

            if 300 <= brawler_trophies <= 399:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = 0
                rank_7_val = 0
                rank_8_val = -3
                rank_9_val = -4
                rank_10_val = -4

            if 400 <= brawler_trophies <= 499:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 5
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -3
                rank_9_val = -5
                rank_10_val = -5

            if 500 <= brawler_trophies <= 599:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 2
                rank_6_val = -1
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -6
                rank_10_val = -6

            if 600 <= brawler_trophies <= 699:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -2
                rank_7_val = -2
                rank_8_val = -5
                rank_9_val = -7
                rank_10_val = -8

            if 700 <= brawler_trophies <= 799:
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 6
                rank_4_val = 4
                rank_5_val = 1
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -5
                rank_9_val = -8
                rank_10_val = -9

            if 800 <= brawler_trophies <= 899:
                rank_1_val = 9
                rank_2_val = 7
                rank_3_val = 5
                rank_4_val = 2
                rank_5_val = 0
                rank_6_val = -3
                rank_7_val = -4
                rank_8_val = -7
                rank_9_val = -9
                rank_10_val = -10

            if 900 <= brawler_trophies <= 999:
                rank_1_val = 8
                rank_2_val = 6
                rank_3_val = 4
                rank_4_val = 1
                rank_5_val = -1
                rank_6_val = -3
                rank_7_val = -6
                rank_8_val = -8
                rank_9_val = -10
                rank_10_val = -11

            if 1000 <= brawler_trophies <= 1099:
                rank_1_val = 6
                rank_2_val = 5
                rank_3_val = 3
                rank_4_val = 1
                rank_5_val = -2
                rank_6_val = -5
                rank_7_val = -6
                rank_8_val = -9
                rank_9_val = -11
                rank_10_val = -12

            if 1100 <= brawler_trophies <= 1199:
                rank_1_val = 5
                rank_2_val = 4
                rank_3_val = 1
                rank_4_val = 0
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -7
                rank_8_val = -10
                rank_9_val = -12
                rank_10_val = -13

            if brawler_trophies >= 1200:
                rank_1_val = 5
                rank_2_val = 3
                rank_3_val = 0
                rank_4_val = -1
                rank_5_val = -2
                rank_6_val = -6
                rank_7_val = -8
                rank_8_val = -11
                rank_9_val = -12
                rank_10_val = -13


        if self.player.rank == 1:
            new_trophies = old_tr + rank_1_val
            TrophiesResult = rank_1_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_1_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_1_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 2:
            new_trophies = old_tr + rank_2_val
            TrophiesResult = rank_2_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_2_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_2_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 3:
            new_trophies = old_tr + rank_3_val
            TrophiesResult = rank_3_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_3_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_3_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 4:
            new_trophies = old_tr + rank_4_val
            TrophiesResult = rank_4_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_4_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_4_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 5:
            new_trophies = old_tr + rank_5_val
            TrophiesResult = rank_5_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_5_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_5_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 6:
            new_trophies = old_tr + rank_6_val
            TrophiesResult = rank_6_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_6_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_6_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 7:
            new_trophies = old_tr + rank_7_val
            TrophiesResult = rank_7_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_7_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_7_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 8:
            new_trophies = old_tr + rank_8_val
            TrophiesResult = rank_8_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_8_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_8_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 9:
            new_trophies = old_tr + rank_9_val
            TrophiesResult = rank_9_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_9_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_9_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

        elif self.player.rank == 10:
            new_trophies = old_tr + rank_10_val
            TrophiesResult = rank_10_val
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_10_val
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_high_trophies + rank_10_val
            self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
            self.db.update_player_account(self.player.token, "BrawlersTrophies", self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

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
        
        self.writeVInt(1) # Players
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