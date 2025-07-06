symvols = list("0123456789⁰¹²³⁴⁵⁶⁷⁸⁹. ,°=\\\n\t/(){}[]?!¿¡;:*'\"-+&_$¢€£~`|•√π÷×§∆¥^\r©®™✓<>—QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁйцукенгшщзхфывапролджэячсмитьбюё№ҐЇІЄґїієЎў«≤‹⟨›≥»⟩←↑→↓↔️↕️¿∞≠≈₽%\x00\x01₴■□▪️▫️▲▼◀️▶️●○◎◉─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬")

def inc(symvol: str):
    if len(symvol) != 1:
        raise ValueError("Требуется один символ!")
    
    c = ord(symvol)
    try:
        return symvols[c]
    except IndexError:
        return "?"

def dec(symvol: str):
    if len(symvol) != 1:
        raise ValueError("Требуется один символ!")
    
    sl = {ord(k): v for k, v in zip(symvols, range(256))}
    return chr(sl[ord(symvol)])

def localOrd(x: str):
    return symvols.index(x)

def localChr(x: int):
    return symvols[x]
    
class Ard:
    def __init__(self, content: str):
        self.text = content  # обычный текст
        self.codes = [symvols.index(ch) for ch in content]  # список кодов (0–255)

    def encode(self) -> bytes:
        return bytes(self.codes)

    @classmethod
    def decode(cls, data: bytes) -> 'Ard':
        chars = ''.join(symvols[b] for b in data)
        return cls(chars)

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"Ard('{self.text}')"

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        return self.text[index]

    def savefile(self, name: str):
        with open(name, 'wb') as file:
            file.write(bytes([ord(dec(s)) for s in self.text]))
    
def loadfile(name: str):
    with open(name, 'rb') as file:
        content = file.read()
    decoded = ''.join([inc(chr(b)) for b in content])
    return Ard(decoded)
