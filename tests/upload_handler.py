from .models import QuestionModel, AnswerModel

'''
    Loop thru all files:
        if img:
            img_dic.append
    loop thru all files again (?)
        if txt
            if in line [img] and [/img]
                search img_dic for img_file
                create models with imgs

'''
def handle_uploaded_file(f, form, request):
    print(f)
    test_choice = form.cleaned_data.get('test_choice')
    encoding = form.cleaned_data.get('encoding')
    data_dic = []
    img_dic = []

    if is_txt(f):
        for line in f:
            data_dic.append(line.decode(encoding))#.encode('utf-8'))
        create_models(data_dic, test_choice)
    else:
        img_dic.append(f)
        print(f)


def create_models(data, test_choice):
    question = QuestionModel(question=data[1], hint='', test=test_choice, img_question=None)
    question.save()
    cor_ans = correct_answer(data[0])
    i = 1
    for x in data[2:]:
        if i == cor_ans:
            a = AnswerModel(answer=x, question=question, is_correct=True)
        else:
            a = AnswerModel(answer=x, question=question)
        i+=1
        a.save()


def correct_answer(data):
    return data.find(str(1))


def is_txt(file):
    if str(file).find('txt') != -1:
        return True
    else:
        return False


class UploadHander():
    def __init__(self, request, files, form):
        self.data = []
        self.img_dic = []
        self.txt_dic = []
        self.user = request.user
        self.encoding = form.cleaned_data.get('encoding')
        self.test_choice = form.cleaned_data.get('test_choice')

        for f in files:
            if self.is_txt(f):
                self.txt_dic.append(f)
            elif self.is_img(f):
                self.img_dic.append(f)
            else:
                print('wrong file ') #TODO exception handler
        print('VVVVVVVVVVVv')
        print(self.img_dic)
        print('^^^^^^^^^^')
        for f in self.txt_dic:
            self.read_fle(f)

    def read_fle(self, f):
        data_dic = []
        images_index = []
        i=0
        for l in f:
            line = l.decode(self.encoding)
            data_dic.append(line)
            if self.is_img_required(line):
                images_index.append(i)
            i+=1
        print(f)
        if 1 in images_index:
            question = self.create_question_model(f, self.img_dic[0])
        else:
            question = self.create_question_model(data_dic[1])

        # if f in self.img_dic:
        #     question = self.create_question_model(f, data_dic[1])
        # else:
        #     question = self.create_question_model(data_dic[1])

        question.save()
        cor_ans = self.correct_answer(data_dic[0])
        y = 1
        q=0
        for x in data_dic[2:]:
            if q in images_index:
                if y == cor_ans:
                    answ = self.create_answer_model(question=question, answer=q, img_answer=self.img_dic[q], is_correct=True )
                else:
                    answ =self.create_answer_model(question=question, answer=q, img_answer=self.img_dic[q])
            else:
                if y == cor_ans:
                    answ =self.create_answer_model(question=question, answer=x, is_correct=True)
                else:
                    answ =self.create_answer_model(question=question, answer=x)

            q += 1
            y += 1
            answ.save()

    def check_imgs(self, data, idx):
        pass

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

    def correct_answer(self, data):
        return data.find(str(1))

    # def is_img(self, file):
    #     if str(file).find('png') != -1 or \
    #                     str(file).find('jpg') != -1 or \
    #                     str(file).find('jpeg') != -1 :
    #         return True
    #     else:
    #         return False

    def create_question_model(self, question=None, img_question=None):
        # if img_question is not None:
        #     question = QuestionModel(user=self.user,
        #                              img_question=img_question,
        #                              hint=hint,
        #                              test=self.test_choice)
        # else:
        question = QuestionModel(user=self.user,
                                 question=question,
                                 img_question=img_question,
                                 test=self.test_choice)
        return question
        #question.save()

    def create_answer_model(self, question, answer=None, img_answer=None, is_correct=False):
        # if img_answer is not None:
        #     answer = AnswerModel(user=self.user,
        #                          img_answer=img_answer,
        #                          is_correct=is_correct,
        #                          question=question)
        # else:
        answer = AnswerModel(user=self.user,
                             answer=answer,
                             img_answer=img_answer,
                             is_correct=is_correct,
                             question=question)
        return answer
       # answer.save()

        # user = models.ForeignKey(User, default=1)
        # answer = models.CharField(max_length=120, blank=True, null=True)
        # img_answer = models.ImageField(null=True, blank=True)
        # is_correct = models.BooleanField(default=False)
        # question = models.ForeignKey(QuestionModel, blank=True)