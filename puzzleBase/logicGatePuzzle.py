import random

class LogicGatePuzzle:
    VALID_GATES = {"and", "nand", "or", "nor", "xor"}
    # Valid gates are "and", "nand", "or", "nor", "xor"
    def __init__(self, rows, gate="and"):
        if (rows < 1):
            raise ValueError("Rows cannot be less than 1")
        if gate not in self.VALID_GATES:
            raise ValueError(f"Invalid gate type: {gate}")
        self.rows = int(rows)
        self.set_gate = LogicGate(gate)
        self.build_puzzle()
        print(self.puzzle)

        
    # Checks if the current solution is correct
    def check_solution(self):
        tmp_inputs = []
        tmp_inputs1 = []
        # Checks the last row
        for i in range(self.rows+1):
            tmp_input1 = self.puzzle[self.rows][f'input{2*i}']
            tmp_input2 = self.puzzle[self.rows][f'input{2*i+1}']
            tmp_inputs.append(self.puzzle[self.rows-1][f'gate{i}'].output(tmp_input1, tmp_input2))
        for i in range(self.rows - 2, -1, -1):
            for j in range(i*2):
                tmp_inputs1.append(self.puzzle[i][f'gate{j}'].output(tmp_inputs[2*j], tmp_inputs[2*j+1]))
        ### ADD LOGIC TO MAKE THIS INFINTELY SCALABLE
        return tmp_inputs1
        return False
    
    # Builds the puzzle by placing dictionaries inside a list, the list index represents row and 
    # columns are referenced via key-pair values (ie. 'gate0', 'gate1', etc.)
    def build_puzzle(self):
        self.puzzle = []
        self.locked_gates = [[0, 'gate0']]
        for i in range(self.rows + 1):
            self.puzzle.append({})
        if (self.rows > 2):
            for i  in range(self.rows):
                for j in range(i*2):
                    temp = random.choice(['and','nand','or','nor','xor'])
                    if (random.randint(0,2) == 0):
                        self.locked_gates.append([i, f"gate{j}"])
                    self.puzzle[i][f"gate{j}"] = LogicGate(temp)
            for i in range(2**self.rows):
                self.puzzle[self.rows][f"input{i}"] = random.choice([True, False])
        else:
            self.puzzle[1]["gate0"] = LogicGate("and")
            self.puzzle[1]["gate1"] = LogicGate("and")
            for i in range(self.rows**2):
                self.puzzle[self.rows][f'input{i}'] = random.choice([True, False])
        self.puzzle[0]["gate0"] = self.set_gate
        return self.puzzle
        
    # Changes a gate by taking a list and the type of gate, throws an error if the gate doesn't exit
    # If the ref doesn't exist no change will be noticable but it will be added to the dictionary
    def change_gate(self, ref, gate):
        if gate not in self.VALID_GATES:
            raise ValueError(f"Invalid gate type: {gate}")
        if ref in self.locked_gates:
            raise ValueError(f"Gate is locked and cannot be changed: {ref}")
        self.puzzle[ref[0]][ref[1]].change_gate(gate)
        return self.puzzle
    
    # All things start from 1 instead of 0 so it's more like normal counting
    def easy_change_gate(self, row, column, gate):
        if gate not in self.VALID_GATES:
            raise ValueError(f"Invalid gate type: {gate}")
        if (row > self.rows):
            raise ValueError(f"Invalid row reference, row {row} does not exist")
        tmp_row = row-1
        tmp_col = f"gate{column-1}"
        if [tmp_row, tmp_col] in self.locked_gates:
            raise ValueError(f"Gate is locked and cannot be changed. Row: {row}, Column: {column}")
        return self.change_gate([tmp_row, tmp_col], gate)
    
    def show_puzzle(self):
        return self.puzzle
    
    def show_gate(self, row, column):
        return self.puzzle[row-1][f"gate{column-1}"].display_gate()
    
    def show_locked_gates(self):
        return self.locked_gates

class LogicGate:
    def __init__(self, gate):
        self.gate = gate

    def display_gate(self):
        return self.gate
    
    def output(self, input1, input2):
        match self.gate:
            case "and":
                if (input1 and input2):
                    return True
                return False
            case "nand":
                if (input1 and input2):
                    return False
                return True
            case "or":
                if (input1 or input2):
                    return True
                return False
            case "nor":
                if (input1 or input2):
                    return False
                return True
            case "xor":
                if (input1 and input2):
                    return False
                if (input1 or input2):
                    return True
                return False
            
    def change_gate(self, gate):
        self.gate = gate