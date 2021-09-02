import sqlite3 as sql


def getCon():
    con = sql.connect('database.db')
    return con


def getMusicById(id):
    con = getCon()
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from music where id = ?", [id])
    return cur.fetchall()


def getMusic():
    con = getCon()
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from music")
    return cur.fetchall()


def getSingerList():
    con = getCon()
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select distinct main_singer from music")
    return cur.fetchall()


def createMusic(form):
    album = form['album']
    title = form['title']
    singer = form['singer']
    lyrics = form['lyrics']
    music = form['music']
    publisher = form['publisher']
    singer_2 = form['singer_2']
    custom_1 = form['custom_1']
    custom_2 = form['custom_2']
    year = form['year']

    con = getCon()
    cur = con.cursor()
    cur.execute(
        "insert into music (album, song_title, main_singer, lyrics, music, publisher, singer_2, custom_1 ,custom_2, "
        "year) values(?,?,?,?,?,?,?,?,?,?)",
        (album, title, singer, lyrics, music, publisher, singer_2, custom_1, custom_2, year))
    con.commit()


def updateMusic(form):
    id = form['id']
    album = form['album']
    title = form['title']
    singer = form['singer']
    lyrics = form['lyrics']
    music = form['music']
    publisher = form['publisher']
    singer_2 = form['singer_2']
    custom_1 = form['custom_1']
    custom_2 = form['custom_2']
    year = form['year']

    con = getCon()
    cur = con.cursor()
    cur.execute(
        "update music set album = ?, song_title = ?, main_singer = ?, lyrics = ?, music = ?, publisher = ?, "
        "singer_2 = ?, custom_1 = ?, custom_2 = ?, year = ? where id = ?",
        (album, title, singer, lyrics, music, publisher, singer_2, custom_1, custom_2, year, id))
    con.commit()


# admin function, not exposed to front-end
def clearDb():
    con = getCon()
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("delete from music where 1=1")
    con.commit()