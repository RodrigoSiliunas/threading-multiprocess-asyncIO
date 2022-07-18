import multiprocessing


def do_something(name: str):
    return print(f'Fazendo algo com o valor... {name}')


def main() -> None:
    multi = multiprocessing.Process(target=do_something, args=('Dimas',), name='Dimas Process')

    print(f'Inicializando o processo: {multi.name}')

    # Start multi process from multi variable;
    [multi.start(), multi.join()]


if __name__ == '__main__':
    print(f'O processo principal é chamado de... {multiprocessing.current_process().name}')

    main()
