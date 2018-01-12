#!usr/bin/env python
#coding=utf-8

#for final update

#from transitions.extensions import GraphMachine as Machine
from transitions import Machine
from google import search # Easy to GoogleSearch
import random
import time, _thread


url_list = []
lock = False

def my_timer(self, update):
    global lock
    lock = True
    time.sleep(15)
    self.go_back(update)


Correct = 0
counter = 0

class TocMachine(Machine):
    def __init__(self, **machine_configs):
        self.machine = Machine(
            model = self,
            **machine_configs
        )
    
    def is_going_to_no1(self, update):
        text = update.message.text
        return text.lower() == 'b' or text == '不想' or text == '否'

    def is_going_to_no2(self, update):
        text = update.message.text
        return ( text.lower() == 'b' or text == '不想' or text == '否')

    def is_going_to_no3(self, update):
        text = update.message.text
        return ( text.lower() == 'b' or text == '不想' or text == '否')

    def is_going_to_askwhy(self, update):
        text = update.message.text
        return ( text.lower() == 'a' or text == '想' or text == '是')

    def is_going_to_notrasher(self, update):
        text = update.message.text
        return ( text.lower() == 'b' or text == '不想' or text == '否' )

    def is_going_to_askdicision(self, update):
        text = update.message.text
        return ( text.lower() == 'a' or text == '就只是想炸')

    def is_going_to_askmission(self, update):
        text = update.message.text 
        return ( text.lower () == 'a' or text == '是' or text == '知' or text == '有' or text == '知道' or text == '瞭解' or text == '了解')

    def is_going_to_tellmission(self, update):
        text = update.message.text
        return ( text.lower () == 'b' or text == '否')

    def is_going_to_quiz(self, update):
        text = update.message.text
        return ( text.lower () == 'a' or text == '是' or text == '想')

    def is_going_to_practice(self, update):
        text = update.message.text
        return (text == '我想再複習一次教義')

    def is_going_to_practicemore(self, update):
        text = update.message.text
        return text == '我想更瞭解教義'

    def is_going_to_quizstart(self, update):
        text = update.message.text
        return text != '我想更瞭解教義'

    def is_going_to_askpressure(self, update):
        text = update.message.text
        return (text.lower() == 'b' or text == '心情不好')

    def is_going_to_OS(self, update):
        text = update.message.text
        return (text.lower() == 'c' or text == '一轉身OS爆開')

    def is_going_to_tips(self, update):
        text = update.message.text
        return (text.lower() == 'a' or text == "是" or text == "大")

    def is_going_to_tip1(self, update):
        text = update.message.text
        return (text.lower() == 'a' or text == '音樂')

    def is_going_to_tip2(self, update):
        text = update.message.text
        return (text.lower() == 'b' or text == '動物')

    def is_going_to_tip3(self, update):
        text = update.message.text
        return (text.lower() == 'c' or text == '地獄梗')

    def is_going_to_another(self, update):
        text = update.message.text
        return ( text.lower() == 'd' or text == '不行' or text == '否' or text == '沒' or text == '不' or text == '其他')

    def is_going_to_retarded(self, update):
        text = update.message.text
        return ( text.lower() == 'b' or text == '不' or text == '不大' or text == '否')

    def is_going_to_keepAddress(self, update):
        text = update.message.text
        return ( text.lower() == 'a' or text == '想' )

    def is_going_to_askwhatyoudo(self, update):
        text = update.message.text
        return ( text.lower() == 'b' or text == '不想' )

    def is_going_to_guao(self, update):
        return True
#        text = update.message.text
#        return (text == '滿意' or text == '是' or text == '可以' or text.lower() == 'a')

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
        update.message.reply_text("為什麼想要爆炸呢？\n(a.)就只是想炸\n(b.)心情不好\n(c.)一轉身OS爆開")

    def on_exit_askwhy(self, update):
        pass

    def on_enter_askmission(self, update):
        update.message.reply_text("你知道聖戰士的職責嗎？")
    
    def on_exit_askmission(self, update):
        pass
    
    def on_enter_tellmission(self, update):
        update.message.reply_text("以下向你說明：")
        update.message.reply_text("我們遵從一切可蘭的教導，若遇到難以抉擇的問題，它能指引我們前往正確的道路")
        update.message.reply_text("穆罕默德是我們唯一的先知，但我們並不崇拜偶像")
        update.message.reply_text("真主創造了七重天，你在至仁主的造物中，看不出一點參差")
        update.message.reply_text("至仁主引領我們正確者的路，不是受譴怒者的路，亦非迷誤者的路")
        update.message.reply_text("可蘭並沒有教導我們暴力，受到壓迫下的我們只能依靠暴力訴諸信仰")
        update.message.reply_text("暴力雖然不是唯一的解決方式，但它是最簡單且最深植人心的")
        update.message.reply_text("你現在瞭解了聖戰士大略的職責，請問你還想成為聖戰士嗎？")

    def on_exit_tellmission(self, update):
        pass

    def on_enter_notrasher(self, update):
        global lock
        lock = False
        update.message.reply_text("抱歉，我們不提供庸人資源。")
        if(lock == False):
            _thread.start_new_thread(my_timer, (self, update))

    def on_exit_notrasher(self, update):
        pass

    def on_enter_askdicision(self, update):
        update.message.reply_text("你是否擁有成為聖戰士的決心嗎？")

    def on_exit_askdicision(self, update):
        pass

    def on_enter_askmission(self, update):
        update.message.reply_text("你瞭解聖戰士的職責嗎？")

    def on_exit_askmisson(self, update):
        pass

    def on_enter_askpressure(self, update):
        update.message.reply_text("真主最擅長治癒病痛了！壓力大嗎？")

    def on_exit_askpreesure(self, update):
        pass

    def on_enter_retarded(self, update):
        update.message.reply_text("你腦袋有問題嗎？")

    def on_exit_retarded(self, update):
        pass

    def on_enter_askwhatyoudo(self, update):
        update.message.reply_text("那你來幹嘛的？")

    def on_exit_askwhatyoudo(self, update):
        pass

    def on_enter_ososos(self, update):
        update.message.reply_text("這種真主真的沒辦法！但你想炸掉OS老師的腦袋嗎？\n(a.)想\n(b.)不想")

    def on_exit_ososos(self, update):
        pass

    def on_enter_tips(self, update):
        update.message.reply_text("推薦你幾種紓壓方式，想看哪個？\n(a.)音樂\n(b.)動物\n(c.)地獄梗\n(d.)其他")

    def on_exit_tips(self, update):
        pass

    def on_enter_tip1(self, update): ##wait
        update.message.reply_text("https://www.youtube.com/watch?v=C14oQ3zSTnA")
        update.message.reply_text("https://www.youtube.com/watch?v=o7iL2KzDh38")
        update.message.reply_text("https://www.youtube.com/watch?v=kqCdbl0ic9k")
        update.message.reply_text("這幾首歌可以讓你紓壓嗎？")        

    def on_exit_tip1(self, update):
        pass

    def on_enter_tip2(self, update):
        update.message.reply_text("準備圖檔中，請稍等 ..")
        update.message.reply_document(open("./img/001.gif", 'rb'), timeout = 20)
        update.message.reply_document(open("./img/002.gif", 'rb'), timeout = 20)
        update.message.reply_document(open("./img/003.gif", 'rb'), timeout = 20)
        update.message.reply_text("這些貓咪可以讓你紓壓嗎？")
        
    def on_exit_tip2(self, update):
        pass

    def on_enter_tip3(self, update):
        update.message.reply_text("準備圖檔中，請稍等 ..")
        update.message.reply_photo(open("./img/001.jpg", 'rb'), timeout = 20)
        update.message.reply_photo(open("./img/002.PNG", 'rb'), timeout = 20)
        update.message.reply_photo(open("./img/003.JPG", 'rb'), timeout = 20)
        update.message.reply_photo(open("./img/004.JPG", 'rb'), timeout = 20)       
        update.message.reply_text("這些梗圖可以讓你紓壓嗎？")          

    def on_exit_tip3(self, update):
        pass

    def on_enter_another(self, update):
        update.message.reply_text("那你需要什麼協助？我可以幫你搜尋")

    def on_exit_another(self, update):
        pass

    def on_enter_guao(self, update):
        update.message.reply_text("干我屁事？想炸東西再來找我")
        update.message.reply_text("掰")
        self.go_back(update)

    def on_exit_guao(self, update):
        global url_list
        del url_list[:]

    def on_enter_keepAddress(self, update):
        update.message.reply_text("我真的替你生氣，我這邊直接開炸，請問詳細資料是？")

    def on_exit_keepAddress(self, update):
        pass
    
    def on_enter_BePatient(self, update):
        global lock
        lock = False
        update.message.reply_text("請耐心等待，稍後完成任務會再提醒您\n如果不想被波及的話，建議您先暫時不要去上課！")
        if(lock == False):
            _thread.start_new_thread(my_timer, (self, update))

    def on_exit_BePatient(self, update):
        pass

    def on_enter_user(self, update):
        update.message.reply_text("已重置對話\n想看提示輸入 'note',\n想跳入 search 功能請輸入 'search'\n想進入主要功能請輸入 'main'")

    def on_exit_user(self, update):
        pass
#        update.message.reply_text("通常請照著提示回應")

    def on_enter_quiz(self, update):
        update.message.reply_text("有心想成為聖戰士很好，現在先做個小測驗，請回答a,b...")
        update.message.reply_text("題目只有10題，合格為正確7題，若想再複習一次，請輸入\n'我想再複習一次教義'")
        update.message.reply_text("準備好考試再和我說一聲！")

    def on_exit_quiz(self, update):
        pass

    def on_enter_practice(self, update):
        update.message.reply_text("以下再次向你說明：")
        update.message.reply_text("我們遵從一切可蘭的教導，若遇到難以抉擇的問題，它能指引我們前往正確的道路")
        update.message.reply_text("穆罕默德是我們唯一的先知，但我們並不崇拜偶像")
        update.message.reply_text("真主創造了七重天，你在至仁主的造物中，看不出一點參差")
        update.message.reply_text("至仁主引領我們正確者的路，不是受譴怒者的路，亦非迷誤者的路")
        update.message.reply_text("可蘭並沒有教導我們暴力，受到壓迫下的我們只能依靠暴力訴諸信仰")
        update.message.reply_text("暴力雖然不是唯一的解決方式，但它是最簡單且最深植人心的")
        update.message.reply_text("若想知道更深入，請輸入'我想更瞭解教義'，準備好了就提醒我")
    
    def on_exit_practice(self, update):
        pass

    def on_enter_practicemore(self, update):
        update.message.reply_text("這裡提供你網址，各種資訊都在這")
        update.message.reply_text("http://www.islam.org.hk/")
        update.message.reply_text("準備好了跟我說一聲")

    def on_exit_practicemore(self,update):
        pass

    def on_enter_quizstart(self, update):
        global Correct, counter
        
        if(counter == 0):
            update.message.reply_text("我們聖書是什麼？\n(a.)蘭可經\n(b.)可蘭經\n(c.)杜蘭經")
        elif(counter == 1):
            update.message.reply_text("你知道做了爆炸這件事等同你是恐怖份子嗎\n(a.)是\n(b.)否")
        elif(counter == 2):
            update.message.reply_text("真主引導我們走向\n(a.)迷誤者的路\n(b.)譴怒者的路\n(c.)正確者的路")
        elif(counter == 3):
            update.message.reply_text("你知道爆炸會讓人受傷嗎？\n(a.)是\n(b.)否")
        elif(counter == 4):
            update.message.reply_text("成為聖戰士之後不得洩漏任何有關組織的訊息，否則一切福利將被剝奪。\n(a.)知\n(b.)不知")
        elif(counter == 5):
            update.message.reply_text("請問穆罕默德是我們的？\n(a.)偶像\n(b.)先知\n(c.)神明")
        elif(counter == 6):
            update.message.reply_text("你在執行聖戰士任務時有大機率會死亡，你能承擔這樣的風險嗎？\n(a.)能\n(b.)不能")
        elif(counter == 7):
            update.message.reply_text("至仁主創造的是\n(a.)九重天\n(b.)七重天\n(c.)三重天")
        elif(counter == 8):
            update.message.reply_text("在你死亡後我們能妥善照顧你的親人，但你的親人可能因死而悲傷，你可以接受嗎？\n(a.)是\n(b.)否")
        elif(counter == 9):
            update.message.reply_text("如果有人汙衊我們的教義，你應該做的事是\n(a.)當場打爆他\n(b.)請他吃慶記\n(c.)回家找爸媽\n(d.)灌輸他正確的觀念")
        elif(counter == 10):
            update.message.reply_text("伊斯蘭朝聖地為\n(a.)麥加\n(b.)耶路薩冷\n(c.)戴斯蒙\n(d.)麥地納")
        
        elif(counter == 11):
            if(Correct >= 7):
                self.go_final(update)
                counter = 0
                Correct = 0
            else:
                self.go_trash(update)
                update.message.reply_text("不合格")
                counter = 0
                Correct = 0
    
    def on_exit_quizstart(self, update):
        global Correct, counter

        text = update.message.text

        if(counter == 0):
            if(text == 'b'):
                Correct = Correct + 1
        elif(counter == 1):
            if(text == 'a'):
                Correct = Correct + 1
        elif(counter == 2):
            if(text == 'c'):
                Correct = Correct + 1
        elif(counter == 3):
            if(text == 'a'):
                Correct = Correct + 1
        elif(counter == 4):
            if(text == 'a'):
                Correct = Correct + 1
        elif(counter == 5):
            if(text == 'b'):
                Correct = Correct + 1
        elif(counter == 6):
            if(text == 'a'):
                Correct = Correct + 1
        elif(counter == 7):
            if(text == 'b'):
                Correct = Correct + 1
        elif(counter == 8):
            if(text == 'a'):
                Correct = Correct + 1
        elif(counter == 9):
            if(text != 'c'):
                Correct = Correct + 1
            else:
                update.message.reply_text("大錯特錯")
        elif(counter == 10):
            if(text != 'c'):
                Correct = Correct + 1
            else:
                update.message.reply_text("三個答案你能選到錯的也太強")
        
        counter = counter + 1

    def on_enter_final(self, update):
        global lock
        lock = False
        update.message.reply_text("恭喜你合格，現在你是聖戰士了\n稍後會有專人與你聯繫，請等待！！")
        if(lock == False):
            _thread.start_new_thread(my_timer, (self, update))


    def on_exit_final(self, update):
        pass
    
    def newsearch(self, update):
        text = update.message.text
        if ( text == '可以' or text == '繼續'):
            return False
        else:
            return True

    def guaola(self, update):
        text = update.message.text
        return text == '可以'

    def oldsearch(self, update):
        text = update.message.text
        return text == '繼續'

    def on_enter_WebSearch(self, update):
        global url_list
        del url_list[:]

        text = update.message.text

        for url in search(text, stop = 10):
            url_list.append(url)

        k = random.randint(0, 10)
        
        update.message.reply_text(url_list[k])
        url_list.remove(url_list[k])
        update.message.reply_text("這次搜尋結果你滿意嗎？")
        update.message.reply_text("若覺得可以請輸入'可以'")
        update.message.reply_text("還想要搜尋其他的請輸入你想搜尋的內容")
        update.message.reply_text("若想繼續搜索當前內容請輸入'繼續'")

    def on_exit_WebSearch(self, update):
        pass

    def on_enter_OldSearch(self, update):
        global url_list

        p = len(url_list)
        k = random.randint(0, p)
        update.message.reply_text(url_list[k])
        url_list.remove(url_list[k])

        update.message.reply_text("這次搜尋的結果你滿意嗎？")
        update.message.reply_text("若覺得可以請輸入'可以'")
        update.message.reply_text("若想要搜尋其他內容請輸入你想搜尋的內容")
        update.message.reply_text("若想繼續搜索當前內容請輸入'繼續'")

    def on_exit_OldSearch(self, update):
        pass

    def toNote(self, update):
        text = update.message.text
        return text.lower() == 'note'

    def on_enter_note(self, update):
        update.message.reply_text("大部分都有回覆提示")
        update.message.reply_text("如果沒有的就照著直覺回復就可以了")
        update.message.reply_text("這只是個玩笑的bot，FBI別關注我拜託")
        update.message.reply_document(open("README.md",'rb'))
#        self.go_back(update)

    def on_exit_note(self, update):
        pass

    def goSearch(self, update):
        text = update.message.text
        return text == 'search'
    
    def goMain(self, update):
        text = update.message.text
        return text.lower() == 'main'

    def on_enter_jpsearch(self, update):
        update.message.reply_text("請直接輸入你想搜尋的內容")

    def on_exit_jpsearch(self, update):
        pass

    def recur(self, update):
        text = update.message.text
        if(text.lower() == 'search' or text.lower() == 'main' or text.lower() == 'note'):
            return False
        else:
            return True

    def goNote(self, update):
        text = update.message.text
        return text == 'note'
        
    def on_enter_note2(self, update):
        update.message.reply_text("note2")
