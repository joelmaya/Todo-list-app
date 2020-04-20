from django import forms


class todoform(forms.Form):
    text=forms.CharField(max_length=300,widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Enter Todo e.g. Junk File','aria-label':'todo','aria-describedby':'add-btn'}))
    


    