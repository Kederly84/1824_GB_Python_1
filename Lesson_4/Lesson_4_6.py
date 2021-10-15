from utils import currency_rates

def curr(argv):
    arg = argv[1]
    value = currency_rates(arg)
    print(value)

if __name__ == '__main__':
    import sys

    exit(curr(sys.argv))