# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 00:54:30 2020

@author: HP
"""

import unittest

import simpledb

class TestSum(unittest.TestCase):  
    
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
        
        self.assertEqual(db.get_table_names(), ["staffs", "students"])
    
    
    def test_drop_table(self):
        """
        Test that a table can be retrieved from the database
        """
        db = simpledb.Database("school")
        db.create_table("students")
        db.create_table("staffs")
        
        db.drop_table("staffs")
        
        self.assertEqual(db.get_table_names(), ["students"])
    
    
    def test_drop_table_exception(self):
        with self.assertRaises(Exception):
            db = simpledb.Database("apps")
            db.drop_table("stores") 
            
            
            
    

if __name__ == '__main__':
    unittest.main()

