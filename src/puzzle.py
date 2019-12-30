# -*- coding: utf-8 -*-

from solver import SudokuSolver

class Puzzle(object):
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._original_puzzle = [[col for col in row] for row in puzzle]
    

    def solve(self):
        sudoku_solver = SudokuSolver(self._puzzle)
        self._puzzle = sudoku_solver.retrieve_results()

    def display_puzzle(self):
        for i, row in enumerate(self._puzzle):
            if i % 3 == 0:
                self._display_dashes()
            print(self._format_string(row))
        self._display_dashes()
     

    def _display_dashes(self):
        print("-------------------------------")  


    def _format_string(self, row):
        replacements = {"[": "",
                        "]": "",
                        "-1": "|",
                        "0": " ",
                        ",": " "}

        copied_row = [col for col in row]
        
        # Insert "-1" values that will be replaced with | in the output string
        copied_row.insert(6, -1)
        copied_row.insert(3, -1)
        
        result = str(copied_row)
        for orig_char, new_char in replacements.items():
            result = result.replace(orig_char, new_char)
        
        return result


    def check_puzzle(self):
        self._check_limit_exeedings()
        self._check_double_entries()
        return True
    
    
    def _check_limit_exeedings(self):
        for i, row in enumerate(self._puzzle):
            assert max(row) <= 9, "Row " + str(i) + " exceeds board limit"
                
    
    def _check_double_entries(self):
        self._check_double_entries_horizontal()
        self._check_double_entries_vertical()
        self._check_double_entries_subfield()
    
    
    def _check_double_entries_horizontal(self):
        for i, row in enumerate(self._puzzle):
            assert not self._contains_duplicates(row), "Row " + str(i+1) + " contains duplicates"
    
    
    def _check_double_entries_vertical(self):
        for i in range(len(self._puzzle)):
            col = [row[i] for row in self._puzzle]
            assert not self._contains_duplicates(col), "Column " + str(i+1) + " contains duplicates"
    
    
    def _check_double_entries_subfield(self):
        for horizontal in range(3):
            for vertical in range(3):
                values = []
                for i in range(3):
                    for j in range(3):
                        values.append(self._puzzle[3 * horizontal + i][3 * vertical + j])
                message = "Subfield (" + str(horizontal+1) + "," + str(vertical+1) + ") contains duplicates"
                assert not self._contains_duplicates(values), message      
    
    
    def _contains_duplicates(self, elements):
        check_elements = self._remove_negative_values_for_check(elements)
        if len(check_elements) == len(set(check_elements)):
            return False
        else:
            return True
    
    
    def _remove_negative_values_for_check(self, values):
        return [value for value in values if value > 0]
