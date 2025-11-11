import psycopg2

def get_connection():
  return psycopg2.connect(
    host="localhost",
    database="exam_5thmonth",
    user="johnibek",
    password="123john",
    port=5433
  )

def execute_query(query, params=None, fetch=False, many=False):
  conn = get_connection()
  cur = conn.cursor()
  try:
    if params:
      if many:
        cur.executemany(query, params)
      else:
        cur.execute(query, params)
    else:
      cur.execute(query)
    
    if fetch:
      result = cur.fetchall()
    else:
      result = None

    conn.commit()
    return result
  except Exception as e:
    print("Database error:", e)
    conn.rollback()
  finally:
    cur.close()
    conn.close()