from django import forms
from .models import Assessment

class AssessmentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-400'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-400'
        })
    )

    class Meta:
        model = Assessment
        exclude = ['employee', 'ai_summary', 'ai_recommendations', 'wellness_score', 'created_at']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-400'
            })