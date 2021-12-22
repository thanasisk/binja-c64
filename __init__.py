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
        BinaryView.__init__(self, parent_view=data, file_metadata=data.file)
        self.platform = Architecture['6502'].standalone_platform
        self.data :BinaryView = data
        self.br = BinaryReader(self.data)
        self.base_addr :int = self.br.read16le()
        self.add_auto_segment( self.base_addr, len(self.data), 2, len(self.data)-2, SegmentFlag.SegmentReadable | SegmentFlag.SegmentExecutable)
        for addr in KERNAL.keys():
            #self.define_user_data_var(addr, _type)
            self.define_auto_symbol(Symbol(SymbolType.DataSymbol, addr, KERNAL[addr]))
    @classmethod
    def is_valid_for_data(self, data):
        if data.file.original_filename.lower().endswith(".prg"):
            return True
        else:
            print("Not a .prg file")
            return False

C64PRG.register()
