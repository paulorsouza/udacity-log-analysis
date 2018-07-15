"""
This module is responsible to fetching data in db
"""


import psycopg2

def connect():
    """Returns a connection with news db."""
    return psycopg2.connect("dbname=news")

def get_top_articles(count):
    """Returns rank of articles."""
    sql = '''
    select count(b.id) as views, a.slug, a.title
    from articles a
    left join log b on b.path = '/article/'||a.slug
    and b.method = 'GET'
    and status = '200 OK'
    group by a.slug, a.title order by views desc limit %s;
    '''
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql, (str(count),))
    rank_list = cursor.fetchall()
    conn.close()
    return rank_list

print(get_top_articles(3))
