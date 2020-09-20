def makebold(func):
    def wrapped():
        return "В траве сидел кузнечик\n" * 2 + func()
    return wrapped
 
def makeitalic(func):
    def wrapped():
        return "Совсем как огурчик\n" + func()
    return wrapped
@makebold
@makeitalic
def func():
    return "Зелёненький он был" 
 
print (func())
