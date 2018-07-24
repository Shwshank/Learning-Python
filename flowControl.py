# x = int(input("Plz enter an integer: "))
# print(x)

# words = ['cat', 'dog', 'bird']
# j=0;
# for i in words:
#     print(j,'.', i, len(i))
#     j+=1

# Range
# for i in range(5,10):
#     print(i)

# ary = ['bus', 'car', 'bike', 'auto']
# for i in range(len(ary)):
#     print(i+1, ary[i])


#  Fabonacci Series example
# def fib(n):
#
#     """Print a Fibonacci series up to n. """
#
#     a,b = 0,1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# fib(1000)


# def ask_ok(promt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(promt)
#         if ok in ('y', 'ya', 'yes'):
#             return True
#         if ok in ('n', 'no', 'na'):
#             return False
#         retries -= 1
#         if retries < 0:
#             raise ValueError('Invalid!!!!')
#         print(reminder)
#
# ask_ok('Do you want to continue? ')


i = 5

def f(arg=i):
    print(arg)

i = 6
f()
