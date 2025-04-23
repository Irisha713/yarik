def log(filename=None):
    """автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""
    def my_function(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    file = open(filename, 'a')
                    file.write(f"{func.__name__} ok\n")
                    file.close()
                else:
                    print(f"{func.__name__} ok")
                    return result
            except Exception as e:
                if filename:
                    file = open(filename, 'a')
                    file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                    file.close()
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
            return None
        return inner
    return my_function
