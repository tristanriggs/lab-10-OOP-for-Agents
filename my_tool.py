# my_tool.py
# Author: Tristan Riggs


class GymInfo:
    def __init__(self, memberships):
        self.memberships = memberships

    def find_plan(self, text):
        for plan in self.memberships:
            if plan in text.lower():
                return plan
        return None

    def get_price(self, plan):
        return self.memberships.get(plan)
