from eth_account import Account
from eth_utils import keccak
from eth_account.messages import encode_defunct

def generate_test_data():
    # Generate a new Ethereum account (private key and address)
    account = Account.create()

    # Define a message and encode it for signing
    message = "Hello, Ethereum!"
    encoded_message = encode_defunct(text=message)

    # Sign the encoded message
    signed_message = Account.sign_message(encoded_message, account._private_key)

    # Extract the address, signature, and message hash
    address = account.address
    message_hash = signed_message.message_hash.hex()  # Use the exact message hash that was signed
    signature = signed_message.signature.hex()

    return address, message_hash, signature

# Generate test data
address, message_hash, signature = generate_test_data()
print("Address:", address)
print("Message Hash:", message_hash)
print("Signature:", signature)
