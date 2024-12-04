#Пространство имен

def test_function():
    def inner_function():
        print("Я в области видимости функции inner_function")
    # Вызов функции inner_function внутри функции test_function
    inner_function()
    print("Я в области видимости функции test_function")

#Вызов функции
test_function()

#Попробуем вызывать inner_function вне функции test_function и посмотреть на результат выполнения программы
#Обработка исключений (try except)
try:
    inner_function()  # Это вызовет ошибку, так как inner_function не доступна за пределами функции test
except Exception:
    print(f"inner_function не доступна вне функции")