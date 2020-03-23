import json

from django.http import HttpResponse
from django.shortcuts import render
from gpt2_sciq.app.gpt2.gen import main
from rest_framework import generics
from gpt2_sciq.app.gpt2_distractor_generation.serializers import *

def create_prompt_string(support, question, key):
    return '<|support|>'+support+'<|question|>'+question+'<|key|>'+key+'<|distractor|>'


# Create your views here.
def generate_distractor(request):
    prompt_text  = create_prompt_string(support=request.GET.get('s'),
                         question=request.GET.get('q'),
                         key=request.GET.get('k'))
    generated_sequences, text = main(prompt = prompt_text,
                                     gen_number = request.GET.get('gen_number'))
    result = {}
    for ids, generated_sequence in enumerate(generated_sequences):
        result['generated_sequence_'+str(ids)] = str(generated_sequence).replace(prompt_text, '')
    result = json.dumps(result)
    return HttpResponse(result)
