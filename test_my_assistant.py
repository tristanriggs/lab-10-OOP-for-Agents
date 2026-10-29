# test_my_assistant.py
# Author: Tristan Riggs

from my_assistant import GymAssistant
from my_tool import GymInfo


def make_bot():
    tool = GymInfo({"basic": 20, "premium": 40})
    return GymAssistant("Max", "Be friendly.", tool)


def test_membership_price():
    bot = make_bot()
    assert "$20" in bot.respond("What is the basic price?")


def test_unknown_plan():
    bot = make_bot()
    assert "Which membership" in bot.respond("What is the price?")


def test_human_handoff():
    bot = make_bot()
    assert "staff member" in bot.respond("Cancel my membership")


def test_unknown_question():
    bot = make_bot()
    assert "not sure" in bot.respond("What is the weather?")


def test_history():
    bot = make_bot()
    bot.respond("hello")
    bot.respond("What is the premium price?")
    assert len(bot.history) == 4
