# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:23:01 2020

@author: HP
"""

import unittest

import simpledb

class TestSum(unittest.TestCase):
    
    table = simpledb.Table("students")
    
    def test_create(self):
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
            self.table.create(record)
        
        expected = records
        actual = self.table.read_all()
        self.assertEqual(actual, expected)
    
    
    def test_read(self):
        """
        Test that a record is inserted into the table
        """
        query_dicts =  [
                {'faculty':'sciences'},
                {'faculty':'sciences', 'level':'100'},
                {'level':'100'},
                {'faculty':'arts', 'name':'Josh'},
                {'name':'Tola', 'age':'19'},
                {'name':'Sharon', 'age':25}
                ]
        
        expecteds = [
                [
                {'age':27, 'name':'Josh', 'faculty':'sciences', 'level':'100'},
                {'age':21, 'name':'John', 'faculty':'sciences', 'level':'100'},
                {'age':24, 'name':'Jane', 'faculty':'sciences', 'level':'200'},
                {'age':19, 'name':'Tola', 'faculty':'sciences', 'level':'400'},
                ],
                [
                {'age':27, 'name':'Josh', 'faculty':'sciences', 'level':'100'},
                {'age':21, 'name':'John', 'faculty':'sciences', 'level':'100'},
                ],
                [
                {'age':27, 'name':'Josh', 'faculty':'sciences', 'level':'100'},
                {'age':21, 'name':'John', 'faculty':'sciences', 'level':'100'},
                {'age':20, 'name':'Kate', 'faculty':'arts', 'level':'100'},
                ],
                [],
                [],
                [
                {'age':25, 'name':'Sharon', 'faculty':'arts', 'level':'300'}
                ]
                   ]
                
        for i in range(len(query_dicts)):
            actual = self.table.read_where(query_dicts[i])
            self.assertEqual(actual, expecteds[i])




if __name__ == '__main__':
    unittest.main()