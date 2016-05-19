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

def compress(data, compressionType = CompressionType.GZIP, compressLevel = 6):
    """
    Compresses specified data.
    data: The data to compress. MUST be byte data, not object or string data.
    compressionType: The compression format to use, as specified in CompressionType enum.
    compressLevel: Compression scale from 1-9. 1 being little compression, 9 being heavy compression.
    """
    if compressionType == CompressionType.GZIP:
        return zlib.compress(data, compressLevel)
    elif compressionType == CompressionType.BZIP2:
        return bz2.compress(data, compressLevel)
    elif compressionType == CompressionType.LZMA:
        return lzma.compress(data)
    else:
        return data

def decompress(data, compressionType = CompressionType.GZIP):
    """
    Decompresses specified data.
    data: The data to decompress. MUST be byte data, not object or string data.
    compressionType: The compression format to use, as specified in CompressionType enum.
    """
    if compressionType == CompressionType.GZIP:
        return zlib.decompress(data)
    elif compressionType == CompressionType.BZIP2:
        return bz2.decompress(data)
    elif compressionType == CompressionType.LZMA:
        return lzma.decompress(data)
    else:
        return data