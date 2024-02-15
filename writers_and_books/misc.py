from django.db import connection


def get_writer_and_books(writer_id) -> dict or list:
    raw_query = """
            SELECT
                w.id AS id,
                w.name AS writer_name,
                json_agg(json_build_object(
                    'id', b.id,
                    'title', b.title
                )) AS books
            FROM
                writers_and_books_writermodel w
            LEFT JOIN
                writers_and_books_bookmodel b ON w.id = b.author_id
            WHERE
                w.id = %s
            GROUP BY
                w.id, w.name
        """

    with connection.cursor() as cursor:
        cursor.execute(raw_query, [writer_id])
        row = cursor.fetchone()

    if row:
        writer_data = {
            'id': row[0],
            'name': row[1],
            'books': row[2]
        }
        return writer_data
    else:
        return []
