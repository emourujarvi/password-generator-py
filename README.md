# password-generator-py

By default generates password using all allowed letters.
Program flags are used to exclude characters. 
If all flags are given, the password will be generated from A-Z letters.

## usage

```bash
$ pwg -h
usage: pwg [-h] [-s] [-d] [-n] [-l] [-u] [length]

Generate a secure password based on user input.

positional arguments:
  length                Specify the length of the password. Defaults to 24.

optional arguments:
  -h, --help            show this help message and exit
  -s, --avoid-symbols   Avoid using symbols in the password.
  -d, --avoid-dangerous-symbols
                        Avoid using dangerous symbols in the password.
  -n, --avoid-numbers   Avoid using numbers in the password.
  -l, --avoid-lowercase
                        Avoid using lowercase letters in the password.
  -u, --avoid-umlauts   Avoid using umlauts letters in the password.
```

## install

```bash
install -m 755 password_generator.py ~/.local/bin/pwg
```

## examples
```bash
$ pwg
cSUHCÉ-3ÑY5eLkXð2JHhXUu]

$ pwg 32
9bBuNO8Laçtoä-9va=8pk#wo<d1L}z,R

$ pwg 32 -sl
AT5HJø6L6á'ÓKQ'ÚS&XUKXQQNÇB\9SüN

$ pwg 32 -snuld
OGNDZYGBBEHFZIEQTIBQLJJORGUKTIIV
```