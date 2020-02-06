from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import string
import random
import hashlib

def hashing_password(user_pw):
    count = random.randint(4, 12)
    string_pool = string.ascii_letters + string.digits + string.punctuation
    salt = "".join(random.choices(string_pool, k=count))

    hashed_pw = hashlib.md5(str(user_pw + salt).encode('utf-8')).hexdigest()

    return salt, hashed_pw