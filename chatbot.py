# def get_chat_response(user_input):
#     user_input = user_input.lower()

#     if "hello" in user_input or "hi" in user_input:
#         return "Hello there! 👋 How can I help you today?"
#     elif "admission" in user_input:
#         return "You can find all admission details on the university’s official portal."
#     elif "course" in user_input:
#         return "We offer multiple programs. Could you tell me which department you’re interested in?"
#     elif "thanks" in user_input:
#         return "You're welcome! 😊"
#     else:
#         return "I’m still learning 🤖. Please try asking in a different way."

def get_chat_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you?"
    else:
        return "I'm still learning. Could you rephrase that?"
