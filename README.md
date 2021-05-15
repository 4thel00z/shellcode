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

### With defaults (x86 in 32bit mode)

```
echo "\x48\x83\xEC\x40\xB0\x3B\x48\x31\xD2\x48\x31\xF6\x52\x48\xBB\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x53\x54\x5F\x0F\x05" | shellcode 
```

Outputs:

```
0x0:	dec	eax
0x1:	sub	esp, 0x40
0x4:	mov	al, 0x3b
0x6:	dec	eax
0x7:	xor	edx, edx
0x9:	dec	eax
0xa:	xor	esi, esi
0xc:	push	edx
0xd:	dec	eax
0xe:	mov	ebx, 0x69622f2f
0x13:	outsb	dx, byte ptr [esi]
0x14:	das	
0x15:	jae	0x7f
0x17:	push	ebx
0x18:	push	esp
0x19:	pop	edi
0x1a:	syscall
```

### Fullblown

```
Usage: shellcode [OPTIONS] COMMAND [ARGS]...

  Supported archs are (default: CS_ARCH_X86):

          - CS_ARCH_ARM

          - CS_ARCH_ARM64

          - CS_ARCH_MIPS

          - CS_ARCH_X86

          - CS_ARCH_PPC

          - CS_ARCH_SPARC

          - CS_ARCH_SYSZ

          - CS_ARCH_XCORE

          - CS_ARCH_M68K

          - CS_ARCH_TMS320C64X

          - CS_ARCH_M680X

          - CS_ARCH_EVM

          - CS_ARCH_ALL

  Supported modes are (default: CS_MODE_32):

          - CS_MODE_LITTLE_ENDIAN

          - CS_MODE_BIG_ENDIAN

          - CS_MODE_16

          - CS_MODE_32

          - CS_MODE_64

          - CS_MODE_ARM

          - CS_MODE_THUMB

          - CS_MODE_MCLASS

          - CS_MODE_MICRO

          - CS_MODE_MIPS3

          - CS_MODE_MIPS32R6

          - CS_MODE_MIPS2

          - CS_MODE_V8

          - CS_MODE_V9

          - CS_MODE_QPX

          - CS_MODE_M68K_000

          - CS_MODE_M68K_010

          - CS_MODE_M68K_020

          - CS_MODE_M68K_030

          - CS_MODE_M68K_040

          - CS_MODE_M68K_060

          - CS_MODE_MIPS32

          - CS_MODE_MIPS64

          - CS_MODE_M680X_6301

          - CS_MODE_M680X_6309

          - CS_MODE_M680X_6800

          - CS_MODE_M680X_6801

          - CS_MODE_M680X_6805

          - CS_MODE_M680X_6808

          - CS_MODE_M680X_6809

          - CS_MODE_M680X_6811

          - CS_MODE_M680X_CPU12

          - CS_MODE_M680X_HCS08

Options:
  --arch TEXT                     [default: CS_ARCH_X86]
  --mode TEXT                     [default: CS_MODE_32]
  --color / --no-color            [default: True]
  --verbose / --no-verbose        [default: False]
  --b64 / --no-b64                [default: False]
  --start INTEGER                 [default: 0]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

## License

This project is licensed under the GPL-3 license.
