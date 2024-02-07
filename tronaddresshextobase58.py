import base58

hex_address = "41d491042bc85ed538a1215b6ac3ea988426a9d8e0"


# HEX to Base58
byte_address = bytes.fromhex(hex_address)
base58_address = base58.b58encode_check(byte_address).decode('utf-8')

print("Base58 Address:", base58_address)