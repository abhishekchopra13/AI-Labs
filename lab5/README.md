### CS561
### Artifical Intelligence Lab
### Indian Institute of Technology Patna
### 2021-22

# Assignment 5

## Team Details:

Team Code: `1801cs03_1801cs07_1801cs46`

Team Name: `MnMnM`

Team Members:

| Name              | Roll Number |
| ----------------- | ----------- |
| Abhishek Chopra   | 1801CS03    |
| Amish Mittal      | 1801CS07    |
| Shashwat Mahajan  | 1801CS46    |

## Question 1: Deduction Theorem

### Running the Code
```python Q1_deduction_theorem.py```

**Note:** The LHS and RHS of expressions given as input must always be in parenthesis. For example: P=>Q must be written as (P)=>(Q).  

### Sample Outputs
#### Example 1
```
Enter an expression to parse: (P=>Q)=>((~Q=>P)=>Q)
Parsing...
Evaluating...
The expression is a THEOREM!
```
#### Example 2
```
Enter an expression to parse: (P)=>(PVQ)
Parsing...
Evaluating...
The expression is a THEOREM!
```
#### Example 3
```
Enter an expression to parse: (P^Q)=>(PVR)
Parsing...
Evaluating...
The expression is a THEOREM!
```
#### Example 4
```
Enter an expression to parse: (P)=>(Q)
Parsing...
Evaluating...
The expression is NOT A THEOREM!
```

## Question 2: Prolog Programming
### Running Queries
1. Open prolog terminal using: ```prolog```
2. Inside the prolog terminal, load the Knowledge Base (Facts and Rules)
```
consult('Q2_prolog').
```
3. Use the **query written inside the prolog file** to directly ask - 'Is there a member who is a mountain climber but not a
skier?':
```
query(Member).
```

### Sample Output
```
query(Member).
Member = b.
```
______________________
Thanking You!

MnMnM


















