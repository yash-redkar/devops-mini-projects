import os
import time

import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        port=os.environ.get("DB_PORT", "5432"),
        database=os.environ.get("DB_NAME", "notesdb"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres")
    )


def initialize_database():
    retries = 10

    while retries > 0:
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

            connection.commit()
            cursor.close()
            connection.close()

            print("Database initialized successfully")
            return

        except Exception as error:
            print(f"Waiting for database connection... {error}")
            retries -= 1
            time.sleep(3)

    raise Exception("Database connection failed after multiple retries")


@app.route("/api/health", methods=["GET"])
def health_check():
    try:
        connection = get_db_connection()
        connection.close()

        return jsonify({
            "status": "healthy",
            "service": "student-notes-api",
            "database": "connected"
        })

    except Exception:
        return jsonify({
            "status": "unhealthy",
            "service": "student-notes-api",
            "database": "disconnected"
        }), 500


@app.route("/api/notes", methods=["GET"])
def get_notes():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, content, created_at
        FROM notes
        ORDER BY id DESC;
        """
    )

    rows = cursor.fetchall()

    notes = []
    for row in rows:
        notes.append({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "created_at": str(row[3])
        })

    cursor.close()
    connection.close()

    return jsonify(notes)


@app.route("/api/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"message": "Title and content are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO notes (title, content)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (title, content)
    )

    note_id = cursor.fetchone()[0]
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Note created successfully",
        "id": note_id,
        "title": title,
        "content": content
    }), 201


@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM notes WHERE id = %s RETURNING id;",
        (note_id,)
    )

    deleted_note = cursor.fetchone()
    connection.commit()

    cursor.close()
    connection.close()

    if not deleted_note:
        return jsonify({"message": "Note not found"}), 404

    return jsonify({"message": "Note deleted successfully"})


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5000)
