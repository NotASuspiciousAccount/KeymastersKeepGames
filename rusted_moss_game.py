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
    pass

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

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.trinkets, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.trinkets, 2)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS using only WEAPONS",
                data={
                    "BOSS": (self.bosses, 1),
                    "WEAPONS": (self.weapons, 2)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete CLIMBER's climb",
                data={
                    "CLIMBER": (self.climbs, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            
        ]

    # Datasets
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
            "Seer"
        ]
    
    @staticmethod
    def trinkets() -> List[str]:
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
            "Spiced Gunpowder",
            "Powdered Fae Silver",
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
            "Energy Disruptor",
            "Energy Converter",
            "Soft Fae"
        ]
    
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