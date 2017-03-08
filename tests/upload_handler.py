from string import ascii_lowercase, ascii_uppercase

from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import QuestionModel, AnswerModel


class UploadHandler():
    """Handle uploading many questions files
        :keys
        request
        request.FILES.getlist('file')
        form
    """
    def __init__(self, request, files, form, is_rest=False):
        self.img_dic = []
        self.img_names_dic = []
        self.txt_dic = []
        self.user = request.user
        if not is_rest:
            self.encoding = form.cleaned_data.get('encoding')
            self.test_choice = form.cleaned_data.get('test_choice')
        else:
            self.encoding = form.data.get('encoding')
            self.test_choice = form.data.get('test_choice')
        self.check_files(files)

        for f in self.txt_dic:
            self.read_fle(f)

    def read_fle(self, f):
        data_dic = []
        i = 0
        for l in f:
            line = l.decode(self.encoding)
            if self.is_img_required(line):
                data_dic.append(self.get_img(i, f))
            else:
                data_dic.append(line)
            i += 1

        self.create_completed_objects(data_dic)

    def create_completed_objects(self, data_dic):
        if type(data_dic[1]) is InMemoryUploadedFile:
            question = self.create_question_model(data_dic[1], data_dic[1])
        else:
            question = self.create_question_model(data_dic[1])
        question.save()
        a = 1
        for x in data_dic[2:]:
            is_correct = self.correct_answer(data_dic[0], a)
            if type(x) is InMemoryUploadedFile:
                answer = self.create_answer_model(question,answer=x, img_answer=x, is_correct=is_correct)
            else:
                answer = self.create_answer_model(question, answer=x, is_correct=is_correct)
            answer.save()
            a += 1

    def check_files(self, files):
        for f in files:
            if self.is_txt(f):
                self.txt_dic.append(f)
            elif self.is_img(f):
                self.img_dic.append(f)
                self.img_names_dic.append(f.name[:-4])
            else:
                print('wrong file ') #TODO exception handler

    def get_img(self, i, file):
        print(i)
        if i >= 2:
            return self.get_img_answer(file, i)
        else:
            return self.get_img_question(file)

    def get_img_question(self, file):
        """
        Check if file is img and return it
        """
        fn = file.name[:-4]
        if fn in self.img_names_dic:
            return self.img_dic[self.img_names_dic.index(fn)]

    def get_img_answer(self, file, index):
        fn = file.name[:-4] + ascii_uppercase[index-2]
        fnlc = file.name[:-4] + ascii_lowercase[index-2]
        if fn in self.img_names_dic or fnlc in self.img_names_dic:
            return self.img_dic[self.img_names_dic.index(fn)]

    def is_txt(self, file):
        if 'txt' in str(file):
            return True
        else:
            return False

    def is_img(self, file):
        fn=str(file)
        if 'png' in fn or \
                'jpg' in fn or \
                'jpeg' in fn:
            return True
        else:
            return False

    def is_img_required(self, line):
        if '[img]' in line and '[/img]' in line:
            return True
        else:
            return False

    def correct_answer(self, data, a):
        if data[a] == '1':
            return True
        else:
            return False

    def create_question_model(self, question=None, img_question=None):
        question = QuestionModel(user=self.user,
                                 question=question,
                                 img_question=img_question,
                                 test=self.test_choice)
        return question

    def create_answer_model(self, question, answer=None, img_answer=None, is_correct=False):
        answer = AnswerModel(user=self.user,
                             answer=answer,
                             img_answer=img_answer,
                             is_correct=is_correct,
                             question=question)
        return answer
