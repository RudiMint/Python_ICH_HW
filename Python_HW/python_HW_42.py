import pymysql
from pymysql.cursors import DictCursor

from congiguration import config_edit


connection = pymysql.connect(**config_edit)

db_name = "notes_app_121225ptm_anastasiia_shevchenko"

try:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"db '{db_name}' successfully created or already exists")

        cursor.execute(f"USE {db_name}")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(250) NOT NULL,
        content TEXT NOT NULL
        )
        """)
        print("table 'notes' created")

        cursor.execute("""
        INSERT INTO notes (title, content)
        VALUES (%s, %s)
        """, (
            "Classic Pancakes",
            "In a bowl, whisk together the flour, baking powder, sugar, and salt.\n"
            "In another bowl, whisk the milk, egg, melted butter, and vanilla.\n"
            "Pour the wet ingredients into the dry ingredients and stir gently"
            " until just combined. A few lumps are okay.\n"
            "Heat a lightly buttered skillet or pan over medium heat.\n"
            "Pour about 1/4 cup batter for each pancake.\n"
            "Cook until bubbles form on the surface, "
            "then flip and cook another 1–2 minutes until golden brown.\n"
            "Serve warm with syrup, butter, fruit, or whipped cream.")
        )

    connection.commit()

    with connection.cursor(DictCursor) as cursor:
        cursor.execute(f"USE {db_name}")
        cursor.execute("SELECT * FROM notes")

        notes = cursor.fetchall()

        print("notes:")
        for note in notes:
            print(note)

except pymysql.MySQLError as e:
    print(f"error with db: {e}")

finally:
    connection.close()

