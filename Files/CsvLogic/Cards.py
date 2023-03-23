from Files.CsvReader import CsvReader

class Cards:
    def get_spg_id(self):
        CardSkillsID = []
        reader = CsvReader()
        rowData = reader.readCsv('GameAssets/csv_logic/cards.csv')
        for row in rowData:
            if row[7] == '4' and row[4].lower() != "true" and row[5].lower() != "true":
                CardSkillsID.append(rowData.index(row))
        return CardSkillsID


    def check_spg_id(self, id):
        reader = CsvReader()
        rowData = reader.readCsv('GameAssets/csv_logic/cards.csv')
        for row in rowData:
            if rowData.index(row) == id:
                return row[5].lower()


    def get_brawler_unlock(self):
        CardUnlockID = []
        reader = CsvReader()
        rowData = reader.readCsv('GameAssets/csv_logic/cards.csv')
        for row in rowData:
            if row[5].lower() == '0':
                CardUnlockID.append(rowData.index(row))
        return CardUnlockID


    def get_spg_by_brawler_id(self, brawler_id, type):
        reader = CsvReader()
        charsData  = reader.readCsv('GameAssets/csv_logic/characters.csv')
        cardsData  = reader.readCsv('GameAssets/csv_logic/cards.csv')
        for row in charsData:
            if charsData.index(row) == brawler_id:
                name = row[0]
                for row in cardsData:
                    if type == 4:
                        if row[5].lower() == '4' and row[3] == name:
                            return cardsData.index(row)
                    elif type == 5:
                        if row[3] == name and row[6].lower() == '5':
                            return cardsData.index(row)



    def get_unlock_by_brawler_id(self, brawler_id):
        reader = CsvReader()
        charsData  = reader.readCsv('GameAssets/csv_logic/characters.csv')
        cardsData  = reader.readCsv('GameAssets/csv_logic/cards.csv')
        for row in charsData:
            if charsData.index(row) == brawler_id:
                name = row[0]
                for row in cardsData:
                    if row[7] == '0' and row[4].lower() != "true" and row[5].lower() != "true":
                        return cardsData.index(row)
