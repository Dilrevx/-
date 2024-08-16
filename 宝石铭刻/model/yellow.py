from model.base import _Card, Ena, Playground


class YellowEna1(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Yellow Ena 1",
            Ena.YELLOW,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        playground.enaCounts[Ena.YELLOW][0] *= 5

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class YellowEna2(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Yellow Ena 2",
            Ena.YELLOW,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        playground.enaCounts[Ena.YELLOW][0] *= 8

    manufacturesByLevel = {3: manufactureLevel3.__func__}


class YellowEna3(_Card):

    def __init__(self, upgradeLevel=3):
        super().__init__(
            "Yellow Ena 3",
            Ena.YELLOW,
            upgradeLevel=upgradeLevel,
        )

    @staticmethod
    def manufactureLevel3(playground: Playground) -> None:
        playground.enaCounts[Ena.YELLOW][0] *= 9
        playground.enaValue.addBonus(Ena.YELLOW, 0, 1)

    manufacturesByLevel = {3: manufactureLevel3.__func__}
