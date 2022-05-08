# Iterated Prisoner's Dilemma

The iterated prisoner's dilemma is an extension of the general form except the game is repeatedly played by the same participants. An iterated prisoner's dilemma differs from the original concept of a prisoner's dilemma because participants can learn about the behavioral tendencies of their counterparty.

The theory behind the game has captivated many scholars over the years. More recently, organizational design researchers have used the game to model corporate strategies. The prisoner's dilemma is also now commonplace for game theories becoming popular with investment strategist. Globalization and integrated trade have further driven demand for financial and operational models that can describe geopolitical issues. 

The game is played iteratively for a number of rounds until it is ended (as if you are repeatedly interrogated for separate crimes). The scores from each round are accumulated, so the object is to optimize the point score before reaching game over. Game over is determined randomly anywhere between 1 and 100 rounds. At the end of the game, the scores are translated into percentages of the best possible scores. 

More information: https://www.investopedia.com/terms/i/iterated-prisoners-dilemma.asp

## Angry gradual

I have implemented a classical prisoner's dilemma with the following strategies: Randon, AlwaysCooperate, AlwaysDefect, TitForTat, Mistrust, Spiteful, PerCD, PerCCD, PerDDC, SoftMajo, HardMajo, Pavlov, Tf2t, HardTft, SlowTft, Gradual, Prober, Mem2. More about these strategies: https://hal.inria.fr/hal-01635333/document. These strategies than play a round robin tournament 20 times to determine their scores. Scores determine how many strategies will go to the next iteration(hence iterated prisoner's dilemma). The game is played until strategies reach an equilibrium. Some strategies will die out and some will stay at the fixed number of points.

I have come up with an upgrade to one of the winning basic strategies: Gradual. Gradual ooperates on the first move, then defect n times afer nth defections of its opponent, and calms down with 2 cooperations.

I have found out that gradual is optimal at the first iterations when there are more strategies present that tend to defect. But when game progresses and there are more cooperative strategies it should punish more harshly. So to calculate hom many times to defect before calming down we use the following formula: floor(n*(1+n*(angryCoefficient))). Angry coefficient tells us how much to increase the number of defections. I found the optimal value to be 0.75.

Behaviour of strategies:
![alt text](https://github.com/zmazk123/iterated-prisoner-s-dilemma/blob/main/program.png "Program")
