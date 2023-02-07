import wave

foo = wave.open('findme.wav', 'rb')

ch = foo.getnchannels()
wid = foo.getsampwidth()
rate = foo.getframerate()
nfrm = foo.getnframes()

print("Chan: {}; Wid: {}; Rate: {}; NFrm: {}".format(ch, wid, rate, nfrm))

vol = False

for i in range(0, nfrm):
    frame = foo.readframes(1)
    if frame == b'\x00\x00\x00\x00' and vol:
        print("off: {}".format(i / rate))
        vol = False
    if frame != b'\x00\x00\x00\x00' and not vol:
        print("on: {}".format(i / rate))
        vol = True
