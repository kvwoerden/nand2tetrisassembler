import unittest
from pathlib import Path

from ..Parser import Parser, COMMAND

input_file = Path(__file__).parent / 'parser_input.asm'

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(input_file)

    
    def test_line_parsing(self):
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), COMMAND['A'], 'Wrong command type')
        self.assertEqual(self.parser.symbol(), '0', 'Wrong symbol')
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), COMMAND['C'], 'Wrong command type')
        self.assertEqual(self.parser.dest(), 'D', 'Wrong destination')
        self.assertEqual(self.parser.comp(), 'M', 'Wrong computation')
        self.assertEqual(self.parser.jump(), '', 'Wrong jump')
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), COMMAND['C'], 'Wrong command type')
        self.assertEqual(self.parser.dest(), '', 'Wrong destination')
        self.assertEqual(self.parser.comp(), 'D', 'Wrong computation')
        self.assertEqual(self.parser.jump(), 'JLE', 'Wrong jump')
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), COMMAND['C'], 'Wrong command type')
        self.assertEqual(self.parser.dest(), 'D', 'Wrong destination')
        self.assertEqual(self.parser.comp(), 'M', 'Wrong computation')
        self.assertEqual(self.parser.jump(), 'JGE', 'Wrong jump')
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), COMMAND['L'], 'Wrong command type')
        self.assertEqual(self.parser.symbol(), 'hellothere', 'Wrong symbol')
        self.parser.advance()
        self.assertEqual(self.parser.commandType(), COMMAND['L'], 'Wrong command type')
        self.assertEqual(self.parser.symbol(), 'hellothere', 'Wrong symbol')

