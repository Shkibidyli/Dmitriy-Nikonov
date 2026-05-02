# Импорт библиотек
import tkinter as tk  # Импортируем основную библиотеку для создания графического интерфейса
from tkinter import ttk, messagebox  # Импортируем дополнительные компоненты: ttk (стилизованные виджеты) и messagebox (окна сообщений)
import random  # Импортируем библиотеку для генерации случайных чисел

def generate_random():
    """
    Функция для генерации случайного числа в заданном диапазоне.
    Обрабатывает ввод пользователя, проверяет корректность данных и выводит результат.
    """
    try:
        # Получаем значения из полей ввода и преобразуем их в целые числа
        min_val = int(min_entry.get())  # Минимальное значение диапазона
        max_val = int(max_entry.get())  # Максимальное значение диапазона

        # Проверяем, что минимальное значение не превышает максимальное
        if min_val > max_val:
            # Показываем сообщение об ошибке, если условие нарушено
            messagebox.showerror("Ошибка", "Минимальное значение не может быть больше максимального!")
            return  # Прерываем выполнение функции

        # Генерируем случайное целое число в заданном диапазоне [min_val, max_val]
        result = random.randint(min_val, max_val)
        # Обновляем текст метки, отображающей результат (делаем текст акцентным цветом)
        result_label.config(text=f"Случайное число: {result}", foreground="#00a896")

    except ValueError:
        # Обрабатываем ошибку преобразования в целое число (если введены нечисловые данные)
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа в оба поля.")

# Создание основного окна приложения
root = tk.Tk()  # Инициализируем главное окно
root.title("Генератор случайных чисел")  # Устанавливаем заголовок окна
root.geometry("220x240")  # Немного увеличили размеры для лучшей читаемости
root.resizable(False, False)  # Запрещаем изменение размеров окна пользователем
root.configure(bg="#1a2b3c")  # Тёмно‑синий фон основного окна

# Создаём стиль для виджетов ttk
style = ttk.Style()
style.configure("TLabel", background="#1a2b3c", foreground="white")  # Белые надписи на тёмном фоне
style.configure("TButton", background="#00a896", foreground="white", font=("Arial", 10, "bold"))
style.map("TButton",
          background=[("active", "#008f80"), ("pressed", "#007a6c")])  # Изменение цвета при наведении и нажатии
style.configure("TEntry", fieldbackground="white", foreground="#333333")

# Виджет для ввода минимального значения
min_label = ttk.Label(root, text="Минимум:")  # Создаём метку с текстом «Минимум:»
min_label.grid(row=0, column=0, padx=10, pady=12, sticky="e")  # Размещаем метку в сетке (строка 0, столбец 0)

min_entry = ttk.Entry(root, width=15)  # Создаём поле ввода с шириной 15 символов
min_entry.grid(row=0, column=1, padx=10, pady=12)  # Размещаем поле ввода рядом с меткой
min_entry.insert(0, "1")  # Вставляем значение по умолчанию — «1»

# Виджет для ввода максимального значения
max_label = ttk.Label(root, text="Максимум:")  # Создаём метку с текстом «Максимум:»
max_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")  # Размещаем метку в сетке (строка 1, столбец 0)

max_entry = ttk.Entry(root, width=15)  # Создаём второе поле ввода
max_entry.grid(row=1, column=1, padx=10, pady=8)  # Размещаем его рядом с соответствующей меткой
max_entry.insert(0, "100")  # Вставляем значение по умолчанию — «100»

# Кнопка для запуска генерации случайного числа
generate_btn = ttk.Button(root, text="Сгенерировать", command=generate_random)  # Создаём кнопку с надписью и привязкой к функции
generate_btn.grid(row=2, column=0, columnspan=2, pady=15)  # Размещаем кнопку (занимает 2 столбца)

# Метка для отображения результата генерации
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))  # Создаём пустую метку с заданным шрифтом
result_label.grid(row=3, column=0, columnspan=2, pady=5)  # Размещаем её в нижней части окна (занимает 2 столбца)

# Запускаем главный цикл обработки событий (ожидание действий пользователя)
root.mainloop()
