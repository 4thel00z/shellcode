import typer
from capstone import *

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


def disassemble(
        shellcode: bytes,
        arch_type: int = CS_ARCH_X86,
        mode_type: int = CS_MODE_32,
        start=0x00):
    dis = Cs(arch_type, mode_type)
    return (instruction for instruction in dis.disasm(shellcode, start))


__version__ = '0.2.1'
