# Test string output solution found here https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print

import unittest
import sys
import io

import bin.diagnostic
test = bin.diagnostic

class TestDiagnostic(unittest.TestCase):
  """Provides test cases for python-classes-diagnostic"""

  def test_question_one(self):
    """Tests the Person class"""
    person = test.Person('Paul', 25, 'Georgia')
    self.assertEqual(person.description(), 'My name is Paul, I\'m 25 years old, and I live in Georgia.')
    self.assertEqual(person.age, 25)
    self.assertEqual(person.name, 'Paul')
    self.assertEqual(person.location, 'Georgia')
    self.assertEqual(test.response['dave'].description(), 'My name is Dave, I\'m 32 years old, and I live in Sommerville.')

  def test_question_two(self):
    """Tests the Developer class"""
    dev = test.Developer('Dave', 32, 'Ohio')
    self.assertEqual(dev.solve_problems(), 'think, think, think')
    self.assertEqual(dev.description(), 'My name is Dave, I\'m 32 years old, and I live in Ohio.')

  def test_question_three(self):
    """Tests the housecat noise value"""
    self.assertEqual(test.response['housecat_noise'], "I am a HouseCat, and I go 'meow'")

  def test_question_four(self):
    """Tests the Lion class"""
    # create StringIO object
    captured_output = io.StringIO()
    # Redirect stdout
    sys.stdout = captured_output

    expected = ''

    # Should inherit from Cat
    test.Lion().groom()
    expected += 'lick... lick...\n'

    # Should use Carnivorous mixin
    test.Lion().eat_meat(9)
    expected += 'Yuck!\n'

    # Should use Carnivorous mixin
    test.Lion().roar()
    expected += 'ROAR!\n'

    self.assertEqual(captured_output.getvalue(), expected)

    # reset redirect
    sys.stdout = sys.__stdout__

  def test_question_five(self):
    """Tests the ComboAttack class"""
    self.assertEqual(test.ComboAttack().possible_moves(), 'kick, move, punch')
    self.assertEqual(test.ComboAttack().punch().move('left').kick().damage, 15)

if __name__ == '__main__':
    unittest.main()
