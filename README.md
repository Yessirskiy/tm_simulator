# Turing Machine Simulator
Python program to simulate Turing Machines from [turingmachine.io](https://turingmachine.io/)

## Guide
1. Load your code from [turingmachine.io](https://turingmachine.io/) to some .txt file.
2. Create instance of Parser.
3. Call method parseTM() with filename and final TM state name provided.

Example can be found [here](example.py)
```python
from Parser import Parser

if __name__ == "__main__":
    parser = Parser()
    tm = parser.parseTM("example.txt", "done")
    input1 = "1001"
    input2 = "1"
    input3 = "111"
    print(input1, "->", tm.simulate(input1))
    print(input2, "->", tm.simulate(input2))
    print(input3, "->", tm.simulate(input3))

# 1001 -> 1010
# 1 -> 10
# 111 -> 1000
```
Original code is taken from [turingmachine.io](https://turingmachine.io/):
```
# Adds 1 to a binary number.
input: '1011'
blank: ' '
start state: right
table:
  # scan to the rightmost digit
  right:
    [1,0]: R
    ' '  : {L: carry}
  # then carry the 1
  carry:
    1      : {write: 0, L}
    [0,' ']: {write: 1, L: done}
  done:
```

