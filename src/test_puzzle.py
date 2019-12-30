# -*- coding: utf-8 -*-
import test_data
from puzzle import Puzzle
import pytest

def test_feasible_puzzle_does_not_fail_check():
    puzzle = Puzzle(test_data.get_puzzle())
    puzzle.check_puzzle()

def test_check_throws_error_if_any_number_exceeds_9():
    data = test_data.get_puzzle()
    data[4][5] = 10
    puzzle = Puzzle(data)
    with pytest.raises(AssertionError):
        puzzle._check_limit_exeedings()

def test_check_throws_error_if_any_row_contains_duplicates():
    data = test_data.get_puzzle()
    data[1][1] = 4
    puzzle = Puzzle(data)
    with pytest.raises(AssertionError):
        puzzle._check_double_entries_horizontal()

def test_check_throws_error_if_any_column_contains_duplicates():
    data = test_data.get_puzzle()
    data[7][5] = 1
    puzzle = Puzzle(data)
    with pytest.raises(AssertionError):
        puzzle._check_double_entries_vertical()

def test_check_throws_error_if_any_subfield_contains_duplicates():
    data = test_data.get_puzzle()
    data[8][8] = 7
    puzzle = Puzzle(data)
    with pytest.raises(AssertionError):
        puzzle._check_double_entries_subfield()

def test_solver_correctly_solves_puzzle():
    expected_result = test_data.get_expected_solution()
    input_data = test_data.get_puzzle()
    puzzle = Puzzle(input_data)
    obtained_result = puzzle.solve()
    
    for row in range(len(expected_result)):
        for col in range(len(expected_result[row])):
            assert expected_result[row][col] == obtained_result[row][col]

