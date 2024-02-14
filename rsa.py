from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def gen_private_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def serialize_priv_key(private_key):
    pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption())
    return pem



private_key = gen_private_key()
private_nums = private_key.private_numbers()

public_key = private_key.public_key()
public_nums = public_key.public_numbers()

p = private_nums.p
q = private_nums.q
d = private_nums.d
print(private_nums.dmp1)
dmp1 = private_nums.dmp1 + 2
print(dmp1)
print(type(dmp1))
dmq1 = private_nums.dmq1
iqmp = private_nums.iqmp

corr_private_nums = rsa.RSAPrivateNumbers(p,q,d,dmp1,dmq1,iqmp,public_nums)

corr_private_key = corr_private_nums.private_key(unsafe_skip_rsa_key_validation=True)



