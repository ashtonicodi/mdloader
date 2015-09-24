__author__ = 'Ashton'

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        # Теперь мы распакуем *args и **kwargs
        # Если вы не слишком хорошо знакомы с распаковкой, можете прочесть следующую статью:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # Теперь мы можем указать значение по умолчанию
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))

m = Mary()
m.sayYourAge()