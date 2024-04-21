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
