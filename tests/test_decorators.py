from src.decorators import log

def test_my_function(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"

def test_my_function1(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function(1, '2')
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"

def test_my_function2():
    @log(filename="tests/mylog.txt")
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    file = open('tests/mylog.txt', 'r')
    content = file.read()
    file.close()
    assert content == "my_function ok\n"
