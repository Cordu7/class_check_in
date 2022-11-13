
import unittest
from models.carer import Carer
import datetime
 
 
class TestCarer(unittest.TestCase):
    def setUp(self):
        self.carer_1= Carer("John", "Miller", "2 Burton Way, EH1112B, Edinburgh", "1234567")
       
    def test_carer_has_f_name(self):
        self.assertEqual("John", self.carer_1.f_name)

    def test_carer_has_l_name(self):
        self.assertEqual("Miller", self.carer_1.l_name)

    def test_carer_has_details(self):
        self.assertEqual("2 Burton Way, EH1112B, Edinburgh", self.carer_1.details)

    def test_carer_has_phone_num(self):
        self.assertEqual("1234567", self.carer_1.phone_num)

    def test_student_has_id(self):
        self.assertEqual(None, self.carer_1.id)