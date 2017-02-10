from django import forms

from .models import TestModel, QuestionModel, AnswerModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = [
            'title',
            'user'

        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = [
            'question',
            'hint',
            'test'
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = [
            'answer',
            'img_answer',
            'is_correct',
            'question',
            'user'
        ]


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    test_choice = forms.ModelChoiceField(queryset=TestModel.objects.all(), empty_label=None)


class FileUploadForm(forms.Form):

    file = forms.FileField()

    def clean_file(self):
        data = self.cleaned_data["file"]

        # read and parse the file, create a Python dictionary `data_dict` from it
        form = QuestionForm(data)
        if form.is_valid():
            # we don't want to put the object to the database on this step
            self.instance = form.save(commit=False)
        else:
            # You can use more specific error message here
            raise forms.ValidationError(u"The file contains invalid data.")
        return data

    def save(self):
        # We are not overriding the `save` method here because `form.Form` does not have it.
        # We just add it for convenience.
        instance = getattr(self, "instance", None)
        if instance:
            instance.save()
        return instance