from tkinter import *
import psycopg2

class Form:
    def __init__(self, form_name, geom):
        self.root = Tk()
        self.root.title(form_name)
        self.root.geometry(geom)
        self.width = 50

class Entry_1:
    def __init__(self, form, label, data):
        self.lab_1 = Label(form.root, text=label)
        self.ent_1 = Entry(form.root, width=form.width + 16)
        self.lab_1.pack()
        self.ent_1.pack()
        self.ent_1.insert(0, data)
    
    def set_1(self, text):
        self.ent_1.delete(0, END)
        self.ent_1.insert(0, text)
    
    def get(self):
        return self.ent_1.get()

class Button_1:
    def __init__(self, form, text_b, width_b, height_b, command_b):
        self.b1 = Button(form.root, text=text_b, width=width_b, height=height_b)
        self.b1.config(command=command_b)
        self.b1.pack()

class Scene_1:
    def __init__(self):
        self.n = 0
        self.load_data()
        self.form1 = Form('Форма для доступа к таблице "Клиент"', '500x500+400+200')
        
        self.qstn_1 = Entry_1(self.form1, 'ID_поставщика:', self.rows[self.n][0])
        self.qstn_2 = Entry_1(self.form1, 'Название поставщика:', self.rows[self.n][1])
        self.qstn_3 = Entry_1(self.form1, 'Фамилия:', self.rows[self.n][2])
        self.qstn_4 = Entry_1(self.form1, 'Имя:', self.rows[self.n][3])
        self.qstn_5 = Entry_1(self.form1, 'Отчество:', self.rows[self.n][4])
        self.qstn_6 = Entry_1(self.form1, 'Телефон:', self.rows[self.n][5])
        
        self.but_1 = Button_1(self.form1, "Следующая запись", 50, 2, self.next_record)
        self.but_2 = Button_1(self.form1, "Предыдущая запись", 50, 2, self.previous_record)
        self.but_3 = Button_1(self.form1, "Добавить запись", 50, 2, self.add_record)
        self.but_4 = Button_1(self.form1, "Удалить запись", 50, 2, self.delete_record)

        self.form1.root.mainloop()

    def load_data(self):
        conn = psycopg2.connect(database="torg_firm", user="postgres", password="postgres", host="10.1.66.19", port="5432")
        cur = conn.cursor()
        cur.execute('SELECT * FROM "поставщики";')
        self.rows = cur.fetchall()
        conn.close()
        if not self.rows:
            self.rows = [[0, 0, 0, 0, 0, 0]]

    def next_record(self):
        if self.n < len(self.rows) - 1:
            self.n += 1
            self.update_entries()

    def previous_record(self):
        if self.n > 0:
            self.n -= 1
            self.update_entries()

    def update_entries(self):
        self.qstn_1.set_1(self.rows[self.n][0])
        self.qstn_2.set_1(self.rows[self.n][1])
        self.qstn_3.set_1(self.rows[self.n][2])
        self.qstn_4.set_1(self.rows[self.n][3])
        self.qstn_5.set_1(self.rows[self.n][4])
        self.qstn_6.set_1(self.rows[self.n][5])

    def add_record(self):
        new_data = (
            self.qstn_1.get(),
            self.qstn_2.get(),
            self.qstn_3.get(),
            self.qstn_4.get(),
            self.qstn_5.get(),
            self.qstn_6.get(),
        )
        
        conn = psycopg2.connect(database="torg_firm", user="postgres", password="postgres", host="10.1.66.19", port="5432")
        cur = conn.cursor()
        cur.execute('INSERT INTO "поставщики" VALUES (%s, %s, %s, %s, %s, %s);', new_data)
        conn.commit()
        cur.close()
        conn.close()
        self.load_data()  # Reload data to reflect changes
        self.update_entries()

    def delete_record(self):
        id_to_delete = self.qstn_1.get()
        
        conn = psycopg2.connect(database="torg_firm", user="postgres", password="postgres", host="10.1.66.19", port="5432")
        cur = conn.cursor()
        cur.execute('DELETE FROM "поставщики" WHERE "id поставщика"=%s;', (id_to_delete,))
        conn.commit()
        cur.close()
        conn.close()
        
        self.load_data()  # Reload data to reflect changes
        self.update_entries()

scene = Scene_1()
