#!usr/bin/env python
#coding=utf-8

#from transitions.extensions import GraphMachine as Machine
from transitions import Machine

class TocMachine(Machine):
    def __init__(self, **machine_configs):
        self.machine = Machine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'go to state3'

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
#        self.go_back(update)

    def on_exit_state1(self, update):
        update.message.reply_text("???")

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        update.message.reply_text("e0e0e")

    def on_enter_state3(self, update):
        update.message.reply_text("I'm entering state3")

    def on_exit_state3(self, update):
        update.message.reply_text("WLWLW")
        self.go_back(update)



    def is_going_to_ask(self, update):
        text = update.message.text
        return True

    def is_going_to_no(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_askwhy(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def on_enter_no(self, update):
        update.message.reply_text("NO? Are you SURE ?????? ")
        self.go_back(update)

    def on_exit_no(self, update):
        update.message.reply_text("Allakhuaguak！Fuck you jesus")

    def on_enter_ask(self, update):
        update.message.reply_text("Allakhuaguak！想來一場轟轟烈烈的大爆炸嗎？\n(a.)想\n(b.)不想")

    def on_exit_ask(self, update):
        pass

    def on_enter_askwhy(self, update):
        update.message.reply_text("為什麼想要爆炸呢？\n(a.)就只是想炸\n(b.)心情不好\n(c.)亦轉身os炸開")

    def on_exit_askwhy(self, update):
        pass
        
