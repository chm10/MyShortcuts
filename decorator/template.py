def function(func):
    def decorate(*args, **kwargs):
        print("call")
        return func(*args,**kwargs)
    return decorate