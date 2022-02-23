def calculate(num):

    if num  > 0:
        k =  num ** 2
        return k
        num -= 1
        calculate(num)



if __name__ == "__main__":

    value = 4
    calculate(value)
