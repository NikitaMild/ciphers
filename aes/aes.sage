# -*- coding: utf-8 -*-
from array import array
from collections import deque
from sage.crypto.util import bin_to_ascii
from getpass import getpass
from functools import wraps
import hashlib

Sbox = array('i',
            [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
    )
InvSbox = array('i',
        [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
        )
Rcon = [
        [0x00, 0x00, 0x00, 0x00],
        [0x01, 0x00, 0x00, 0x00],
        [0x02, 0x00, 0x00, 0x00],
        [0x04, 0x00, 0x00, 0x00],
        [0x08, 0x00, 0x00, 0x00],
        [0x10, 0x00, 0x00, 0x00],
        [0x20, 0x00, 0x00, 0x00],
        [0x40, 0x00, 0x00, 0x00],
        [0x80, 0x00, 0x00, 0x00],
        [0x1b, 0x00, 0x00, 0x00],
        [0x36, 0x00, 0x00, 0x00]
        ]


def openfile(name):
    f = open(name,'r')
    string = f.read()
    return string


class AES(object):
    def __init__(self, object=None):
        self.Nb = 4
        self.Nk = 4
        self.Nr = 10
        self.msg = object[0]
        self.key = object[1]
        self.state = matrix(SR, self.Nb, 4)
        self.inputkey = matrix(SR, 4, self.Nk, [ord(x) for x in self.key])
        self.keystorage = []
        self.roundkey = []
        self.decrypto = ""
        self.padding = 0
        self.polynom = matrix(SR,[[2,3,1,1],
                                  [1,2,3,1],
                                  [1,1,2,3],
                                  [3,1,1,2]])
        self.Invpolynom = matrix(SR,[[0xe, 0xb, 0xd,0x9],
                                    [0x9, 0xe, 0xb, 0xd],
                                    [0xd, 0x9, 0xe, 0xb],
                                    [0xb, 0xd, 0x9, 0xe]])


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
        word = AES.RotWordLeft(word,1,None)
        for j in range(len(word)):
            sbox_row = int(word[j]) // 0x10
            sbox_col = int(word[j]) % 0x10
            sbox_elem = int(Sbox[16 * sbox_row + sbox_col])
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
        counter = self.Nb * (self.Nr + 1)
        inputkey_t = self.inputkey.transpose()
        for i in range(self.Nk):
            self.keystorage.append(list(inputkey_t[i]))
        for i in range(self.Nk, counter):
            temp = self.keystorage[i - 1]
            if not mod(i, self.Nk):
                temp = self.xor_lists(AES.SubWord(temp), (Rcon[i // self.Nk]))
            elif self.Nk > 6 and mod(i, self.Nk) == 4:
                temp = AES.SubWord(temp)
            self.keystorage.append(self.xor_lists(
                                  self.keystorage[i - self.Nk], temp))

    def AddRoundKey(self,number):
        counter = number*4
        self.roundkey = matrix(SR, 4, 4, [self.keystorage[i]
                              for i in range(counter,counter+4)]).transpose()
        tmp = []
        for i in range(4):
            tmp.append(self.xor_lists(
                      list(self.state[i]), list(self.roundkey[i])))
        self.state = matrix(SR, 4, 4, tmp)

    def SubBytes(self,flag=None):
        if flag is None:
            sbox = Sbox
        elif flag == 'Inv':
            sbox = InvSbox
        for i in range(self.Nb):
            for j in range(4):
                self.state[i, j] = sbox[self.state[i, j]]

    def ShiftRow(self, flag=None):
        new_state = []
        for x in ((self.state[i], i) for i in range(self.Nb)):
            new_state.append(AES.RotWordLeft(list(x[0]), x[1], flag))
        self.state = matrix(SR, self.Nb, 4, new_state)

    def MixColumns(self,flag=None):
        if flag is None:
            poly = self.polynom
        elif flag == 'Inv':
            poly = self.Invpolynom
        new_state = []
        q = self.state.transpose()
        F = GF(2**8, 'x')
        for f in range(4):
            new_state_column = []
            for i in range(self.Nb):
                res=0
                for j in range(4):
                    row = [int(x) for x in bin(poly[i,j])[2:]][::-1]
                    col = [int(x) for x in bin(q[f,j])[2:]][::-1]
                    res += F(row)*F(col)
                new_state_column.append(F(res).integer_representation())
            new_state.append(new_state_column)
        self.state = matrix(SR,new_state).transpose()

    @prettyprint
    def encrypt_to_msg(self,encrypt_file):
        with open('encrypt.txt', 'w') as file:
            for string in self.encrypt:
                for item in string:
                    for x in item:
                        file.write("%s," % x)
            file.close()
            printf = "you message has been encrypt into {} file".format(encrypt_file)
            return printf

    def str_to_list_with_padding(self, string, len_sub_string):
        self.padding = 0
        if len(string) % len_sub_string:
            self.padding = len_sub_string - (len(string) % len_sub_string)
        str_to_list = [ord(x) for x in string]
        for i in range(self.padding-1):
            str_to_list.append(0)
        if self.padding:
            str_to_list.append(self.padding)
        return str_to_list

    def encrypt(self):
        n = 16
        msg_store = [self.msg[i:i+n] for i in range(0, len(self.msg), n)]
        tmp = []
        for msg in msg_store:
            msg_list = self.str_to_list_with_padding(msg, n)
            self.inputblock = matrix(SR, self.Nb, self.Nk, msg_list).transpose()
            for i in range(4):
                for j in range(self.Nb):
                    self.state[i, j] = self.inputblock[(i + 4*j)//4, (i + 4*j) % 4]
            self.KeyExpansion()
            self.AddRoundKey(0)
            for i in range(1, self.Nr):
                 self.SubBytes()
                 self.ShiftRow()
                 self.MixColumns()
                 self.AddRoundKey(i)
            self.SubBytes()
            self.ShiftRow()
            self.AddRoundKey(self.Nr)
            tmp.append(list(self.state))
        self.encrypt = tmp
        self.encrypt_to_msg('encrypt.txt')

    def dec_to_msg(self):
        dec_msg = [str(unichr(x)) for q in self.state for x in list(q)]
        for x in dec_msg:
            self.decrypto += x

    @prettyprint
    def write_decrypt_msg(self, decrypt_file):
        file = open('decrypt.txt', 'w')
        file.write(self.decrypto[:-self.padding])
        file.close()
        printf = "you message has been decrypt into {} file".format(decrypt_file)
        return printf

    @staticmethod
    def cut_to_lists(list_string):
        main_list = []
        for i in range(len(list_string)//16):
            cut = slice(16*i, 16*(i+1))
            main_list.append(list_string[cut])
        return main_list

    def decrypt(self):
        string = openfile('encrypt.txt')
        list_string = string.split(',')[:-1]
        main_list = AES.cut_to_lists(list_string)
        for item in main_list:
            self.state = matrix(SR, 4, 4, item)
            self.AddRoundKey(self.Nr)
            for i in range(self.Nr-1,0,-1):
                self.ShiftRow(flag='Inv')
                self.SubBytes(flag='Inv')
                self.AddRoundKey(i)
                self.MixColumns(flag='Inv')
            self.ShiftRow(flag='Inv')
            self.SubBytes(flag='Inv')
            self.AddRoundKey(0)
            self.dec_to_msg()
        self.write_decrypt_msg('decrypt.txt')

    def run(self):
        self.encrypt()
        self.decrypt()

def main():
    filename = raw_input("please, enter filename for encrypt: ")
    key_valuve = getpass(prompt='enter secret key: ')
    passwd = hashlib.md5()
    passwd.update(key_valuve)
    msg = openfile(filename)
    data_storage = [msg, passwd.digest()]
    aes = AES(data_storage)
    aes.run()


if __name__ == '__main__':
    main()
