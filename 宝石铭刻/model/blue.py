import math
from model.base import _Card, Ena, Playground


class BlueEna1(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Blue Ena 1",
            Ena.BLUE,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        enas[Ena.BLUE][1] += enas[Ena.BLUE][0]
        enas[Ena.YELLOW][0] += enas[Ena.BLUE][1]
        enas[Ena.BLUE][0] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class BlueEna2(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Blue Ena 2",
            Ena.BLUE,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        total = enas[Ena.BLUE][1]
        enas[Ena.BLUE][2] += math.ceil(total * 4 / 5)
        enas[Ena.YELLOW][0] += math.floor(total * 1 / 5) + enas[Ena.BLUE][2] * 2
        enas[Ena.BLUE][1] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class BlueEna3(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Blue Ena 3",
            Ena.BLUE,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        total = enas[Ena.BLUE][2]
        enas[Ena.BLUE][3] += math.ceil(total * 7 / 10)
        enas[Ena.YELLOW][0] += math.floor(total * 3 / 10) + enas[Ena.BLUE][3] * 2
        enas[Ena.BLUE][2] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}
