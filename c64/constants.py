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


KERNAL = { 0xFF81: "SCINIT",
    0xFF84: "IOINIT", #. Initialize CIA's, SID volume; setup memory configuration; set and start interrupt timer.
    0xFF87: "RAMTAS",
    0xFF8A: "RESTOR",
    0xFF8D: "VECTOR",
    0xFF90: "SETMSG",
    0xFF93: "LSTNSA",
    0xFF96: "TALKSA",
    0xFF99: "MEMBOT",
    0xFF9C: "MEMTOP",
    0xFF9F: "SCNKEY",
    0xFFA2: "SETTMO",
    0xFFA5: "IECIN",
    0xFFA8: "IECOUT",
    0xFFAB: "UNTALK",
    0xFFAE: "UNLSTN",
    0xFFB1: "LISTEN",
    0xFFB4: "TALK",
    0xFFB7: "READST",
    0xFFBA: "SETLFS",
    0xFFBD: "SETNAM",
    0xFFC0: "OPEN",
    0xFFC3: "CLOSE",
    0xFFC6: "CHKIN",
    0xFFC9: "CHKOUT",
    0xFFCC: "CLRCHN",
    0xFFCF: "CHRIN",
    0xFFD2: "CHROUT",
    0xFFD5: "LOAD",
    0xFFD8: "SAVE",
    0xFFDB: "SETTIM",
    0xFFDE: "RDTIM",
    0xFFE1: "STOP",
    0xFFE4: "GETIN",
    0xFFE7: "CLALL",
    0xFFEA: "UDTIM",
    0xFFED: "SCREEN",
    0xFFF0: "PLOT",
    0xFFF3: "IOBASE" }
