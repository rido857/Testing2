# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:40:06 2019

@author: user
"""

if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('test.db')
    print "Opened database successfully";
    
    conn.execute('''CREATE TABLE SCHOOL
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         MARKS          INT);''')
    print "Table created successfully";
    conn.close()
