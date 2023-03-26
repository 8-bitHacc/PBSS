import json
from Utils.Helpers import Helpers
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Emotes import Emotes

class Player:
    try:
        config = open('config.json', 'r')
        content = config.read()
    except FileNotFoundError:
        Helpers().create_config()
        config = open('config.json', 'r')
        content = config.read()

    settings = json.loads(content)

    skins_id = Skins().get_skins_id()
    brawlers_id = Characters().get_brawlers_id()
    emotes_id = Emotes().get_emotes_id()

    ID = 0
    token = None

    trophies = settings['Trophies']
    tickets = settings['Tickets']
    gems = settings['Gems']
    resources = [{'ID': 1, 'Amount': settings['BrawlBoxTokens']}, {'ID': 8, 'Amount': settings['Gold']}, {'ID': 9, 'Amount': settings['BigBoxTokens']}, {'ID': 10, 'Amount': settings['StarPoints']}]
    high_trophies = 0
    trophy_reward = 1
    exp_points = 0
    profile_icon = 0
    name_color = 0
    selected_brawler = 0
    region = settings['Region']
    content_creator = "Modern Brawl"
    name_set = False
    name = 'Guest'
    map_id = 0
    use_gadget = True
    starpower = 76
    gadget = 255
    home_brawler = 0
    home_skin = 0
    leaderboard_type = 0
    leaderboard_is_global = False
    bp_activated = False
    token_doubler = 0
    welcome_msg_viewed = False
    theme_id = settings['ThemeID']
    content_creator_codes = settings['ContentCreatorCodes']
    maintenance = settings['Maintenance']
    maintenance_time  = settings['SecondsTillMaintenanceOver']
    patch = settings['Patch']
    patch_url = settings['PatchURL']
    patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")
    update_url = settings['UpdateURL']
    TrophiesAnimation = 0
    tutorial = 0

    delivery_items = {}
    box_rewards = {}

    db = None

    battle_tick = 0

    unlocked_skins = [0]
    unlocked_spgs = [0]

    selected_skins = {}
    for id in brawlers_id:
        selected_skins.update({f"{id}": 0})

    brawlers_unlocked = [0]

    pins_unlocked = []

    selected_pins = {}
    for id in brawlers_id:
        selected_pins.update({f"{id}": 0})

    brawlers_card_id = []
    for x in brawlers_unlocked:
        brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

    brawlers_spg = Cards().get_spg_id()

    def_trophies = 0
    def_high_trophies = 0

    brawlers_trophies = {}
    for x in brawlers_id:
        brawlers_trophies.update({f'{x}': def_trophies})

    brawlers_high_trophies = {}
    for x in brawlers_id:
        brawlers_high_trophies.update({f'{x}': def_high_trophies})

    def_level = 0

    brawlers_level = {}
    for x in brawlers_id:
        brawlers_level.update({f'{x}': def_level})

    def_pp = 0

    brawlers_powerpoints = {}
    for x in brawlers_id:
        brawlers_powerpoints.update({f'{x}': def_pp})


    club_id = 0
    club_role = 0

    message_tick = 0

    game_major = 0
    game_minor = 0
    game_build = 0

    # Team Data
    isReady = 0

    clients = {}


    def __init__(self, device):
        self.device = device


