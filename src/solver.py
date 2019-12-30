# -*- coding: utf-8 -*-

from ortools.linear_solver import pywraplp

class SudokuSolver(object):
    def __init__(self, puzzle):
        self._setup_board_size()
        self._initialize_model()
        self._create_variables()
        self._add_constraints(puzzle)
        self._solve_model()
    
    
    def _setup_board_size(self):
        board_size = 9
        self.subfield = {"number_horizontal": 3, # Number of subfields in horizontal direction
                         "number_vertical": 3,
                         "amount_horizontal": 3, # Number of fields per subfield in horizontal direction
                         "amount_vertical": 3}
        self.rows = range(board_size)
        self.cols = range(board_size)
        self.candidates = range(1, board_size+1)
    
    
    def _initialize_model(self):
        self.model = pywraplp.Solver("Sudoku", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
        
    
    def _create_variables(self):
        self.numbers = {}
        for row in self.rows:
            for col in self.cols:
                for candidate in self.candidates:
                    label = str(candidate) + "_in_field_" + str(row) + "_" + str(col)
                    self.numbers[row, col, candidate] = self.model.BoolVar(label)
    
    
    def _add_constraints(self, puzzle):
        self._every_field_has_one_number()
        self._fix_already_given_fields(puzzle)
        self._no_duplicates_per_row()
        self._no_duplicates_per_column()
        self._no_duplicates_per_subfield()
    
    
    def _solve_model(self):
        status = self.model.Solve()
        assert status in (pywraplp.Solver.OPTIMAL, pywraplp.Solver.FEASIBLE), "Optimization failed"
        

    def _every_field_has_one_number(self):
        for row in self.rows:
            for col in self.cols:
                self.model.Add(self.model.Sum([self.numbers[row, col, candidate] for candidate in self.candidates]) == 1,
                               "every_field_has_one_number_" + str(row) + "_" + str(col))
    
    
    def _fix_already_given_fields(self, puzzle):
        for row in self.rows:
            for col in self.cols:
                candidate = puzzle[row][col]
                if candidate > 0.0:
                    self.model.Add(self.numbers[row, col, candidate] == 1,
                                   "fix_already_given_field_" + str(row) + "_" + str(col))
    
    
    def _no_duplicates_per_row(self):
        for row in self.rows:
            for candidate in self.candidates:
                selection = [self.numbers[row, col, candidate] for col in self.cols]
                self._no_duplicates_in_selection(selection, "row_" + str(row) + "_" + str(candidate))
    
    
    def _no_duplicates_per_column(self):
        for col in self.cols:
            for candidate in self.candidates:
                selection = [self.numbers[row, col, candidate] for row in self.rows]
                self._no_duplicates_in_selection(selection, "col_" + str(col) + "_" + str(candidate))
    
    
    def _no_duplicates_per_subfield(self):
        for candidate in self.candidates:        
            for horizontal in range(self.subfield["number_horizontal"]):
                for vertical in range(self.subfield["number_vertical"]):
                    label = "subfield_" + str(horizontal) + "_" + str(vertical) + "_" + str(candidate)
                    selection = [self.numbers[self.subfield["number_horizontal"] * horizontal + i, 
                                              self.subfield["number_vertical"] * vertical + j,
                                              candidate]
                                 for i in range(self.subfield["amount_horizontal"])
                                 for j in range(self.subfield["amount_vertical"])]
                    self._no_duplicates_in_selection(selection, label)

    
    def _no_duplicates_in_selection(self, selection, label):
        self.model.Add(self.model.Sum([element for element in selection]) == 1,
                       "no_duplicates_per_" + label)


    def retrieve_results(self):
        result = []
        for row in self.rows:
            current_row = []
            for col in self.cols:
                for candidate in self.candidates:
                    if self.numbers[row, col, candidate].SolutionValue() == 1:
                        current_row.append(candidate)
            result.append(current_row)
        
        return result
