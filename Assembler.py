#!/usr/local/bin/python3
from Parser import Parser, COMMAND
from Code import Code
from SymbolTable import SymbolTable

import argparse
from pathlib import Path


if __name__ == "__main__":
    code = Code()
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    args = vars(parser.parse_args())
    input_file = Path(args['input'])
    output_file = Path(args['output'])
    parser = Parser(input_file)
    symbolTable = SymbolTable()
    # First pass
    ROMix = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == COMMAND['L']:
            symbolTable.addEntry(parser.symbol(), ROMix)
        else:
            ROMix += 1
    # Second pass
    parser = Parser(input_file)
    RAMix = 16
    with open(output_file, 'w') as out:
        while parser.hasMoreCommands():
            parser.advance()
            if parser.commandType() == COMMAND['L']:
                continue
            if parser.commandType() == COMMAND['A']:
                symbol = parser.symbol()
                if symbol.isdigit():
                    number = int(symbol)
                    to_write = format(number, '016b')
                elif symbolTable.contains(symbol):
                    number = int(symbolTable.GetAddress(symbol))
                    to_write = format(number, '016b')
                else:
                    symbolTable.addEntry(symbol, RAMix)
                    to_write = format(RAMix, '016b')
                    RAMix += 1
            elif parser.commandType() == COMMAND['C']:
                dest = code.dest(parser.dest())
                comp = code.comp(parser.comp())
                jump = code.jump(parser.jump())
                to_write = '111' + comp + dest + jump
            else:
                raise Exception('Wrong command type')
            out.write(to_write+'\n')