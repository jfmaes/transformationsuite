import base64
import random
class Transformer:
    def __init__(self):
        pass

    def transform(self, args, data):
        if args.xor:
            return self.xor(data, args.key)
        elif args.caesar:
            return self.caesar(data, str(args.rotation))
        elif args.reverse:
            return self.reverse(data)
        elif args.base64:
            return self.base64(data)

    def caesar(self, payload, rotation):
        caesarstuff = bytearray(len(payload))
        length = len(payload)
        positiverotation = False
        if "-" not in rotation:
            positiverotation = True
            rotation = rotation.strip("+")
        else:
            rotation = rotation.strip("-")
        for i in range(length):
            if positiverotation:
                caesarstuff[i] = ((payload[i] + int(rotation)) & 0xFF)
            else:
                caesarstuff[i] = ((payload[i] - int(rotation)) & 0xFF)
        print("[+] Successfully ciphered the payload!")
        return caesarstuff


    def xor(self,payload,key):
        xorStuff = bytearray(len(payload))
        keyEncoded = bytearray(str(key).encode('ascii'))
        length = len(payload)
        for i in range(length):
            xorStuff[i] = payload[i] ^ keyEncoded[i % len(keyEncoded)]
        print("[+] Successfully XOR'd the payload!")
        return xorStuff

    def reverse(self,payload):
        data = payload[::-1]
        return data
    

    def base64(self,payload):
        return base64.b64encode(payload)

#https://en.wikipedia.org/wiki/List_of_file_signatures

    def prepend_magic_bytes(self,args,payload):
        allowed_formats = {"ico":b"\x00\x00\x01\x00",
                           "gif":b"\x47\x49\x46\x38\x37\x61",
                           "jpeg":b"\xFF\xD8\xFF\xDB",
                           "jpg":b"\xFF\xD8\xFF\xEE",
                           "zip":b"\x50\x4B\x03\x04",
                           "rar":b"\x52\x61\x72\x21\x1A\x07\x01\x00",
                           "png":b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A",
                           "mp3":b"\xFF\xF3",
                           "iso":b"\x43\x44\x30\x30\x31",
                           "7z":b"\x37\x7A\xBC\xAF\x27\x1C"}
        magic = b''
        if args not in allowed_args:
            raise ValueError
        elif args.lower() == "random":
            key = random.choice(allowed_formats.keys())
            print("random format chosen was {0), magic bytes are {1}",key,allowed_formats[key])
            magic = allowed_formats[key]
        else:
            magic = allowed_formats[args]
    
        





