import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "quiz_results.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    with get_connection() as connection:

        connection.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                total_questions INTEGER NOT NULL,
                percentage REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_result(player_name, score, total, percentage):

    with get_connection() as connection:

        connection.execute("""
            INSERT INTO results
            (player_name, score, total_questions, percentage)
            VALUES (?, ?, ?, ?)
        """, (
            player_name,
            score,
            total,
            percentage
        ))


def get_recent_results(limit=10):

    with get_connection() as connection:

        cursor = connection.execute("""
            SELECT
                player_name AS Name,
                score AS Score,
                total_questions AS Total,
                percentage AS Percentage,
                created_at AS Date
            FROM results
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        columns = [
            description[0]
            for description in cursor.description
        ]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
