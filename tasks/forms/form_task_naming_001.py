from django import forms
from django.forms import ModelForm
from tasks.forms.common import CONFIDENCE_CHOICES, HorizontalRadioRenderer
from tasks.models import Task_Naming_001

class Form_Task_Naming_001_001(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_a0', 'confidence_a0', )
    cell_a0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX A0")
    confidence_a0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_002(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_b0', 'confidence_b0', )
    cell_b0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX B0")
    confidence_b0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_003(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_c0', 'confidence_c0', )
    cell_c0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX C0")
    confidence_c0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_004(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_d0', 'confidence_d0', )
    cell_d0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX D0")
    confidence_d0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_005(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_e0', 'confidence_e0', )
    cell_e0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX E0")
    confidence_e0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_006(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_f0', 'confidence_f0', )
    cell_f0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX F0")
    confidence_f0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_007(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_g0', 'confidence_g0', )
    cell_g0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX G0")
    confidence_g0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_008(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_h0', 'confidence_h0', )
    cell_h0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX H0")
    confidence_h0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_009(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_i0', 'confidence_i0', )
    cell_i0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX I0")
    confidence_i0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")

class Form_Task_Naming_001_010(ModelForm):
    class Meta:
        model = Task_Naming_001
        fields = ( 'cell_j0', 'confidence_j0', )
    cell_j0 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-lg'}), label="BOX J0")
    confidence_j0 = forms.ChoiceField(widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                      choices=CONFIDENCE_CHOICES, label="How sure are you?")
