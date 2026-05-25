import pymysql
from congiguration import config


connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:
        cursor.execute("USE world")

        cursor.execute("""
        SELECT Code, Name
        FROM country
        ORDER BY Name
        """)

        countries = cursor.fetchall()

        print("list of countries:")
        for i, country in enumerate(countries, start=1):
            print(f"{i}. {country[0]}")

        choice = input("enter the number or name of the chosen country >>>").strip()

        selected_country = None

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index <= len(countries):
                selected_country = countries[index]
        else:
            for country in countries:
                if country[1].lower() == choice.lower():
                    selected_country = country
                    break

        if not selected_country:
            print("404: country not found.")
        else:
            country_code = selected_country[0]

            cursor.execute("""
                SELECT Name, Population
                FROM city
                WHERE CountryCode = %s
                ORDER bY Population DESC
            """, (country_code,))

            cities = cursor.fetchall()

            if cities:
                for i, city in enumerate(cities, start=1):
                    print(f"{i}. {city[0]} — population: {city[1]}")
            else:
                print("cities not found")



finally:
    connection.close()

