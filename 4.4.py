def ext_gcd(a, b):
    """扩展欧几里得算法，返回(x, y, gcd)"""
    if b == 0:
        return (1, 0, a)
    x, y, g = ext_gcd(b, a % b)
    return (y, x - (a // b) * y, g)

def hex_to_char(hex_str):
    """十六进制字符串转UTF-8字符"""
    return bytes.fromhex(hex_str).decode('utf-8')

def read_frame(filename):
    """读取Frame文件，返回(n, e, c)"""
    with open(filename) as f:
        data = f.read()
        return (int(data[:256], 16),
                int(data[256:512], 16),
                int(data[512:], 16))

# 读取两个Frame的数据
n1, e1, c1 = read_frame("Frame0")
n2, e2, c2 = read_frame("Frame4")

# 求解线性同余方程并解密
x, y, g = ext_gcd(e1, e2)
plaintext = (pow(c1, x, n1) * pow(c2, y, n2)) % n1

print(hex(plaintext))
print(hex_to_char(hex(plaintext)[-16:]))