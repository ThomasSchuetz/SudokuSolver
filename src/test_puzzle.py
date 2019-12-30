# -*- coding: utf-8 -*-
import test_data
from puzzle import Puzzle
import pytest

def test_feasible_puzzle_does_not_fail_check():
    puzzle = Puzzle(test_data.puzzle)
    puzzle.check_puzzle()

def test_check_throws_error_if_any_number_exceeds_9():
    data = test_data.puzzle
    data[4][5] = 10
    puzzle = Puzzle(test_data.puzzle)
    with pytest.raises(AssertionError):
        puzzle._check_limit_exeedings()

def test_check_throws_error_if_any_row_contains_duplicates():
    data = test_data.puzzle
    data[1][1] = 4
    puzzle = Puzzle(test_data.puzzle)
    with pytest.raises(AssertionError):
        puzzle._check_double_entries_horizontal()

def test_check_throws_error_if_any_column_contains_duplicates():
    data = test_data.puzzle
    data[7][5] = 1
    puzzle = Puzzle(test_data.puzzle)
    with pytest.raises(AssertionError):
        puzzle._check_double_entries_vertical()

def test_check_throws_error_if_any_subfield_contains_duplicates():
    data = test_data.puzzle
    data[8][8] = 7
    puzzle = Puzzle(test_data.puzzle)
    with pytest.raises(AssertionError):
        puzzle._check_double_entries_subfield()
