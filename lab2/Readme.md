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

### Sample Run 1 (Success case)

Test Case:

Start State:
|   |   |   |
| - | - | - |
| T2 | T8| T3|
| T1 | B | T4| 
| T7 | T6| T5|

Goal State:
|   |   |   |
| - | - | - |
| T1 | T2| T3|
| T8 | B | T4| 
| T7 | T6| T5|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Best First Search
2. A * 
1
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
2
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Start State:
T2 T8 T3 
T1 B T4 
T7 T6 T5 
Goal State:
T1 T2 T3 
T8 B T4 
T7 T6 T5 
Total number of states explored: 10
Total number of states to Optimal Path: 5
Optimal Path Cost: 4
Time taken: 0.00284576416015625

T2 T8 T3 
T1 B T4 
T7 T6 T5 

   |
   |
   v

T2 B T3 
T1 T8 T4 
T7 T6 T5 

   |
   |
   v

B T2 T3 
T1 T8 T4 
T7 T6 T5 

   |
   |
   v

T1 T2 T3 
B T8 T4 
T7 T6 T5 

   |
   |
   v

T1 T2 T3 
T8 B T4 
T7 T6 T5
```

### Sample Run 2 (Failure Case)

Test Case:

Start State:
|   |   |   |
| - | - | - |
| T2 | T8| T3|
| T1 | B | T5| 
| T7 | T6| T4|

Goal State:
|   |   |   |
| - | - | - |
| T1 | T2| T3|
| T8 | B | T4| 
| T7 | T6| T5|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Best First Search
2. A * 
2
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
1
Boo ! Unable to find a solution !
Start State:
T2 T8 T3 
T1 B T5 
T7 T6 T4 
Goal State:
T1 T2 T3 
T8 B T4 
T7 T6 T5 
Total number of states explored before termination: 181440
```
```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Best First Search
2. A * 
2
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
2
Boo ! Unable to find a solution !
Start State:
T2 T8 T3 
T1 B T5 
T7 T6 T4 
Goal State:
T1 T2 T3 
T8 B T4 
T7 T6 T5 
Total number of states explored before termination: 181440
```

### Sample Run 3 (Success case)

Test Case:

Start State:
|   |   |   |
| - | - | - |
| T8 | T7| T6|
| T1 | B | T5| 
| T2 | T3| T4|

Goal State:
|   |   |   |
| - | - | - |
| T1 | T2| T3|
| T8 | B | T4| 
| T7 | T6| T5|

```
python eight_puzzle.py input/start_state.txt input/end_state.txt 
Enter Search Algorithm type:
1. Best First Search
2. A * 
2
Enter Hueristic type:
1. h1(n) = number of tiles displaced from their destined position.
2. h2(n) = sum of Manhattan distance of each tile from the goal
3. h(n) = 0 Zero heuristic
1
Voila ! Found a solution to the puzzle ! Gretings from MnMnM !
Start State:
T8 T7 T6 
T1 B T5 
T2 T3 T4 
Goal State:
T1 T2 T3 
T8 B T4 
T7 T6 T5 
Total number of states explored: 108984
Total number of states to Optimal Path: 29
Optimal Path Cost: 28
Time taken: 13.253159284591675

T8 T7 T6 
T1 B T5 
T2 T3 T4 

   |
   |
   v

T8 T7 T6 
T1 T3 T5 
T2 B T4 

   |
   |
   v

T8 T7 T6 
T1 T3 T5 
B T2 T4 

   |
   |
   v

T8 T7 T6 
B T3 T5 
T1 T2 T4 

   |
   |
   v

T8 T7 T6 
T3 B T5 
T1 T2 T4 

   |
   |
   v

T8 T7 T6 
T3 T5 B 
T1 T2 T4 

   |
   |
   v

T8 T7 T6 
T3 T5 T4 
T1 T2 B 

   |
   |
   v

T8 T7 T6 
T3 T5 T4 
T1 B T2 

   |
   |
   v

T8 T7 T6 
T3 B T4 
T1 T5 T2 

   |
   |
   v

Output trimmed for clear documentation purposes
```


## Q3
### `BFS` vs `A*` search
Both Greedy BFS and A* are Best first searches but Greedy BFS is neither complete, nor optimal whereas A* is both complete and optimal. However, A* uses more memory than Greedy BFS, but it guarantees that the path found is optimal. BFS is not complete while A* is complete. BFS Time complexity - O(b^m), (in worst case) but a good heuristic can give dramatic improvement (m is max depth of search space). A* star time complexity also depends a lot on the heuristic being used; otherwise with a poor heuristic it is exponential. 

A heuristic h(n) is admissible if  for every node n,
`h(n) ≤ h*(n)`, where `h*(n)` is the true cost to reach the goal 
state from n.

Since in the given problem admissible heursitics have been chosen the A* search is optimal with similar execution time as compared to BFS which makes it better in the given case.

### Test Case:

Start State:
|   |   |   |
| - | - | - |
| T8 | T7| T6|
| T1 | B | T5| 
| T2 | T3| T4|

Goal State:
|   |   |   |
| - | - | - |
| T1 | T2| T3|
| T8 | B | T4| 
| T7 | T6| T5|

### Result: 

| Algorithm | Heuristic | Optimal Path Cost | Time Taken | States Explored | Optimal| 
| - | - | - | - | - | - |
| BFS | Zero heuristic | 28 | 25.3924 | 181273 | Fluke |
| BFS | Tiles Displaced | 50 | 0.09780 | 961 | No |
| BFS | Manhattan | 44 | 0.02950 | 332 | No |
| A* | Zero heuristic | 28 | 25.4986 | 181273 | Yes |
| A* | Tiles Displaced | 28 | 11.3247 | 108984 | Yes |
| A* | Manhattan | 28 | 2.91534 | 27227 | Yes |


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