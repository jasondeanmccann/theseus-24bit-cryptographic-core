"""
THESEUS 24-BIT CRYPTOGRAPHIC CORE
RC1

State size: 24 bits
Representation: three 8-bit words

Construction:
    S-box -> matrix diffusion -> bit permutation

Inverse:
    inverse permutation -> inverse matrix -> inverse S-box
"""

MASK8 = 0xFF
MASK24 = 0xFFFFFF


# ============================================================
# 8-BIT S-BOX
# ============================================================

# Affine permutation over Z/256Z.
# 197 is odd, therefore multiplication by 197 is invertible mod 256.
SBOX_A = 197
SBOX_B = 123

# 197^-1 mod 256
SBOX_A_INV = pow(SBOX_A, -1, 256)


def sbox(x: int) -> int:
    """Invertible 8-bit substitution."""
    return ((SBOX_A * x) + SBOX_B) & MASK8


def inverse_sbox(x: int) -> int:
    """Inverse of sbox()."""
    return (SBOX_A_INV * (x - SBOX_B)) & MASK8


# ============================================================
# 3x3 DIFFUSION MATRIX MOD 256
# ============================================================

MATRIX = (
    (1, 2, 3),
    (0, 1, 4),
    (0, 0, 1),
)

# det(MATRIX) = 1 mod 256, so the matrix is invertible.
MATRIX_INV = (
    (1, 254, 5),
    (0, 1, 252),
    (0, 0, 1),
)


def matrix_multiply(state, matrix):
    """Multiply a 3-byte state by a 3x3 matrix modulo 256."""
    a, b, c = state

    return (
        (
            matrix[0][0] * a
            + matrix[0][1] * b
            + matrix[0][2] * c
        ) & MASK8,

        (
            matrix[1][0] * a
            + matrix[1][1] * b
            + matrix[1][2] * c
        ) & MASK8,

        (
            matrix[2][0] * a
            + matrix[2][1] * b
            + matrix[2][2] * c
        ) & MASK8,
    )


# ============================================================
# 24-BIT PERMUTATION
# ============================================================

# Multiplication by 5 modulo 24 permutes all bit positions because
# gcd(5, 24) = 1.
PERMUTATION = tuple((5 * i) % 24 for i in range(24))


def build_inverse_permutation(permutation):
    inverse = [0] * len(permutation)

    for source, destination in enumerate(permutation):
        inverse[destination] = source

    return tuple(inverse)


INVERSE_PERMUTATION = build_inverse_permutation(PERMUTATION)


def bytes_to_int(state):
    """Convert three bytes into one 24-bit integer."""
    a, b, c = state
    return ((a & MASK8) << 16) | ((b & MASK8) << 8) | (c & MASK8)


def int_to_bytes(value):
    """Convert a 24-bit integer into three bytes."""
    value &= MASK24

    return (
        (value >> 16) & MASK8,
        (value >> 8) & MASK8,
        value & MASK8,
    )


def permute_bits(state):
    """Apply the 24-bit permutation."""
    value = bytes_to_int(state)
    result = 0

    for source, destination in enumerate(PERMUTATION):
        bit = (value >> source) & 1
        result |= bit << destination

    return int_to_bytes(result)


def inverse_permute_bits(state):
    """Apply the inverse 24-bit permutation."""
    value = bytes_to_int(state)
    result = 0

    for source, destination in enumerate(INVERSE_PERMUTATION):
        bit = (value >> source) & 1
        result |= bit << destination

    return int_to_bytes(result)


# ============================================================
# ROUND FUNCTION
# ============================================================

def encrypt(state):
    """
    Encrypt one 24-bit state.

    Input:
        iterable containing exactly three byte values

    Output:
        tuple of three encrypted bytes
    """

    if len(state) != 3:
        raise ValueError("THESEUS operates on exactly 3 bytes.")

    state = tuple(x & MASK8 for x in state)

    # Substitution
    state = tuple(sbox(x) for x in state)

    # Diffusion
    state = matrix_multiply(state, MATRIX)

    # Bit permutation
    state = permute_bits(state)

    return state


def decrypt(state):
    """
    Reverse encrypt() exactly.
    """

    if len(state) != 3:
        raise ValueError("THESEUS operates on exactly 3 bytes.")

    state = tuple(x & MASK8 for x in state)

    # Reverse permutation
    state = inverse_permute_bits(state)

    # Reverse matrix diffusion
    state = matrix_multiply(state, MATRIX_INV)

    # Reverse substitution
    state = tuple(inverse_sbox(x) for x in state)

    return state


# ============================================================
# SELF TEST
# ============================================================

def self_test():
    test_vectors = (
        (0x00, 0x00, 0x00),
        (0x12, 0x34, 0x56),
        (0xFF, 0xFF, 0xFF),
        (0xCE, 0x1B, 0x79),
        (0x52, 0x6F, 0x0C),
        (0x4F, 0x65, 0x3A),
    )

    for plaintext in test_vectors:
        ciphertext = encrypt(plaintext)
        recovered = decrypt(ciphertext)

        assert recovered == plaintext, (
            f"Round-trip failure: "
            f"{plaintext} -> {ciphertext} -> {recovered}"
        )

    return True


if __name__ == "__main__":
    assert self_test()

    print("THESEUS 24-BIT CORE")
    print("RC1 self-test: PASS")

    example = (0x12, 0x34, 0x56)

    encrypted = encrypt(example)
    decrypted = decrypt(encrypted)

    print(
        "Plaintext :",
        " ".join(f"{x:02X}" for x in example)
    )

    print(
        "Encrypted :",
        " ".join(f"{x:02X}" for x in encrypted)
    )

    print(
        "Recovered :",
        " ".join(f"{x:02X}" for x in decrypted)
    )
