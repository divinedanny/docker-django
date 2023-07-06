from django.urls import path, re_path
from .views import CreateNoteView, ViewAllNotesView, ViewOneNoteView,HealthCheckView

app_name = 'notes'

urlpatterns = [
    path('', HealthCheckView.as_view(), name='health_check'),
    path('create-note/', CreateNoteView.as_view(), name= 'create_note'),
    path('view-all-note/', ViewAllNotesView.as_view(), name='view_all_notes'),
    path('note/<uuid:id>/', ViewOneNoteView.as_view(), name='view_note'),
    
]