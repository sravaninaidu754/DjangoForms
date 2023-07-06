from django import forms
c=[('python','PYTHON'),('java','JAVA'),('sql','SQL'),('Django','DJANGO'),('web','WEB')]
g=[('male','MALE'),('female','FEMALE')]
class signupform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
