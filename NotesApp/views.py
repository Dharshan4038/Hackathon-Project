from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from NotesApp.models import Notes
from NotesApp.serializers import NoteSerializers

@csrf_exempt
def noteApi(request,id=0):
    if request.method == 'GET':
        notes = Notes.objects.all()
        note_serializer = NoteSerializers(notes,many=True)
        return JsonResponse(note_serializer.data,safe=False)

    elif request.method == 'POST':
        note_data = JSONParser().parse(request)
        note_serializer = NoteSerializers(data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Note Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method == 'PUT':
        note_data = JSONParser().parse(request)
        note = Notes.objects.get(NoteId=note_data['NoteId'])
        note_serializer = NoteSerializers(note,data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Failed to update.",safe=False)
    
    elif request.method == 'DELETE':
        note = Notes.objects.get(NoteId=id)
        note.delete()
        return JsonResponse("Deleted Successfully!!",safe=False)
    