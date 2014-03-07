import serial

class ArguementError(Exception):
  pass

class Display:
  positions = {
      0: '\x7B',
      1: '\x7C',
      2: '\x7D',
      3: '\x7E' }

  cursors = {
      0: '\x00',
      1: '\x01',
      2: '\x02',
      3: '\x03' }

  def __init__(self):
    self.port = serial.Serial("/dev/ttyAMA0", baudrate=9600)
    self.reset()

  def reset(self):
    self.reset_cursor()
    self.clear()
    self.colon_off()

  def set_cursor(self,pos):
    self.write('\x79' + self.cursors[pos])

  def reset_cursor(self):
    self.set_cursor(0)

  def clear(self):
    self.write('\x76')

  def write(self, string):
    self.port.write(string)

  def colon_on(self):
    self.write('\x77\x10')
    self._colon = True

  def colon_off(self):
    self.write('\x77\x00')
    self._colon = False

  def toggle_colon(self):
    if self._colon:
      self.colon_off()
    else:
      self.colon_on()

  def write_string(self, string):
    if len(string) > 4: raise ArguementError("4 characters or less!")

    self.reset_cursor()
    for idx, char in enumerate(string):
      translit = self.translit(char)

      if translit:
        self.write(self.positions[idx] + translit)
      else:
        self.set_cursor(idx)
        self.write(char)

  def translit(self, char):
    if char.upper() == 'W':
      return '\x49'

    if char.upper() == 'Z':
      return '\x52'

    if char.upper() == 'P':
      return '\x73'

    return False
