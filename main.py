import argparse
from transformer import Transformer
from format import Formatter
from Crypto.Hash import MD5

parser = argparse.ArgumentParser(description="Transformer next generation by jfmaes")
#DONT FORGET TO PUT REQUIRED TRUE
parser.add_argument("-f", "--file", help="the payload file", required=True)
parser.add_argument("-x", "--xor", help="use xor encryption", action="store_true")
parser.add_argument("-key", help="the xor key")
parser.add_argument("-c", "--caesar", help="use caesar cipher", action="store_true")
parser.add_argument("-rotation", help="the rotation to follow, can be + or - ")
parser.add_argument("-b64","-base64","--base64", help= "base 64 encode payload", action="store_true")
parser.add_argument("-rev","--reverse", help= "reverse payload", action="store_true")
parser.add_argument("-o", "--output-file", help="the output file")
parser.add_argument("-vba", help="format to vba", action="store_true")
parser.add_argument("-csharp", help="format to csharp", action="store_true")
parser.add_argument("-cpp", help="format to cpp", action="store_true")
parser.add_argument("-raw", help="format to raw payload", action="store_true")
parser.add_argument("-v", "--verbose", help="print shellcode to terminal", action="store_true")
parser.add_argument("--no-transform", help="doesnt transform payload, just formats.", action="store_true")


def check_args(args):
    if args.xor and not args.key:
        print(f"[!] XOR encryption needs a key")
        quit()

    if args.caesar and not args.rotation:
        print(f"[!] Caesar encryption needs a rotation")
        quit()

    if not args.verbose and not args.output_file:
        print(f"[!] Your payload needs to go somewhere. Use either verbose or outfile params, or both.")
        quit()

def get_shellcode_from_file(inFile):
    try:
        with open(inFile, "rb") as shellcodeFileHandle:
            shellcodeBytes = bytearray(shellcodeFileHandle.read())
            shellcodeFileHandle.close()
            print (f"[*] Payload file [{inFile}] successfully loaded")
    except IOError:
        print(f"[!] Could not open or read file [{inFile}]")
        quit()
    print("[*] MD5 hash of the initial payload: [{}]".format(MD5.new(shellcodeBytes).hexdigest()))
    print("[*] Payload size: [{}] bytes".format(len(shellcodeBytes)))
    return shellcodeBytes


def main(args):
    transformer = Transformer()
    formatter = Formatter()
    data = get_shellcode_from_file(args.file)
    transform_blob = transformer.transform(args, data)
    if not args.no_transform:
        formatter.format(args, transform_blob)
    if args.no_transform:
        formatter.format(args, data)


if __name__ == '__main__':
    args = parser.parse_args()
    check_args(args)
    main(args)
