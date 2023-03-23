import json
from datetime import datetime

class LogicShopData:

    shop_resources = json.loads(open('shop.json', 'r').read())

    gold_packs = shop_resources['GoldPacks']
    gold_cost, gold_amount = [], []

    for x in gold_packs:
        gold_cost.append(x['Cost'])
        gold_amount.append(x['Amount'])

    boxes = shop_resources['Boxes']
    token_doubler = shop_resources['TokenDoubler']

    offers = shop_resources['Offers']

    def encodeShopPacks(self):
        # Brawler Upgrade Cost
        self.writeArrayVint([8, 40, 80, 145, 295, 485, 805, 1255])
        # Gold
        self.writeArrayVint(LogicShopData.gold_cost)
        self.writeArrayVint(LogicShopData.gold_amount)

    def encodeShopResources(self):
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        LogicShopData.encodeBoxes(self)
        LogicShopData.encodeTokenDoubler(self)


    def encodeShopOffers(self):
        self.writeVInt(len(LogicShopData.offers))
        for x in LogicShopData.offers:
            self.writeVInt(1) # Count
            for y in range(1):
                self.writeVInt(x['OfferID']) # ID
                self.writeVInt(x['Multiplier']) # Count
                self.writeDataReference(x['DataReference'][0],x['DataReference'][1])
                self.writeVInt(x['ItemID']) # ItemID (Like Skins)

            self.writeVInt(x['Currency']) # Currency (0-Gems, 1-Gold, 3-StarPoints)
            self.writeVInt(x['Cost']) # Cost
            self.writeVInt(x['Timer']) # Time
            self.writeVInt(x['State']) # State (0-New with Animations, 1-New, 2-Nothing)

            self.writeVInt(0)
            self.writeBoolean(x['Claimed']) # Offer Claimed
            self.writeVInt(0) # Offer Index
            self.writeVInt(0)
            self.writeBoolean(x['isDaily']) # isDaily?
            self.writeVInt(x['OldCost']) # OldPrice
            self.writeInt(0)
            self.writeString(x['OfferText']) # Offer Text

            self.writeBoolean(False)
            self.writeString(x['OfferBG']) # Offer Background
            self.writeVInt(0)
            self.writeBoolean(x['isProcessed']) # isProcessed
            self.writeVInt(x['ExtraType']) # ExtraType
            self.writeVInt(x['Extra'])# Extra
            self.writeString()
            self.writeBoolean(x['isOneTimePurchase'])# isOneTimePurchase

    def encodeBoxes(self):
        self.writeVInt(100) # Tokens for 1 Brawl Box
        self.writeVInt(10)  # Tokens for 1 Big Box

        self.writeVInt(LogicShopData.boxes[0]['Cost'])
        self.writeVInt(LogicShopData.boxes[0]['Multiplier'])

        self.writeVInt(LogicShopData.boxes[1]['Cost'])
        self.writeVInt(LogicShopData.boxes[1]['Multiplier'])


    def encodeTokenDoubler(self):
        self.writeVInt(LogicShopData.token_doubler[0]['Cost'])
        self.writeVInt(LogicShopData.token_doubler[0]['Amount'])
