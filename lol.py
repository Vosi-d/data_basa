import sqlite3
from datetime import datetime
conn= sqlite3.connect('bank.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, num TEXT, balance INTEGER, date DATETIME);')
conn.commit()
def regist(name, num, balance=0):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, num, balance, date) VALUES (?,?,?,?);', (name, num, balance,datetime.now()))
    conn.commit()
    return "Регистрация завершена успешно"
def add(num, money):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    acctual_balance = cur.execute('SELECT balance FROM users WHERE num=?;', (num,)).fetchone()
    new_balance= acctual_balance[0]+money
    cur.execute('UPDATE users SET balance=? WHERE num=?;',(new_balance, num))
    conn.commit()
    return prosmotr_balance(num)


def minus(num, money):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    acctual_balance = cur.execute('SELECT balance FROM users WHERE num=?;', (num,)).fetchone()
    cur.execute('UPDATE users SET balance=? WHERE num=?;', (acctual_balance[0]-money, num))
    conn.commit()
    return prosmotr_balance(num)
def godovoy_pr(num, money):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    acctual_balance = cur.execute('SELECT balance FROM users WHERE num=?;', (num,)).fetchone()
    cur.execute('UPDATE users SET balance=? WHERE num=?;',(acctual_balance[0]*101/100,num))
    conn.commit()
    return "Годовой процент добавлен"
def prosmotr_balance(num):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    acctual_balance = cur.execute('SELECT balance FROM users WHERE num=?;', (num,)).fetchone()
    return acctual_balance
def proverka_nomera(num):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    tuls=cur.execute('SELECT num FROM users WHERE num=?;', (num,))
    if tuls:
        return True
    else:
        return False

