### CS561
### Artifical Intelligence Lab
### Indian Institute of Technology Patna
### 2021-22

# Assignment 2

## Team Details:

Team Code: `1801cs03_1801cs07_1801cs46`

Team Name: `MnMnM`

Team Members:

| Name              | Roll Number |
| ----------------- | ----------- |
| Abhishek Chopra   | 1801CS03    |
| Amish Mittal      | 1801CS07    |
| Shashwat Mahajan  | 1801CS46    |

## Q1

### Sample Run 1 (Hill Climbing - Success case)

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
| T2 | T4| T3|
| T1 | B | T5| 
| T6 | T7| T8|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Hill Climbing
2. Simulated Annealing 
1
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
1
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Start State:
B T2 T3 
T1 T4 T5 
T6 T7 T8 
Goal State:
T2 T4 T3 
T1 B T5 
T6 T7 T8 
Total number of states explored: 5
Total number of states to Sub-Optimal Path: 3
Optimal Path Cost: 2
Time taken: 0.002745389938354492

B T2 T3 
T1 T4 T5 
T6 T7 T8 

   |		
   |		
   v		
				
T2 B T3 
T1 T4 T5 
T6 T7 T8 

   |		
   |		
   v		
				
T2 T4 T3 
T1 B T5 
T6 T7 T8 
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
| T4 | T5 | T8| 
| T6 | T7| B|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Hill Climbing
2. Simulated Annealing 
1
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
1
Boo ! Unable to find a solution !
Start State:
B T2 T3 
T1 T4 T5 
T6 T7 T8 
Goal State:
T1 T2 T3 
T4 T5 T8 
T6 T7 B 
Total number of states explored before termination: 4
```


### Sample Run 3 (Simulated Annealing - Success case)

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
| T4 | T5 | T8| 
| T6 | T7| B|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Hill Climbing
2. Simulated Annealing 
2
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
2
Enter the max temperature: 100
1. Exponential decay
2. Linear decay
3. Logarithmic decay
2
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Start State:
B T2 T3 
T1 T4 T5 
T6 T7 T8 
Goal State:
T1 T2 T3 
T4 T5 T8 
T6 T7 B 
Total number of states explored: 5
Total number of states to Sub-Optimal Path: 5
Optimal Path Cost: 4
Time taken: 0.006196498870849609

B T2 T3 
T1 T4 T5 
T6 T7 T8 

   |		
   |		
   v		
				
T1 T2 T3 
B T4 T5 
T6 T7 T8 

   |		
   |		
   v		
				
T1 T2 T3 
T4 B T5 
T6 T7 T8 

   |		
   |		
   v		
				
T1 T2 T3 
T4 T5 B 
T6 T7 T8 

   |		
   |		
   v		
				
T1 T2 T3 
T4 T5 T8 
T6 T7 B 
```

### Sample Run 4 (Simulated Annealing - Success case)

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
| T2 | T4| T3|
| T1 | B | T5| 
| T6 | T7| T8|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Hill Climbing
2. Simulated Annealing 
2
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
2
Enter the max temperature: 35
1. Exponential decay
2. Linear decay
3. Logarithmic decay
3
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Start State:
B T2 T3 
T1 T4 T5 
T6 T7 T8 
Goal State:
T2 T4 T3 
T1 B T5 
T6 T7 T8 
Total number of states explored: 3
Total number of states to Sub-Optimal Path: 3
Optimal Path Cost: 2
Time taken: 0.0029616355895996094

B T2 T3 
T1 T4 T5 
T6 T7 T8 

   |		
   |		
   v		
				
T2 B T3 
T1 T4 T5 
T6 T7 T8 

   |		
   |		
   v		
				
T2 T4 T3 
T1 B T5 
T6 T7 T8
```


## Notes (Questions asked)
### 1. Check whether the heuristics are admissible.
`h1`: number of tiles displaced from their destined position.
`h1` is an admissible heuristic, since it is clear that every tile that is out of position must be moved at least once.

`h2`: sum of Manhattan distance of each tile from the goal position.
`h2` is an admissible heuristic, since in every move, one tile can only move closer to its goal by one step.

Whichever we are estimating is less than the actual final answer. Hence, both are admissible.

### 2. What happens if we make a new heuristics h3 (n)= h1 (n) * h2 (n).
No `h3(n)` is not admissible as h3 is product of h1 & h2 and it can exceed both of them  in magnitude, so we cant be sure that it always underestimates the optimal cost.

### 3. What happens if you consider the blank tile as another tile?
If we consider now swapping 2 tiles as our move instead of moving a tile to blank location then we can say that both heuristic are not admissible as see this case

Input state

1 2 3

4 5 6

7 8 9

Goal State

2 1 3

4 5 6

7 8 9

Here using both `h1` and `h2` our cost comes out to be 2, but in reality only 1 swap is required to reach the goal state( there H <= H* does not hold) Hence both are not admissible.

### 4. What if the search algorithm got stuck into Local optimum? Is there any way to get out of this
Hill CLimibing can get stuck at a local optimum, but Simulated Annealing can't.  Simulated annealing solves it by considering worse solutions also at the same time. It does so by assigning some probability to the worse solutions and that helps us to seperate from a greedy paradigm and allows us to move towards some local bad solutions to find the global best solution.


## Instructions to run the code

1. Install dependencies using `pip install -r requirements.txt` after creating a `conda` environment.

2. Enter the initial state and goal state in `/input/start_state.txt` and `/input/end_state.txt`.

3. Run:
```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
```


______________________
Thanking You!

MnMnM