
import unittest
from models.parent import Parent
import datetime
 
 
class TestParent(unittest.TestCase):
    def setUp(self):
        self.parent_1= Parent("John", "Miller", "2 Burton Way, EH1112B, Edinburgh", "1234567")
       
    def test_parent_has_f_name(self):
        self.assertEqual("John", self.parent_1.f_name)

    def test_parent_has_l_name(self):
        self.assertEqual("Miller", self.parent_1.l_name)

    def test_parent_has_address(self):
        self.assertEqual("2 Burton Way, EH1112B, Edinburgh", self.parent_1.address)

    def test_parent_has_phone_num(self):
        self.assertEqual("1234567", self.parent_1.phone_num)

    def test_student_has_id(self):
        self.assertEqual(None, self.parent_1.id)