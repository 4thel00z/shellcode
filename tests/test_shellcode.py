from pytest import main

from shellcode import (
    __version__,
    disassemble
)

SHELLCODE_TESTS = {
    b"\x48\x83\xEC\x40\xB0\x3B\x48\x31\xD2\x48\x31\xF6\x52\x48\xBB\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x53\x54\x5F\x0F\x05"
    : """0x0:	dec	eax
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
0x1a:	syscall"""

}

def stringify(instruction):
    return "0x%x:\t%s\t%s" % (instruction.address, instruction.mnemonic, instruction.op_str)


def test_disassemble():
    for shellcode, expected in SHELLCODE_TESTS.items():
        result = "\n".join(stringify(line) for line in disassemble(shellcode))
        assert result.strip() == expected.strip()


if __name__ == '__main__':
    main(["-vv", ])
