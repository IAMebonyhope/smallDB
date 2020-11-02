# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:23:01 2020

@author: HP
"""

import unittest

import simpledb

class TestSum(unittest.TestCase):
    
    def insert_into_table(self):
        
        table = simpledb.Table("students")
        records = [
                {'age':27, 'name':'Josh', 'faculty':'sciences', 'level':'100'},
                {'age':21, 'name':'John', 'faculty':'sciences', 'level':'100'},
                {'age':24, 'name':'Jane', 'faculty':'sciences', 'level':'200'},
                {'age':19, 'name':'Tola', 'faculty':'sciences', 'level':'400'},
                {'age':20, 'name':'Kate', 'faculty':'arts', 'level':'100'},
                {'age':25, 'name':'Sharon', 'faculty':'arts', 'level':'300'},
                   ]
        
        for record in records:
            table.create(record)
        
        return table
    
    
    def test_get_name(self):
       """
       Test that a table can return its name
       """
       table = self.insert_into_table()
       actual = table.get_name()
        
       self.assertEqual(actual, "students")
        
        
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
        table = self.insert_into_table()
        
        expected = records
        actual = table.read_all()
        self.assertEqual(actual, expected)
    
    
    def test_read(self):
        """
        Test that a records can be gotten from the table, if the where condition is met
        """
        table = self.insert_into_table()
            
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
            actual = table.read_where(query_dicts[i])
            self.assertEqual(actual, expecteds[i])


    def test_update(self):
        """
        Test that records can be updated in the table
        """
        table = self.insert_into_table()
        query_dicts =  [
                {'name':'Josh'},
                {'faculty':'sciences'},
                {'faculty':'arts', 'level':'300'},
                ]
        
        changed_dicts = [
                {'name':'Joshua', 'faculty':'arts', 'level':'200'},
                {'faculty':'science', 'department':'chemistry'},
                {'department':'music', 'courses':['MUS101', 'DAN309', 'CIV378']},
                ]
        
        expected = [
                {'age':27, 'name':'Joshua', 'faculty':'arts', 'level':'200'},
                {'age':21, 'name':'John', 'faculty':'science', 'department':'chemistry', 'level':'100'},
                {'age':24, 'name':'Jane', 'faculty':'science', 'department':'chemistry', 'level':'200'},
                {'age':19, 'name':'Tola', 'faculty':'science', 'department':'chemistry', 'level':'400'},
                {'age':20, 'name':'Kate', 'faculty':'arts', 'level':'100'},
                {'age':25, 'name':'Sharon', 'faculty':'arts', 'level':'300', 'department':'music', 'courses':['MUS101', 'DAN309', 'CIV378']},
                   ]
        
        for i in range(len(query_dicts)):
            table.update_where(query_dicts[i], changed_dicts[i])
        
        actual = table.read_all()
        self.assertEqual(actual, expected)
        
    
    def test_count(self):
        """
        Test that it returns number of records in the table
        """
        table = self.insert_into_table()
        expected = 6
        actual = table.count()
        self.assertEqual(actual, expected)


    def test_delete_where(self):      
        """
        Test that records can be deleted in the table
        """
        table = self.insert_into_table()
        query_dict = {'name':'Josh', 'age':27}
        
        expected = [
                {'age':21, 'name':'John', 'faculty':'sciences', 'level':'100'},
                {'age':24, 'name':'Jane', 'faculty':'sciences', 'level':'200'},
                {'age':19, 'name':'Tola', 'faculty':'sciences', 'level':'400'},
                {'age':20, 'name':'Kate', 'faculty':'arts', 'level':'100'},
                {'age':25, 'name':'Sharon', 'faculty':'arts', 'level':'300'},
                   ]
        
        table.delete_where(query_dict)
        actual = table.read_all()
        self.assertEqual(actual, expected)
    

    def test_count_where(self):
        """
        Test that it returns number of records in the table where the query is the query is met
        """
        table = self.insert_into_table()
        expected = 4
        actual = table.count({'faculty':'sciences'})
        self.assertEqual(actual, expected)
        
        
    def test_delete_all(self):      
        """
        Test that all records can be deleted in the table
        """
        table = self.insert_into_table()
        table.delete_all()
        
        actual = table.read_all()
        self.assertEqual(actual, [])



if __name__ == '__main__':
    unittest.main()