import binner as ard

class CFS:
    def __init__(self, bytecode: bytes):
        self.code = ''.join([ard.localChr(i) for i in bytecode])
        self.sl = {}
    
    def ins(self, command: str):
        if command.startswith(ard.localChr(222) * 2):
            if len(command) >= 3:
                if command[2] == ard.localChr(0):
                    args = command.split(ard.localChr(221) + ard.localChr(222))
                    if len(args) == 3:
                        self.sl[bytes([ard.localOrd(i) for i in args[1]])] = bytes([ard.localOrd(i) for i in args[2]])
                elif command[2] == ard.localChr(1):
                    args = command.split(ard.localChr(221) + ard.localChr(222))
                    if len(args) == 2:
                        self.sl[bytes([ard.localOrd(i) for i in args[1]])] = {}
                elif command[2] == ard.localChr(2):
                    args = command.split(ard.localChr(221) + ard.localChr(222))
                    if len(args) == 2:
                        self.sl[bytes([ard.localOrd(i) for i in args[1]])]
    
    def go(self):
        for command in self.code.split(ard.localChr(221) * 2):
            self.ins(command)