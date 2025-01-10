import os, sys
sys.path.append(os.path.abspath("../"))

import utils
from itertools import pairwise

def check_order(report):
    up, down = -1, -1
    for i, j in pairwise(report):
        if i - j >= 0:
            down += 1
        else:
            up += 1
    return up, down

def elements_diff():
    pass

def main():
    inputs = utils.read_inputs("2i")
    for reporrt in inputs:
        inc, dec = check_order(report)
        if inc == 3:
            print(f"Strictly Increasing")
        elif dec == 3:
            print(f"Strictly Decreasing")
        else:
            
    
if __name__ == "__main__":
    # main()
    check_order([7, 6, 4, 2, 1])