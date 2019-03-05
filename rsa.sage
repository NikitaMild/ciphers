from random import getrandbits, randint
from array import array
from sage.crypto.util import bin_to_ascii
from sage.crypto.util import ascii_to_bin

class RSA(object):
    def __init__(self, object=None):
        self.message = object

    def session_key(self):
        binary = ascii_to_bin(self.message)
        binary = str(binary)
        print binary
        if len(binary)%8:
            q = 8-(len(binary)%8)
            binary = (q+2)*'0'+binary[2:]
        bin_blocks = [binary[i:i+8] for i in range(0,len(binary),8)]
        m = int(binary,2)
        return m

    @staticmethod
    def __test_Ferma(number=0, rounds=128):
        if mod(number, 2) == 0:
            return False
        for _ in range(rounds):
            a = (randint(2, number-1))**(number-1)
            if mod(a, number) != 1:
                return False
        return True

    @staticmethod
    def gen_primary_number(bits, p=0):
        p = getrandbits(bits)
        while not RSA.__test_Ferma(p):
            p = getrandbits(bits)
        return p

    @staticmethod
    def __ColculationPublicExponent(n, Fi):
        e = randint(2, Fi-1)
        while gcd(e, Fi) != 1:
            e = randint(2, Fi-1)
        return e

    @staticmethod
    def __ColculationSecretExponent(e, Fi):
        return mod(xgcd(e, Fi)[1], Fi)

    @staticmethod
    def encrypt(n,m,public_key):
        R = IntegerModRing(n)
        return R(m**public_key[0])

    @staticmethod
    def decrypt(n,encryption_message,private_key):
        R = IntegerModRing(n)
        tmp = R(encryption_message**private_key[0])
        binary = bin(tmp)
        q = 8-(len(binary)%8)
        binary = (q+2)*'0'+binary[2:]
        print "binary: %s" % binary
        tmp = bin_to_ascii(binary)
        return tmp

    def run(self):
        m = self.session_key()
        print "m: %s" % m
        p = RSA.gen_primary_number(8)
        q = RSA.gen_primary_number(8)
        print "p: %s " % p
        print "q: %s" % q
        n = p*q
        Fi = euler_phi(n)
        e = RSA.__ColculationPublicExponent(n, Fi)
        d = RSA.__ColculationSecretExponent(e, Fi)
        if mod(e*d, Fi) != 1:
            print "Bad calculations :("
            return
        public_key = array('I', [e, n])
        private_key = array('I', [d, n])
        encryption_message = RSA.encrypt(n,m,public_key)
        print "enc: {}".format(encryption_message)
        decryption_message = RSA.decrypt(n,encryption_message,private_key)
        print "dec: {}".format(decryption_message)

def main():
    rsa = RSA("k")
    rsa.run()


if __name__ == "__main__":
    main()
