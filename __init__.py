# coding=utf-8
"""
Copyright (c) 2021 Athanasios Kostopoulos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
import binaryninja
from binaryninja.binaryview import BinaryReader, BinaryView
from binaryninja.architecture import Architecture
from binaryninja.enums import (SectionSemantics, SegmentFlag, SymbolType)
from binaryninja.types import Symbol

from .c64.constants import KERNAL

class C64PRG(BinaryView):
    name = "C64 PRG Format"
    long_name = "C64 PRG Format"

    def __init__(self, data):
        # PRG format is 2bytes for memloc + 15 bytes boilerplate setup code
        # that was inserted via db thus offset = 0x0F + 0x02 = 0x11
        offset = 0x11
        BinaryView.__init__(self, parent_view=data, file_metadata=data.file)
        self.platform = Architecture['6502'].standalone_platform
        self.data :BinaryView = data
        self.br = BinaryReader(self.data)
        self.base_addr :int = self.br.read16le()
        self.add_auto_segment(0x00, len(self.data), offset, len(self.data), SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable)
        for addr in KERNAL.keys():
            self.define_auto_symbol(Symbol(SymbolType.DataSymbol, addr, KERNAL[addr]))
        self.add_entry_point(0x00)

    @classmethod
    def is_valid_for_data(self, data):
        if data.file.original_filename.lower().endswith(".prg"):
            return True
        else:
            print("Not a .prg file")
            return False

C64PRG.register()
