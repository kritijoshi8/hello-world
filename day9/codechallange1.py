# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:36:24 2018

@author: Dell
"""
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost',27017)
mydb = client.db_university

def add_client(Student_Name,Student_Age,Student_Roll_no,Student_Branch):
    unique_client = mydb.students.find_one({"Student_Roll_no":Student_Roll_no},{"_id":0})
    if unique_client:
        return "Client already exists"
    else:
        mydb.students.insert(
                {
                "Student_Name":Student_Name,
                "Student_Age":Student_Age,
                "Student_Roll_no": Student_Roll_no,
                "Student_Branch" : Student_Branch,
                "Date-Time" : datetime.now()
                })
        return "Student added successfully"

def view_client(Student_Roll_no):
    user = mydb.students.find_one({"Student_Roll_no" :Student_Roll_no}, {"_id":0})
    if user:
        name = user["Student_Name"]
        age = user["Student_Age"]
        roll_no = user["Student_Roll_no"]
        branch = user["Student_Branch"]
        #time = user["Date-Time"]
        return {"Student_Name":name,"Student_Age":age,"Student_Roll_no":roll_no,"Student_Branch":branch}
    else:
        return "Sorry, No such user exists"


name = raw_input("Enter Student Name: ")
age = raw_input("Enter Student Age: ")
roll_no = raw_input("Enter Student Roll no :")
branch = raw_input("Enter Student Branch: ")

print add_client(name,age,roll_no,branch)

user = raw_input("Enter Student Roll no to find: ")
user_data = view_client(user)

print user_data
                        
    
