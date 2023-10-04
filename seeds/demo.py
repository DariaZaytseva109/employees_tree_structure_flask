from flask_seeder import Seeder, Faker, generator
from flask_seeder.generator import Generator

from logic import Employee_logic


AMOUNT = 50000  #количество генерируемых seeder'ом работников


class MyPosition(Generator):
  """ генератор должностей из моего файла """
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self._lines = None

  def generate(self):
      if self._lines is None:
          file = open('data/positions.txt', encoding='utf-8')
          self._lines = file.readlines()
          file.close()
      result = self.rnd.choice(self._lines)
      return result


class MyName(Generator):
  """ генератор имен из моего файла """
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self._lines = None

  def generate(self):
      if self._lines is None:
          file = open('data/names.txt', encoding='utf-8')
          self._lines = file.readlines()
          file.close()
      result = self.rnd.choice(self._lines)
      return result

class DemoSeeder(Seeder):
  def run(self) -> object:
    faker = Faker(
      cls=Employee_logic,
      init={
        "fullname": MyName(),
        "position": MyPosition(),
        "salary": generator.Integer(start=800, end=10000),
        "boss_id": generator.Integer(start=2, end=7)
        }
    )

    for elem in faker.create(AMOUNT):
        elem.add_employee()
