import psycopg2

def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="[username]}",
        password="[password]",
        port="5432")
    return conn

def initate_leaderboard():
    conn = connect()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS snakeLeaderboard (id text, score integer)')
    conn.commit()
    conn.close()

def add_score(id, score):
    conn = connect()
    cur = conn.cursor()
    cur.execute('INSERT INTO snakeLeaderboard (id, score) VALUES (%s, %s)', (id, score))
    conn.commit()
    conn.close()

def view_leaderboard():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM snakeLeaderboard LIMIT 5')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def check_rank(score):
    leaderboard = view_leaderboard()
    ## sort leaderboard by score which is returned as the second element in the tuple
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    #
    ## check if the score is higher than the lowest score in the leaderboard
    if score > sorted_leaderboard[-1][1]:
        print('--LEADERBOARD--')
        for i in range(len(sorted_leaderboard)):
            print(f'{i+1}. {sorted_leaderboard[i][0]}: {sorted_leaderboard[i][1]}')
        return True
    else:
        return False
    
def update_leaderboard(id, score):
    add_score(id, score)