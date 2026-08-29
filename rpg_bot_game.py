from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class RPGBotArchipelagoOptions:
    pass

# Main Class
class RPGBotGame(Game):
    name = "Template"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
    ]

    is_adult_only_or_unrated = False

    options_cls = RPGBotArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            # Intentionally empty
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            # Hunting Objectives
            GameObjectiveTemplate(
                label="Complete a hunt HUNTS times.",
                data={
                    "HUNTS": (self.hunt_count_low, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Complete a hunt HUNTS times.",
                data={
                    "HUNTS": (self.hunt_count_high, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=7,
            ),
            GameObjectiveTemplate(
                label="Complete a hunt HUNTS times in AREA area.",
                data={
                    "HUNTS": (self.hunt_count_low, 1),
                    "AREA": (self.random_area, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=12,
            ),
            # Adventure Objectives
            GameObjectiveTemplate(
                label="Complete an adventure.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Complete an adventure ADVENTURES times.",
                data={
                    "ADVENTURES": (self.adventure_count, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Complete an adventure in AREA area.",
                data={
                    "AREA": (self.random_area, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=12,
            ),
            # Material Gathering Objectives
            GameObjectiveTemplate(
                label="GATHER AMOUNT times.",
                data={
                    "GATHER": (self.gathering_methods, 1),
                    "AMOUNT": (self.material_count_low, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=15,
            ),
            GameObjectiveTemplate(
                label="GATHER AMOUNT times.",
                data={
                    "GATHER": (self.gathering_methods, 1),
                    "AMOUNT": (self.material_count_high, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Complete the following AMOUNT times each: GATHER",
                data={
                    "GATHER": (self.gathering_methods, 2),
                    "AMOUNT": (self.material_count_low, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=6,
            ),
            # Training Objectives
            GameObjectiveTemplate(
                label="Complete training AMOUNT times.",
                data={
                    "AMOUNT": (self.training_count_low, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Complete training AMOUNT times.",
                data={
                    "AMOUNT": (self.training_count_high, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            # Enchantment Objectives
            GameObjectiveTemplate(
                label="Enchant any equipment piece to ENCHANT or better.",
                data={
                    "ENCHANT": (self.random_enchants, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            # Crafting Objectives
            GameObjectiveTemplate(
                label="Craft any item.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Dismantle any material.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            # Gambling Objectives
            GameObjectiveTemplate(
                label="Win COIN coins from GAMBLE.",
                data={
                    "COIN": (self.gambling_coins, 1),
                    "GAMBLE": (self.gambling_games, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Win COIN coins from gambling.",
                data={
                    "COIN": (self.gambling_coins, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Lose COIN coins from gambling.",
                data={
                    "COIN": (self.gambling_coins, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            # Shop/Item Objectives
            GameObjectiveTemplate(
                label="Buy AMOUNT life potions.",
                data={
                    "AMOUNT": (self.random_life_potions, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=7,
            ),
            GameObjectiveTemplate(
                label="Buy or obtain a lootbox.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=7,
            ),
            GameObjectiveTemplate(
                label="Open a lootbox.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Eat 3 arena cookies.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Eat AMOUNT arena cookies.",
                data={
                    "AMOUNT": (self.random_cookies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            # Long Cooldown Objectives (>1 hour)
            # All of these will be marked as time consuming.
            GameObjectiveTemplate(
                label="Participate in a duel.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Participate in an arena.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Claim your daily or weekly rewards.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Attempt horse breeding.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Attempt a miniboss or dungeon.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete a quest.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=4,
            ),
            # Random Objectives
            # These can be unreliable, so they will be rare to mitigate this.
            GameObjectiveTemplate(
                label="Participate in a random event.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get a material drop from a hunt or adventure.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            # Gimmick Objectives
            # These won't require progress as much as they will require out of the box thinking.
            GameObjectiveTemplate(
                label="Have 30 or less HP.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Have AMOUNT or less cooldowns ready.",
                data={
                    "AMOUNT": (self.remaining_cooldowns_count, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Participate in any command requiring more than one player.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Consecutively complete a hunt and an adventure without healing.",
                data={
                    # Intentionally empty
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Consecutively complete HUNTS hunts without healing.",
                data={
                    "HUNTS": (self.hunt_count_low, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

        ]

    # Datasets
    @staticmethod
    def gambling_games() -> List[str]:
        return [
            "Dice",
            "Cups",
            "Blackjack",
            "Slots",
            "Coinflip",
            "Lottery",
        ]

    def gathering_methods() -> List[str]:
        return [
            "Chop",
            "Fish",
            "Chop",
            "Fish",
            "Pick up fruits",
        ]

    def random_enchants() -> List[str]:
        return [
            "Good",
            "Great",
            "Mega",
        ]
    
    @staticmethod
    def gambling_coins() -> range:
        return range(100, 10000)

    @staticmethod
    def hunt_count_low() -> range:
        return range(3, 7)
    
    @staticmethod
    def hunt_count_high() -> range:
        return range(7, 13)

    @staticmethod
    def random_area() -> range:
        return range(1, 4)

    @staticmethod
    def adventure_count() -> range:
        return range(2, 4)

    def training_count() -> range:
        return range(2, 5)

    @staticmethod
    def material_count_low() -> range:
        return range(2, 5)

    @staticmethod
    def material_count_high() -> range:
        return range(3, 9)

    @staticmethod
    def remaining_cooldowns_count() -> range:
        return range(1, 4) # Never zero, as I don't want to force players to vote if they don't want to

    def random_life_potions() -> range:
        return range(1, 11)

    def random_cookies() -> range:
        return range(5, 13)