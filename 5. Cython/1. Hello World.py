import hello


def main(message: str):
    hello.say_hello(message)


if __name__ == '__main__':
    main('Boa noite, esse é o meu primeiro programa com Cython!')
