class Ram:
    def __init__(self, size: int):
        self.__mem = bytearray([0] * size)  # bytearray вместо bytes
        self.size = size
    
    def __getitem__(self, index: int):
        return self.__mem[index]
    
    def __setitem__(self, index: int, value: int):  # value должен быть int от 0 до 255
        self.__mem[index] = value