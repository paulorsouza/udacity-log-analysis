"""This module is responsible to fetching data in db"""


import psycopg2

def connect():
    """Returns a connection with news db."""
    return psycopg2.connect("dbname=news")

def execute_query(sql, params):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchall()
    conn.close()
    return result

def list_top_articles(count):
    """Returns rank of articles."""
    sql = '''
    select count(b.id) as views, a.slug, a.title
    from articles a
    left join log b on b.path = '/article/'||a.slug
    and b.method = 'GET'
    and status = '200 OK'
    group by a.slug, a.title 
    order by views desc limit %s;
    '''
    return execute_query(sql,  (str(count),))

def list_authors_views():
    "Returns all views by author"
    sql = '''
    select count(c.id) as views, c.name
    from articles a
    join log b on b.path = '/article/'||a.slug
    join authors c on c.id = a.author
    group by c.name order by views desc 
    '''
    return execute_query(sql, ())

def list_critical_days():
    "Return the days that log more than 1% requests 404"
    sql = '''
    select error.date, error.num as error_count, success.num as success_count
    from (select time::date as date, count(1) as num from log where status = '404 NOT FOUND' group by date) as error, 
         (select time::date as date, count(1) as num from log where status = '200 OK' group by date) as success 
    where error.date = success.date and ((error.num * 100)/(success.num + error.num)) >= 1   
    '''
    return execute_query(sql, ())
