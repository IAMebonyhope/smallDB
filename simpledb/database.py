# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:24:34 2020

@author: HP
"""
from .utils import Utils
from .table import Table
import os.path

class Database:
    def __init__(self, filename):
        """
        Initialize the underlying database. If filename contains data, load it.
        """
        self.database = {}
        self.filename = filename

        if os.path.isfile(self.filename):
            file = open(self.filename, "r")
            json_file = file.read()
            self.database = Utils.decoder(json_file)
      
        
    def create_table(self, name):
        """
        Create a collection in the DB and return it.
        """
        if name in self.database:
            raise Exception("table already exists")
            
        self.database[name] = Table(name)
        return self.database[name]
    

    def get_table(self, name):
        """
        Return the Table with the name
        """
        if name not in self.database:
            raise Exception("table does not exist")

        return self.database[name]
    
    
    def get_table_names(self):
        """
        Return a list of the sorted names of the tables in the database.
        """
        table_names = list(self.database.keys())
        return sorted(table_names)


    def drop_table(self, name):
        """
        Drop the specified table from the database.
        """
        if name in self.database:
            del self.database[name]
        
        else:
            raise Exception("table does not exist")

    
    def close(self):
        """
        Save and close file.
        """
        file = open(self.filename, "w")
        file.write(Utils.encoder(self.database))
        file.close()

    