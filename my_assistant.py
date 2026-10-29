# my_assistant.py
# Author: Tristan Riggs


class GymAssistant:
    def __init__(self, name, instructions, gym_tool):
        self.name = name
        self.instructions = instructions
        self.gym_tool = gym_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        text = user_message.lower()

        if any(word in text for word in ["cancel", "refund", "change"]):
            reply = "I'll pass your request to a staff member."

        elif "price" in text or "cost" in text:
            plan = self.gym_tool.find_plan(text)
            if plan is None:
                reply = "Which membership plan? Basic or premium?"
            else:
                price = self.gym_tool.get_price(plan)
                if price is None:
                    reply = "I couldn't find that price."
                else:
                    reply = f"The {plan} plan costs ${price} per month."

        elif "hello" in text or "hi" == text:
            reply = f"Hello! I'm {self.name}. Ask me about gym memberships."

        else:
            reply = "I'm not sure how to help with that. I can check membership prices."

        self.history.append({"role": "assistant", "content": reply})

        return reply
