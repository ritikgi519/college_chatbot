# chatbot.py

def chatbot_response(user_msg):
    user_msg = user_msg.lower()
    
    # Hardcoded responses with multiple lines
    responses = {
        "course": [
            "We offer B.Tech, B.Sc, MBA, and MCA programs.",
            "Each course has specialized streams and electives."
        ],
        "fee": [
            "The average fee is ₹1,00,000 per year depending on the course.",
            "Scholarships are available for meritorious students."
        ],
        "admission": [
            "Admissions start in June every year.",
            "Process includes entrance exam + interview."
        ],
        "faculty": [
            "We have highly qualified faculty from IITs and NITs.",
            "Faculty regularly publish research papers and guide projects."
        ]
    }

    # Match user message with keywords
    for key in responses:
        if key in user_msg:
            # Join multiple lines into a single string
            return "\n".join(responses[key])

    return "I can help with courses, fees, admissions, or faculty. Please ask specifically."
