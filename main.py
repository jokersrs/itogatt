from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import time



#Тестирование выполнения сортировки, если сортировка выполнится некорректно программа не стартанет
def trytest():
    test = [1,7,5,4]
    bubble_sort(test)
    assert(test == [1,4,5,7])
    print("Тест успешен")

#Сортировка пузырьком
def bubble_sort(nums):
    first = True
    while first:
        first = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                first = True
#Сортировка вставкой
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
#Сортировка выборкой
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#Сортировка пирамидой
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)
#Сортрировка пирамидой
def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

#Функция создания списка и его проверки
def ent(lst):
    while True:
        try:
            listres = list(map(int, lst.split(", ")))
            return listres
        except ValueError:
            return False



#процедура нажатия функциональной кнопки
def start():
    lists = (lst.get()) #Значения entry
    text.delete(1.0, END) #Отчищаем поле для вывода
    numerlist = ent(lists) #из entry получаем значения и формируем список для сортировки
    if numerlist == False: #проверяем наличие букв и прочего
        mb.showerror("Ошибка", "Введите числа через запятую!")
    # Проверка заполнения поля ввода
    elif len(lst.get()) == 0:
        mb.showerror("Ошибка", "Вы ничего не ввели!")
    #Проверка комбобокс на выбор
    elif len(cmb.get()) == 0:
        mb.showerror("Ошибка", "Выберите тип сортировки!")
    #запускаем сортировку в соответствии с выбором
    elif cmb.get() == 'Пузырьковая':
        start_time = time.time() #запуск таймера
        bubble_sort(numerlist) #запуск сорта
        end_time = time.time() #фиксируем окончание сортировки
        elapsed_time = end_time - start_time #получаем время выполнения
        text.configure(state='normal') #открываем возможность редактирования поля текста
        text.delete(1.0, END) #отчищаем поле тексат, если ранее уже была другая сортировка
        text.insert("2.0", numerlist) #выводим сортировку 2ым элементом поля текста
        text.insert("1.0", "время выполнения: " + str(elapsed_time) + " секунд\n\n") #выводим время сортировки 1ым элементом и делаем отступ в две строки
        text.configure(state='disabled') #закрываем возможность редактировать текст
        mb.showinfo("Успешно!", "Сортировка выполнена!")
    #Все аналогично пузырьковой сортировке
    elif cmb.get() == 'Выборкой':
        start_time = time.time()
        selection_sort(numerlist)
        end_time = time.time()
        elapsed_time = end_time - start_time
        text.configure(state='normal')
        text.delete(1.0, END)
        text.insert("2.0", numerlist)
        text.insert("1.0", "время выполнения: " + str(elapsed_time) + " секунд\n\n")
        text.configure(state='disabled')
        mb.showinfo("Успешно!", "Сортировка выполнена!")
    # Все аналогично пузырьковой сортировке
    elif cmb.get() == 'Вставками':
        start_time = time.time()
        insertion_sort(numerlist)
        end_time = time.time()
        elapsed_time = end_time - start_time
        text.configure(state='normal')
        text.delete(1.0, END)
        text.insert("2.0", numerlist)
        text.insert("1.0", "время выполнения: " + str(elapsed_time) + " секунд\n\n")
        text.configure(state='disabled')
        mb.showinfo("Успешно!", "Сортировка выполнена!")
    # Все аналогично пузырьковой сортировке
    elif cmb.get() == 'Пирамидальная':
        start_time = time.time()
        heap_sort(numerlist)
        end_time = time.time()
        elapsed_time = end_time - start_time
        text.configure(state='normal')
        text.delete(1.0, END)
        text.insert("2.0", numerlist)
        text.insert("1.0", "время выполнения: " + str(elapsed_time) + " секунд\n\n")
        text.configure(state='disabled')
        mb.showinfo("Успешно!", "Сортировка выполнена!")


trytest() #тестирование корректности выполнения пузырьковой сортировкой
choice = ['Пузырьковая', 'Выборкой', 'Вставками', 'Пирамидальная'] #Данные комбобокаса
#Формируем основное окно
myroot = Tk()
myroot.title('Соритровка')
myroot.geometry('600x300')
f = ('Helvetica', 10)
lst = StringVar()
cmb = StringVar()
myroot.resizable(False, False)
label1 = Label(myroot, text='Введите числа через запятую:', font=f).place(x=10, y=10)
entry1 = (Entry(myroot, font=f, width=50, textvariable=lst))
entry1.place(x=15, y=40)
label2 = Label(myroot, text='Выебрите тип сортировки:', font=f).place(x=400, y=10)
combobox = ttk.Combobox(myroot, values=choice, state="readonly", textvariable=cmb).place(x=405, y=40)
text = Text(width=67, height=10)
text.configure(state='disabled')
text.place(x=10, y=70)
btn1 = Button(text='Сортировать', font= f, command=start).place(x=10, y=250)
btn2 = Button(text='Выход', font= f, command=myroot.destroy).place(x=455, y=250)
myroot.mainloop()




