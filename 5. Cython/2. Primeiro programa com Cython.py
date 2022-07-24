from datetime import datetime
import compute


def main():
    start = datetime.now()
    compute.compute(50_000_000)
    time = datetime.now() - start
    print(
        f'A execução dessa função deurou {time.total_seconds():.2f} segundos.')


if __name__ == '__main__':
    main()

"""
    1. A execução dessa função deurou 26.27 segundos.
"""
