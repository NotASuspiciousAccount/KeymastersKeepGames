from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class RustedMossArchipelagoOptions:
    rusted_moss_trial_types: RustedMossTrialTypes
    rusted_moss_include_dlc: RustedMossDLCTrials

class Rusted_Moss(Game):
    name = "Rusted Moss"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX
    ]

    is_adult_only_or_unrated = False

    options_cls = RustedMossArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Also equip TRINKET if possible",
                data={
                    "TRINKET": (self.trinkets, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Don't equip TRINKET if possible",
                data={
                    "TRINKET": (self.trinkets, 3)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Don't use ABILITY",
                data={
                    "ABILITY": (self.mana_abilities, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Don't use ITEM if possible",
                data={
                    "ITEM": (self.movement_items, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Use only WEAPON if possible",
                data={
                    "WEAPON": (self.weapons, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Don't take damage!",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()
        if self.include_bosses:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Defeat BOSS.",
                    data={
                        "BOSS": (self.bosses, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.trinkets, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=5,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.trinkets, 2)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.uncommon_trinkets, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=5,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.uncommon_trinkets, 2)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS using only WEAPONS.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "WEAPONS": (self.weapons, 2)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
                # Empowered boss kills
                GameObjectiveTemplate(
                    label="Defeat BOSS (Empowered).",
                    data={
                        "BOSS": (self.bosses, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS (Empowered) with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.trinkets, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=5,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS (Empowered) with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.trinkets, 2)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS (Empowered) with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.uncommon_trinkets, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=5,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS (Empowered) with TRINKET equipped.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "TRINKET": (self.uncommon_trinkets, 2)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Defeat BOSS (Empowered) using only WEAPONS.",
                    data={
                        "BOSS": (self.bosses, 1),
                        "WEAPONS": (self.weapons, 2)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=3,
                ),
            ])
        if self.include_bosses and self.include_dlc:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Complete the boss rush!",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Complete the empowered boss rush!",
                    data={},
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=3,
                ),
            ])
        if self.include_climbs:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Complete CLIMBER's climb.",
                    data={
                        "CLIMBER": (self.climbs, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Complete CLIMBER's climb in TIME seconds.",
                    data={
                        "CLIMBER": (self.climbs, 1),
                        "TIME": (self.rand_climb_seconds, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=5,
                ),
                GameObjectiveTemplate(
                    label="Complete CLIMBER's climb in TIME seconds.",
                    data={
                        "CLIMBER": (self.climbs, 1),
                        "TIME": (self.rand_hardclimb_seconds, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=5,
                ),
                GameObjectiveTemplate(
                    label="Complete CLIMBER's climb without using ITEM.",
                    data={
                        "CLIMBER": (self.climbs, 1),
                        "ITEM": (self.movement_items, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=5,
                ),
            ])
        if self.include_climbs and self.include_dlc:
            game_objective_templates.extend([        
                GameObjectiveTemplate(
                    label="Complete The Great Climb. (after resetting doors/arenas)",
                    data={
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete The Hardmode Great Climb.",
                    data={
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])
        if self.include_traversal:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2 without teleports.",
                    data={
                        "AREA1": (self.areas, 1),
                        "AREA2": (self.areas, 1)                        
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2 without teleports or ITEM.",
                    data={
                        "AREA1": (self.areas, 1),
                        "AREA2": (self.areas, 1),
                        "ITEM": (self.movement_items, 1)                       
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2, then to AREA3 without teleports.",
                    data={
                        "AREA1": (self.areas, 1),
                        "AREA2": (self.areas, 1),
                        "AREA3": (self.areas, 1)                      
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2, then to AREA3 without teleports or ITEM.",
                    data={
                        "AREA1": (self.areas, 1),
                        "AREA2": (self.areas, 1),
                        "AREA3": (self.areas, 1),
                        "ITEM": (self.movement_items, 1)                      
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
            ])
        if self.include_traversal and self.include_dlc:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2 without teleports.",
                    data={
                        "AREA1": (self.dlc_areas, 1),
                        "AREA2": (self.dlc_areas, 1)                        
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2, then to AREA3 without teleports.",
                    data={
                        "AREA1": (self.dlc_areas, 1),
                        "AREA2": (self.dlc_areas, 1),
                        "AREA3": (self.dlc_areas, 1)                      
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2 without teleports.",
                    data={
                        "AREA1": (self.all_areas, 1),
                        "AREA2": (self.all_areas, 1)                        
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Travel from AREA1 to AREA2, then to AREA3 without teleports.",
                    data={
                        "AREA1": (self.all_areas, 1),
                        "AREA2": (self.all_areas, 1),
                        "AREA3": (self.all_areas, 1)                      
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ])
        if self.include_new_save:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="From a new save file, collect COUNT trinkets.",
                    data={
                        "COUNT": (self.rand_collectibles, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, collect COUNT stat upgrades.",
                    data={
                        "COUNT": (self.rand_collectibles, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, read COUNT lore boxes.",
                    data={
                        "COUNT": (self.rand_collectibles, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, defeat COUNT bosses.",
                    data={
                        "COUNT": (self.rand_bosses, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                # Hard variants of the above
                GameObjectiveTemplate(
                    label="From a new save file, collect COUNT trinkets.",
                    data={
                        "COUNT": (self.rand_collectibles_hard, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, collect COUNT stat upgrades.",
                    data={
                        "COUNT": (self.rand_collectibles_hard, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, read COUNT lore boxes.",
                    data={
                        "COUNT": (self.rand_collectibles_hard, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, defeat COUNT bosses.",
                    data={
                        "COUNT": (self.rand_bosses_hard, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="From a new save file, achieve ENDING.",
                    data={
                        "ENDING": (self.ending, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ])
        if self.include_speedrun:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Achieve Ending E in under TIME minutes.",
                    data={
                        "TIME": (self.rand_ending_e, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Achieve Ending A in under TIME minutes.",
                    data={
                        "TIME": (self.rand_ending_a, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Achieve Ending D in under 1 hour and TIME minutes.",
                    data={
                        "TIME": (self.rand_ending_d, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])
        if self.include_speedrun and self.include_dlc:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Achieve Blossoming Summit and defeat Frøy in under 2 hours and TIME minutes.",
                    data={
                        "TIME": (self.rand_summit_time, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Achieve One More Final and defeat Frøy? in under HOUR hours and MIN minutes.",
                    data={
                        "HOUR": (self.rand_summithard_hour, 1),
                        "MIN": (self.rand_summithard_minute, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])
        return game_objective_templates

    # Settings allocation
    @property
    def modes(self) -> List[str]:
        return sorted(self.archipelago_options.rusted_moss_trial_types.value)
    @property
    def include_bosses(self) -> bool:
        return "Bosses" in self.modes
    @property
    def include_climbs(self) -> bool:
        return "Climbs" in self.modes
    @property
    def include_traversal(self) -> bool:
        return "Traversal" in self.modes
    @property
    def include_new_save(self) -> bool:
        return "New Save" in self.modes
    @property
    def include_speedrun(self) -> bool:
        return "Speedrunning" in self.modes
    @property
    def include_dlc(self) -> bool:
        return self.rusted_moss_include_dlc

    # Datasets
    @functools.cached_property
    def base_bosses(self) -> List[str]:
        return [
            "Bonnie",
            "Great Witch Ameli",
            "Maya 1",
            "War",
            "Elecia",
            "Pestilence",
            "Priestess Friea",
            "Spirella",
            "Lenore, Fae-Touched Witch",
            "Face Stealers",
            "Maya 2",
            "Void Worm",
            "Famine",
            "Seer",
            "Robin",
            "Legacy Robin",
            "any boss"
        ]
    
    @functools.cached_property
    def dlc_bosses(self) -> List[str]:
        return [
            "Forgotten experiment \"Noah\"",
            "Diana",
            "Elicia 2",
            "Frøy",
        ]
    
    def bosses(self) -> List[str]:
        bosses: List[str] = self.base_bosses()

        if self.include_dlc:
            bosses.extend(self.dlc_bosses)

        return sorted(bosses)

    @staticmethod
    def bosses() -> List[str]:
        return [
            "Bonnie",
            "Great Witch Ameli",
            "Maya 1",
            "War",
            "Elecia",
            "Pestilence",
            "Priestess Friea",
            "Spirella",
            "Lenore, Fae-Touched Witch",
            "Face Stealers",
            "Maya 2",
            "Void Worm",
            "Famine",
            "Forgotten experiment \"Noah\"",
            "Seer",
            "Robin",
            "Legacy Robin",
            "Diana",
            "Elicia 2",
            "Frøy",
            "any boss"
        ]
    
    @staticmethod
    def base_trinkets() -> List[str]:
        return [
            "Incendiary Essence",
            "Tattered Blindfold",
            "Giant Chambers",
            "Magnet",
            "Ruby Slippers",
            "Fairy Ointment",
            "Energy Refiner",
            "Lucky Clover Pearl",
            "Time Manipulator",
            "Sprite's Breath",
            "Wing Clipper",
            "Powdered Nightshade",
            "Cracked Monocle",
            "Magnetic Bullets",
            "Thorny Rose",
            "Rusted Coin",
            "Cleansing Charm",
            "Erosive Bullets",
            "Guardian Fae",
            "Cricket Bone Whip",
            "Dandelion Bomb",
            "HP Overload",
            "Heavy Ammo",
            "Short Fuse",
            "Thorny Wings",
            "Maya's Trinket",
            "Fern's Trinket",
            "Fae of Love",
            "Fae of Hate",
            "Fae of Glass",
            "Titania's Protection",
            "Energy Disruptor"
        ]

    @staticmethod
    def dlc_trinkets() -> List[str]:
        return [
            "Energy Converter",
            "Soft Fae",
            "Mossy Wings",
            "Glass Coin"
        ]

    def trinkets(self) -> List[str]:
        trinkets: List[str] = self.base_trinkets()

        if self.include_dlc:
            trinkets.extend(self.dlc_trinkets)

        return sorted(trinkets)
    
    @staticmethod
    def uncommon_base_trinkets() -> List[str]:
        return [
            "Magnet",
            "Fairy Ointment",
            "Energy Refiner",
            "Time Manipulator",
            "Spiced Gunpowder",
            "Powdered Fae Silver",
            "Sprite's Breath",
            "Wing Clipper",
            "Powdered Nightshade",
            "Cracked Monocle",
            "Magnetic Bullets",
            "Rusted Coin",
            "Erosive Bullets",
            "Cricket Bone Whip",
            "Short Fuse",
            "Thorny Wings",
            "Fae of Love",
            "Fae of Hate",
            "Titania's Protection",
            "Energy Disruptor",
        ]

    def uncommon_dlc_trinkets() -> List[str]:
        return [
            "Energy Converter",
            "Soft Fae",
            "Mossy Wings"
        ]

    def uncommon_trinkets(self) -> List[str]:
        trinkets: List[str] = self.uncommon_base_trinkets()

        if self.include_dlc:
            trinkets.extend(self.uncommon_dlc_trinkets)

        return sorted(trinkets)
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Rail",
            "Pistol",
            "Rocket Launcher",
            "Shotgun",
            "Sniper",
            "Bolt Launcher"
        ]
    
    @staticmethod
    def climbs() -> List[str]:
        return [
            "Seer",
            "Ameli",
            "Shopkeeper",
            "Fern",
            "Juni"
        ]
    @staticmethod
    def areas() -> List[str]:
        return [
            "Mossy Hills",
            "Factory Roof",
            "Snowy Outpost",
            "Smokestack Forest",
            "Mountainside",
            "Lake",
            "Pipe",
            "Ichor Refinery",
            "Living Quarters",
            "The Lab",
            "Barrows Ceiling",
            "Elfame"
        ]
    @staticmethod
    def dlc_areas() -> List[str]:
        return [
            "Overgrown Tundra",
            "Forest of Remembrance",
            "Sunken Library",
            "Court of Ash",
            "Temple of the Wild Dance",
            "Juni's Village",
            "(Interlude 1)",
            "Piercing Morning Fog",
            "(Interlude 2)",
            "Red Velvet Corridor",
            "The First Mire",
            "Violent Twisting Architecture",
            "Blossoming Summit"
        ]
    @staticmethod
    def all_areas() -> List[str]:
        return [
            "Mossy Hills",
            "Factory Roof",
            "Snowy Outpost",
            "Smokestack Forest",
            "Mountainside",
            "Lake",
            "Pipe",
            "Ichor Refinery",
            "Living Quarters",
            "The Lab",
            "Barrows Ceiling",
            "Elfame",
            "Overgrown Tundra",
            "Forest of Remembrance",
            "Sunken Library",
            "Court of Ash",
            "Temple of the Wild Dance",
            "Juni's Village",
            "(Interlude 1)",
            "Piercing Morning Fog",
            "(Interlude 2)",
            "Red Velvet Corridor",
            "The First Mire",
            "Violent Twisting Architecture",
            "Blossoming Summit"
        ]
    
    @staticmethod
    def ending() -> List[str]:
        return [
            "Ending A",
            "Ending B",
            "Ending C",
            "Ending D",
            "Ending E"
        ]

    @staticmethod
    def mana_abilities() -> List[str]:
        return [
            "Heal",
            "Grenades"
        ]
    
    @staticmethod
    def movement_items() -> List[str]:
        return [
            "Grapple",
            "Grapple Fling",
            "High Jump",
            "Weapon Knockback"
        ]

    @staticmethod
    def rand_collectibles() -> range:
        return range(4, 8)
    @staticmethod
    def rand_bosses() -> range:
        return range(2, 5)
    @staticmethod
    def rand_collectibles_hard() -> range:
        return range(7, 13)
    @staticmethod
    def rand_bosses_hard() -> range:
        return range(4, 7)
    
    @staticmethod
    def rand_ending_e() -> range:
        return range(20, 35)
    @staticmethod
    def rand_ending_a() -> range:
        return range(37, 50)
    @staticmethod
    def rand_ending_d() -> range:
        return range(5, 30)
    @staticmethod
    def rand_summit_time() -> range:
        return range(5, 59)
    @staticmethod
    def rand_summithard_hour() -> range:
        return range(3, 4)
    @staticmethod
    def rand_summithard_minute() -> range:
        return range(0, 59)
    @staticmethod
    def rand_climb_seconds() -> range:
        return range(80, 110)
    @staticmethod
    def rand_hardclimb_seconds() -> range:
        return range(50, 70)
    
# Options
class RustedMossTrialTypes(OptionSet):
    """
    Defines what types of trials can appear:
    Bosses: Trials for beating specific bosses can appear. Bosses are expected to be fought in the Forest of Remembrance, regardless of whether the Major Content Update is enabled.
    Climbs: Trials for beating specific climbs can appear. Note: The Great Climb will appear if time consuming and DLC are enabled.
    Traversal: Trials for travelling from one game area to another can appear.
    New Save: Trials requiring a new save file can appear.
    
    Speedrunning: Trials expecting a speedrun from a game start to a specified goal can appear. Warning: These can be quite difficult, so it is recommended to not enable this without prior speedrunning experience.
    Seriously, Speedrunning trials can be very hard. By enabling them, you accept the potential for having to beat Hardmode Climb from a fresh save in 3 hours. You have been warned.
    """
    display_name = "Rusted Moss Trial Types"
    valid_keys = [
        "Bosses",
        "Climbs",
        "Traversal",
        "New Save",
        "Speedrunning"
    ]
    default = [
        "Bosses",
        "Climbs",
        "Traversal",
        "New Save"
    ]

class RustedMossDLCTrials(Toggle):
    """
    Defines whether the Major Content Update and Winter Update can appear in trials.
    """
    display_name = "Rusted Moss Enable DLC"
    default = False