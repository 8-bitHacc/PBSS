import random

class LogicBoxData:

    def randomize(self, type):
        self.box_rewards = { 'Rewards': [] }

        if (type == 10):
            check = False

            if (random.randint(0,500) < 5):
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if brawler not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers',self.player.brawlers_unlocked)
                    check = True

            if (random.randint(0,100) < 100) and not check:
                gold_value = random.randint(20, 100)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                self.box_rewards['Rewards'].append(gold_reward)
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                rewarded = []
                for x in range(1):
                    pp_value = random.randint(5, 30)
                    brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                    if (self.player.brawlers_level[str(brawler)] < 9):
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints[ str(brawler)] + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler)
                    if (self.player.brawlers_level[str(brawler)] > 9):
                        value = random.randint(20, 100)
                        item = {'Amount': value, 'DataRef': [0,0], 'Value': 1, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                        self.box_rewards['Rewards'].append(item)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

            if (random.randint(0,100) < 20) and not check:
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if brawler not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            if (random.randint(0,100) < 30):
                bonus_value = random.randint(20, 50)
                self.player.token_doubler = self.player.token_doubler + bonus_value
                self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': 2, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                self.box_rewards['Rewards'].append(bonus_reward)

        elif (type == 12):
            if (random.randint(0,100) < 100):
                gold_value = random.randint(50, 150)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                self.box_rewards['Rewards'].append(gold_reward)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

                if len(self.player.brawlers_unlocked) in [1, 2]:
                    rewarded = []
                    for x in range(len(self.player.brawlers_unlocked)):
                        pp_value = random.randint(30, 50)
                        brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                        if (self.player.brawlers_level[str(brawler)] < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints[ str(brawler)] + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                            rewarded.append(brawler)
                        if (self.player.brawlers_level[str(brawler)] > 9):
                            value = random.randint(20, 100)
                            item = {'Amount': value, 'DataRef': [0,0], 'Value': 1, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                            self.box_rewards['Rewards'].append(item)
                            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                            self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                else:
                    rewarded = []
                    for x in range(random.choice([2, 3])):
                        pp_value = random.randint(30, 50)
                        brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                        if (self.player.brawlers_level[str(brawler)] < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints[ str(brawler)] + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                            rewarded.append(brawler)

            if (random.randint(0,500) < 35):
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if brawler not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            if (random.randint(0,100) < 40):
                bonus_value = random.randint(40, 80)
                self.player.token_doubler = self.player.token_doubler + bonus_value
                self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': 2, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                self.box_rewards['Rewards'].append(bonus_reward)


        elif (type == 11):
            if (random.randint(0,100) < 100):
                gold_value = random.randint(100, 500)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                self.box_rewards['Rewards'].append(gold_reward)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

                if len(self.player.brawlers_unlocked) in [1, 2, 3, 4]:
                    rewarded = []
                    for x in range(len(self.player.brawlers_unlocked)):
                        pp_value = random.randint(50, 150)
                        brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                        if (self.player.brawlers_level[str(brawler)] < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints[ str(brawler)] + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                            rewarded.append(brawler)
                else:
                    rewarded = []
                    for x in range(random.choice([4, 5])):
                        pp_value = random.randint(50, 150)
                        brawler = random.choice(sorted(set(self.player.brawlers_unlocked) - set(rewarded)))
                        if (self.player.brawlers_level[str(brawler)] < 8):
                            pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler], 'Value': 6, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                            self.box_rewards['Rewards'].append(pp_reward)
                            self.player.brawlers_powerpoints[str(brawler)] = self.player.brawlers_powerpoints[ str(brawler)] + pp_value
                            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                            rewarded.append(brawler)

            if (random.randint(0,500) < 55):
                locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if brawler not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            if (random.randint(0,100) < 50):
                bonus_value = random.randint(100, 400)
                self.player.token_doubler = self.player.token_doubler + bonus_value
                self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Value': 2, 'SkinID': [0,0], 'PinID': [0,0], 'SPGID': [0,0]}
                self.box_rewards['Rewards'].append(bonus_reward)


        return self.box_rewards


