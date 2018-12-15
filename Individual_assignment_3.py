#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 18:16:53 2018

@author: anikkengjeruldsen
"""

#%%
from Ex1 import Product
from Ex1 import recalculate_quality

def test_potatoe():
    products = [Product("potato",-5),Product("potato",0),Product("potato",5),Product("potato",10),Product("potato",15)]
    for case in products:
        before = case.quality
        recalculate_quality(case)
        after = case.quality
        assert after  == before - 0.5 


def test_cheese():
    products = [Product("cheese",-5),Product("cheese",0),Product("cheese",5),Product("cheese",10),Product("cheese",15)]
    for case in products:
        before = case.quality
        recalculate_quality(case)
        after = case.quality
        assert  after == before - 2
        

        
def test_recalculate_randomlow():
    products = [Product("apple",-5),Product("tomatoe",0)]
    for case in products:
        before = case.quality
        recalculate_quality(case)
        after = case.quality
        assert  after == before - 3
        
def test_recalculate_randomhigh():
    products = [Product("water",5),Product("beer",6),Product("wine",15)]
    for case in products:
        before = case.quality
        recalculate_quality(case)
        after = case.quality
        assert  after == before
                  

#%%
            
#Exercise 2
# Using Github API:
# - Create a function that: takes all repositories form my account
            
def get_anikken_repos():
    response = requests.get("https://api.github.com/users/abagj/repos")
    repos = response.json()
    dicti_description = {}
    for i in repos:
        description = "The repo " + str(i['name']) +  " has " + str(i['stargazers_count']) + " star(s), is mainly written in " + str(i['language']) +  " and can be found on: "+ str(i['html_url'])
        dicti_description[str(i['name'])] = description
    return dicti_description

import requests


#print a short description  of each repository, name, stars, language and url

def print_my_repositories():
    response = requests.get("https://api.github.com/users/abagj/repos").json()
    l = []
    for i in response:
        description = {}
        description["name"] = i['name']
        description["Stars"] = i['stargazers_count']
        description["language"] = i['language']
        description["URL"] = i['url']
        l.append(description)
    return l


#%%
#Exercise3
    
from flask import Flask, jsonify

server = Flask("phonebook server ")

phonebook = {"Me" : "40724090",
              "Mum": "98280272",
              "Dad":"95060255",
              "Sis": "47617893"}


@server.route("/phonebook")
def phonebook_handler():
    return jsonify(phonebook)


@server.route("/phonebook/<name>", methods = ["GET"])
def getphone_handler(name):
    for contact in phonebook:
        if contact == name:
            return jsonify(phonebook[name]) 
    return  jsonify({"message":"Name not found!"})        
   
@server.route("/add/<name>/<phone>", methods = ["POST"])
def addcontact_handler(name,phone):
    for contact in phonebook:
        if contact == name:
            return jsonify({"message":"Contact already exists"})
    phonebook[name] = str(phone) 
    return jsonify({"message":"Added Contact!"})
        
       
@server.route("/delete/<name>", methods = ["DELETE"])
def deletecontact_handler(name):
    for contact in phonebook:
        if contact != name:
            phonebook.pop(name)
            return jsonify("deleted contact!")
    return jsonify({"message":"Name not found!"})

@server.route("/update/<name>/<phone>", methods = ["POST"])
def updatecontact_handler(name,phone):
    for contact in phonebook:
        if contact == name:
            phonebook[name] = str(phone) 
            return jsonify({"message":"added contact"})
    return jsonify({"message":"Name not found!"})

    

server.run()



import requests


def phonebook():
    response = requests.get("http://127.0.0.1:5000/phonebook")
    if response.status_code == 200:
        return response.json()
    else:
        return "It failed"
    
def getphone(user):
    response = requests.get("http://127.0.0.1:5000/phonebook/"+user)
    if response.status_code == 200:
        return response.json() 
    else:
        return "It failed"

def addcontact(name,phone):
    response = requests.post("http://127.0.0.1:5000/add/"+name+"/"+str(phone))
    if response.status_code == 200:
        return response.json()
    else:
        return "It failed"

def deletecontact(name):
    response = requests.delete("http://127.0.0.1:5000/delete/"+name)
    if response.status_code == 200:
        return response.json() 
    else:
        return "It failed"  
    
def updatecontact(name,phone):
    response = requests.post("http://127.0.0.1:5000/update/"+name+"/"+str(phone))
    if response.status_code == 200:
        return response.json()
    else:
        return "It failed"  