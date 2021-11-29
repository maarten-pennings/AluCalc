from ctypes import c_ushort, c_ubyte

print( c_ubyte(-1) )

class U8:
  def __init__(self, value) :
    self.value = c_ubyte(value).value
  def uvalue(self):
    return self.value
  def svalue(self):
    return self.value-2**8
  def __str__(self):
    return '0b'+('0'*8 + bin(self.value)[2:])[-8:]
  def __add__(self, other):
    return U8( self.value + other.value )
  def __mul__(self, other):
    return U8( self.value * other.value )

class U16:
  def __init__(self, value) :
    self.value = c_ushort(value).value
  def uvalue(self):
    return self.value
  def svalue(self):
    return self.value-2**16
  def __str__(self):
    return '0b'+('0'*16 + bin(self.value)[2:])[-16:]
  def __add__(self, other):
    return U16( self.value + other.value )
  def __mul__(self, other):
    return U16( self.value * other.value )
  def msb(self) :
    return U8(self.value//256)
    
for v in [0,1,10,127,128,254,255,256] :
  print( v, U8(v) )

for v in [-1,-2,-10,-127,-128] :
  print( v, U8(v) )

def addtest(a,b):
  c = U8(a)+U8(b)
  print( f"{a}+{b} = {c} {c.uvalue()} {c.svalue()}" )

addtest(9,3)
addtest(100,30)
addtest(-9,3)
addtest(-9,12)
addtest(-9,-3)

def wiki_U(ws,vs) :
  s = ws[0]*vs[0] + ws[1]*vs[1] + ws[2]*vs[2]
  print(s)
  s += U16(128)
  print(s)
  s = s.msb()
  print(s)
  s += U8(128)
  print(s)

wiki_U( (U16(-43),U16(-84),U16(127)) , (U16(255),U16(255),U16(0)) )


