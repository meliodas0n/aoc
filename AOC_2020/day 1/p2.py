def main(inputs):
    result = 0
    for first_num in inputs:
        for second_num in inputs:
            for third_num in inputs:
                if first_num + second_num + third_num == 2020:
                    result = first_num * second_num * third_num
                    print(result)


if __name__ == "__main__":
    with open('input2.txt') as f:
        inputs = list(map(int, f))
        main(inputs)