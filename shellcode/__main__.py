#! /usr/bin/env python3
import os
import sys

import typer
from capstone import *

app = typer.Typer()
ARCHS = {k: v for k, v in locals().items() if k.startswith("CS_ARCH")}
MODES = {k: v for k, v in locals().items() if k.startswith("CS_MODE")}
ARCHS_TEXT = "\n\n\t- ".join(["", *ARCHS.keys()])
MODES_TEXT = "\n\n\t- ".join(["", *MODES.keys()])


def secho(address: int, mnemonic: int, op_str: int) -> None:
    """
    Print an disassembled instruction with colors.
    TODO: colors look probably shitty and need to be tweaked

    :param address:
    :param mnemonic:
    :param op_str:
    :return:
    """
    typer.echo("\t".join((
        typer.style('0x%x:' % address, fg='blue'),
        typer.style('%s' % mnemonic, fg='green'),
        typer.style('%s' % op_str, fg='yellow'),
    )))


def echo(address: int, mnemonic: int, op_str: int) -> None:
    """
    Print an disassembled instruction without colors.

    :param address:
    :param mnemonic:
    :param op_str:
    :return:
    """
    typer.echo("0x%x:\t%s\t%s" % (address, mnemonic, op_str))


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

    dis = Cs(arch_type, mode_type)

    # TODO: deal with bad shellcode characters here
    shellcode = sys.stdin.read().encode("ascii")
    
    for instruction in dis.disasm(shellcode, 0x00):
        log(instruction.address, instruction.mnemonic, instruction.op_str)


if __name__ == "__main__":
    app()
