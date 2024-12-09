from flask import Flask,url_for,redirect
import sqlite3 

year = int(input("Рік народження "))
def index():
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE "Birth Year" = (?)',[year])
    data = cursor.fetchall()

    if len(data)==0:
        return "У базі немає таких митців"
    elif len(data) == 1:
        return "" + str(year) + "роцы народився " + data[0][0]
    else:
        res = "<ol>"
        for i in data:
            res += "<li>"+i[0]+"</li>"
        res +="</ol>"
    return res

app = Flask(__name__)
app.add_url_rule("/", "index",index)

if __name__ == "__main__":
    app.run()



