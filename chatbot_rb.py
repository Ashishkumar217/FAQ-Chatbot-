
import re
from datetime import datetime
import ipywidgets as widgets
from IPython.display import display
from nltk.chat.util import Chat,reflections

#Chatbot Pairs for response.
pairs = [

    [r"hi|hello|hey|helo|hlo",
     ["Hello! How are you Buddy",
      "How can I help you today?"]],

     [r"my name is (.*)",
     ["Nice to meet you ,%1!"]],

    [r".*(what is ai|artificial intelligence|ai)",
     ["AI (Artificial Intelligence) is the ability of a computer or machine to perform tasks that normally require human intelligence, such as learning, reasoning, problem-solving, and understanding language."]],

    [r".*(what is ml|machine learning|ml)",
     ["ML (Machine Learning) is a branch of AI that enables computers to learn from data and improve their performance without being explicitly programmed."]],

    [r".*(what is deep learning|deep learning)",
     ["Deep Learning (DL) is a subset of Machine Learning that uses artificial neural networks with many layers to learn patterns from large amounts of data and make predictions or decisions."]],

    [r"(.*)",
     ["I can't understand that. Could you please rephrase it?"]]

]

#Widgets

output_area = widgets.Output( layout={ 'border': '1px solid gray', 'height': '350px', 'overflow_y':'auto' } )
text_input = widgets.Text( placeholder = "Type your message here..." )
send_button = widgets.Button( description ="send", button_style = "primary" )
input_box = widgets.HBox([text_input,send_button])

class RuleBasedChatbot:
    def __init__(self, pairs, reflections):
      # Initialize the NLTK Chat instance
      self.chat = Chat(pairs, reflections) # Corrected 'chat' to 'Chat'
      self.user_name = None

    def respond(self, user_input):
      # Store user name if provided
      name_match = re.match(r"my name is (.*)", user_input.lower())
      if name_match:
        self.user_name = name_match.group(1).title()
        return f"Nice to meet you, {self.user_name}!"

      # Personalized greeting
      if user_input.lower() in ["hi","hello","hey","helo"] and self.user_name:
        return f"Hello Again {self.user_name}! How can I help you today?"

      # Get response from the NLTK Chat instance
      response = self.chat.respond(user_input.lower())

      if response:
         return response
      return "Sorry, I can't understand that. Please rephrase."

# creating chatbot instance
chatbot = RuleBasedChatbot(pairs, reflections)

# Widgets
output_area = widgets.Output(
    layout={
      'border': '1px solid gray',
      'height': '350px',
      'overflow_y':'auto'
    }
)
text_input = widgets.Text(
    placeholder = "Type your message here..."
)
send_button = widgets.Button(
    description ="send",
    button_style = "primary"
)
input_box = widgets.HBox([text_input,send_button])

# Message Handler.
def process_message(_):
  user_message = text_input.value.strip()
  if not user_message:
    return
  current_time = datetime.now().strftime("%H:%M:%S")
  with output_area:
    print(f"[{current_time}] You {user_message}")

    if user_message.lower() in ["bye","quit","exsit"]:
      print(f"[{current_time}] Bot: Goodbye! Have a Nice day!")
      text_input.disabled = True
      send_button.disabled = True

    else:
      bot_response = chatbot.respond(user_message)
      print(f"[{current_time}] Bot:{bot_response}")

      print("-" * 50)
  text_input.value=""

#Event
send_button.on_click(process_message)
text_input.on_submit(process_message)

# Display Interface
display(output_area)
display(input_box)
with output_area:

 print("🤖 Bot: Hello I am your Rulebased Chatbot, Type your Message and press Enetr!")
 print("-"*50)
