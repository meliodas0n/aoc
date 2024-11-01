def main(inputs):
    for first_num in inputs:
        for second_num in inputs:
            if first_num + second_num == 2020:
                print(first_num, second_num)
                result = first_num * second_num
                print(result)
        

if __name__ == "__main__":
    with open('input1.txt') as f:
        inputs = list(map(int, f))
        main(inputs)
