class ForcedDrops:
    
    def encode(self):
        self.writeVInt(0) # Starpower Drop
        self.writeVInt(0) # Gadget Drop

        self.writeVInt(5) # Rarity Count
        self.writeVInt(0) # Rare Drop
        self.writeVInt(0) # Super Rare Drop
        self.writeVInt(0) # Epic Drop
        self.writeVInt(0) # Mythic Drop
        self.writeVInt(0) # Legendary Drop