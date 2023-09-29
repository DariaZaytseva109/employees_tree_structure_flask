from flask_seeder import Seeder, Faker, generator
from flask_seeder.generator import read_resource, Generator

from logic import Employee_logic

AMOUNT = 50


class MyPosition(Generator):
  """ Random Name generator """

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self._lines = None

  def generate(self):
    """ Generate a random name

    Returns:
        A random name in string format
    """
    if self._lines is None:
      self._lines = read_resource("names/positions.txt")

    result = self.rnd.choice(self._lines)

    return result
class DemoSeeder(Seeder):
  def run(self) -> object:
    # Create a new Faker and tell it how to create User objects
    faker = Faker(
      cls=Employee_logic,
      init={
        "fullname": generator.Name(),
        "position": MyPosition(),
        "salary": generator.Integer(start=800, end=10000),
        "boss_id": generator.Integer(start=1, end=6)
      }
    )

    # Create 10 users
    for user in faker.create(AMOUNT):
      print("Adding user: %s" % user)
      user.add_employee()
