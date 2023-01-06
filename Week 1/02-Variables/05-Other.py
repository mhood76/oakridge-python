X = (
"Hello World",                            # 'str'
20,                                       # 'int'
20.5,                                     # 'float'
1j,                                       # 'complex'
["apple", "banana", "cherry"],            # 'list'
("apple", "banana", "cherry"),            # 'tuple'
range(6),                                 # 'range'
{"name" : "John", "age" : 36},            # 'dict'
{"apple", "banana", "cherry"},            # 'set'
frozenset({"apple", "banana", "cherry"}), # 'frozenset'
True,                                     # 'bool'
b"Hello",                                 # 'bytes'
bytearray(5),                             # 'bytearray'
memoryview(bytes(5)),                     # 'memoryview'
None)                                     # 'NoneType'

for x in X:
    print(type(x))
