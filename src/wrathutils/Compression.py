# The MIT License (MIT)
# Python Wrath Utils Copyright (c) 2016 Trent Spears

from enum import Enum
import zlib
import bz2
import lzma

class CompressionType(Enum):
    GZIP = 0
    BZIP2 = 1
    LZMA = 2

# Compresses specified data. compressionType is the format in CompressionType enum. compressLevel is compression scale from 1-9 - 1 being little compression, 9 being heavy compression.
def compress(data, compressionType = CompressionType.GZIP, compressLevel = 6):
    if compressionType == CompressionType.GZIP:
        return zlib.compress(data, level)
    elif compressionType == CompressionType.BZIP2:
        return bz2.compress(data, level)
    elif compressionType == CompressionType.LZMA:
        return lzma.compress(b(data))
    else:
        return data

# Decompresses specified data. compressionType is the format in CompressionType enum.
def decompress(data, compressionType = CompressionType.GZIP):
    if compressionType == CompressionType.GZIP:
        return zlib.decompress(data)
    elif compressionType == CompressionType.BZIP2:
        return bz2.decompress(data)
    elif compressionType == CompressionType.LZMA:
        return lzma.decompress(b(data))
    else:
        return data