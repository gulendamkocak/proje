
class Person:
    def _init_(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Yaş: {self.yas}"


class Student(Person):
    def _init_(self, ad, yas, ogrenci_no):
        super()._init_(ad, yas)
        self.ogrenci_no = ogrenci_no

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Yaş: {self.yas}, Öğrenci No: {self.ogrenci_no}"


class Teacher(Person):
    def _init_(self, ad, yas, ders):
        super()._init_(ad, yas)
        self.ders = ders

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Yaş: {self.yas}, Ders: {self.ders}"


ogrenci = Student("Ali", 20, "12345")
ogretmen = Teacher("Ayşe", 35, "Matematik")

print(ogrenci.bilgileri_goster())
print(ogretmen.bilgileri_goster())
