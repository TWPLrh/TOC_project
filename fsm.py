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
        self.go_back(update)

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

    def is_going_to_no1(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_no2(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_no3(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_askwhy(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_notrasher(self, update): #可能要再加
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_askdicision(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_askpressure(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_OS(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def on_enter_ask(self, update):
        update.message.reply_text("Allakhuaguak！想來一場轟轟烈烈的大爆炸嗎？\n(a.)想\n(b.)不想")

    def on_exit_ask(self, update):
        pass

    def on_enter_no1(self, update):
        update.message.reply_text("什麼？你說不想？")

    def on_exit_no1(self, update):
        pass

    def on_enter_no2(self, update):
        update.message.reply_text("你再說一次不想試試看阿！")

    def on_exit_no2(self, update):
        pass

    def on_enter_no3(self, update):
        update.message.reply_text("給你最後一次機會 想或不想？")

    def on_exit_no3(self, update):
        pass

    def on_enter_askwhy(self, update):
        update.message.reply_text("為什麼想要爆炸呢？\n(a.)就只是想炸\n(b.)心情不好\n(c.)亦轉身os炸開")

    def on_exit_askwhy(self, update):
        pass

    def on_enter_notrasher(self, update):
        update.message.reply_text("抱歉，我們不提供庸人資源。")

    def on_exit_notrasher(self, update):
        pass

    def on_enter_askdicision(self, update):
        update.message.reply_text("你擁有成為聖戰士的決心嗎？")

    def on_exit_askdicision(self, update):
        pass

    def on_enter_askpressure(self, update):
        update.message.reply_text("真主最擅長治癒病痛了！壓力大嗎？")

    def on_exit_askpreesure(self, update):
        pass

    def on_enter_ososos(self, update):
        update.message.reply_text("這種真主真的沒辦法！但你想炸掉OS老師的腦袋嗎？")

    def on_exit_ososos(self, update):
        pass
