from django import forms

from create.views import create
from form.views import google_Form_choice


class google_Form(forms.Form):
    dict=google_Form_choice()
    for i in range(1,len(dict['field_name'])):
        choice=[]
        for ele in dict['option']:
            choice.append((ele,ele))
            choice=tuple(choice)
        dict['field_name'][i] = "forms."+dict['type'][i]+"Field(label="+dict['field_name'][i]+", max_length=100, required="+ dict['mandatory'][i]+",choices=choice)"