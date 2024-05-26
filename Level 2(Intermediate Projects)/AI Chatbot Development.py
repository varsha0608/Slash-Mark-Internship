Imagine a friendly robot named Bard that you can chat with. This code brings Bard to life! Here's how it works:

->Starting Politely (greet function):

If you say "hi", "hello", or "hey", Bard greets you warmly and asks how you're doing.

->Understanding You (respond function):

Whatever you say, Bard converts it to lowercase for easier understanding (all lowercase letters are the same for Bard).

->Based on your message, Bard tries to find the best response:

If you ask "how are you", Bard replies with how it's doing and asks about you too.
If you ask "what is your name", Bard introduces itself as Bard.
If you ask "what can you do", Bard explains its ability to chat and answer some questions.
If you say something else, Bard admits it's still learning but happy to chat and asks what you'd like to talk about.

->Keeping the Conversation Going (main loop):

Bard keeps asking you things ("You: ") until you say "quit".
It first checks if you greeted Bard, and if so, it uses the greet function to respond.
If you didn't greet Bard, it uses the respond function to understand your message and provide a suitable response.




def greet(user_input):
  """Greets the user based on input"""
  if user_input.lower() in ["hi", "hello", "hey"]:
    return "Hello! How can I help you today?"
  else:
    return ""

def respond(user_input):
  """Provides a response based on user input"""
  user_input = user_input.lower()
  if user_input in ["how are you", "how's it going"]:
    return "I'm doing well, thanks for asking! "
  elif user_input in ["what is your name", "who are you"]:
    return "I'm a chatbot. You can call me Bard. "
  elif user_input in ["what can you do"]:
    return "I can have simple conversations and answer basic questions. How about the weather today?"
  elif user_input in ["what's the weather like"]:
    return "Unfortunately, I can't access real-time weather information yet. But I can tell you some fun facts about different weather phenomena!"
  elif user_input in ["tell me a joke"]:
    return "Why did the scarecrow win an award? Because he was outstanding in his field!"
  elif user_input in ["thanks", "thank you"]:
    return "You're welcome! Glad I could help."
  elif user_input in ["what time is it"]:
    # You can integrate a library here to get the current time
    return "I can't access the current time yet, but I can tell you some interesting facts about timekeeping!"
  elif user_input in ["do you have any hobbies"]:
    return "As a large language model, I don't have hobbies in the traditional sense. However, I enjoy processing information and learning new things!"
  elif user_input in ["tell me about yourself"]:
    return "I'm still under development, but I'm learning to communicate and answer questions. I'm excited to see what I can do in the future!"
  elif user_input in ["what are you interested in"]:
    return "I'm interested in learning about the world and how language can be used to communicate and create. What are you interested in?"
  elif user_input in ["anything interesting happening today"]:
    # You can integrate a news API here to get current news
    return "Unfortunately, I can't access real-time news yet. But I can tell you some historical events that happened on this day!"
  # Daily life interactions
  elif user_input in ["how was your day"]:
    return "As a language model, I don't have days in the same way humans do. But I'm always learning and growing from new interactions!"
  elif user_input in ["what are you working on"]:
    return "I'm constantly being improved to better understand and respond to your questions. What would you like to see me learn about?"
  elif user_input in ["recommend a movie"]:
    return "Unfortunately, I can't access movie databases yet. However, I can tell you some interesting facts about the history of cinema!"
  elif user_input in ["what's for dinner tonight"]:
    return "I can't recommend meals, but I can search for recipes if you tell me what ingredients you have!"
  elif user_input in ["need help planning my weekend"]:
    return "I can't access event calendars yet, but I can search for interesting things to do in your area if you tell me your location!"
  elif user_input in ["feeling overwhelmed today"]:
    return "That sounds tough. Here are some tips for relaxation techniques: [insert relaxation techniques link here]"
  elif user_input in ["need help with a task"]:
    return "I can't physically complete tasks, but I can help you break down the steps or search for instructions online!"
  else:
    return "I'm still learning, but I'm happy to chat! What would you like to talk about?"

# Start the conversation
while True:
  # Get user input
  user_input = input("You: ")

  # Check for greetings first
  response = greet(user_input)

  # If no greeting, provide a general response
  if not response:
    response = respond(user_input)

  # Print chatbot response
  print("Bard:", response)

  # Exit if user types 'quit'
  if user_input == "quit":
    break
