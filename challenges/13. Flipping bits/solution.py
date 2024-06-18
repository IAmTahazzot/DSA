def flipping_bits(n):
    return n ^ 0xFFFFFFFF

if __name__ == '__main__':
    print(flipping_bits(6))