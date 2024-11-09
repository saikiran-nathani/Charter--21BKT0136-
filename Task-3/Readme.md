Verify ECDSA Signatures
It's a Python project that provides functionality to check ECDSA signatures for Ethereum transactions. A public key can be recovered from a signature using the eth_keys and eth_utils libraries, thus enabling verification whether it matches a particular Ethereum address.

Requirements
Python 3.6+
library eth_keys
eth_utils library
You can get the libraries installed by running this command:

bash
Copy code
pip install eth-keys eth-utils
Code Explanation
verify_ecdsa_signature(address: str, signed_hash: bytes, signature: bytes) -> bool
It checks the validity of an ECDSA signature by the process of

Signature Length Check: Checks if the signature has length 65 bytes.
Recovery Byte Adjustment: the recovery byte of ethereum is 27 or 28, which needs to be adjusted to be 0 or 1.
Public Key Recovery: Using this eth_keys library, the message hash along with the given signature will recover the public key.
Address Comparison : Converts the given public key recovered into an Ethereum address and compares it to the given one.
Parameters:
str: the Ethereum address in checksum format to verify.
signed_hash (bytes): It contains signed hash of message.
signature (octets): The signature to be verified using ECDSA.
Return Value:
This function returns true if the signature is valid and corresponds to the address passed.
Returns False if the signature is invalid or does not match with the address.
How to Use
Clone or download the repository.
Install the dependencies required by using pip install eth-keys eth-utils.
Run the script:
bash
Copy code
python verify_signature.py
You would then be prompted to provide the following:

Ethereum address: The address to be searched.
Message hash: Hash of the message that was signed (in hexadecimal format).
Signature: Signature to verify against (in hexadecimal).
The following script will print whether the signature is valid or not.

Example:
For instance, when asking for inputs, it should look something like this:
Address: 0x665F1f07a644adf7690f027Ce92c747AF4E774bD
Message Hash: 5b001f2ad81fe86899545b51f8ecd1ca08674437d5c4748e1b70ba5dcf85ed86
Signature: 5fd499d5e359473c1bebbfd6c68b5b5b88f639175abb47a3c496db44898252ab3a632dbc1dc93e8143864989156dfb736d16567c13c0bc6e226ddfd98be67c621b


 License This project is licensed under the MIT License. See the LICENSE file for more information.
