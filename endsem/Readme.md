### CS561
### Artifical Intelligence Lab
### Indian Institute of Technology Patna
### 2021-22

# End Semester Assignment

## Amish Mittal
## 1801CS07

## Q1

### Sample Run 1 (Hill Climbing - Success case)

Test Case:

Start State:
|   |   |   |
| - | - | - |
| T1 | T2| B|
| T4 | T5 | T3| 
| T7 | T8| T6|

Goal State:
|   |   |   |
| - | - | - |
| T1 | T2| T3|
| T4 | T5 | T6| 
| T7 | T8| B|

```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
1
Consider blank tile as regular tile?
0
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Heuristic: Number of displaced tiles
Start State:
T1 T2 B
T4 T5 T3
T7 T8 T6
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored: 5
Total number of states to Sub-Optimal Path: 3
Optimal Path Cost: 2
Time taken: 0.0008704662322998047

T1 T2 B
T4 T5 T3
T7 T8 T6

   |
   |
   v

T1 T2 T3
T4 T5 B
T7 T8 T6

   |
   |
   v

T1 T2 T3
T4 T5 T6
T7 T8 B
```
```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
2
Consider blank tile as regular tile?
0
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Heuristic: Total Manhattan distance
Start State:
T1 T2 B
T4 T5 T3
T7 T8 T6
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored: 4
Total number of states to Sub-Optimal Path: 3
Optimal Path Cost: 2
Time taken: 0.0006840229034423828

T1 T2 B
T4 T5 T3
T7 T8 T6

   |
   |
   v

T1 T2 T3
T4 T5 B
T7 T8 T6

   |
   |
   v

T1 T2 T3
T4 T5 T6
T7 T8 B
```

### Sample Run 2 (Hill Climbing - Failure Case)

Test Case:

Start State:
|   |   |   |
| - | - | - |
| B | T2| T3|
| T1 | T4 | T5| 
| T6 | T7| T8|

Goal State:
|   |   |   |
| - | - | - |
| T1 | T2| T3|
| T4 | T5 | T6| 
| T7 | T8| B|

```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
2
Consider blank tile as regular tile?
0
Boo ! Unable to find a solution !
Heuristic: Total Manhattan distance
Start State:
B T2 T3
T1 T4 T5
T6 T7 T8
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored before termination: 9
```
```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
1
Consider blank tile as regular tile?
0
Boo ! Unable to find a solution !
Heuristic: Number of displaced tiles
Start State:
B T2 T3
T1 T4 T5
T6 T7 T8
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored before termination: 4
```

## Constraints to be checked: (Questions asked)
### 1. Check whether the heuristics are admissible.
`h1`: number of tiles displaced from their destined position.
`h1` is an admissible heuristic, since it is clear that every tile that is out of position must be moved at least once. Hence it would always be less than or equal to the optimal.

`h2`: sum of Manhattan distance of each tile from the goal position.
`h2` is an admissible heuristic, since in every move, one tile can only move closer to its goal by one step.

Whichever we are estimating is less than the actual final answer. Hence, both are admissible.

This can also be shown emperically via code as both the heiristics work perfectly when Simulated Annealing is used. We can't demonstrate it using Hill Climbing as it would get stuck in local minima. 

### 2. What happens if we make a new heuristics h3 (n)= h1 (n) + h2 (n).

No `h3(n)` is not admissible as h3 is sum of h1 & h2 and it can exceed both of them  in magnitude, so we can't be sure that it always underestimates the optimal cost.

Sample Outputs:
```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
3
Consider blank tile as regular tile?
0
Boo ! Unable to find a solution !
Zero heuristic
Start State:
T1 T2 B
T8 T5 T3
T7 T4 T6
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored before termination: 4
```
```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
3
Consider blank tile as regular tile?
0
Boo ! Unable to find a solution !
Zero heuristic
Start State:
T1 B T2
T8 T5 T3
T7 T4 T6
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored before termination: 6
```

__Example 3:__

Consider start and end states as:

Start state:

1 0 3

4 2 5 

7 8 6

End State:

1 2 3

4 5 6 

7 8 0

For the given case, h1(n) = 3 and h2(n) = 3
Hence, h3(n) = h1(n) + h2(n) = 6

But, the path from the start state to end state is as follows:
```
1 0 3       1 2 3       1 2 3       1 2 3
4 2 5  -->  4 0 5  -->  4 5 0  -->  4 5 6
7 8 6       7 8 6       7 8 6       7 8 0
```

Here, `h*(n) = 3`, which is less than `h3(n)`. 

Hence, `h3(n)` is not admissible and is not a correct heuristic.


### 3. What happens if you consider the blank tile as another tile?

__Example 1: We also show the same thing via our code for number of tiles displaced heuristic__

```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
1
Consider blank tile as regular tile?
1
Boo ! Unable to find a solution !
Heuristic: Number of displaced tiles
Start State:
T1 B T2
T8 T5 T3
T7 T4 T6
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored before termination: 6
```
__Example 2: We also show the same thing via our code for total manhattan distance heuristic__
```
python eight_puzzle.py ./input/start_state.txt input/end_state.txt
Using Hill Climbing Algorithm

1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h3(n) = h1(n) + h2(n) - Not admissible
4. h(n) = 0 Zero heuristic
Enter Hueristic type:
2
Consider blank tile as regular tile?
1
Boo ! Unable to find a solution !
Heuristic: Total Manhattan distance
Start State:
T1 B T2
T8 T5 T3
T7 T4 T6
Goal State:
T1 T2 T3
T4 T5 T6
T7 T8 B
Total number of states explored before termination: 7
```

__Example 3:__

in the pervious example taken, `h1(n) = 4` and `h2(n) = 6`. 
But we know that `h*(n) = 3`. 

Thus, if we consider blank tile as a regular tile, both `h1(n) `and `h2(n)` become non-admissible.

__Example 4:__

If we consider now swapping 2 tiles as our move instead of moving a tile to blank location then we can say that both heuristic are not admissible as see this case

Input state
```
1 2 3
4 5 6
7 8 9
```
Goal State
```
2 1 3
4 5 6
7 8 9
```
Here using both `h1` and `h2` our cost comes out to be 2, but in reality only 1 swap is required to reach the goal state( there `H <= H*` does not hold) Hence both are not admissible.

### 4. What if the search algorithm got stuck into Local optimum? Is there any way to get out of this?

Hill Climibing can get stuck at a local optimum and not proceed further as it just choses the best option at each iteration. In this case, it would never reach the total optimum. One quick seed is to run the algorithm again with different hyperparameters or seed, so that the algorithm makes different choices and we can hope that with these new hyperparameters and seed, it might converge to the global optimum solution. We can only guess and hope with this algorithm. Often, in practice we can run this algo multiple times with different hyperparameters and cherry pick the best solution obtained.

Other solution is to use better search algorithms such as Simulated Annealing. Simulated annealing can solve it by considering worse solutions also at the same time. It does so by assigning some probability to the worse solutions and that helps us to seperate from a greedy paradigm and allows us to move towards some local bad solutions to find the global best solution in infinite time.

### 5. What happens when all the neighbours of the current state have the same value? How to get rid of this situation?

When all the neighbours of the current state have the same value (heuristic), then in this case the hill climbing algorithm choses a random neighbour to continue the algorithm. In this case, we choose the first element of array after using a stable sorting method. 
This can also be avoided via code, by using a random seed with each possible path. 
i.e. the heuristic now becomes `h(n) -> h(n) + epsilon`. This would ensure that each neighbour now has a different value.


## Instructions to run the code

1. Install dependencies using `pip install -r requirements.txt` after creating a `conda` environment.

2. Enter the initial state and goal state in `/input/start_state.txt` and `/input/end_state.txt`.

3. Run:
```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
```


______________________
Thanking You!

Amish Mittal

1801CS07