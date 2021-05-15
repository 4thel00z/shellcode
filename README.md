# shellcode
![shellcode logo](https://raw.githubusercontent.com/4thel00z/shellcode/master/logo.png)

## Motivation

In the course of pawning n00bs often the need arises to introspect some (generated) shellcode or check
it for sanity.

This tools does exactly that.

## Installation

```
pip install shellcode
```

## Usage
```
echo "\x48\x83\xEC\x40\xB0\x3B\x48\x31\xD2\x48\x31\xF6\x52\x48\xBB\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x53\x54\x5F\x0F\x05" | shellcode 
```

## License

This project is licensed under the GPL-3 license.
