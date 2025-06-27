from django.urls import path
from .views import assessment_view, report_view
from .views import assessment_view, report_view, export_pdf_view



urlpatterns = [
    path('', assessment_view, name='assessment'),
    path('report/<int:assessment_id>/', report_view, name='report'),
    path('report/<int:assessment_id>/pdf/', export_pdf_view, name='export_pdf'),
]