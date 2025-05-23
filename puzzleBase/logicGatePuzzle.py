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
        
    # Checks if the current solution is correct
    def check_solution(self):
        # Creates two empty list and a boolean to decide which list to use
        tmp_inputs0 = []
        tmp_inputs1 = []
        input_use = True
        # Checks the outputs for the last row, has to be done due to inputs having different references
        for i in range(self.rows+1):
            tmp_input1 = self.puzzle[self.rows][f'input{2*i}']
            tmp_input2 = self.puzzle[self.rows][f'input{2*i+1}']
            tmp_inputs0.append(self.puzzle[self.rows-1][f'gate{i}'].output(tmp_input1, tmp_input2))
        # Goes through every row and checks their outputs
        for i in range(self.rows - 2, -1, -1):
            # Checks every row except the top one due to i=0 when top
            for j in range(2*i):
                if (input_use):
                    tmp_inputs1.append(self.puzzle[i][f'gate{j}'].output(tmp_inputs0[2*j], tmp_inputs0[2*j+1]))
                else: 
                    tmp_inputs0.append(self.puzzle[i][f'gate{j}'].output(tmp_inputs1[2*j], tmp_inputs1[2*j+1]))
            # When i = 0, for j does not work but we can use this to check.
            if (i == 0):
                if (input_use):
                    return self.puzzle[0]['gate0'].output(tmp_inputs0[0], tmp_inputs0[1])
                else:
                    return self.puzzle[0]['gate0'].output(tmp_inputs1[0], tmp_inputs1[1])
            # Emptys the list so that this has infinite scalability
            if (input_use):
                tmp_inputs0 = []
            else: 
                tmp_inputs1 = []
            # Flips input_use so that the other list will be used
            input_use = not input_use
    
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
        tmp_row = row - 1
        tmp_col = f"gate{column-1}"
        if [tmp_row, tmp_col] in self.locked_gates:
            raise ValueError(f"Gate is locked and cannot be changed. Row: {row}, Column: {column}")
        return self.change_gate([tmp_row, tmp_col], gate)
    
    def show_puzzle(self):
        puzzle = []
        for i in range(len(self.puzzle) - 1):
            tmp = {}
            for j in range(2**i):
                tmp[f'gate{j}'] = self.puzzle[i][f'gate{j}'].display_gate()
            puzzle.append(tmp)
        tmp = {}
        for i in range(2**self.rows):
            tmp[f'input{i}'] = self.puzzle[self.rows][f"input{i}"]
        puzzle.append(tmp)
        return puzzle
    
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
        
def test(rows):
    puzzle = LogicGatePuzzle(rows)
    print(puzzle.show_puzzle())
    
test(3)