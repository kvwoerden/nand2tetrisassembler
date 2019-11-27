import argparse
from pathlib import Path
import re
from enum import Enum

COMMAND = { 'A': 'A_COMMAND', 'C': 'C_COMMAND', 'L': 'L_COMMAND' }

class Parser:
    def __init__(self, input_file):
        with open(input_file, 'r') as input_file_object:
            self.input_lines = [line for line in input_file_object]
        self.remove_whitespace()
        self.remove_comments()
        self.remove_emptylines()
        self.current_command = None
        self.length = len(self.input_lines)
        self.ix = -1

    def print(self):
        print(self.input_lines)

    def remove_whitespace(self):
        self.input_lines = list(map(lambda s: re.sub(r"\s+", "", s), self.input_lines))

    def remove_comments(self):
        self.input_lines = list(map(lambda s: re.sub(r"//.*", "", s), self.input_lines))

    def remove_emptylines(self):
        self.input_lines = list(filter(lambda s: s != '', self.input_lines))

    def hasMoreCommands(self):
        if self.ix + 1 < self.length:
            return True
        else:
            return False
    
    def advance(self):
        self.ix += 1
        self.current_command = self.input_lines[self.ix]

    def commandType(self):
        if self.current_command[0] == '@':
            return COMMAND['A']
        elif self.current_command[0] == '(':
            return COMMAND['L']
        else:
            return COMMAND['C']
    
    def symbol(self):
        # See https://docs.python.org/3/library/re.html#match-objects
        if self.commandType() == COMMAND['A']:
            symbol_match = re.match(r"@(.*)", self.current_command)
        elif self.commandType() == COMMAND['L']:
            symbol_match = re.match(r"\((.*)\)", self.current_command)
        else:
            raise Exception('Wrong command type')
        return symbol_match.group(1)

    def dest(self):
        if '=' in self.current_command:
            split = self.current_command.split('=')
            return split[0]
        else:
            return ''
    
    def jump(self):
        if ';' in self.current_command:
            split = self.current_command.split(';')
            return split[1]
        else:
            return ''

    def comp(self):
        split = self.current_command
        if ';' in split:
            split = split.split(';')[0]
        if '=' in split:
            split = split.split('=')[1]
        return split






