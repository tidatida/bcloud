# Copyright (C) 2014-2015 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

"""Calculate file hashes."""

import hashlib
import os
import zlib

_kChunkSize = 2 ** 20


def crc(path):
    _crc = 0
    file_stream = open(path, "rb")
    while True:
        chunk = file_stream.read(_kChunkSize)
        if not chunk:
            break
        _crc = zlib.crc32(chunk, _crc)
    file_stream.close()
    return "%X" % (_crc & 0xFFFFFFFF)

def md5(path, start=0, stop=-1):
    _md5 = hashlib.md5()
    file_stream = open(path, "rb")
    if start > 0:
        file_stream.seek(start)
    if stop == -1:
        stop = os.path.getsize(path)
    pos = start
    while pos < stop:
        size = min(_kChunkSize, stop - pos)
        chunk = file_stream.read(size)
        if not chunk:
            break
        pos += len(chunk)
        _md5.update(chunk)
    file_stream.close()
    return _md5.hexdigest()

def sha1(path):
    _sha1 = hashlib.sha1()
    file_stream = open(path, "rb")
    while True:
        chunk = file_stream.read(_kChunkSize)
        if not chunk:
            break
        _sha1.update(chunk)
    file_stream.close()
    return _sha1.hexdigest()

def sha224(path):
    _sha224 = hashlib.sha224()
    file_stream = open(path, "rb")
    while True:
        chunk = file_stream.read(_kChunkSize)
        if not chunk:
            break
        _sha224.update(chunk)
    file_stream.close()
    return _sha224.hexdigest()

def sha256(path):
    _sha256 = hashlib.sha256()
    file_stream = open(path, "rb")
    while True:
        chunk = file_stream.read(_kChunkSize)
        if not chunk:
            break
        _sha256.update(chunk)
    file_stream.close()
    return _sha256.hexdigest()

def sha384(path):
    _sha384 = hashlib.sha384()
    file_stream = open(path, "rb")
    while True:
        chunk = file_stream.read(_kChunkSize)
        if not chunk:
            break
        _sha384.update(chunk)
    file_stream.close()
    return _sha384.hexdigest()

def sha512(path):
    _sha512 = hashlib.sha512()
    file_stream = open(path, "rb")
    while True:
        chunk = file_stream.read(_kChunkSize)
        if not chunk:
            break
        _sha512.update(chunk)
    file_stream.close()
    return _sha512.hexdigest()
