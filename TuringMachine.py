from typing import Dict, Tuple

TRANSITION_TEMPLATE = {"write": "", "shift": 1, "next": ""}


class State:
    def __init__(self, name: str):
        self.name: str = name
        self.transitions: Dict[str, Dict[str, str | None]] = {}

    def get_move(self, inp: str) -> Tuple[str]:
        move = self.transitions.get(inp, None)
        assert (
            move is not None
        ), f"Invalid input for the state (state={self.name}, input={inp})"

        return (move["write"], move["shift"], move["next"])

    def add_transition(self, inp: str, write: str, shift: str, nxt: str):
        if not write:
            write = inp
        if not nxt:
            nxt = self.name
        new_transition = TRANSITION_TEMPLATE.copy()
        new_transition["write"] = write
        new_transition["shift"] = shift
        new_transition["next"] = nxt
        self.transitions[inp] = new_transition

    def parse_raw(self, raw: str):
        def process_input(s: str):
            return s.strip().replace("'", "")

        def process_transition(s: str):
            if s == "R":
                return (None, 1, None)
            elif s == "L":
                return (None, -1, None)
            else:
                params = list(map(str.strip, s[1:-1].split(",")))
                write = None
                shift = 1
                nxt = None
                for param in params:
                    if param == "L" or param == "R":
                        name = param
                        val = self.name
                    else:
                        name, val = map(str.strip, param.split(":"))

                    if name == "write":
                        if len(val) == 3:
                            val = val[1:-1]
                        write = val
                    elif name == "R":
                        shift = 1
                        nxt = val
                    elif name == "L":
                        shift = -1
                        nxt = val
                return (write, shift, nxt)

        for line in raw.split("\n"):
            raw_input, raw_trans = map(str.strip, line.split(":", 1))
            if raw_input == "' '":
                inps = [" "]
            elif len(raw_input) == 1:
                inps = [raw_input]
            else:
                inps = list(map(process_input, raw_input[1:-1].split(",")))
            # print(line, "=", inps)
            for single_input in inps:
                if len(single_input) == 3:
                    self.add_transition(
                        single_input[-1:1], *process_transition(raw_trans)
                    )
                else:
                    self.add_transition(single_input, *process_transition(raw_trans))

    def __str__(self):
        trans = "\n".join(
            [f"{key}: {value}" for key, value in self.transitions.items()]
        )
        return f"{self.name}: \n{trans} "


class TuringMachine:
    PADDING = 100

    def __init__(self):
        self.start_state = None
        self.final_state = None
        self.states = {}
        self.cur_state = None
        self.head = 0

    def add_state(self, state: State):
        self.states[state.name] = state

    def set_start_state(self, state_name: str):
        self.start_state = state_name

    def set_final_state(self, state_name: str):
        self.final_state = state_name

    def simulate(self, input_string: str, logging: bool = False) -> str:
        line = " " * self.PADDING + input_string + " " * self.PADDING
        self.head = self.PADDING
        self.cur_state = self.start_state
        itr = 1
        while self.cur_state != self.final_state:
            line1 = ""
            inp = line[self.head]

            move = self.states[self.cur_state].get_move(inp)
            for i in range(len(line)):
                if i == self.head:
                    line1 += move[0]
                else:
                    line1 += line[i]

            self.head += move[1]
            self.cur_state = move[2]
            line = line1
            if logging:
                print(itr, line.strip())
            itr += 1
        return line.strip()

    def __str__(self) -> str:
        text = (
            f"TM: \nstart:  {self.start_state} \nfinish:  {self.final_state} \ntable:"
        )
        for state in self.states.values():
            text += "\n" + str(state)
        return text
