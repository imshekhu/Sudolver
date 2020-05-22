from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse

class MyView(View):
    #get The sudoku board in Render.
    def get(self, request):
        template ='sudokuboard.html'
        return TemplateResponse(request,template)