from random import getrandbits, randint
from array import array
from sage.crypto.util import bin_to_ascii
from sage.crypto.util import ascii_to_bin


class RSA(object):

    def __init__(self, object=None):
        self.message = object
        self.m = []
        self.n = 0
        self.blocks = []
        self.e = 0
        self.d = 0
        self.encryption_message = []
        self.decryption_message = ""

    def session_key(self, block_bits):
        binary = ascii_to_bin(self.message)
        binary = str(binary)
        self.m = [int(binary[i:i+block_bits], 2)
                  for i in range(0, len(binary), block_bits)]

    @staticmethod
    def gen_primary_number(bits, p=0):
        p = getrandbits(bits)
        while p not in Primes():
            p = getrandbits(bits)
        return p

    def __CalculationPublicExponent(self, Fi):
        self.e = randint(2, Fi-1)
        while gcd(self.e, Fi) != 1:
            self.e = randint(2, Fi)

    def __CalculationSecretExponent(self, Fi):
        self.d = inverse_mod(self.e, Fi)

    def encrypt(self):
        R = IntegerModRing(self.n)
        self.encryption_message = [R(x)**R(self.e) for x in self.m]
        string = ""
        for x in self.encryption_message:
            string += str(x)
        with open("encrypt.txt", "w") as text_file:
            text_file.write("{0}\n".format(string))

    def decrypt(self):
        R = IntegerModRing(self.n)
        dec_blocks = [str(R(x)**R(self.d)) for x in self.encryption_message]
        dec_blocks = [bin(int(block))[2:] for block in dec_blocks]
        for i in range(len(dec_blocks)):
            if len(dec_blocks[i]) % 8:
                block = (8-(len(dec_blocks[i]) % 8))*"0"+dec_blocks[i]
                dec_blocks.pop(i)
                dec_blocks.insert(i, block)
        dec_msg = [bin_to_ascii(x) for x in dec_blocks]
        for x in dec_msg:
            self.decryption_message += x
        with open("decrypt.txt", "w") as text_file:
            text_file.write("{0}\n".format(self.decryption_message))

    def run(self):
        try:
            bits = int(raw_input(
                       "Please input number of bits for primary numbers: "))
            block_bits = int(raw_input(
                        "Please input number of bits in block: "))
        except:
            print "KOGO NAEBAT` XOCHESH?"
            return
        self.session_key(block_bits)
        p = RSA.gen_primary_number(bits)
        q = RSA.gen_primary_number(bits)
        print "p: %s " % p
        print "q: %s" % q
        self.n = p*q
        Fi = (p-1)*(q-1)
        self.__CalculationPublicExponent(Fi)
        self.__CalculationSecretExponent(Fi)
        if mod(self.e*self.d, Fi) != 1:
            print "Bad calculations :("
            return
        self.encrypt()
        self.decrypt()
        if self.message == self.decryption_message:
            print "All right!"


def main():
    with open('plaintext.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')
    rsa = RSA(data)
    rsa.run()


if __name__ == "__main__":
    main()
