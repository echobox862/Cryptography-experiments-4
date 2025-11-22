import gmpy2

def gcd(a, b):
    """计算最大公约数"""
    return a if b == 0 else gcd(b, a % b)

def ext_gcd(a, b):
    """扩展欧几里得算法，返回(x, y, gcd)"""
    if b == 0:
        return (1, 0, a)
    x, y, g = ext_gcd(b, a % b)
    return (y, x - (a // b) * y, g)

def crt(a_list, m_list):
    """中国剩余定理求解x ≡ a_i mod m_i"""
    # 检查模数互质
    for i in range(len(m_list)):
        for j in range(i + 1, len(m_list)):
            if gcd(m_list[i], m_list[j]) != 1:
                print("不能直接使用中国剩余定理")
                return None
    
    m = 1
    for mi in m_list:
        m *= mi
    
    x = 0
    for a, mi in zip(a_list, m_list):
        Mi = m // mi
        inv_Mi, _, _ = ext_gcd(Mi, mi)
        inv_Mi %= mi  # 确保逆元为正数
        x = (x + a * Mi * inv_Mi) % m
    
    # 尝试开5次方根
    root, is_perfect = gmpy2.iroot(x, 5)
    return root if is_perfect else x

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

# 读取多个Frame数据
frames = ["frame3", "frame8", "frame12", "frame16", "frame20"]
c_list = []
n_list = []
for frame in frames:
    n, e, c = read_frame(frame)
    c_list.append(c)
    n_list.append(n)

# 解密并输出
plaintext_hex = hex(crt(c_list, n_list))
print(hex_to_char(plaintext_hex[-16:]))