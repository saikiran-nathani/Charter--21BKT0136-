from eth_account import Account
from eth_utils import keccak
from eth_account.messages import encode_defunct

def generate_test_data():
    
    account = Account.create()

    
    message = "Hello, Ethereum!"
    encoded_message = encode_defunct(text=message)
    
    signed_message = Account.sign_message(encoded_message, account._private_key)

    
    address = account.address
    message_hash = signed_message.message_hash.hex() 
    signature = signed_message.signature.hex()

    return address, message_hash, signature


address, message_hash, signature = generate_test_data()
print("Address:", address)
print("Message Hash:", message_hash)
print("Signature:", signature)
