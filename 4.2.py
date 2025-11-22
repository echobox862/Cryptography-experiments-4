import gmpy2

def pollard_factor(n):
    """使用Pollard算法分解n的质因数"""
    a = 2
    B = 2
    while True:
        a = gmpy2.powmod(a, B, n)
        res = gmpy2.gcd(a - 1, n)
        if res != 1 and res != n:
            return (res, n // res)
        B += 1

def hex_to_char(hex_str):
    """十六进制字符串转UTF-8字符"""
    return bytes.fromhex(hex_str).decode('utf-8')

# 读取加密数据并解密
with open("Frame19") as f:
    data = f.read()
    n = int(data[:256], 16)
    e = int(data[256:512], 16)
    c = int(data[512:], 16)

p, q = pollard_factor(n)
print(f"p={hex(p)}")
print(f"q={hex(q)}")

phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
print(f"d={hex(d)}")

m = gmpy2.powmod(c, d, n)
print(f"m={hex(m)}")

plaintext = hex(m)[-16:]
print(hex_to_char(plaintext))