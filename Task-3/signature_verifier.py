from eth_keys import keys
from eth_utils import to_bytes

# ECDSA signature verification function
def verify_ecdsa_signature(address: str, signed_hash: bytes, signature: bytes) -> bool:
    """
    Verifies an ECDSA signature.
    """
    if len(signature) != 65:
        print("Invalid ECDSA signature length.")
        return False

    # Adjust recovery byte if needed (from 27 or 28 to 0 or 1)
    recovery_byte = signature[-1]
    if recovery_byte >= 27:
        recovery_byte -= 27
        signature = signature[:-1] + bytes([recovery_byte])

    # Recover the public key
    try:
        public_key = keys.Signature(signature).recover_public_key_from_msg_hash(signed_hash)
    except Exception as e:
        print("Error recovering public key:", e)
        return False

    # Verify if the recovered address matches the provided address
    recovered_address = public_key.to_checksum_address()
    return recovered_address.lower() == address.lower()

# Test Data
address = input("Enter Ethereum address: ")
message_hash = input("Enter message hash (in hexadecimal): ")
signature_hex = input("Enter signature (in hexadecimal): ")

# Convert inputs to bytes
signed_hash_bytes = to_bytes(hexstr=message_hash)
signature_bytes = to_bytes(hexstr=signature_hex)

is_valid = verify_ecdsa_signature(address, signed_hash_bytes, signature_bytes)
print("Signature is valid:", is_valid)
