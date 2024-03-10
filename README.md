# Multiobjective Optimization

## Set-up
```shell
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Description of the Portfolio Game

Participating in the Portfolio Game can give you an opportunity **to skip the Test (lectures)**. The rules are simple.

1. The game is founded on the basic Markowitz's model from 1952.
2. You start with 100 PLN ( fictitious 😊 )
3. There are 20 assets, and the historical data on their prices is provided (Bundle1.zip).
4. The game consists of three rounds.
5. Consider round no. 1. The data for T ∈ [−1,0] is known (see the first illustration).
   Regarding datasets, T = −1 corresponds to the zeroeth (counting from zero) data point, while T = 0 to the 100th.
   Your task is to predict prices for T = +1 (200th data point) and approximate the problem's Pareto front.
   Then, you have to select one solution that is the most relevant to your preferences.
   Then, send me a brief report that includes info on your **predictions**, **constructed Pareto front (visualizations)**, **the selected solution, and the justification of such a selection (refer to your predictions on prices)**.
   The result **must be sent before the deadline** and in the proper format (the deadlines are listed on the eKursy system; If you **miss** the **deadline**, you are **excluded** from the game!).
   After the deadline passes, I will reveal the data for T ∈ (0,+1] (100th-200th data points) and update your fictitious cash according to the true assets' prices.

![](repo_images/stock_example.png)

6. The game continues for the next two rounds in a similar fashion (predictions for T = +2 and +3).
   Every time one step is done, I will upload the next bundle file.
7. Note that the weights **must sum to 1**. That is, it is assumed that every time you **resell all** your shares.
8. **Important: For every round**: Apart from a brief report (pdf) send a \*.txt file describing your solution, which will allow me to automatize the process of updating your cash.
   The file should have the following form:
    1. **Filename**: StudentID1\_StudentID2.txt (or StudentID.txt in the case of working alone).
    2. There should be exactly one line consisting of several fields separated by spaces (use dots, not commas, for separating integers from fractions):
        1. FIELD\_1 = expected total return
        1. FIELD\_2 = expected total risk
        1. FIELDS\_3–22 should be the weights

**Example**: 124.53 74.11 0.23 0.11 0.02 …. (and so on)

**IMPORTANT NOTE**: the weights should be provided in the following order of assets:

|1 |SuperFuture |
| - | - |
|2 |Apples |
|3 |WorldNow |
|4 |Electronics123 |
|5 |Photons |
|6 |SpaceNow |
|7 |PearPear |
|8 |PositiveCorrelation |
|9 |BetterTechnology |
|10 |ABCDE |
|11 |EnviroLike |
|12 |Moneymakers |
|13 |Fuel4 |
|14 |MarsProject |
|15 |CPU-XYZ |
|16 |RoboticsX |
|17 |Lasers |
|18 |WaterForce |
|19 |SafeAndCare |
|20 |BetterTomorrow |

9. **Grading:**
    1. If, in the end, you have less than 100 PLN, you can have 3.0 for the lecture.
    2. Otherwise, you may treat your grade attained during laboratories as your final grade for the lecture.

10. **Important**: In your reports, you have to justify your decisions.
    That is, you cannot send random weight vectors hoping to avoid the Test 😊 
