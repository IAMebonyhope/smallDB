# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:23:01 2020

@author: HP
"""

import unittest

import simpledb

class TestSum(unittest.TestCase):
    
    table = simpledb.Table("students")
    
    def test_insert(self):
        """
        Test that a record is inserted into the table
        """
        records = [
                {'age':27, 'name':'Josh', 'faculty':'sciences', 'level':'100'},
                {'age':21, 'name':'John', 'faculty':'sciences', 'level':'100'},
                {'age':24, 'name':'Jane', 'faculty':'sciences', 'level':'200'},
                {'age':19, 'name':'Tola', 'faculty':'sciences', 'level':'400'},
                {'age':20, 'name':'Kate', 'faculty':'arts', 'level':'100'},
                {'age':25, 'name':'Sharon', 'faculty':'arts', 'level':'300'},
                   ]
        
        for record in records:
            table.insert(record)
        
        actual = records
        expected = table.get_all()
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()