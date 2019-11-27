# Nand hack assembler
Implementation of an assembler for the Hack assembly language from the book The Elements of Computing Systems by Noam Nisan and Shimon Schocken. This is project number 6.

# Usage
The main script is `Assembler.py`. Make sure it's executable:
```bash
$ chmod u+x Assembler.py
```
Then run it using the `--input` and `--output` parameters to point to the input `.ams`-file and output `.hack`-file:
```bash
$ ./Assembler.py --input input.asm --output output.hack
```