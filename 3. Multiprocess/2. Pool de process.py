import multiprocessing


def show_current_process_name():
    return print(f'Nome do processo atual: {multiprocessing.current_process().name}')


def number_to_square(number):
    return number ** 2


def main():
    pool_length = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_length, initializer=show_current_process_name)
    print(f'O tamanho da nossa pool de processo é de: {pool_length}')

    input = list(range(7))
    output = pool.map(number_to_square, input)
    [pool.close(), pool.join()]

    print(f'Saídas: {output}')


if __name__ == '__main__':
    main()
