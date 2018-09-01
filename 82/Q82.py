
import zlib
s = 'hello world!hello world!hello world!hello world!'
t=zlib.compress(s.encode())
print(t)
print(zlib.decompress(t))
