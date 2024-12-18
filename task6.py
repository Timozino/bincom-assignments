import psycopg2
from collections import Counter


### Save colors and their frequencies in PostgreSQL

def save_colors_to_db(colors):
    # Count the frequency of each color
    count = Counter(colors)

    
    DB_NAME = "colors_db"
    DB_USER = "postgres"
    DB_PASSWORD = ""  
    DB_HOST = "localhost"         
    DB_PORT = "5432"              

    try:
        
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Insert color data into the database
        for color, freq in count.items():
            cursor.execute(
                "INSERT INTO colors (color, frequency) VALUES (%s, %s) ON CONFLICT (color) DO UPDATE SET frequency = colors.frequency + EXCLUDED.frequency",
                (color, freq)
            )

        # Commit changes and close the connection
        conn.commit()
        print("Data successfully saved to PostgreSQL database.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")


colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
save_colors_to_db(colors)
