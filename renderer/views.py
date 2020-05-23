from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
from .sudoku import start

@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    #get The sudoku board in Render.
    
    def get(self, request):
        template ='sudokuboard.html'
        return TemplateResponse(request,template)
    
    
    def post(self, request):
        print(type(request.body))
        data = json.loads (request.body)
        start(data)
        return  HttpResponse({"response":"jeirjrs"}, content_type="application/json")
        