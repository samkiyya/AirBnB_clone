#!/usr/bin/python3
"""test BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def setUp(self):
        self.testbasemodel = BaseModel()

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_save_BaesModel(self):
        """test save_Basemodel"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_times(self):
        """ Test created_at and updated_at times """
        bm = BaseModel()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_doc(self):
        """ Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        """ Test kwargs """
        basemodel = BaseModel(name="base")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))

    def test_string_rep(self):
        """ Test string representation of basemodel """
        basemodel = BaseModel()
        self.assertEqual(str(basemodel), "[BaseModel] ({}) {}".format(basemodel.id, basemodel.__dict__))

    def test_unique_id(self):
        """ Test unique ids """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == "__main__":
    unittest.main()
