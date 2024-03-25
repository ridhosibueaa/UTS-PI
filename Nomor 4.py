class BMI:
  def _init_(self, berat, tinggi):
    self.berat = berat
    self.tinggi = tinggi

  @property
  def berat(self):
    return self._berat

  @berat.setter
  def berat(self, value):
    self._berat = value

  @property
  def tinggi(self):
    return self._tinggi

  @tinggi.setter
  def tinggi(self, value):
    self._tinggi = value

  def BMI_Value(self):
    return self.berat / (self.tinggi**2)

  def _eq_(self, other):
    return self.berat == other.berat and self.tinggi == other.tinggi
# Contoh penggunaan
bmi_1 = BMI(65, 1.6)
bmi_2 = BMI(70, 1.5)
    
print(f"BMI orang pertama: {bmi_1.BMI_Value()}")
print(f"BMI orang kedua: {bmi_2.BMI_Value()}")

print(f"Apakah BMI mereka sama? {bmi_1 == bmi_2}")