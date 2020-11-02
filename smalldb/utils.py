# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:25:08 2020

@author: HP
"""
import json

class Utils:

    @staticmethod
    def is_record_match_where(where_dict, record):
        
        is_equal = True
        
        for k in where_dict:
            if (k not in record):
                return False

            if (type(where_dict[k]) is not dict) and (where_dict[k] != record[k]):
                return False

            if (type(where_dict[k]) is dict):
                is_equal = is_equal and Utils.is_record_match_where(where_dict[k], record[k])

        return is_equal
    
    
    @staticmethod
    def add_or_update(changes_dict, record):
        for k in changes_dict:
            record[k] = changes_dict[k]
            

    @staticmethod
    def obj_to_dict(obj):

        obj_dict = {
            "__class__": obj.__class__.__name__,
            "__module__": obj.__module__
        }

        obj_dict.update(obj.__dict__)

        return obj_dict
    

    @staticmethod
    def dict_to_obj(our_dict):

        if "__class__" in our_dict:
            # Pop ensures we remove metadata from the dict to leave only the instance arguments
            class_name = our_dict.pop("__class__")

            # Get the module name from the dict and import it
            module_name = our_dict.pop("__module__")

            # We use the built in __import__ function since the module name is not yet known at runtime
            module = __import__(module_name)

            # Get the class from the module
            class_ = getattr(module, class_name)

            # Use dictionary unpacking to initialize the object
            obj = class_(**our_dict)
            
        else:
            obj = our_dict

        return obj
    
    
    @staticmethod
    def encoder(database):
        json_dict = {}

        for key in database:
            json_dict[key] = json.dumps(database[key], default=Utils.obj_to_dict, indent=4, sort_keys=True)

        return json.dumps(json_dict)
    

    @staticmethod
    def decoder(json_file):
        database = {}
        json_dict = json.loads(json_file)

        for key in json_dict:
            database[key] = json.loads(json_dict[key], object_hook=Utils.dict_to_obj)
            
        return database