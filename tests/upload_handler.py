from .models import QuestionModel, AnswerModel, TestModel


def handle_uploaded_file(f, form, request):
    print(request.user)
    test_choice = form.cleaned_data.get('test_choice')
    encoding = form.cleaned_data.get('encoding')
    data_dic = []
    for line in f:
        data_dic.append(line.decode(encoding))#.encode('utf-8'))
    create_models(data_dic, test_choice)


def create_models(data, test_choice):
    question = QuestionModel(question=data[1], hint='ds', test=test_choice)
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
