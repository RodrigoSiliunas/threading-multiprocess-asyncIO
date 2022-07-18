from datetime import datetime
import math


def main():
    start = datetime.now()
    compute(50_000_000)
    time = datetime.now() - start
    print(
        f'A execução dessa função deurou {time.total_seconds():.2f} segundos.')


def compute(end, start=1):
    pos = start
    fator = 1000 * 1000

    while pos < end:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()

"""
    1. A execução dessa função deurou 26.27 segundos.
"""
