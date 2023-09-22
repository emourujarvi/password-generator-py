# password-generator-py

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