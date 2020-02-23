from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.contrib import messages
from accounts.models import User
from django.contrib.auth import authenticate, login, logout
import string
import random
import hashlib
import base64
from django.contrib.auth.hashers import pbkdf2

def hashing_password(user_pw):
    count = random.randint(16, 21)
    string_pool = string.ascii_letters + string.digits + string.punctuation
    salt = "".join(random.choices(string_pool, k=count))

    hash = pbkdf2(user_pw, salt, 10000, digest=hashlib.sha256)
    hashed_pw = base64.b64encode(hash).decode('ascii').strip()

    return salt, hashed_pw