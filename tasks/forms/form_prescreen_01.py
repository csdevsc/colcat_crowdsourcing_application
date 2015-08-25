from django import forms
from django.forms import ModelForm
from tasks.forms.common import CONFIDENCE_CHOICES, HorizontalRadioRenderer
from tasks.models import Task_Prescreen_01

class Form_Task_Prescreen_01_a(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'answer_01', 'answer_02', 'answer_03', 'answer_04', 'answer_05',
                   'answer_06', 'answer_07', 'answer_08', 'answer_09', 'answer_10')
    question_01 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_02 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")
    question_03 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_04 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_05 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_06 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_07 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_08 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_09 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")
    question_10 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="ANSWER")

class Form_Task_Prescreen_01_b(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'answer_11', 'answer_12', 'answer_13', 'answer_14', 'answer_15',
                   'answer_16', 'answer_17', 'answer_18', 'answer_19', 'answer_20')
    cell_a1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX A1")
    confidence_a0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")
                                          cell_a0 = forms.CharField(widget=forms.TextInput(), label="A", required=False)
