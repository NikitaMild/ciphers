# -*- coding: utf-8 -*-

# This file was *autogenerated* from the file aes.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0xcf = Integer(0xcf); _sage_const_0x91 = Integer(0x91); _sage_const_0xcd = Integer(0xcd); _sage_const_0xcc = Integer(0xcc); _sage_const_0xcb = Integer(0xcb); _sage_const_0xca = Integer(0xca); _sage_const_0xb8 = Integer(0xb8); _sage_const_0xb9 = Integer(0xb9); _sage_const_0xb4 = Integer(0xb4); _sage_const_0xb5 = Integer(0xb5); _sage_const_0xb6 = Integer(0xb6); _sage_const_0xb7 = Integer(0xb7); _sage_const_0xb0 = Integer(0xb0); _sage_const_0xb1 = Integer(0xb1); _sage_const_0xb2 = Integer(0xb2); _sage_const_0xb3 = Integer(0xb3); _sage_const_0x73 = Integer(0x73); _sage_const_0x72 = Integer(0x72); _sage_const_0x71 = Integer(0x71); _sage_const_0xa3 = Integer(0xa3); _sage_const_0x77 = Integer(0x77); _sage_const_0x76 = Integer(0x76); _sage_const_0x75 = Integer(0x75); _sage_const_0x14 = Integer(0x14); _sage_const_0x90 = Integer(0x90); _sage_const_0x79 = Integer(0x79); _sage_const_0x78 = Integer(0x78); _sage_const_0x17 = Integer(0x17); _sage_const_0x4f = Integer(0x4f); _sage_const_0x4d = Integer(0x4d); _sage_const_0x4e = Integer(0x4e); _sage_const_0x4b = Integer(0x4b); _sage_const_0x4c = Integer(0x4c); _sage_const_0x4a = Integer(0x4a); _sage_const_0x11 = Integer(0x11); _sage_const_0xce = Integer(0xce); _sage_const_0x10 = Integer(0x10); _sage_const_0x13 = Integer(0x13); _sage_const_0x0d = Integer(0x0d); _sage_const_0xbd = Integer(0xbd); _sage_const_0xbe = Integer(0xbe); _sage_const_0xbf = Integer(0xbf); _sage_const_0xba = Integer(0xba); _sage_const_0xbb = Integer(0xbb); _sage_const_0xbc = Integer(0xbc); _sage_const_10 = Integer(10); _sage_const_16 = Integer(16); _sage_const_0xc9 = Integer(0xc9); _sage_const_0xc8 = Integer(0xc8); _sage_const_0xc7 = Integer(0xc7); _sage_const_0xc6 = Integer(0xc6); _sage_const_0xc5 = Integer(0xc5); _sage_const_0xc4 = Integer(0xc4); _sage_const_0xc3 = Integer(0xc3); _sage_const_0xc2 = Integer(0xc2); _sage_const_0xc1 = Integer(0xc1); _sage_const_0xc0 = Integer(0xc0); _sage_const_0x46 = Integer(0x46); _sage_const_0x47 = Integer(0x47); _sage_const_0x44 = Integer(0x44); _sage_const_0x45 = Integer(0x45); _sage_const_0x42 = Integer(0x42); _sage_const_0x43 = Integer(0x43); _sage_const_0x40 = Integer(0x40); _sage_const_0x41 = Integer(0x41); _sage_const_0x48 = Integer(0x48); _sage_const_0x49 = Integer(0x49); _sage_const_0x7c = Integer(0x7c); _sage_const_0x7b = Integer(0x7b); _sage_const_0x7a = Integer(0x7a); _sage_const_0x7f = Integer(0x7f); _sage_const_0x7e = Integer(0x7e); _sage_const_0x7d = Integer(0x7d); _sage_const_0x86 = Integer(0x86); _sage_const_0x2e = Integer(0x2e); _sage_const_0xf8 = Integer(0xf8); _sage_const_0x8c = Integer(0x8c); _sage_const_0x59 = Integer(0x59); _sage_const_0x58 = Integer(0x58); _sage_const_0xb = Integer(0xb); _sage_const_0xe = Integer(0xe); _sage_const_0x03 = Integer(0x03); _sage_const_0x51 = Integer(0x51); _sage_const_0x50 = Integer(0x50); _sage_const_0x53 = Integer(0x53); _sage_const_0x52 = Integer(0x52); _sage_const_0x55 = Integer(0x55); _sage_const_0x54 = Integer(0x54); _sage_const_0x57 = Integer(0x57); _sage_const_0x56 = Integer(0x56); _sage_const_0x01 = Integer(0x01); _sage_const_0xe1 = Integer(0xe1); _sage_const_0x2d = Integer(0x2d); _sage_const_0x06 = Integer(0x06); _sage_const_0x2f = Integer(0x2f); _sage_const_0x2a = Integer(0x2a); _sage_const_0x2b = Integer(0x2b); _sage_const_0x2c = Integer(0x2c); _sage_const_0x0b = Integer(0x0b); _sage_const_0xac = Integer(0xac); _sage_const_0x0c = Integer(0x0c); _sage_const_0x05 = Integer(0x05); _sage_const_0xae = Integer(0xae); _sage_const_0xe0 = Integer(0xe0); _sage_const_0x0a = Integer(0x0a); _sage_const_0x0f = Integer(0x0f); _sage_const_0x3e = Integer(0x3e); _sage_const_0x3d = Integer(0x3d); _sage_const_0x28 = Integer(0x28); _sage_const_0x29 = Integer(0x29); _sage_const_0x24 = Integer(0x24); _sage_const_0x25 = Integer(0x25); _sage_const_0x26 = Integer(0x26); _sage_const_0x27 = Integer(0x27); _sage_const_0x20 = Integer(0x20); _sage_const_0x21 = Integer(0x21); _sage_const_0x22 = Integer(0x22); _sage_const_0x23 = Integer(0x23); _sage_const_0x5a = Integer(0x5a); _sage_const_0x5c = Integer(0x5c); _sage_const_0x5b = Integer(0x5b); _sage_const_0x5e = Integer(0x5e); _sage_const_0x5d = Integer(0x5d); _sage_const_0x5f = Integer(0x5f); _sage_const_2 = Integer(2); _sage_const_0xa9 = Integer(0xa9); _sage_const_0x32 = Integer(0x32); _sage_const_0xf0 = Integer(0xf0); _sage_const_0xf1 = Integer(0xf1); _sage_const_0xf2 = Integer(0xf2); _sage_const_0xf3 = Integer(0xf3); _sage_const_0xf4 = Integer(0xf4); _sage_const_0xf5 = Integer(0xf5); _sage_const_0xf6 = Integer(0xf6); _sage_const_0xf7 = Integer(0xf7); _sage_const_0x8b = Integer(0x8b); _sage_const_0xf9 = Integer(0xf9); _sage_const_0x16 = Integer(0x16); _sage_const_0x8a = Integer(0x8a); _sage_const_0x8f = Integer(0x8f); _sage_const_0xd = Integer(0xd); _sage_const_0x8d = Integer(0x8d); _sage_const_0x8e = Integer(0x8e); _sage_const_0xa5 = Integer(0xa5); _sage_const_0xa4 = Integer(0xa4); _sage_const_0xa7 = Integer(0xa7); _sage_const_0x9f = Integer(0x9f); _sage_const_0xa1 = Integer(0xa1); _sage_const_0xa0 = Integer(0xa0); _sage_const_0x39 = Integer(0x39); _sage_const_0xa2 = Integer(0xa2); _sage_const_0x37 = Integer(0x37); _sage_const_0x36 = Integer(0x36); _sage_const_0x35 = Integer(0x35); _sage_const_0x34 = Integer(0x34); _sage_const_0x33 = Integer(0x33); _sage_const_0xa8 = Integer(0xa8); _sage_const_0x31 = Integer(0x31); _sage_const_0x30 = Integer(0x30); _sage_const_0xea = Integer(0xea); _sage_const_0xe7 = Integer(0xe7); _sage_const_0x74 = Integer(0x74); _sage_const_0x0e = Integer(0x0e); _sage_const_0xe6 = Integer(0xe6); _sage_const_0x97 = Integer(0x97); _sage_const_0x9 = Integer(0x9); _sage_const_0xfa = Integer(0xfa); _sage_const_0xfb = Integer(0xfb); _sage_const_0xfc = Integer(0xfc); _sage_const_0xfd = Integer(0xfd); _sage_const_0xfe = Integer(0xfe); _sage_const_0xff = Integer(0xff); _sage_const_0x1d = Integer(0x1d); _sage_const_0x82 = Integer(0x82); _sage_const_0x83 = Integer(0x83); _sage_const_0x80 = Integer(0x80); _sage_const_0x81 = Integer(0x81); _sage_const_0x88 = Integer(0x88); _sage_const_0x87 = Integer(0x87); _sage_const_0x84 = Integer(0x84); _sage_const_0x85 = Integer(0x85); _sage_const_0x1f = Integer(0x1f); _sage_const_0x1e = Integer(0x1e); _sage_const_6 = Integer(6); _sage_const_0x64 = Integer(0x64); _sage_const_0x92 = Integer(0x92); _sage_const_8 = Integer(8); _sage_const_0x66 = Integer(0x66); _sage_const_0x89 = Integer(0x89); _sage_const_0x67 = Integer(0x67); _sage_const_0x9a = Integer(0x9a); _sage_const_0x02 = Integer(0x02); _sage_const_0xad = Integer(0xad); _sage_const_0x00 = Integer(0x00); _sage_const_0xaf = Integer(0xaf); _sage_const_0xaa = Integer(0xaa); _sage_const_0x07 = Integer(0x07); _sage_const_0x04 = Integer(0x04); _sage_const_0xab = Integer(0xab); _sage_const_0x3f = Integer(0x3f); _sage_const_0x08 = Integer(0x08); _sage_const_0x09 = Integer(0x09); _sage_const_0x3c = Integer(0x3c); _sage_const_0x3b = Integer(0x3b); _sage_const_0x3a = Integer(0x3a); _sage_const_3 = Integer(3); _sage_const_0x38 = Integer(0x38); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_0x99 = Integer(0x99); _sage_const_0x98 = Integer(0x98); _sage_const_4 = Integer(4); _sage_const_0x95 = Integer(0x95); _sage_const_0x94 = Integer(0x94); _sage_const_0xec = Integer(0xec); _sage_const_0x96 = Integer(0x96); _sage_const_0xee = Integer(0xee); _sage_const_0xed = Integer(0xed); _sage_const_0x93 = Integer(0x93); _sage_const_0xef = Integer(0xef); _sage_const_0xd6 = Integer(0xd6); _sage_const_0xd7 = Integer(0xd7); _sage_const_0xd4 = Integer(0xd4); _sage_const_0xd5 = Integer(0xd5); _sage_const_0xd2 = Integer(0xd2); _sage_const_0xd3 = Integer(0xd3); _sage_const_0xd0 = Integer(0xd0); _sage_const_0xd1 = Integer(0xd1); _sage_const_0xd8 = Integer(0xd8); _sage_const_0xd9 = Integer(0xd9); _sage_const_0xeb = Integer(0xeb); _sage_const_0x15 = Integer(0x15); _sage_const_0x6a = Integer(0x6a); _sage_const_0x6b = Integer(0x6b); _sage_const_0x6c = Integer(0x6c); _sage_const_0x6d = Integer(0x6d); _sage_const_0x6e = Integer(0x6e); _sage_const_0x6f = Integer(0x6f); _sage_const_0x12 = Integer(0x12); _sage_const_0x70 = Integer(0x70); _sage_const_0x19 = Integer(0x19); _sage_const_0x18 = Integer(0x18); _sage_const_0xdf = Integer(0xdf); _sage_const_0xdd = Integer(0xdd); _sage_const_0xde = Integer(0xde); _sage_const_0xdb = Integer(0xdb); _sage_const_0xdc = Integer(0xdc); _sage_const_0xda = Integer(0xda); _sage_const_0xa6 = Integer(0xa6); _sage_const_0xe9 = Integer(0xe9); _sage_const_0xe8 = Integer(0xe8); _sage_const_0x9e = Integer(0x9e); _sage_const_0x9d = Integer(0x9d); _sage_const_0xe3 = Integer(0xe3); _sage_const_0xe2 = Integer(0xe2); _sage_const_0xe5 = Integer(0xe5); _sage_const_0xe4 = Integer(0xe4); _sage_const_0x9c = Integer(0x9c); _sage_const_0x9b = Integer(0x9b); _sage_const_0x60 = Integer(0x60); _sage_const_0x61 = Integer(0x61); _sage_const_0x62 = Integer(0x62); _sage_const_0x63 = Integer(0x63); _sage_const_0x1a = Integer(0x1a); _sage_const_0x65 = Integer(0x65); _sage_const_0x1c = Integer(0x1c); _sage_const_0x1b = Integer(0x1b); _sage_const_0x68 = Integer(0x68); _sage_const_0x69 = Integer(0x69)
from array import array
from collections import deque
from sage.crypto.util import bin_to_ascii
from getpass import getpass
from functools import wraps

Sbox = array('i',
            [_sage_const_0x63 , _sage_const_0x7c , _sage_const_0x77 , _sage_const_0x7b , _sage_const_0xf2 , _sage_const_0x6b , _sage_const_0x6f , _sage_const_0xc5 , _sage_const_0x30 , _sage_const_0x01 , _sage_const_0x67 , _sage_const_0x2b , _sage_const_0xfe , _sage_const_0xd7 , _sage_const_0xab , _sage_const_0x76 ,
            _sage_const_0xca , _sage_const_0x82 , _sage_const_0xc9 , _sage_const_0x7d , _sage_const_0xfa , _sage_const_0x59 , _sage_const_0x47 , _sage_const_0xf0 , _sage_const_0xad , _sage_const_0xd4 , _sage_const_0xa2 , _sage_const_0xaf , _sage_const_0x9c , _sage_const_0xa4 , _sage_const_0x72 , _sage_const_0xc0 ,
            _sage_const_0xb7 , _sage_const_0xfd , _sage_const_0x93 , _sage_const_0x26 , _sage_const_0x36 , _sage_const_0x3f , _sage_const_0xf7 , _sage_const_0xcc , _sage_const_0x34 , _sage_const_0xa5 , _sage_const_0xe5 , _sage_const_0xf1 , _sage_const_0x71 , _sage_const_0xd8 , _sage_const_0x31 , _sage_const_0x15 ,
            _sage_const_0x04 , _sage_const_0xc7 , _sage_const_0x23 , _sage_const_0xc3 , _sage_const_0x18 , _sage_const_0x96 , _sage_const_0x05 , _sage_const_0x9a , _sage_const_0x07 , _sage_const_0x12 , _sage_const_0x80 , _sage_const_0xe2 , _sage_const_0xeb , _sage_const_0x27 , _sage_const_0xb2 , _sage_const_0x75 ,
            _sage_const_0x09 , _sage_const_0x83 , _sage_const_0x2c , _sage_const_0x1a , _sage_const_0x1b , _sage_const_0x6e , _sage_const_0x5a , _sage_const_0xa0 , _sage_const_0x52 , _sage_const_0x3b , _sage_const_0xd6 , _sage_const_0xb3 , _sage_const_0x29 , _sage_const_0xe3 , _sage_const_0x2f , _sage_const_0x84 ,
            _sage_const_0x53 , _sage_const_0xd1 , _sage_const_0x00 , _sage_const_0xed , _sage_const_0x20 , _sage_const_0xfc , _sage_const_0xb1 , _sage_const_0x5b , _sage_const_0x6a , _sage_const_0xcb , _sage_const_0xbe , _sage_const_0x39 , _sage_const_0x4a , _sage_const_0x4c , _sage_const_0x58 , _sage_const_0xcf ,
            _sage_const_0xd0 , _sage_const_0xef , _sage_const_0xaa , _sage_const_0xfb , _sage_const_0x43 , _sage_const_0x4d , _sage_const_0x33 , _sage_const_0x85 , _sage_const_0x45 , _sage_const_0xf9 , _sage_const_0x02 , _sage_const_0x7f , _sage_const_0x50 , _sage_const_0x3c , _sage_const_0x9f , _sage_const_0xa8 ,
            _sage_const_0x51 , _sage_const_0xa3 , _sage_const_0x40 , _sage_const_0x8f , _sage_const_0x92 , _sage_const_0x9d , _sage_const_0x38 , _sage_const_0xf5 , _sage_const_0xbc , _sage_const_0xb6 , _sage_const_0xda , _sage_const_0x21 , _sage_const_0x10 , _sage_const_0xff , _sage_const_0xf3 , _sage_const_0xd2 ,
            _sage_const_0xcd , _sage_const_0x0c , _sage_const_0x13 , _sage_const_0xec , _sage_const_0x5f , _sage_const_0x97 , _sage_const_0x44 , _sage_const_0x17 , _sage_const_0xc4 , _sage_const_0xa7 , _sage_const_0x7e , _sage_const_0x3d , _sage_const_0x64 , _sage_const_0x5d , _sage_const_0x19 , _sage_const_0x73 ,
            _sage_const_0x60 , _sage_const_0x81 , _sage_const_0x4f , _sage_const_0xdc , _sage_const_0x22 , _sage_const_0x2a , _sage_const_0x90 , _sage_const_0x88 , _sage_const_0x46 , _sage_const_0xee , _sage_const_0xb8 , _sage_const_0x14 , _sage_const_0xde , _sage_const_0x5e , _sage_const_0x0b , _sage_const_0xdb ,
            _sage_const_0xe0 , _sage_const_0x32 , _sage_const_0x3a , _sage_const_0x0a , _sage_const_0x49 , _sage_const_0x06 , _sage_const_0x24 , _sage_const_0x5c , _sage_const_0xc2 , _sage_const_0xd3 , _sage_const_0xac , _sage_const_0x62 , _sage_const_0x91 , _sage_const_0x95 , _sage_const_0xe4 , _sage_const_0x79 ,
            _sage_const_0xe7 , _sage_const_0xc8 , _sage_const_0x37 , _sage_const_0x6d , _sage_const_0x8d , _sage_const_0xd5 , _sage_const_0x4e , _sage_const_0xa9 , _sage_const_0x6c , _sage_const_0x56 , _sage_const_0xf4 , _sage_const_0xea , _sage_const_0x65 , _sage_const_0x7a , _sage_const_0xae , _sage_const_0x08 ,
            _sage_const_0xba , _sage_const_0x78 , _sage_const_0x25 , _sage_const_0x2e , _sage_const_0x1c , _sage_const_0xa6 , _sage_const_0xb4 , _sage_const_0xc6 , _sage_const_0xe8 , _sage_const_0xdd , _sage_const_0x74 , _sage_const_0x1f , _sage_const_0x4b , _sage_const_0xbd , _sage_const_0x8b , _sage_const_0x8a ,
            _sage_const_0x70 , _sage_const_0x3e , _sage_const_0xb5 , _sage_const_0x66 , _sage_const_0x48 , _sage_const_0x03 , _sage_const_0xf6 , _sage_const_0x0e , _sage_const_0x61 , _sage_const_0x35 , _sage_const_0x57 , _sage_const_0xb9 , _sage_const_0x86 , _sage_const_0xc1 , _sage_const_0x1d , _sage_const_0x9e ,
            _sage_const_0xe1 , _sage_const_0xf8 , _sage_const_0x98 , _sage_const_0x11 , _sage_const_0x69 , _sage_const_0xd9 , _sage_const_0x8e , _sage_const_0x94 , _sage_const_0x9b , _sage_const_0x1e , _sage_const_0x87 , _sage_const_0xe9 , _sage_const_0xce , _sage_const_0x55 , _sage_const_0x28 , _sage_const_0xdf ,
            _sage_const_0x8c , _sage_const_0xa1 , _sage_const_0x89 , _sage_const_0x0d , _sage_const_0xbf , _sage_const_0xe6 , _sage_const_0x42 , _sage_const_0x68 , _sage_const_0x41 , _sage_const_0x99 , _sage_const_0x2d , _sage_const_0x0f , _sage_const_0xb0 , _sage_const_0x54 , _sage_const_0xbb , _sage_const_0x16 ]
    )
InvSbox = array('i',
        [_sage_const_0x52 , _sage_const_0x09 , _sage_const_0x6a , _sage_const_0xd5 , _sage_const_0x30 , _sage_const_0x36 , _sage_const_0xa5 , _sage_const_0x38 , _sage_const_0xbf , _sage_const_0x40 , _sage_const_0xa3 , _sage_const_0x9e , _sage_const_0x81 , _sage_const_0xf3 , _sage_const_0xd7 , _sage_const_0xfb ,
        _sage_const_0x7c , _sage_const_0xe3 , _sage_const_0x39 , _sage_const_0x82 , _sage_const_0x9b , _sage_const_0x2f , _sage_const_0xff , _sage_const_0x87 , _sage_const_0x34 , _sage_const_0x8e , _sage_const_0x43 , _sage_const_0x44 , _sage_const_0xc4 , _sage_const_0xde , _sage_const_0xe9 , _sage_const_0xcb ,
        _sage_const_0x54 , _sage_const_0x7b , _sage_const_0x94 , _sage_const_0x32 , _sage_const_0xa6 , _sage_const_0xc2 , _sage_const_0x23 , _sage_const_0x3d , _sage_const_0xee , _sage_const_0x4c , _sage_const_0x95 , _sage_const_0x0b , _sage_const_0x42 , _sage_const_0xfa , _sage_const_0xc3 , _sage_const_0x4e ,
        _sage_const_0x08 , _sage_const_0x2e , _sage_const_0xa1 , _sage_const_0x66 , _sage_const_0x28 , _sage_const_0xd9 , _sage_const_0x24 , _sage_const_0xb2 , _sage_const_0x76 , _sage_const_0x5b , _sage_const_0xa2 , _sage_const_0x49 , _sage_const_0x6d , _sage_const_0x8b , _sage_const_0xd1 , _sage_const_0x25 ,
        _sage_const_0x72 , _sage_const_0xf8 , _sage_const_0xf6 , _sage_const_0x64 , _sage_const_0x86 , _sage_const_0x68 , _sage_const_0x98 , _sage_const_0x16 , _sage_const_0xd4 , _sage_const_0xa4 , _sage_const_0x5c , _sage_const_0xcc , _sage_const_0x5d , _sage_const_0x65 , _sage_const_0xb6 , _sage_const_0x92 ,
        _sage_const_0x6c , _sage_const_0x70 , _sage_const_0x48 , _sage_const_0x50 , _sage_const_0xfd , _sage_const_0xed , _sage_const_0xb9 , _sage_const_0xda , _sage_const_0x5e , _sage_const_0x15 , _sage_const_0x46 , _sage_const_0x57 , _sage_const_0xa7 , _sage_const_0x8d , _sage_const_0x9d , _sage_const_0x84 ,
        _sage_const_0x90 , _sage_const_0xd8 , _sage_const_0xab , _sage_const_0x00 , _sage_const_0x8c , _sage_const_0xbc , _sage_const_0xd3 , _sage_const_0x0a , _sage_const_0xf7 , _sage_const_0xe4 , _sage_const_0x58 , _sage_const_0x05 , _sage_const_0xb8 , _sage_const_0xb3 , _sage_const_0x45 , _sage_const_0x06 ,
        _sage_const_0xd0 , _sage_const_0x2c , _sage_const_0x1e , _sage_const_0x8f , _sage_const_0xca , _sage_const_0x3f , _sage_const_0x0f , _sage_const_0x02 , _sage_const_0xc1 , _sage_const_0xaf , _sage_const_0xbd , _sage_const_0x03 , _sage_const_0x01 , _sage_const_0x13 , _sage_const_0x8a , _sage_const_0x6b ,
        _sage_const_0x3a , _sage_const_0x91 , _sage_const_0x11 , _sage_const_0x41 , _sage_const_0x4f , _sage_const_0x67 , _sage_const_0xdc , _sage_const_0xea , _sage_const_0x97 , _sage_const_0xf2 , _sage_const_0xcf , _sage_const_0xce , _sage_const_0xf0 , _sage_const_0xb4 , _sage_const_0xe6 , _sage_const_0x73 ,
        _sage_const_0x96 , _sage_const_0xac , _sage_const_0x74 , _sage_const_0x22 , _sage_const_0xe7 , _sage_const_0xad , _sage_const_0x35 , _sage_const_0x85 , _sage_const_0xe2 , _sage_const_0xf9 , _sage_const_0x37 , _sage_const_0xe8 , _sage_const_0x1c , _sage_const_0x75 , _sage_const_0xdf , _sage_const_0x6e ,
        _sage_const_0x47 , _sage_const_0xf1 , _sage_const_0x1a , _sage_const_0x71 , _sage_const_0x1d , _sage_const_0x29 , _sage_const_0xc5 , _sage_const_0x89 , _sage_const_0x6f , _sage_const_0xb7 , _sage_const_0x62 , _sage_const_0x0e , _sage_const_0xaa , _sage_const_0x18 , _sage_const_0xbe , _sage_const_0x1b ,
        _sage_const_0xfc , _sage_const_0x56 , _sage_const_0x3e , _sage_const_0x4b , _sage_const_0xc6 , _sage_const_0xd2 , _sage_const_0x79 , _sage_const_0x20 , _sage_const_0x9a , _sage_const_0xdb , _sage_const_0xc0 , _sage_const_0xfe , _sage_const_0x78 , _sage_const_0xcd , _sage_const_0x5a , _sage_const_0xf4 ,
        _sage_const_0x1f , _sage_const_0xdd , _sage_const_0xa8 , _sage_const_0x33 , _sage_const_0x88 , _sage_const_0x07 , _sage_const_0xc7 , _sage_const_0x31 , _sage_const_0xb1 , _sage_const_0x12 , _sage_const_0x10 , _sage_const_0x59 , _sage_const_0x27 , _sage_const_0x80 , _sage_const_0xec , _sage_const_0x5f ,
        _sage_const_0x60 , _sage_const_0x51 , _sage_const_0x7f , _sage_const_0xa9 , _sage_const_0x19 , _sage_const_0xb5 , _sage_const_0x4a , _sage_const_0x0d , _sage_const_0x2d , _sage_const_0xe5 , _sage_const_0x7a , _sage_const_0x9f , _sage_const_0x93 , _sage_const_0xc9 , _sage_const_0x9c , _sage_const_0xef ,
        _sage_const_0xa0 , _sage_const_0xe0 , _sage_const_0x3b , _sage_const_0x4d , _sage_const_0xae , _sage_const_0x2a , _sage_const_0xf5 , _sage_const_0xb0 , _sage_const_0xc8 , _sage_const_0xeb , _sage_const_0xbb , _sage_const_0x3c , _sage_const_0x83 , _sage_const_0x53 , _sage_const_0x99 , _sage_const_0x61 ,
        _sage_const_0x17 , _sage_const_0x2b , _sage_const_0x04 , _sage_const_0x7e , _sage_const_0xba , _sage_const_0x77 , _sage_const_0xd6 , _sage_const_0x26 , _sage_const_0xe1 , _sage_const_0x69 , _sage_const_0x14 , _sage_const_0x63 , _sage_const_0x55 , _sage_const_0x21 , _sage_const_0x0c , _sage_const_0x7d ]
        )
Rcon = [
        [_sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x01 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x02 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x04 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x08 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x10 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x20 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x40 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x80 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x1b , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ],
        [_sage_const_0x36 , _sage_const_0x00 , _sage_const_0x00 , _sage_const_0x00 ]
        ]


def openfile(name):
    f = open(name,'r')
    print f.read()
    return f

class AES(object):
    def __init__(self, object=None):
        self.Nb = _sage_const_4 
        self.Nk = _sage_const_4 
        self.Nr = _sage_const_10 
        self.key = object[_sage_const_1 ]
        self.inputblock = matrix(SR, self.Nb, self.Nk,
                                [ord(x) for x in object[_sage_const_0 ]]).transpose()
        self.state = matrix(SR, self.Nb, _sage_const_4 )
        self.inputkey = matrix(SR, _sage_const_4 , self.Nk, [ord(x) for x in self.key])
        self.keystorage = []
        self.roundkey = []
        self.polynom = matrix(SR,[[_sage_const_2 ,_sage_const_3 ,_sage_const_1 ,_sage_const_1 ],
                                  [_sage_const_1 ,_sage_const_2 ,_sage_const_3 ,_sage_const_1 ],
                                  [_sage_const_1 ,_sage_const_1 ,_sage_const_2 ,_sage_const_3 ],
                                  [_sage_const_3 ,_sage_const_1 ,_sage_const_1 ,_sage_const_2 ]])
        self.Invpolynom = matrix(SR,[[_sage_const_0xe , _sage_const_0xb , _sage_const_0xd ,_sage_const_0x9 ],
                                    [_sage_const_0x9 , _sage_const_0xe , _sage_const_0xb , _sage_const_0xd ],
                                    [_sage_const_0xd , _sage_const_0x9 , _sage_const_0xe , _sage_const_0xb ],
                                    [_sage_const_0xb , _sage_const_0xd , _sage_const_0x9 , _sage_const_0xe ]])

    def prettyprint(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            printf = func(*args, **kwargs)
            print '-'*len(printf)
            print printf
            print '-'*len(printf)
            return func(*args, **kwargs)
        return wrapped

    @staticmethod
    def SubWord(word):
        word = AES.RotWordLeft(word,_sage_const_1 ,None)
        for j in range(len(word)):
            sbox_row = int(word[j]) // _sage_const_0x10 
            sbox_col = int(word[j]) % _sage_const_0x10 
            sbox_elem = int(Sbox[_sage_const_16  * sbox_row + sbox_col])
            word[j] = sbox_elem
        return word

    @staticmethod
    def RotWordLeft(word, position, flag):
        q = deque(word)
        if flag is None:
            q.rotate(-position)
        elif flag == 'Inv':
            q.rotate(position)
        word = list(q)
        return word

    def xor_lists(self,list1, list2):
        xor_list = []
        for i in range(len(list1)):
            xor_list.append(int(list1[i]).__xor__(int(list2[i])))
        return xor_list

    def KeyExpansion(self):
        counter = self.Nb * (self.Nr + _sage_const_1 )
        inputkey_t = self.inputkey.transpose()
        for i in range(self.Nk):
            self.keystorage.append(list(inputkey_t[i]))
        for i in range(self.Nk, counter):
            temp = self.keystorage[i - _sage_const_1 ]
            if not mod(i, self.Nk):
                temp = self.xor_lists(AES.SubWord(temp), (Rcon[i // self.Nk]))
            elif self.Nk > _sage_const_6  and mod(i, self.Nk) == _sage_const_4 :
                temp = AES.SubWord(temp)
            self.keystorage.append(self.xor_lists(
                                  self.keystorage[i - self.Nk], temp))

    def AddRoundKey(self,number):
        counter = number *_sage_const_4 
        self.roundkey = matrix(SR, _sage_const_4 , _sage_const_4 , [self.keystorage[i]
                              for i in range(counter,counter+_sage_const_4 )]).transpose()
        tmp = []
        for i in range(_sage_const_4 ):
            tmp.append(self.xor_lists(
                      list(self.state[i]), list(self.roundkey[i])))
        self.state = matrix(SR, _sage_const_4 , _sage_const_4 , tmp)

    def SubBytes(self,flag=None):
        if flag is None:
            sbox = Sbox
        elif flag == 'Inv':
            sbox = InvSbox
        for i in range(self.Nb):
            for j in range(_sage_const_4 ):
                self.state[i, j] = sbox[self.state[i, j]]

    def ShiftRow(self, flag=None):
        new_state = []
        for x in ((self.state[i], i) for i in range(self.Nb)):
            new_state.append(AES.RotWordLeft(list(x[_sage_const_0 ]), x[_sage_const_1 ], flag))
        self.state = matrix(SR, self.Nb, _sage_const_4 , new_state)

    def MixColumns(self,flag=None):
        if flag is None:
            poly = self.polynom
        elif flag == 'Inv':
            poly = self.Invpolynom
        new_state = []
        q = self.state.transpose()
        F=GF(_sage_const_2 **_sage_const_8 , 'x')
        for f in range(_sage_const_4 ):
            tmp = []
            for i in range(self.Nb):
                res=_sage_const_0 
                for j in range(_sage_const_4 ):
                    row = [int(x) for x in bin(poly[i,j])[_sage_const_2 :]][::-_sage_const_1 ]
                    col = [int(x) for x in bin(q[f,j])[_sage_const_2 :]][::-_sage_const_1 ]
                    res += F(row)*F(col)
                tmp.append(F(res).integer_representation())
            new_state.append(tmp)
        self.state = matrix(SR,new_state).transpose()

    @prettyprint
    def encrypt_to_msg(self,encrypt_file):
        #encrypt_file = raw_input("enter filename for encrypted message: ")
        with open('encrypt.txt', 'w') as f:
            for item in self.encrypt:
                for x in item:
                    f.write("%s," % x)
            f.close()
            printf = "you message has been decrypt into {} file".format(encrypt_file)
            return printf


    def encrypt(self):
        for i in range(_sage_const_4 ):
            for j in range(self.Nb):
                self.state[i, j] = self.inputblock[(i + _sage_const_4 *j)//_sage_const_4 , (i + _sage_const_4 *j) % _sage_const_4 ]
        self.KeyExpansion()
        self.AddRoundKey(_sage_const_0 )
        for i in range(_sage_const_1 , self.Nr):
             self.SubBytes()
             self.ShiftRow()
             self.MixColumns()
             self.AddRoundKey(i)
        self.SubBytes()
        self.ShiftRow()
        self.AddRoundKey(self.Nr)
        self.encrypt = list(self.state)
        self.encrypt_to_msg('encrypt.txt')

    @prettyprint
    def dec_to_msg(self,decrypt_file):
        #decrypt_file = raw_input("enter filename for decrypted message: ")
        decrypt = ""
        dec_msg = [str(unichr(x)) for q in self.state for x in list(q)]
        for x in dec_msg:
            decrypt += x
        f = open('decrypt.txt','w')
        f.write(decrypt)
        f.close()
        printf = "you message has been decrypt into {} file".format(decrypt_file)
        return printf

    def decrypt(self):
        self.AddRoundKey(self.Nr)
        for i in range(self.Nr-_sage_const_1 ,_sage_const_0 ,-_sage_const_1 ):
            self.ShiftRow(flag='Inv')
            self.SubBytes(flag='Inv')
            self.AddRoundKey(i)
            self.MixColumns(flag='Inv')
        self.ShiftRow(flag='Inv')
        self.SubBytes(flag='Inv')
        self.AddRoundKey(_sage_const_0 )
        self.dec_to_msg('decrypt.txt')

    def run(self):
        self.encrypt()
        self.decrypt()

def main():
    #filename = raw_input("please, enter filename for encrypt: ")
    #print "enter secret key: "
    #key_valuve = getpass(prompt='enter secret key: ')
    #msg = openfile(filename)
    data_storage = ['mytestbigmessage', 'kekacheburekaloh']
    aes = AES(data_storage)
    aes.run()


if __name__ == '__main__':
    main()

