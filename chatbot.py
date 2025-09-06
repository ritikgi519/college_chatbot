import sqlite3

def get_from_db(query):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Sorry, I don't have info about that."

def chatbot_response(user_msg):
    user_msg = user_msg.lower()

    if "course" in user_msg:
        return get_from_db("SELECT info FROM college WHERE topic='courses'")
    elif "fee" in user_msg:
        return get_from_db("SELECT info FROM college WHERE topic='fees'")
    elif "admission" in user_msg:
        return get_from_db("SELECT info FROM college WHERE topic='admission'")
    elif "faculty" in user_msg:
        return get_from_db("SELECT info FROM college WHERE topic='faculty'")
    else:
        return "I can help with courses, fees, admissions, or faculty. Please ask specifically."
