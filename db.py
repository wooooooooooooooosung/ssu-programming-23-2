import sqlite3 as db
import os.path as path

'''
테이블 리스트
type list
'''
tableList = [ 'user', 'ground', 'sport', 'post', 'postReservation' ]

'''
테이블 생성 쿼리
type dictionary
'''
tableCreateQuery = {
    'user' : '''CREATE TABLE IF NOT EXISTS User(
	uID INTEGER PRIMARY KEY AUTOINCREMENT, 
	userID TEXT,
    userPW TEXT, 
	userName TEXT, 
    userBirth TEXT, 
    userPhone TEXT, 
	userSex TEXT, 
    userAddress TEXT)''', 

    'ground' : '''CREATE TABLE IF NOT EXISTS Ground(
    gID INTEGER PRIMARY KEY AUTOINCREMENT, 
    groundName TEXT, 
    groundAddress TEXT, 
    groundPhone TEXT, 
    sID INTEGER)''', 

    'sport':'''CREATE TABLE IF NOT EXISTS Sport(
    sID INTEGER PRIMARY KEY AUTOINCREMENT, 
    sportName TEXT)''', 

    'post': '''CREATE TABLE IF NOT EXISTS Post(
    pID INTEGER PRIMARY KEY AUTOINCREMENT, 
    postTitle TEXT, 
    postSubTitle TEXT, 
    postDesc TEXT, 
    postTag TEXT, 
    postView INTEGER, 
    postDate DATETIME, 
    postEndDate DATETIME, 
    postDeadline INTEGER, 
    sID INTEGER, 
    uID INTEGER
    )''',

    'postReservation': '''CREATE TABLE IF NOT EXISTS PostReservation(
    pRID INTEGER PRIMARY KEY AUTOINCREMENT,
    isPostCheck INTEGER,
    isUserCheck INTEGER,
    playScore INTEGER, 
    playDesc TEXT,
    pID INTEGER,
    uID INTEGER
    )'''
}

'''
테이블 데이터 임포트 쿼리
type dictionary
'''
tableImportQuery = {
    'user' : '''INSERT INTO User(uID, userID, userPW, userName, userBirth, userPhone, userSex, userAddress) 
	VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', 
    'ground' : '''INSERT INTO Ground(gID, groundName, groundAddress, groundPhone, sID) 
	VALUES(?, ?, ?, ?, ?)''', 
    'sport' : '''INSERT INTO Sport(sID, sportName) 
	VALUES(?, ?)''', 
    'post' : '''INSERT INTO Post(pID, postTitle, postSubTitle, postDesc, postTag, postView, postDate, postEndDate, postDeadline, sID, uID) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
    'postReservation': '''INSERT INTO PostReservation(pRID, isPostCheck, isUserCheck, playScore, playDesc, pID, uID)
    VALUES(?, ?, ?, ?, ?, ?, ?)
    '''
}


con = None
cur = None



'''
# 테이블 임포트
내용 : csv 포맷의 데이터를 읽어서 해당 테이블에 넣음
작성 : 2023-10-19
변경 : 2023-10-19
'''
def importData(cur, query, path):
    data = open(path, 'r', encoding = 'utf-8').readlines()
    for _ in data :
        cur.execute(query, _.split("\t"))

	
	
'''
# db 초기 설정
내용 : sqlite 파일 연동(db 파일 없을 경우 생성)
작성 : 2023-10-19
변경 : 2023-10-19
'''
def init():
    global con, cur

    flag = path.isfile('./db/잡포츠.db')
    con = db.connect('./db/잡포츠.db', check_same_thread=False)
    cur = con.cursor()
    
    # DB 첫 생성이면 기본 데이터 insert
    if flag == False :
        for _ in tableList :
            cur.execute(tableCreateQuery[str(_)])
            importData(cur, tableImportQuery[str(_)], './db/' + str(_) + '.txt')
            con.commit()
            
        
	
	
'''
# 쿼리문 실행
파라미터 : query sqlite3 query
내용 : return 값이 있는 쿼리
작성 : 2023-10-19
변경 : 2023-10-19
'''
def executeQuery(query) :
    return cur.execute(query).fetchall()
	
	
	
'''
# 쿼리문 실행
파라미터 : query sqlite3 query
내용 : return 값이 없는 쿼리
작성 : 2023-10-19
변경 : 2023-10-19
'''
def executeUpdate(query) :
    cur.execute(query)
    con.commit()


'''
# 쿼리문 실행
파라미터 : query sqlite3 query
파라미터 : param list 형태의 파라미터
내용 : return 값이 없는 쿼리
작성 : 2023-10-19
변경 : 2023-10-19
'''
def executeUpdate(query, param):
   cur.execute(query, param)
   con.commit()


def executeUpdateSingle(query) :
    cur.execute(query)
    con.commit()
