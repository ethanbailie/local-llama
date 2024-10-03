from flask import Flask, render_template, jsonify
from threading import Thread
import datetime
from agents import *

app = Flask(__name__)

## test responses
conversation_history = []
initial_response = agent_maya('Now start a conversation with Carlos where you want to get to know him better.').strip()
previous_agent = 'maya'
conversation_history.append({
    'speaker': previous_agent,
    'message': initial_response,
    'timestamp': datetime.datetime.now().strftime('%I:%M %p'),
    'avatar': 'maya.png'
})
i = 0

responding_to = 'responding to the following response from'

while i < 5:
    i += 1
    if i == 1:
        response = agent_carlos(f'{responding_to} {previous_agent}: ' + initial_response, speaking_to=previous_agent).strip()
        previous_agent = 'carlos'
    elif previous_agent == 'maya':
        response = agent_carlos(f'{responding_to} {previous_agent}: ' + response, speaking_to=previous_agent).strip()
        previous_agent = 'carlos'
    else:
        response = agent_maya(f'{responding_to} {previous_agent}: ' + response, speaking_to=previous_agent).strip()
        previous_agent = 'maya'
    
    conversation_history.append({
        'speaker': previous_agent,
        'message': response,
        'timestamp': datetime.datetime.now().strftime('%I:%M %p'),
        'avatar': f'{previous_agent}.png'
    })

conversation = '\n'.join([f"{item['speaker']}: {item['message']}" for item in conversation_history])
print(conversation)

memory = agent_memory('maya', 'carlos', conversation)
print(memory)

@app.route('/')
def conversation():
    return render_template('conversation.html', conversation=conversation_history)

if __name__ == '__main__':
    app.run(debug=True)

# # Sample messages for Bot1 and Bot2
# bot1_messages = [
#     "Hello!",
#     "How are you?",
#     "What's up?",
#     "Did you see the game last night?"
# ]

# bot2_messages = [
#     "Hi there!",
#     "I'm good, thanks!",
#     "Not much, you?",
#     "Yes, it was great!"
# ]

# def generate_bot1_message():
#     return random.choice(bot1_messages)

# def generate_bot2_message():
#     return random.choice(bot2_messages)

# def bot1():
#     while True:
#         time.sleep(2)  # Bot1 sends a message every 2 seconds
#         message = generate_bot1_message()
#         chat_messages.append({'sender': 'Bot1', 'message': message})

# def bot2():
#     while True:
#         time.sleep(3)  # Bot2 sends a message every 3 seconds
#         message = generate_bot2_message()
#         chat_messages.append({'sender': 'Bot2', 'message': message})

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_messages')
# def get_messages():
#     return jsonify(chat_messages)

# if __name__ == '__main__':
#     # Start bot threads
#     t1 = Thread(target=bot1)
#     t2 = Thread(target=bot2)
#     t1.daemon = True
#     t2.daemon = True
#     t1.start()
#     t2.start()
#     app.run(debug=True)
