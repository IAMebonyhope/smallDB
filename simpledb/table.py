# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:23:13 2020

@author: HP
"""
from .utils import Utils

class Table(object):
    
    def __init__(self, name):
        """
        Initialize an empty table.
        """
        self.__name = name
        self.__records = []
        

    def create(self, record):
        """
        Add a new record to the table.
        """
        self.__records.append(record)
        

    def read_all(self):
        """
        Return list of all records in the table.
        """
        return self.__records
    
    
    def read_where(self, query_dict):
        """
        Return list of matching records.
        """
        if (len(query_dict) == 0):
            return self.__records

        matches = []
        for record in self.__records:
            if (Utils.is_record_match_where(query_dict, record)):
                matches.append(record)

        return matches
    
    
    def update_where(self, query_dict, changes_dict):
        """
        Update matching records with the values provided.
        """
        matches = self.read_where(query_dict)
        
        if (len(matches) == 0):
            self.create(changes_dict)
            
        else:
            for match in matches:
                Utils.add_or_update(changes_dict, match)
    

    def delete_all(self):
        """
        Delete all the records in the table.
        """
        self.__records.clear()


    def delete_where(self, query_dict):
        """
        Delete matching records from the table.
        """
        matches = self.read_where(query_dict)
        
        if (len(matches) == len(self.__records)):
            self.delete_all()
            
        else:
            for match in matches:
                self.__records.remove(match)

    
    def count(self, query_dict):
        """
        Return the number of matching docs.
        """
        if (len(query_dict) == 0):
            return len(self.__records)

        return len(self.read_where(query_dict))
    
    