from TuringMachine import TuringMachine, State


class Parser:
    def __init__(self):
        pass

    def parseTM(self, filename: str, final_state: str = None):
        valid = []
        with open(filename) as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip() and line.strip()[0] != "#":
                    valid.append(line.strip())

        cur_state = None
        state = None
        tm = TuringMachine()
        # print("\n".join(valid))
        for line in valid:
            # print(line)
            key, value = line.split(":", 1)
            if value == "" and key != "table":
                cur_state = key
                if state is not None:
                    tm.add_state(state)
                    # print("New state:\n", state, "\n-------", sep="")
                state = State(cur_state)

            if key == "input":
                pass
            elif key == "blank":
                pass
            elif key == "start state":
                tm.set_start_state(value.strip())
            elif key != "table" and key != cur_state:
                state.parse_raw(line)

        tm.add_state(state)
        if final_state is not None:
            tm.set_final_state(final_state)
        return tm
