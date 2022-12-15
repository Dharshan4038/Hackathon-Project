from rest_framework import serializers
from NotesApp.models import Notes

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('NoteId',
                  'NoteTitle',
                  'NoteContent',
                  'NoteCreated')