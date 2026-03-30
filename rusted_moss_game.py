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

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Also equip TRINKET",
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
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Don't equip TRINKET if possible",
                data={
                    "TRINKET": (self.common_trinkets, 3)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
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
                label="Use only WEAPON if possible",
                data={
                    "WEAPON": (self.weapons, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Don't take any damage!",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            # Boss kills
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=15,
            ),
            # Boss kills with trinkets
            GameObjectiveTemplate(
                label="Defeat BOSS with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.trinkets, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.trinkets, 2)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            # Boss kills with uncommon trinkets
            GameObjectiveTemplate(
                label="Defeat BOSS with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.uncommon_trinkets, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.uncommon_trinkets, 2)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            # Boss kills with specific weapons
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
            # Empowered boss kills
            GameObjectiveTemplate(
                label="Defeat BOSS (Empowered)",
                data={
                    "BOSS": (self.bosses, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=15,
            ),
            # Empowered boss kills with trinkets
            GameObjectiveTemplate(
                label="Defeat BOSS (Empowered) with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.trinkets, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS (Empowered) with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.trinkets, 2)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            # Empowered boss kills with uncommon trinkets
            GameObjectiveTemplate(
                label="Defeat BOSS (Empowered) with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.uncommon_trinkets, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS (Empowered) with TRINKET equipped",
                data={
                    "BOSS": (self.bosses, 1),
                    "TRINKET": (self.uncommon_trinkets, 2)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            # Empowered boss kills with specific weapons
            GameObjectiveTemplate(
                label="Defeat BOSS (Empowered) using only WEAPONS",
                data={
                    "BOSS": (self.bosses, 1),
                    "WEAPONS": (self.weapons, 2)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete the boss rush!",
                data={},
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            # Climbs
            GameObjectiveTemplate(
                label="Complete CLIMBER's climb",
                data={
                    "CLIMBER": (self.climbs, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=15,
            ),
            # Fresh save objectives
            GameObjectiveTemplate(
                label="From a new save file, collect COUNT trinkets",
                data={
                    "COUNT": (self.rand_collectibles, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="From a new save file, collect COUNT stat upgrades",
                data={
                    "COUNT": (self.rand_collectibles, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="From a new save file, read COUNT lore boxes",
                data={
                    "COUNT": (self.rand_collectibles, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="From a new save file, defeat COUNT bosses",
                data={
                    "COUNT": (self.rand_bosses, 1)
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
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
            "The Seer",
            "Robin the Beloved Child",
            "any boss"
        ]
    
    # Trinkets that are used in builds often, including most damage + movement buffing trinkets
    def common_trinkets(self) -> List[str]:
        return [
            "Incendiary Essence",
            "Giant Chambers",
            "Ruby Slippers",
            "Time Manipulator",
            "Spiced Gunpowder",
            "Powdered Fae Silver",
            "Powdered Nightshade",
            "Erosive Bullets",
            "Guardian Fae",
            "Dandelion Bomb",
            "HP Overload",
            "Heavy Ammo",
            "Glass Coin",
        ]
    
    # Trinkets that aren't used in builds often, including those with little to no use for boss battles
    def uncommon_trinkets(self) -> List[str]:
        return [
            "Tattered Blindfold",
            "Magnet",
            "Fairy Ointment",
            "Energy Refiner",
            "Lucky Clover Pearl",
            "Sprite's Breath",
            "Wing Clipper",
            "Cracked Monocle",
            "Magnetic Bullets",
            "Thorny Rose",
            "Rusted Coin",
            "Cleansing Charm",
            "Cricket Bone Whip",
            "HP Overload",
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
            "Soft Fae",
            "Mossy Wings"
        ]
    
    def trinkets(self) -> List[str]:
        trinkets: List[str] = self.common_trinkets[:]

        trinkets.extend(self.uncommon_trinkets[:])

        return trinkets
    
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
    def mana_abilities() -> List[str]:
        return [
            "Heal",
            "Grenades"
        ]

    @staticmethod
    def rand_collectibles() -> range:
        return range(4, 8)
    
    @staticmethod
    def rand_bosses() -> range:
        return range(3, 5)
    
