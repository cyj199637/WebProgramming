from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth.decorators import login_required