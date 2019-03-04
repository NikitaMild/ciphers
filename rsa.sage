from random import getrandbits, randint
from array import array


class RSA(object):
    def __init__(self, object=None):
        try:
            self.message = [ord(x) for x in object]
        except:
            self.message = object

    def session_key(self):
        m = ZZ(list(reversed(self.message)), 100)
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
    def __colculation_public_exponent(n, Fi):
        e = randint(2, Fi-1)
        while gcd(e, Fi) != 1:
            e = randint(2, Fi-1)
        return e

    @staticmethod
    def __colculation_secret_exponent(e, Fi):
        return mod(xgcd(e, Fi)[1], Fi)

    @staticmethod
    def encrypt(m,public_key):
        return (m**public_key[0]) % public_key[1]

    @staticmethod
    def decrypt(encryption_message,private_key):
        return (encryption_message**private_key[0]) % private_key[1]

    def run(self):
        m = self.session_key()
        print "m: %s" % m
        p = RSA.gen_primary_number(8)
        q = RSA.gen_primary_number(8)
        print "p: %s " % p
        print "q: %s" % q
        n = p*q
        Fi = euler_phi(n)
        e = RSA.__colculation_public_exponent(n, Fi)
        d = RSA.__colculation_secret_exponent(e, Fi)
        if mod(e*d, Fi) != 1:
            print "Bad calculations :("
            return
        public_key = array('I', [e, n])
        private_key = array('I', [d, n])
        encryption_message = RSA.encrypt(m,public_key)
        print "enc: {}".format(encryption_message)
        decryption_message = RSA.decrypt(encryption_message,private_key)
        print "dec: {}".format(decryption_message)

def main():
    #message = raw_input("please enter your message: ")
    rsa = RSA("loh")
    rsa.run()


if __name__ == "__main__":
    main()
