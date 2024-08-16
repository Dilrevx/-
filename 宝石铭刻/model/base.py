from collections import defaultdict
from enum import Enum
from typing import Callable, Dict, List

TOTAL_ENA = 100
MAX_DESK_SIZE = 6


class Ena(Enum):
    RED = 0
    BLUE = 1
    PURPLE = 2
    YELLOW = 3


class _Card:
    manufacturesByLevel: Dict[int, Callable[[Dict[Ena, List[int]]], None]] = {}

    def __init__(self, name: str, ena: Ena, isBackground=False, upgradeLevel=3):
        self.name = name
        self.ena = ena
        self.background = isBackground
        self.upgradeLevel = upgradeLevel

    def manufacture(self, playground) -> None:
        self.manufacturesByLevel[self.upgradeLevel](playground)


class Playground:
    def __init__(self, deskSize: int) -> None:
        self.enaValue = EnaValue()
        self.enaCounts = {
            Ena.RED: [0, 0, 0, 0, 0],
            Ena.BLUE: [0, 0, 0, 0],
            Ena.PURPLE: [0, 0, 0, 0],
            Ena.YELLOW: [0],
        }
        self.deskSize = deskSize
        self.cards: List[_Card] = []
        self.postfunction: List[Callable[[Playground], int]] = []

    def clear(self):
        self.enaCounts = {
            Ena.RED: [0, 0, 0, 0, 0],
            Ena.BLUE: [0, 0, 0, 0],
            Ena.PURPLE: [0, 0, 0, 0],
            Ena.YELLOW: [0],
        }

        self.enaValue.clearBonus()
        self.cards.clear()
        self.postfunction.clear()


class EnaValue:
    """
    计算每个 ena 的价值。

    不包括空位奖励和数量奖励
    """

    enaValue = {
        Ena.RED: (1, 2, 10, 35, 85),
        Ena.BLUE: (1, 5, 50, 500),
        Ena.PURPLE: (1, 3, 22, 105),
        Ena.YELLOW: (1,),
    }

    def __init__(self) -> None:
        self.enaBonus = {
            Ena.RED: defaultdict(int),
            Ena.BLUE: defaultdict(int),
            Ena.PURPLE: defaultdict(int),
            Ena.YELLOW: defaultdict(int),
        }

    def addBonus(self, ena: Ena, level: int, bonus: int):
        assert level >= 0 and level < len(self.enaValue[ena]), "level out of range"
        self.enaBonus[ena][level] += bonus

    def byEnaWithLevel(self, ena: Ena, gemLevel: int) -> int:
        return EnaValue.enaValue[ena][gemLevel] + self.enaBonus[ena][gemLevel]

    def clearBonus(self):
        for ena in Ena:
            self.enaBonus[ena].clear()
