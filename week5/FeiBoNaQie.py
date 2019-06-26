# FeiBoNaQie
# 1 1 2 3 5 8
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n -2)

def main():
    print(f(5))

main()


