import os, sys
sys.path.append(os.path.abspath("../"))

import utils
from collections import Counter

def main():
    inputs = utils.read_inputs("2.input")
    left_list, right_list = [int(x.split()[0]) for x in inputs], [int(x.split()[-1]) for x in inputs]
    right_counts = Counter(right_list)
    similarity_score = 0
    for loc in left_list:
        if loc in right_counts:
            similarity_score += loc * right_counts[loc]
    print(f"{similarity_score = }")

if __name__ == "__main__":
    main()