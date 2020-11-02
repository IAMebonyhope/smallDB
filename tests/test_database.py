# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 00:54:30 2020

@author: HP
"""

import unittest

import simpledb

class TestSum(unittest.TestCase):
    
    def student_table(self, table):
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
    
    
    def staff_table(self, table):
        records = [
                {'name':'Tunde', 'gender':'Male', 'qualification':'Bsc'},
                {'name':'Katie', 'gender':'Female', 'qualification':'HND'},
                {'name':'Mack', 'gender':'Male', 'qualification':'Msc'},
                   ]      
        for record in records:
            table.create(record)
        
        return table
    
    
    def test_create_table(self):
        """
        Test that a table can be created and added to the database
        """
        db = simpledb.Database("school")
        student_table = db.create_table("students")      
        self.assertEqual(student_table.get_name(), "students")
        
        staff_table = db.create_table("staffs")      
        self.assertEqual(staff_table.get_name(), "staffs")
            
    
    def test_create_table_exception(self):
        with self.assertRaises(Exception):
            """
            Test that an exception is thrown when table exists
            """
            db = simpledb.Database("bank") 
            customers_table = db.create_table("customers")      
            table = db.create_table("customers")      
            
    
    def test_get_table(self):
        """
        Test that a table can be retrieved from the database
        """
        db = simpledb.Database("school")
        db.create_table("students")
        db.create_table("staffs")
        student_table = db.get_table("students")      
        self.assertEqual(student_table.get_name(), "students")
        
        staff_table = db.get_table("staffs")      
        self.assertEqual(staff_table.get_name(), "staffs")
        
    
    def test_get_table_exception(self):
        with self.assertRaises(Exception):
            db = simpledb.Database("apps")
            table = db.get_table("stores")  
    
    
    def test_get_table_names(self):
        """
        Test that a table can be retrieved from the database
        """
        db = simpledb.Database("school")
        db.create_table("students")
        db.create_table("staffs")
        
        self.assertEqual(db.get_table_names, ["staffs", "students"])
            
            
            
    

if __name__ == '__main__':
    unittest.main()

