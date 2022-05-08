from abc import ABC, abstractmethod
import random
import math

# 0 - first move
# 1 - cooperate
# 2 - defect

class Strategy(ABC):
    def __init__(self):
        self.opponentMoves = [0]
        self.myMoves = [0]
        self.scores = []

    @abstractmethod
    def play(self):
        raise NotImplementedError('subclasses must override play()!')

    def setMoves(self, opponentMove, myMove):
        self.opponentMoves.append(opponentMove)
        self.myMoves.append(myMove)

    def reset(self):
        self.opponentMoves = [0]
        self.myMoves = [0]

    def addScore(self, score):
        self.scores.append(score)

    def getAverageScore(self):
        return sum(self.scores) / len(self.scores)

class Rand(Strategy):
    def play(self):
        return random.randint(1, 2)

class AlwaysCooperate(Strategy):
    def play(self):
        return 1

class AlwaysDefect(Strategy):
    def play(self):
        return 2

class TitForTat(Strategy):
    def play(self):
        lastOpponentsMove = self.opponentMoves[len(self.opponentMoves)-1]
        if lastOpponentsMove == 0:
            return 1

        if lastOpponentsMove == 1:
            return 1

        if lastOpponentsMove == 2:
            return 2

class Mistrust(Strategy):
    def play(self):
        lastOpponentsMove = self.opponentMoves[len(self.opponentMoves)-1]
        if lastOpponentsMove == 0:
            return 2

        if lastOpponentsMove == 1:
            return 1

        if lastOpponentsMove == 2:
            return 2

class Spiteful(Strategy):
    def __init__(self):
        super().__init__()
        self.grudge = False

    def play(self):
        if self.grudge == False:
            return 1

        else:
            return 2

    def setMoves(self, opponentMove, myMove):
        super().setMoves(opponentMove, myMove)
        if opponentMove == 2:
            self.grudge = True

    def reset(self):
        super().reset()
        self.grudge = False

class PerCD(Strategy):
    def play(self):
        lastMyMove = self.myMoves[len(self.myMoves)-1]
        if lastMyMove == 0:
            return 1

        if lastMyMove == 1:
            return 2

        if lastMyMove == 2:
            return 1

class PerCCD(Strategy):
    def play(self):
        if len(self.myMoves) < 3:
            return 1

        else:
            if self.myMoves[len(self.myMoves)-1] == 1 and self.myMoves[len(self.myMoves)-2] == 1:
                return 2
            else:
                return 1

class PerDDC(Strategy):
    def play(self):
        if len(self.myMoves) < 3:
            return 2

        else:
            if self.myMoves[len(self.myMoves)-1] == 2 and self.myMoves[len(self.myMoves)-2] == 2:
                return 1
            else:
                return 2

class SoftMajo(Strategy):
    def play(self):
        if len(self.opponentMoves) == 1:
            return 1

        else:
            if self.opponentMoves.count(1) >= self.opponentMoves.count(2):
                return 1
            else:
                return 2

class HardMajo(Strategy):
    def play(self):
        if len(self.opponentMoves) == 1:
            return 2

        else:
            if self.opponentMoves.count(2) >= self.opponentMoves.count(1):
                return 2
            else:
                return 1

class Pavlov(Strategy):
    def play(self):
        if len(self.opponentMoves) == 1:
            return 1

        else:
            if self.opponentMoves[len(self.opponentMoves)-1] == self.myMoves[len(self.myMoves)-1]:
                return 1
            else:
                return 2

class Tf2t(Strategy):
    def play(self):
        if len(self.opponentMoves) <= 2:
            return 1

        else:
            if self.opponentMoves[len(self.opponentMoves)-1] == 2 and self.opponentMoves[len(self.opponentMoves)-2] == 2:
                return 2
            else:
                return 1

class HardTft(Strategy):
    def play(self):
        if len(self.opponentMoves) <= 2:
            return 1

        else:
            if self.opponentMoves[len(self.opponentMoves)-1] == 2 or self.opponentMoves[len(self.opponentMoves)-2] == 2:
                return 2
            else:
                return 1

class SlowTft(Strategy):
    def __init__(self):
        super().__init__()
        self.grudge = False

    def play(self):
        if len(self.opponentMoves) <= 2:
            return 1

        else:
            if self.opponentMoves[len(self.opponentMoves)-1] == 2 and self.opponentMoves[len(self.opponentMoves)-2] == 2:
                self.grudge = True

            if self.opponentMoves[len(self.opponentMoves)-1] == 1 and self.opponentMoves[len(self.opponentMoves)-2] == 1:
                self.grudge = False

        if self.grudge == False:
            return 1
        else:
            return 2

    def reset(self):
        super().reset()
        self.grudge = False

class Gradual(Strategy):
    def __init__(self):
        super().__init__()
        self.counter = -2

    def play(self):
        if len(self.opponentMoves) == 1:
            return 1

        if self.counter != -2:
            if self.counter > 0:
                self.counter = self.counter - 1
                return 2

            if self.counter > -2:
                self.counter = self.counter - 1
                return 1

        else:
            if self.opponentMoves[len(self.opponentMoves)-1] == 2:
                self.counter = -2
                self.counter = self.counter + self.opponentMoves.count(2) + 1
                return 2

            else:
                return 1

    def reset(self):
        super().reset()
        self.counter = -2

class Prober(Strategy):
    def play(self):
        if len(self.opponentMoves) == 1:
            return 2

        if len(self.opponentMoves) == 2:
            return 1

        if len(self.opponentMoves) == 3:
            return 1

        else:
            if self.opponentMoves[2] == 1 and self.opponentMoves[3] == 1:
                return 2
            else:
                lastOpponentsMove = self.opponentMoves[len(self.opponentMoves)-1]
                if lastOpponentsMove == 0:
                    return 1

                if lastOpponentsMove == 1:
                    return 1

                if lastOpponentsMove == 2:
                    return 2

class Mem2(Strategy):
    def __init__(self):
        super().__init__()
        self.moveCounter = 0
        self.strategy = ''
        self.alldCounter = 0

    def play(self):
        if len(self.opponentMoves) <= 2:
            lastOpponentsMove = self.opponentMoves[len(self.opponentMoves)-1]
            if lastOpponentsMove == 0:
                return 1

            if lastOpponentsMove == 1:
                return 1

            if lastOpponentsMove == 2:
                return 2

        if self.alldCounter == 2:
            return 2

        else:
            if self.moveCounter == 0:
                if self.opponentMoves[len(self.opponentMoves)-1] == 1 and self.myMoves[len(self.myMoves)-1] == 1 and self.opponentMoves[len(self.opponentMoves)-2] == 1 and self.myMoves[len(self.myMoves)-2] == 1:
                    self.strategy = 'TFT'
                    self.moveCounter = 2

                elif (self.opponentMoves[len(self.opponentMoves)-1] == 1 and self.myMoves[len(self.myMoves)-1] == 2) or (self.opponentMoves[len(self.opponentMoves)-1] == 2 and self.myMoves[len(self.myMoves)-1] == 1):
                    self.strategy = 'TF2T'
                    self.moveCounter = 2

                else:
                    self.strategy = 'ALLD'
                    self.moveCounter = 2
                    self.alldCounter = self.alldCounter + 1

            if self.strategy == 'TFT':
                lastOpponentsMove = self.opponentMoves[len(self.opponentMoves)-1]
                if lastOpponentsMove == 0:
                    self.moveCounter = self.moveCounter - 1
                    return 1

                if lastOpponentsMove == 1:
                    self.moveCounter = self.moveCounter - 1
                    return 1

                if lastOpponentsMove == 2:
                    self.moveCounter = self.moveCounter - 1
                    return 2

            if self.strategy == 'TF2T':
                if self.opponentMoves[len(self.opponentMoves)-1] == 2 and self.opponentMoves[len(self.opponentMoves)-2] == 2:
                    self.moveCounter = self.moveCounter - 1
                    return 2
                else:
                    self.moveCounter = self.moveCounter - 1
                    return 1

            if self.strategy == 'ALLD':
                self.moveCounter = self.moveCounter - 1
                return 2


    def reset(self):
        super().reset()
        self.moveCounter = 0
        self.strategy = ''
        self.alldCounter = 0

class AngryGradual(Strategy):
    def __init__(self):
        super().__init__()
        self.counter = -2

    def play(self):
        if len(self.opponentMoves) == 1:
            return 1

        if self.counter != -2:
            if self.counter > 0:
                self.counter = self.counter - 1
                return 2

            if self.counter > -2:
                self.counter = self.counter - 1
                return 1

        else:
            if self.opponentMoves[len(self.opponentMoves)-1] == 2:
                self.counter = -2
                self.counter = self.counter + math.floor(self.opponentMoves.count(2)*(1 + self.opponentMoves.count(2)*0.75)) + 1#best: 0.75 -> possible to test further
                return 2

            else:
                return 1

    def reset(self):
        super().reset()
        self.counter = -2

def match(strategyOne, strategyTwo):
    strategyOneScore = 0
    strategyTwoScore = 0

    for i in range(0,20):
        strategyOneResult = strategyOne.play()
        strategyTwoResult = strategyTwo.play()

        if strategyOneResult == 1 and strategyTwoResult == 1:
            strategyOneScore = strategyOneScore + 3
            strategyTwoScore = strategyTwoScore + 3

        if strategyOneResult == 2 and strategyTwoResult == 1:
            strategyOneScore = strategyOneScore + 5
            strategyTwoScore = strategyTwoScore + 0

        if strategyOneResult == 1 and strategyTwoResult == 2:
            strategyOneScore = strategyOneScore + 0
            strategyTwoScore = strategyTwoScore + 5

        if strategyOneResult == 2 and strategyTwoResult == 2:
            strategyOneScore = strategyOneScore + 1
            strategyTwoScore = strategyTwoScore + 1

        strategyOne.setMoves(strategyTwoResult, strategyOneResult)
        strategyTwo.setMoves(strategyOneResult, strategyTwoResult)

    strategyOne.reset()
    strategyTwo.reset()

    strategyOne.addScore(strategyOneScore)
    strategyTwo.addScore(strategyTwoScore)

strategies = []

for i in range(0,20):
    rand = Rand()
    alwaysCooperate = AlwaysCooperate()
    alwaysDefect = AlwaysDefect()
    titForTat = TitForTat()
    mistrust = Mistrust()
    spiteful = Spiteful()
    perCD = PerCD()
    perCCD = PerCCD()
    perDDC = PerDDC()
    softMajo = SoftMajo()
    hardMajo = HardMajo()
    pavlov = Pavlov()
    tft2 = Tf2t()
    hardTft = HardTft()
    slowTft = SlowTft()
    gradual = Gradual()
    prober = Prober()
    mem2 = Mem2()
    angryGradual = AngryGradual()

    strategies.append(rand)
    strategies.append(alwaysCooperate)
    strategies.append(alwaysDefect)
    strategies.append(titForTat)
    strategies.append(mistrust)
    strategies.append(spiteful)
    strategies.append(perCD)
    strategies.append(perCCD)
    strategies.append(perDDC)
    strategies.append(softMajo)
    strategies.append(hardMajo)
    strategies.append(pavlov)
    strategies.append(tft2)
    strategies.append(hardTft)
    strategies.append(slowTft)
    strategies.append(gradual)
    strategies.append(prober)
    strategies.append(mem2)
    strategies.append(angryGradual)

strategiesSum = len(strategies)

for i in range(0, 50):
    for strategyOne in strategies:
        for strategyTwo in strategies:
            match(strategyOne, strategyTwo)

    scores = {
        "Rand": [],
        "AlwaysCooperate": [],
        "AlwaysDefect": [],
        "TitForTat": [],
        "Mistrust": [],
        "Spiteful": [],
        "PerCD": [],
        "PerCCD": [],
        "PerDDC": [],
        "SoftMajo": [],
        "HardMajo": [],
        "Pavlov": [],
        "Tf2t": [],
        "HardTft": [],
        "SlowTft": [],
        "Gradual": [],
        "Prober": [],
        "Mem2": [],
        "AngryGradual": [],
    }

    for strategy in strategies:
        scores[strategy.__class__.__name__] = scores[strategy.__class__.__name__] + strategy.scores

    scoresSum = 0
    for name, score in scores.items():
        scores[name] = sum(score)
        scoresSum = scoresSum + scores[name]

    for name, score in scores.items():
        scores[name] = (scores[name]/scoresSum)*strategiesSum

    cumul = 0
    cumulRounded = 0
    for name, score in scores.items():
        prevCumul = cumulRounded
        cumul = cumul + scores[name]
        cumulRounded = int(round(cumul, 0))
        scores[name] = cumulRounded - prevCumul

    strategies = []
    for name, score in scores.items():
        for i in range(0,scores[name]):
            strat = eval(name)()
            strategies.append(strat)

    print(scores)
