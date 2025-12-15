#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU2025'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30043
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)
            # Check if the inserted document's ID is not None
            if insertSuccess.inserted_id:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

            
# Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            data = self.database.animals.find( {}, {"_id": False})
        # Return dataset else let the error flow up
        return data
    
# Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData })
        else:
            return "{}"
        # Return dataset else let the error flow up
        return result.raw_result

# Create method to implement the D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        # Return dataset else
        return result.raw_result
    
    

# In[3]:


animals = AnimalShelter("aacuser", "SNHU2025")


# In[116]:


print(animals.create ({
    'age_upon_outcome': "2 years",
    'animal_id': "A123456",
    'animal_type': "Dog",
    'breed': "French Bulldog",
    'color': "Black",
    'date_of_birth': "2019-01-01",
    'datetime': "2019-01-01 12:10:00",
    'monthyear': "2019-01-01T12:10:00",
    'name': "Buddy",
    'outcome_subtype': "",
    "outcome_type": "Adoption",
    'sex_upon_outcome': "Neutered Male",
    'location_lat': 30.2672,
    'location_long': -97.7431,
    'age_upon_outcome_in_weeks': 104
}))


# In[4]:


query = animals.read({"name": "Buddy"})
for animal in query:
    print(animal)


# In[6]:


#valid documentation update
updateAnimal = animals.update ({"name": "Buddy"}, {"outcome_type": "Adopted"})
print(updateAnimal)






