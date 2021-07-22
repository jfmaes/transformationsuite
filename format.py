
class Formatter:
    def __init__(self):
        pass

    def format(self, args, data):
        if args.vba:
            self.format_VBA(args,data)
        elif args.csharp:
            self.format_CSharp(args,data)
        elif args.cpp:
            self.format_CPP(args,data)
        elif args.raw:
            print(f"[+] will write raw transformed data into [{args.output_file}]")
            self.format_raw(args,data)
        else:
           print(f"[-] no data transformation was provided! exitting.")

    def format_CPP(self, args, data):
        shellcode = "\\x"
        shellcode += "\\x".join(format(b, '02x') for b in data)
        if args.verbose:
            print("Your formatted payload is: \n")
            print(shellcode+ "\n")
        if args.output_file:
            self.write_to_file(args, shellcode)
        return shellcode

    def format_CSharp(self, args, data):
        shellcode = '0x'
        shellcode += ',0x'.join(format(b, '02x') for b in data)
        if args.verbose:
            print("Your formatted payload is: \n")
            print(shellcode + "\n")
        if args.output_file:
            self.write_to_file(args, shellcode)
        return shellcode

    def format_VBA(self, args, data):
        shellcode = ','.join(format(b,'') for b in data)
        shellcode_splitted = shellcode.split(',')
        for index in range(len(shellcode_splitted)):
            if index != 0 and index % 50 == 0:
                shellcode_splitted.insert(index, ' _\n')
        shellcode = ",".join(shellcode_splitted)
        shellcode = shellcode.replace("_\n,", "_\n")
        if args.verbose:
            print("Your formatted payload is: \n")
            print(shellcode+ "\n")
        if args.output_file:
            self.write_to_file(args, shellcode)
        return shellcode
        
    def format_raw(self, args,data):
        if args.verbose:
            print("Your formatted payload is: \n")
            print(str(data) + "\n")
        if args.output_file:
            self.write_to_file(args, data)
        return data
    	
    def write_to_file(self, args, data):
        if args.raw:
            open(args.output_file, 'wb').write(data)
        else:
            open(args.output_file, 'w').write(data)
        print(f"[+] data written to {args.output_file} successfully!")


