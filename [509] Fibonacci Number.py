def fib(n=995):
    def fibonacci(length, num1, num2):
        while length - 1 > 0:
            temp = num1
            num1 = num2
            num2 = temp + num2
            length -= 1
            print("數1",num1,'數2',num2)
            return fibonacci(length, num1, num2)

        return num2

    return fibonacci(n, 0, 1)


fib()
