import sqlite3


conn = sqlite3.connect(Cell("B1").value + '.db')
c = conn.cursor()

c.execute('''CREATE TABLE ''' + Cell("B1").value +
          '''(ValueSetName text,Code integer,Code System text)''')

ValueSets = []

for cell in Cell("A3").vertical_range:
    ValueSets.append(tuple(cell.horizontal[:3]))

c.executemany('INSERT INTO ValueSets VALUES (?,?,?)',ValueSets)
conn.commit()
conn.close()
