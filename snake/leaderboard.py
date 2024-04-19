import psycopg2

def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        port="5432")
    return conn

def initate_leaderboard():
    conn = connect()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS snakeLeaderboard (Player text, Score integer)')
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
    cur.execute('SELECT * FROM snakeLeaderboard ORDER BY score DESC LIMIT 5')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def check_rank(score):
    leaderboard = view_leaderboard()
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)

    # Check if the leaderboard is empty
    if not sorted_leaderboard:
        # If it's empty, add the first score and return True
        update_leaderboard('p1', score)
        print('--LEADERBOARD--')
        for i in range(len(sorted_leaderboard)):
            print(f'{i+1}. {sorted_leaderboard[i][0]}: {sorted_leaderboard[i][1]}')
        return True

    # If it's not empty, check if the score is higher than the lowest score in the leaderboard
    if score > sorted_leaderboard[-1][1]:
        print('--LEADERBOARD--')
        for i in range(len(sorted_leaderboard)):
            print(f'{i+1}. {sorted_leaderboard[i][0]}: {sorted_leaderboard[i][1]}')
        return True

    # Return False if the score is not higher than the lowest score
    return False
    
def update_leaderboard(id, score):
    add_score(id, score)