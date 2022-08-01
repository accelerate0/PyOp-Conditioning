

# PyOp-Conditioning

Contains many features of operant conditioning modules coded in Python for uses in generating timers and contingency trigger as well as for integration in automated systems such as TDT Pynapse.

## Runtime

 - Two files are available to run:
	 - `pyopcond_standalone.py` is the standalone program with verbose output printing.
	 - `pyopcond_dep.py` is for usages in other programs such as TDT Pynapse runtime environment where the script can be imported and the output variables used.
 - The output is all in an array fashion via Python LIST format.

## Dependencies
- Python 3 is required, as well as the math, random, and numpy Python modules
- This is a dependency for Dr Chandler's Lab Program Scripts.  [Repo Link](https://github.com/accelerate0/Chandler-Lab-Program)

## Usages & Features
- All user inputs should be numeric values only.

| Reinforcement | Command Usage | Parameters | Output Variable | Description
|--|--|--|--|--|
| Variable Interval (VI) Scheduling | `var_int(N, m)` | `N` is the amount of intervals and `m` is the mean VI schedule time. | `var_int.output_random` randomizes the array while `var_int.output_straight`gives the array a sequential order, both given in sec. | Reinforcement is provided after a random (unpredictable) amount of time has passes and following a specific behavior being performed based on the Hoffman-Fleshler Constant Probability Distribution. This is the same as `INITCONSTPROBARR` found in Med Associate program. |
| Random Interval (RI) Scheduling | `rand_int(interval, amount)` or `rand_int_withpi(interval, amount)`| `interval` is the length of each interval (sec) while `amount` is the amount of total intervals acting as a multiplier. | `rand_int.output` or `rand_int_withpi.output` as a array in sec. | Reinforcement arrangement in which the first response after an interval is reinforced, the duration of the intervals varies randomly from reinforcement to reinforcement, and a fixed probability of reinforcement over time is used to reinforce a response. Use `rand_int_withpi` when replicating Med Associates RI Scheduling. |
| Variable Ratio (VR) Scheduling | `var_ratio(amount, min, max)` | `amount` is the total amount of reward, `min` is the minimum probability range for inputs before a reward is given while `max` is the maximum range of inputs for probability before a reward is given. Units are in inputs ie lever presses. | `var_ratio.output` where it is given in subject response inputs ie lever presses before reward trigger. | Scheduling of reinforcement where a behavior is reinforced after a random number of responses. |
| Random Ratio (RR) Scheduling | `rand_ratio(mean, amount)` | `mean` is the mean ratio value while `amount` is the amount of response inputs, or "amount of mean instances". | `rand_int.output` given in responses ie lever presses  before a reward is triggered. | Scheduling in which the number of responses required for each reinforcement varies randomly from reinforcement to reinforcement. |

## TDT Pynapse Integration

**Installing The Script:**
 - Download or copy paste the script into a file.
 - Save this file preferably in the Python directory in the TDT software folder.
	 - The directory path should look like `C:\TDT\python-3.7.9\Scripts`
	 - Make sure it is saved with the `.py` file extension.
 - Open the Synapse software.
 - Go into the Pynapse module and right click anywhere inside the `Code Tree:` block.
 - Click `Add Python Import File`
 - A directory explorer should pop up, navigate to the directory where the script is and select it.
 - Now you should see an additional python file module pop up in the `Code Tree:` block as well as the pynapse script.

 **Example Usage of The Script:**

 Using the Variable Interval function of PyOp:

 *Pynapse Input:*
 ![Input](https://i.gyazo.com/083deb95f416b407991f51adf8050662.png)

*Synapse Console Output:* Chose 7 as the random number integer
![Output](https://i.gyazo.com/daf15be35399eb25278872b3fbee8e09.png)
