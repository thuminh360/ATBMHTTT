def mahoa(plaintext, k):
    ciphertext = ""
    for x in plaintext:
        if x.isalpha():  
            shift = ord('A') if x.isupper() else ord('a')
            new_char = chr((ord(x) - shift + k) % 26 + shift)
            ciphertext += new_char.upper()  
        else:
            ciphertext += x 
    return ciphertext

plaintext = "NguyenThiThuMinh"
k = 11
ciphertext = mahoa(plaintext, k)
print("Sau khi ma hoa:", ciphertext)