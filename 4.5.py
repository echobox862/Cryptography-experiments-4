import gmpy2

def gcd(a, b):
    """计算最大公约数"""
    return a if b == 0 else gcd(b, a % b)

def hex_to_char(hex_str):
    """十六进制字符串转UTF-8字符"""
    return bytes.fromhex(hex_str).decode('utf-8')

def decrypt(p, n, e, c):
    """使用已知素数p解密数据"""
    q = n // p
    phi = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phi)
    m = pow(c, d, n)
    return hex(m)

# 读取两个Frame的加密数据
with open("Frame1") as f:
    data = f.read()
    n1, e1, c1 = (int(data[:256], 16), 
                  int(data[256:512], 16), 
                  int(data[512:], 16))

with open("Frame18") as f:
    data = f.read()
    n2, e2, c2 = (int(data[:256], 16), 
                  int(data[256:512], 16), 
                  int(data[512:], 16))

# 找到公共素数p并解密
p = gcd(n1, n2)
cipher1 = decrypt(p, n1, e1, c1)
print(cipher1)
print(hex_to_char(cipher1[-16:]))

cipher2 = decrypt(p, n2, e2, c2)
print(cipher2)
print(hex_to_char(cipher2[-16:]))