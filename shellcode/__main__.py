#! /usr/bin/env python3
import os
import sys
from base64 import b64decode as d64

from shellcode import *

app = typer.Typer()


@app.callback(
    invoke_without_command=True,
    help=f"""Supported archs are (default: CS_ARCH_X86):
{ARCHS_TEXT}

Supported modes are (default: CS_MODE_32):
{MODES_TEXT}
"""
)
def to_asm(
        arch: str = "CS_ARCH_X86",
        mode: str = "CS_MODE_32",
        color: bool = True,
        verbose: bool = False,
        b64: bool = False,
        start: int = 0x00

):
    log = echo if not color else secho

    try:
        arch_type = ARCHS[arch]
        if verbose:
            typer.secho(f"Selected arch type: {arch_type}", fg='green')

    except KeyError:
        typer.secho(f"Could not find arch {arch} in the following list:", fg='red')
        typer.secho(f"{ARCHS_TEXT}", fg='red')
        sys.exit(os.EX_SOFTWARE)

    try:
        mode_type = MODES[mode]
        if verbose:
            typer.secho(f"Selected mode type: {mode_type}", fg='green')

    except KeyError:
        typer.secho(f"Could not find mode {mode} in the following list:", fg='red')
        typer.secho(f"{MODES_TEXT}", fg='red')
        sys.exit(os.EX_SOFTWARE)

    decoder = (lambda a: a) if not b64 else d64

    # TODO: deal with bad shellcode characters here
    shellcode = decoder(sys.stdin.buffer.read())

    if verbose:
        typer.secho(f"Read shellcode: {shellcode}", fg='yellow')

    for instruction in disassemble(shellcode, arch_type, mode_type, start):
        log(instruction.address, instruction.mnemonic, instruction.op_str)


if __name__ == "__main__":
    app()
