import math
from model.base import _Card, Ena, Playground


class FireEna1(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Fire Ena 1",
            Ena.RED,
            upgradeLevel=upgradeLevel,
            isBackground=upgradeLevel == 3,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        enas[Ena.RED][1] += enas[Ena.RED][0] * 2
        enas[Ena.RED][0] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class FireEna2(_Card):
    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Fire Ena 2",
            Ena.RED,
            upgradeLevel=upgradeLevel,
            isBackground=upgradeLevel == 3,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        enas[Ena.RED][2] += enas[Ena.RED][1] * 2
        enas[Ena.RED][1] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class FireEna3(_Card):
    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Fire Ena 3",
            Ena.RED,
            upgradeLevel=upgradeLevel,
            isBackground=upgradeLevel == 3,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        enas[Ena.RED][3] += math.ceil(enas[Ena.RED][2] * 2.4)
        enas[Ena.RED][2] = 0

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class FireEna4(_Card):
    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Fire Ena 4",
            Ena.RED,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        enas = playground.enaCounts
        enas[Ena.RED][4] += enas[Ena.RED][3]
        enas[Ena.RED][3] = 0

        playground.postfunction.append(
            lambda playground: (playground.deskSize - len(playground.cards)) * 5000
        )

    manufacturesByLevel = {3: manufactureLevel3.__func__}
