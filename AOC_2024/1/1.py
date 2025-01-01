import os, sys
sys.path.append(os.path.abspath("../"))

import utils

def main():
    inputs = utils.read_inputs("1.input")
    first_set, second_set = sorted([int(x.split()[0]) for x in inputs]), sorted([int(x.split()[-1]) for x in inputs])
    total_distance = 0
    for x, y in zip(first_set, second_set):
        total_distance += abs(x - y)
    print(f"{total_distance = }")

if __name__ == "__main__":
    main()