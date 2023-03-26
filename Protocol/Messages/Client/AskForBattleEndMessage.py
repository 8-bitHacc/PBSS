from Protocol.Messages.Server.BattleResultMessage import BattleResultMessage
from Protocol.Messages.Server.BattleResult2Message import BattleResult2Message
from Protocol.Messages.Server.BattleResultTutorialMessage import BattleResultTutorialMessage
from ByteStream.Reader import Reader
#from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.battle_result = self.readVInt()
        self.readVInt()
        self.player.rank = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()

        self.player.team = self.readVInt() #red or blue

        self.readVInt()

        self.readString() #Your Name

        self.readVInt()
        self.Bot1 = self.readVInt() #bot brawler
        self.readVInt()
        self.readVInt() #red or blue
        self.readVInt()

        self.Bot1N = self.readString()

        self.readVInt()
        self.Bot2 = self.readVInt() #bot brawler
        self.readVInt()
        self.readVInt() #red or blue
        self.readVInt()

        self.Bot2N = self.readString()

        self.readVInt()
        self.Bot3 = self.readVInt() #bot brawler
        self.readVInt()
        self.readVInt() #red or blue
        self.readVInt()

        self.Bot3N = self.readString()

        self.readVInt()
        self.Bot4 = self.readVInt() #bot brawler
        self.readVInt()
        self.readVInt() #red or blue
        self.readVInt()

        self.Bot4N = self.readString()

        self.readVInt()
        self.Bot5 = self.readVInt() #bot brawler
        self.readVInt()
        self.readVInt() #red or blue
        self.readVInt()

        self.Bot5N = self.readString()

    def process(self, db):
        if self.player.rank != 0 and not self.player.map_id == 124:
            BattleResultMessage(self.client, self.player, db).send()
        else:
            if self.player.tutorial == 1:
                if self.player.team == 0 or self.player.team == 1:
                    self.player.bot1_n = self.Bot1N
                    self.player.bot2_n = self.Bot2N
                    self.player.bot3_n = self.Bot3N
                    self.player.bot4_n = self.Bot4N
                    self.player.bot5_n = self.Bot5N
                    self.player.bot1 = self.Bot1
                    self.player.bot2 = self.Bot2
                    self.player.bot3 = self.Bot3
                    self.player.bot4 = self.Bot4
                    self.player.bot5 = self.Bot5
                    BattleResultTutorialMessage(self.client, self.player, db).send()
                else:
                    self.player.bot1_n = self.Bot1N
                    self.player.bot2_n = self.Bot2N
                    self.player.bot3_n = self.Bot3N
                    self.player.bot4_n = self.Bot4N
                    self.player.bot5_n = self.Bot5N
                    self.player.bot1 = self.Bot1
                    self.player.bot2 = self.Bot2
                    self.player.bot3 = self.Bot3
                    self.player.bot4 = self.Bot4
                    self.player.bot5 = self.Bot5
                    BattleResultTutorialMessage(self.client, self.player, db).send()
            else:

                if self.player.team == 0 or self.player.team == 1:
                   self.player.bot1_n = self.Bot1N
                   self.player.bot2_n = self.Bot2N
                   self.player.bot3_n = self.Bot3N
                   self.player.bot4_n = self.Bot4N
                   self.player.bot5_n = self.Bot5N
                   self.player.bot1 = self.Bot1
                   self.player.bot2 = self.Bot2
                   self.player.bot3 = self.Bot3
                   self.player.bot4 = self.Bot4
                   self.player.bot5 = self.Bot5
                   BattleResult2Message(self.client, self.player, db).send()
                else:
                    self.player.bot1_n = self.Bot1N
                    self.player.bot2_n = self.Bot2N
                    self.player.bot3_n = self.Bot3N
                    self.player.bot4_n = self.Bot4N
                    self.player.bot5_n = self.Bot5N
                    self.player.bot1 = self.Bot1
                    self.player.bot2 = self.Bot2
                    self.player.bot3 = self.Bot3
                    self.player.bot4 = self.Bot4
                    self.player.bot5 = self.Bot5
                    BattleResult2Message(self.client, self.player, db).send()
