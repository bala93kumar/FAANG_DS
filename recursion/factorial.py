def fact(number):
    if number == 0:
        return 1
    small = number * fact(number-1)
    return small

if __name__ == "__main__":

    input_number = 5

    print(fact(input_number))