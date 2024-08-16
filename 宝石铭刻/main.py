from collections import Counter, defaultdict
from enum import Enum
import itertools
from typing import Dict, List, Tuple, Callable

from model.base import MAX_DESK_SIZE, TOTAL_ENA, _Card, Ena, Playground, EnaValue
from model.red import FireEna1, FireEna2, FireEna3, FireEna4
from model.purple import PurpleEna1, PurpleEna2, PurpleEna3
from model.blue import BlueEna1, BlueEna2, BlueEna3
from model.yellow import YellowEna1, YellowEna2, YellowEna3


class ManufactureEngine:
    def __init__(self, allCards: List[_Card], deskSize: int) -> None:
        self.playground = Playground(deskSize=deskSize)
        self.allCards = allCards
        self.backgroundCards = [card for card in allCards if card.background]
        self.nonBackgroundCards = [card for card in allCards if not card.background]

    def setInitialEnas(self, _enas: Dict[Ena, int]):
        assert sum(_enas.values()) == TOTAL_ENA

        enas = self.playground.enaCounts
        for ena, value in _enas.items():
            enas[ena][0] = value

    def setCards(self, cards: List[_Card]):
        assert len(cards) <= self.playground.deskSize

        self.playground.cards = cards

    def manufacture(self) -> Playground:
        for card in self.backgroundCards:
            card.manufacture(self.playground)

        for card in self.playground.cards:
            if card.background:
                continue
            card.manufacture(self.playground)

        return self.playground.enaCounts

    def calculateEnaValue(self) -> int:
        enaCounts = self.playground.enaCounts
        enaValues = self.playground.enaValue

        ret = 0
        for func in self.playground.postfunction:
            ret += func(self.playground)

        for ena, levelCounts in enaCounts.items():
            leveledValues = [
                enaValues.byEnaWithLevel(ena, level) * count
                for level, count in enumerate(levelCounts)
            ]

            ret += sum(leveledValues)
        return ret


def print_result(result: Tuple[int, List[_Card]]):
    if isinstance(result, list):
        for r in result:
            print_result(r)
        return
    print(f"Value: {result[0]}")
    print("Cards:")

    for card in result[1]:
        print(card.name)


if __name__ == "__main__":
    allCards = [
        FireEna1(),
        FireEna2(),
        FireEna3(),
        FireEna4(),
        PurpleEna1(),
        PurpleEna2(),
        PurpleEna3(),
        BlueEna1(),
        BlueEna2(),
        BlueEna3(),
        YellowEna1(),
        YellowEna2(),
        YellowEna3(),
    ]
    engine = ManufactureEngine(deskSize=MAX_DESK_SIZE, allCards=allCards)

    perms = itertools.permutations(
        engine.nonBackgroundCards, engine.playground.deskSize
    )

    results = []
    for perm in perms:
        engine.playground.clear()
        engine.setCards(list(perm))

        engine.setInitialEnas(
            {
                Ena.PURPLE: 24,
                Ena.YELLOW: 22,
                Ena.RED: 24,
                Ena.BLUE: 30,
            }
            # {
            #     Ena.PURPLE: 10,
            #     Ena.YELLOW: 10,
            #     Ena.RED: 70,
            #     Ena.BLUE: 10,
            # }
        )

        engine.manufacture()

        value = engine.calculateEnaValue()
        results.append((value, perm))

    results.sort(key=lambda x: x[0], reverse=True)
    print(len(results))

    tmp = [results[0]]
    for r in results:
        if r[0] != tmp[-1][0]:
            tmp.append(r)
    print_result(tmp[:20])
