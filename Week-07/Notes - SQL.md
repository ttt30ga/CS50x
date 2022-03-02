# CS50 Week 7 - SQL

[Watch lecture on Youtube](https://youtu.be/D-1kNFO568c)

---

## Python

## Lambda Function

It's an anonymous function that need to be called once

```
for title in sorted(titles, key=lambda title: titles[title]):
    print(title, titles[title])
```

## Cleaning data

```
if "OFFICE" in title:
    counter += 1
```

## Regular Expressions

`.` any characters\
`.*` 0 or more characters\
`.+` 1 or more characters\
`?` optional\
`^` start of input\
`S` end of input

```
import re
...
if re.search("^(OFFICE|THE.OFFICE)$", title):
    counter += 1
```

## Search

```
import csv

title = input("Title: ").strip().upper()
counter = 0

with open("favourites.csv", "r") as file
    reader = csv.DictReader(file)
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1

print(counter)
```

---

## SQL

## Create, Read, Update, Delete - CRUD

sqlite3 - a lightweight SQL version, commonly used on smartphones apps

`$ sqlite3 favourites.db` - creates new db\
`sqlite> .mode csv` - change to csv mode db\
`sqlite> .import favourites.csv favourites` - import file into favourites\
`$ sqlite3 favourites.db` - run db\
`sqlite> .schema` - this shows the data types, colums etc

## Select

```
$ sqlite3 favourites.db
SQLite version 3.36.0 ...
sqlite> SELECT title FROM favourites;
+---------------------------------------+
|                 title                 |
+---------------------------------------+
| value 1                               |
| value 2                               |
| value 3                               |
+---------------------------------------+
```

```
sqlite> SELECT title, genres FROM favourites;
```

> This show similar table as above but with `genre` column too

Some common functionalties in SWL are:\
`AVG`\
`COUNT`\
`DISTINCT`\
`LOWER`\
`MAX`\
`MIN`\
`UPPER`\
...

```
sqlite> SELECT DISTINCT(title) FROM favourites;
```

> This shows the distinct `title` values

```
sqlite> SELECT DISTINCT(UPPER(title)) FROM favourites;
```

> This shows `title` in uppercase

## Where

Other additional filtration in SQL
`WHERE`\
`LIKE`\
`ORDER BY`\
`LIMIT`\
`GROUP BY`\
...

```
sqlite> SELECT title FROM favourites WHERE title LIKE "office";
```

```
sqlite> SELECT title FROM favourites WHERE title = "office";
```

> `=` sign is for comparison

```
sqlite> SELECT title FROM favourites WHERE title = "%office%";
```

> `%` means or more characters left or right

```
sqlite> UPDATE favourites SET title = "The Office" WHERE title = "Thevoffice";
```

> The code above updates a title

```
sqlite> UPDATE favourites SET title = "The Office" WHERE title = "Thevoffice";
```

> The code above updates a title

# Table Relationships

```
$ sqlite3 favourites8.db\
sqlite> .schema
CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id));\
CREATE TABLE genres (show_id INTEGER, genre TEXT NOT NULL, FOREIGN KEY(show_id) REFERENCES shows(id))\
sqlite>
```

> Two tables called `shows` and `genres`

```
sqlite> SELECT show_id FROM genres WHERE genre = "Comedy";
```

> Return `show_id`

```
sqlite> SELECT DISTINCT(title) FROM shows WHERE id IN ( SELECT show_id FROM genres WHERE genre = "Comedy") ORDER BY title;
```

> Return `titles` that where labled `comedy` sorted by title, removing duplicates

## Python and SQL

```
import csv
from cs50 import SQL

db = SQL("sql:///favourites.db")

title = input("Title: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM favourites WHERE title LIKE ?", title)

row = rows[0]

print(row["counter"])
```

> Return count of the same `title`

```
import csv
from cs50 import SQL

db = SQL("sql:///favourites.db")

title = input("Title: ").strip()

rows = db.execute("SELECT title FROM favourites WHERE title LIKE ?", title)

for row in rows:
    print(row["title"])
```

> Return list of same `title`

## SQL Data Types

`BLOB`\
`INTEGER`\
`NUMERIC`\
`REAL`\
`TEXT`

## Many-to-Many Relashionships

`PRIMARY KEY` is that column that uniquely idenfies all the data.\
`FOREIGN KEY` is the appearance of another tables `PRIMARY KEY` in it own table. Meaning it has been declared in another table, therefore "foreign".

## Indexes

It's a data structure that allows the database to do better than `linear search`

```
sqlite> CREATE INDEX name ON table (column, ...);
```

```
sqlite> SELECT * FROM people WHERE name = "Steve Carrel";
+--------+--------------+-------+
|   id   |     name     | birth |
+--------+--------------+-------+
| 136797 | Steve Carrel | 1962  |
+--------+--------------+-------+

sqlite> SELECT id FROM people WHERE name = "Steve Carrel";
+--------+
|   id   |
+--------+
| 136797 |
+--------+

sqlite> SELECT show_id FROM stars WHERE person_id = (SELECT id from people WHERE name = "Steve Carrel");
+----------+
| show_id  |
+----------+
| 136797   |
| 173570   |
| 165237   |
| ...      |
+----------+

sqlite> SELECT title shows WHERE id IN (SELECT show_id FROM stars WHERE person_id = (SELECT id from people WHERE name = "Steve Carrel"));
+----------------------+
|         title        |
+----------------------+
| The Dana Carvey Show |
| Over The Top         |
| Watching Ellie       |
| ...                  |
+----------------------+
```

```
sqlite> CREATE INDEX person_index ON stars (person_id);
sqlite> CREATE INDEX show_index ON stars (show_id);
sqlite> CREATE INDEX name_index ON people (name);
```

> The above `CREATE INDEX` will drastically increase subsequent queries.

## JOIN

```
sqlite> SELECT title FROM people JOIN stars ON people.id = stars.person.id JOIN shows ON stars.show_id = shows.id WHERE name = "Steve Carrel";
```

or

```
SELECT title FROM people
JOIN stars ON people.id = stars.person.id
JOIN shows ON stars.show_id = shows.id WHERE name = "Steve Carrel";
```

## Race Condition

`BEGIN TRANSACTION`
`COMMIT`
`ROLLBACK`

```
db.execute("BEGIN TRANSACTION")
rows = db.execute("SELECT likes FROM posts WHERE id = ?, id"):
likes = rows[0]["Likes"]
db.execute("UPDATE posts SET likes = > WHERE id = ?, likes + 1, id")
db.execute("COMMIT")
```
