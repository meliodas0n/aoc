import os, sys
sys.path.append(os.path.abspath("../"))

import utils
from itertools import pairwise 

def main():
    unusal_data = utils.read_inputs("1.input")
    safe_rep_count = 0
    for report in unusal_data:
        rep = [int(x) for x in report.split()]
        flag = 0
        if rep == sorted(rep):
            flag = 1
        elif rep == sorted(rep, reverse=True):
            flag = -1
        else:
            continue
        diff_flag = 0
        if flag == -1:
            for prev_ele, next_ele in pairwise(rep):
                if ((prev_ele - next_ele) >= 1) and ((prev_ele - next_ele) <= 3):
                    diff_flag = 1
                else:
                    diff_flag = 0
                    break
        if flag == 1:
            for prev_ele, next_ele in pairwise(rep):
                if ((next_ele - prev_ele) >= 1) and ((next_ele - prev_ele) <= 3):
                    diff_flag = 1
                else:
                    diff_flag = 0
                    break
        if diff_flag == 1:
            safe_rep_count += 1
    print(f"{safe_rep_count = }")
    
if __name__ == "__main__":
    main()
