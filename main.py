#!/usr/bin/env python

import lang

runtime = lang.runtime.Runtime()

try:
    while True:
        input_ = input('> ')

        try:
            tokens = lang.lexer.lex(input_)
            ast = lang.parser.parse(tokens)

            value = runtime.evaluate(ast)

            if value == None:
                print('<nil>')
            elif isinstance(value, int):
                print(f'<integer>: {value}')
            else:
                raise NotImplementedError
        except lang.Error as err:
            print(f'{err.message} at :{err.offset}')
except (KeyboardInterrupt, EOFError):
    print()
