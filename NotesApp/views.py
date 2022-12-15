from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from NotesApp.models import Notes
from NotesApp.serializers import NoteSerializers

import json
from NotesApp import function1

@csrf_exempt
def noteApi(request,id=0):
    if request.method == 'GET':
        notes = Notes.objects.all()
        note_serializer = NoteSerializers(notes,many=True)
        return JsonResponse(note_serializer.data,safe=False)

    elif request.method == 'POST':
        note_data1 = JSONParser().parse(request)
        tamil_data=function1.note_validation(note_data1['NoteTitle'],note_data1['NoteContent'])
        note_serializer = NoteSerializers(data=tamil_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Note Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method == 'PUT':
        note_data1 = JSONParser().parse(request)
        note = Notes.objects.get(NoteId=note_data1['NoteId'])
        tamil_data=function1.note_validation(note_data1['NoteTitle'],note_data1['NoteContent'])
        note_serializer = NoteSerializers(note,data=tamil_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Failed to update.",safe=False)
    
    elif request.method == 'DELETE':
        note = Notes.objects.get(NoteId=id)
        note.delete()
        return JsonResponse("Deleted Successfully!!",safe=False)
    