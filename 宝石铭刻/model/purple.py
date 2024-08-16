from itertools import chain
import math
from model.base import _Card, Ena, Playground


class PurpleEna1(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Purple Ena 1",
            Ena.PURPLE,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts

        for x in range(enas[Ena.PURPLE].__len__()):
            playground.enaValue.addBonus(Ena.PURPLE, x, 5)
        if enas[Ena.PURPLE][0] == 0 or enas[Ena.YELLOW][0] == 0:
            return

        total = enas[Ena.PURPLE][0] + enas[Ena.YELLOW][0]
        enas[Ena.PURPLE][1] += math.ceil(total / 2)
        enas[Ena.PURPLE][0] = enas[Ena.YELLOW][0] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class PurpleEna2(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Purple Ena 2",
            Ena.PURPLE,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts

        for x in range(enas[Ena.PURPLE].__len__()):
            playground.enaValue.addBonus(Ena.PURPLE, x, 15)

        if enas[Ena.PURPLE][1] == 0 or enas[Ena.BLUE][1] == 0:
            return

        total = enas[Ena.PURPLE][1] + enas[Ena.BLUE][1]
        enas[Ena.PURPLE][2] += math.ceil(total / 2)
        enas[Ena.PURPLE][1] = enas[Ena.BLUE][1] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class PurpleEna3(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Purple Ena 3",
            Ena.PURPLE,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        playground.postfunction.append(PurpleEna3.postFunction)

        if enas[Ena.PURPLE][2] == 0 or enas[Ena.RED][3] == 0:
            return
        total = enas[Ena.PURPLE][2] + enas[Ena.RED][3]
        enas[Ena.PURPLE][3] += math.ceil(total / 2)
        enas[Ena.PURPLE][2] = enas[Ena.RED][3] = 0

    # @staticmethod ! it seems not necessary
    def postFunction(playground: Playground) -> int:
        enas = playground.enaCounts

        cnts = list(chain.from_iterable(enas.values()))
        if cnts.count(0) == len(cnts) - 1:
            playground.enaValue.addBonus(Ena.PURPLE, 3, 100)
        return 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}
