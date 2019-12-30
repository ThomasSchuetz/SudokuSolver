# -*- coding: utf-8 -*-
from puzzle import Puzzle
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/solve', methods=['POST',])
def solve():
    
    input_puzzle = []
    for row in range(9):
        current_row = []
        for col in range(9):
            current_row.append(int(request.form["field_"+str(row)+"_"+str(col)]))
        input_puzzle.append(current_row)
    
    puzzle = Puzzle(input_puzzle)
    solution = puzzle.solve()
    
    return render_template('result.html', input_puzzle=input_puzzle, solution=solution)


if __name__ == '__main__':
   app.run(debug = True)