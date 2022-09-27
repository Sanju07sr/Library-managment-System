from flask import Flask, render_template,request,redirect,url_for
import pymysql
db_connection = None
tb_cursor = None

app=Flask(__name__)

@app.route("/")
def index():
    booksData = getAllBooks()
    return render_template("index.html",data=booksData)

@app.route("/add/",methods=["GET","POST"])
def addBook():
    if request.method=="POST":
        data = request.form
        isInserted = insertIntoTable(data['txtName'],data['txtAuthor'],data['txtPrice'],data['txtPublication'],data['txtPublicationDate'])
        if(isInserted):
            message = "Insertion sucess"
            return redirect(url_for("index"))
        else:
            message = "Insertion error"
            return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/update/",methods=["GET","POST"])
def updateBook():
    id = request.args.get("ID",type=int,default=1)
    idData = getBookID(id)
    if request.method == "POST":
        data = request.form
        print(data)
        isUpdated = updateBookIntoTable(data['txtName'],data['txtAuthor'],data['txtPrice'],data['txtPb'],data['txtPbd'],id)
        if(isUpdated):
            message = "Updattion sucess"
            return redirect(url_for("index"))
        else:
            message = "Updattion Error"
        return redirect(url_for("index"))
    return render_template("update.html",data=idData)

@app.route("/delete/")
def deleteBook():
    id = request.args.get("ID",type=int,default=1)
    deleteBookFromTable(id)
    return redirect(url_for("index"))

def dbConnect():
    global db_connection, tb_cursor
    db_connection=pymysql.connect(host="localhost",
    user="root",passwd="",database="lms",port=3306)
    if(db_connection):
        print("Connected")
        tb_cursor = db_connection.cursor()
    else:
        print("Not Connected")

def dbDisconnect():
    db_connection.close()
    tb_cursor.close()

def getAllBooks():
    dbConnect()
    getQuery="select * from books"
    tb_cursor.execute(getQuery)
    booksData = tb_cursor.fetchall()
    dbDisconnect()
    return booksData

def insertIntoTable(name,author,price,publication,publicationdate):
    dbConnect()
    insertQuery = "INSERT INTO Books(name,author,price,publication,publication_date) VALUES(%s, %s, %s, %s,%s);"
    tb_cursor.execute(insertQuery,(name,author,price,publication,publicationdate))
    db_connection.commit()
    dbDisconnect()
    return True

def getBookID(book_id):
    dbConnect()
    selectQuery = "SELECT * FROM books WHERE ID=%s;"
    tb_cursor.execute(selectQuery,(book_id,))
    oneData = tb_cursor.fetchone()
    dbDisconnect()
    return oneData

def updateBookIntoTable(name,author,price,pb,pbd,id):
    dbConnect()
    updateQuery = "UPDATE books SET name=%s,author=%s,price=%s,publication=%s,publication_date=%s WHERE ID=%s;"
    tb_cursor.execute(updateQuery,(name,author,price,pb,pbd,id))
    db_connection.commit()
    dbDisconnect()
    return True

def deleteBookFromTable(id):
    dbConnect()
    deleteQuery = "DELETE FROM books WHERE ID=%s;"
    tb_cursor.execute(deleteQuery,(id,))
    db_connection.commit()
    dbDisconnect()
    return True

if __name__=="__main__":
    app.run(debug=True)
