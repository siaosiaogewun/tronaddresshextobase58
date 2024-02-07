import base58

base58_address = "TVM9ydprtbdeNeVRxozSfuHry4iRduQc7x"

# Base58 to HEX
byte_address = base58.b58decode_check(base58_address)
hex_address = byte_address.hex()

print("Hex Address:", hex_address)
