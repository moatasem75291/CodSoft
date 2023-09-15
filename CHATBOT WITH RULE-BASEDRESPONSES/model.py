class ChatbotModel:
    def __init__(self):
        self.responses = {
            "hello": "Hello! How can I help you today?",
            "how are you": "I'm just a chatbot, but I'm here to assist you!",
            "goodbye": "Goodbye! Feel free to return if you have more questions.",
            "what's your name": "I'm Nemo, your chatbot assistant.",
            "tell me a joke": "Why did the chicken cross the road? To get to the other side!",
            "how do i make a cup of coffee": "To make coffee, you'll need ground coffee beans, hot water, and a coffee maker. Brew the coffee according to your preference, and enjoy!",
            "recommend a book to read": "I recommend 'To Kill a Mockingbird' by Harper Lee. It's a classic novel with a powerful message.",
            "how do i learn programming": "Learning programming involves studying programming languages, practicing coding, and solving problems. There are many online resources and courses available to help you get started.",
        }
        self.default_response = "I'm not sure how to respond to that."

    def query(self, user_input):
        user_input = user_input.lower()
        response = self.responses.get(user_input, self.default_response)
        return response
