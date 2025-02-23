def mahoa(message, p, q, e):
    n = p * q
    z = (p - 1) * (q - 1)
    L = []
    for char in message:
        M = ord(char)  
        C = pow(M, e, n)  
        L.append(C)
    return L

p = 17
q = 23
e = 5
message = "NguyenThiThuMinh"
L = mahoa(message, p, q, e)
print("Sau khi ma hoa:", L)
