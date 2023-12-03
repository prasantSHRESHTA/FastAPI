import sqlite3
from fastapi import FastAPI, Request, File, UploadFile, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import csv

from starlette import status

app = FastAPI()

# setting database
con = sqlite3.connect("Table.db")
cursor = con.cursor()

# creating a Table named data to store value of name and age.

cursor.execute('''CREATE TABLE IF NOT EXISTS data ( id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT,Age INTEGER )''')

con.commit()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def csvfile_upload(request: Request):
    return templates.TemplateResponse("csv_form.html", {"request": request})


# API to fetch the data from csv file and store it in " data " table.


@app.post("/uploadcsv/")
async def csv_database(request: Request, file: UploadFile = File(...), name_col: int = Form(...),
                       age_col: int = Form(...)):
    contents = await file.read()
    content_str = contents.decode("utf-8")
    rows = csv.reader(content_str.split("\n"))
    header = next(rows)

    # To throw exception when entered index value is out of range
    if not (0 <= name_col < len(header) and 0 <= age_col < len(header)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid column indices. Ensure name_column and age_column are within bounds.",
        )

    name_index = name_col if name_col < len(header) else 0
    age_index = age_col if age_col < len(header) else 1
    con = sqlite3.connect("Table.db")
    cursor = con.cursor()

    users = []
    for cols in rows:
        if len(cols) >= max(name_index, age_index) + 1:
            name = cols[name_index]
            age = cols[age_index]
            cursor.execute("INSERT INTO data (Name, Age) VALUES (?, ?)", (name, age))
            users.append({"name": name, "age": age})
    con.commit()
    con.close()

    return {"status": "CSV file Uploaded and Saved in the database successfully", "users": users}


@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request):
    conn = sqlite3.connect("Table.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data")
    users = cursor.fetchall()

    return templates.TemplateResponse("database_table.html", {"request": request, "users": users})