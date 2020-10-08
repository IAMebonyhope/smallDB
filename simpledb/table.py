# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:23:13 2020

@author: HP
"""
from utils import Utils

class Table(object):
    
    def __init__(self, name):
        """
        Initialize an empty table.
        """
        self.name = name
        self.autoincremented_id = 1
        self.records = []
        

    def insert(self, record):
        """
        Add a new record to the table.
        """
        record[id] = self.autoincremented_id
        self.records.append(record)
        self.autoincremented_id += 1


    def get_all(self):
        """
        Return list of all records in the table.
        """
        return self.records
    
    
    def get_first(self, where_dict):
        """
        Return the first matching record.
        If none is found, return None.
        """
        if (len(where_dict) == 0):
            return self.records[0]

        for record in self.records:
            if (Utils.is_record_match_where(where_dict, record)):
                return record
            
        return None
    
    
    def get(self, where_dict):
        """
        Return list of matching records.
        """
        if (len(where_dict) == 0):
            return self.records

        matches = []
        for record in self.records:
            if (Utils.is_record_match_where(where_dict, record)):
                matches.append(record)

        return matches
    
    
    def update(self, where_dict, changes_dict):
        """
        Update matching records with the values provided.
        """
        matches = self.get(where_dict)
        
        if (len(matches) == 0):
            self.insert(changes_dict)
            
        else:
            for match in matches:
                Utils.add_or_update(changes_dict, match)
    

    def delete_all(self):
        """
        Delete all the records in the table.
        """
        self.records.clear()


    def delete(self, where_dict):
        """
        Delete matching records from the table.
        """
        matches = self.get(where_dict)
        
        if (len(matches) == len(self.collections)):
            self.delete_all()
            
        else:
            for match in matches:
                self.records.remove(match)

    
    def count(self, where_dict):
        """
        Return the number of matching docs.
        """
        if (len(where_dict) == 0):
            return len(self.records)

        return len(self.get(where_dict))
    
    