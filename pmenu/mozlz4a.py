#!/usr/bin/env python3
# vim: sw=4 ts=4 et tw=100 cc=+1
#
####################################################################################################
#                                           DESCRIPTION                                            #
####################################################################################################
#
# Decompressor/compressor for files in Mozilla's "mozLz4" format. Firefox uses this file format to
# compress e. g. bookmark backups (*.jsonlz4).
#
# This file format is in fact just plain LZ4 data with a custom header (magic number [8 bytes] and
# uncompressed file size [4 bytes, little endian]).
#
####################################################################################################
#                                           DEPENDENCIES                                           #
####################################################################################################
#
# - Tested with Python 3.10
# - LZ4 bindings for Python, version 4.x: https://pypi.python.org/pypi/lz4
#
####################################################################################################
#                                             LICENSE                                              #
####################################################################################################
#
# Copyright (c) 2015-2022, Tilman Blumenbach
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions
#    and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of
#    conditions and the following disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import sys

import lz4.block


class BinFileArg:
    def __init__(self, mode):
        self._mode = mode

    def __call__(self, arg):
        objs = {
            "r": sys.stdin.buffer,
            "w": sys.stdout.buffer,
        }

        if arg == "-":
            return objs[self._mode]

        try:
            return open(arg, self._mode + "b")
        except OSError as e:
            raise argparse.ArgumentTypeError(
                "failed to open file for %s: %s" % (
                    "reading" if self._mode == "r" else "writing",
                    e
                )
            )


def decompress(file_obj):
    if file_obj.read(8) != b"mozLz40\0":
        raise ValueError("Invalid magic number")

    return lz4.block.decompress(file_obj.read())


def compress(file_obj):
    compressed = lz4.block.compress(file_obj.read())
    return b"mozLz40\0" + compressed


def get_argparser():
    p = argparse.ArgumentParser(
        description="MozLz4a compression/decompression utility"
    )

    p.add_argument(
        "-d", "--decompress", "--uncompress",
        action="store_true",
        help="Decompress the input file instead of compressing it."
    )

    p.add_argument(
        "in_file",
        type=BinFileArg("r"),
        help="Path to input file. `-' means standard input."
    )
    p.add_argument(
        "out_file",
        type=BinFileArg("w"),
        nargs="?",
        default="-",
        help="Path to output file. `-' means standard output (and is the default)."
    )

    return p


def main():
    args = get_argparser().parse_args()

    try:
        with args.in_file as fh:
            if args.decompress:
                data = decompress(fh)
            else:
                data = compress(fh)
    except Exception as e:
        print(
            "Could not compress/decompress file `%s': %s" % (
                args.in_file.name,
                e
            ),
            file=sys.stderr
        )
        sys.exit(4)

    try:
        with args.out_file as fh:
            fh.write(data)
    except Exception as e:
        print(
            "Could not write to output file `%s': %s" % (
                args.out_file.name,
                e
            ),
            file=sys.stderr
        )
        sys.exit(5)


if __name__ == "__main__":
    sys.exit(main())
