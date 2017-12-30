
import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '470479128:AAENFEglNPFqsFFAGzBKbLL6xR3G8QcjulI'
WEBHOOK_URL = 'https://a877a4a1.ngrok.io/mybot'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[

#        'state1',
#        'state2',
#        'state3',
            
        'user',
        'notrasher',

        'ask',
            'no1',
            'no2',
            'no3',
            
            'askwhy',
                'askdicision',
                    'askmission',
                    'tellmission',
                        'quiz',
                            'practice',
                                'practicemore',
                        'quizstart',
                            'final',
                    
                'askpressure',
                    'tips',
                        'tip1',
                        'tip2',
                        'tip3',
                        'another',

                    'retarded',
                        'askwhatyoudo',
                        'guao',
                
                'ososos',
                    'keepAddress',
                    'BePatient'

    ],

    transitions=[
              
#        {
#            'trigger': 'advance',
#            'source': 'user',
#            'dest': 'state1',
#            'conditions': 'is_going_to_state1'
#        },

#        {
#            'trigger': 'advance',
#            'source': 'user',
#            'dest': 'state2',
#            'conditions': 'is_going_to_state2'
#        },
        
#        {
#            'trigger':'advance',
#            'source': 'state1',
#            'dest': 'state3',
#            'conditions': 'is_going_to_state3'
#        },
        

        {
            'trigger': 'go_back',
            'source': [
#                'state1',
#                'state2',
                'guao',
                'BePatient',
                'notrasher',
                'final',
            ],
            'dest': 'user'
        },
    
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'ask',
        },

        {
            'trigger' : 'advance',
            'source' : 'final',
            'dest' : 'final'
        },

        {
            'trigger': 'advance',
            'source': 'ask',
            'dest': 'no1',
            'conditions': 'is_going_to_no1'
        },

        {
            'trigger': 'advance',
            'source': 'ask',
            'dest': 'askwhy',
            'conditions': 'is_going_to_askwhy'
        },

        {
            'trigger':'advance',
            'source': 'no1',
            'dest': 'askwhy',
            'conditions' : 'is_going_to_askwhy'
        },

        {
            'trigger': 'advance',
            'source': 'no1',
            'dest': 'no2',
            'conditions': 'is_going_to_no2'
        },

        {
            'trigger': 'advance',
            'source': 'no2',
            'dest': 'askwhy',
            'conditions': 'is_going_to_askwhy'
                
        },

        {
            'trigger': 'advance',
            'source': 'no2',
            'dest': 'no3',
            'conditions': 'is_going_to_no3'
        },

        {
            'trigger': 'advance',
            'source': 'no3',
            'dest': 'askwhy',
            'conditions': 'is_going_to_askwhy'
        },

        {
            'trigger': 'advance',
            'source': 'no3',
            'dest': 'notrasher',
            'conditions': 'is_going_to_notrasher'
        },

        {
            'trigger' : 'advance',
            'source': 'notrasher',
            'dest': 'notrasher'
        },

        {
            'trigger' : 'advance',
            'source': 'askwhy',
            'dest':'askdicision',
            'conditions':'is_going_to_askdicision'
        },

        {
            'trigger' : 'advance',
            'source' : 'askdicision',
            'dest' : 'notrasher',
            'conditions': 'is_going_to_notrasher'

        },

        {
            'trigger' : 'advance',
            'source' : 'askdicision',
            'dest' : 'askmission',
            'conditions':'is_going_to_askmission'
        },

        {
            'trigger' : 'advance',
            'source' : 'askmission',
            'dest' : 'tellmission',
            'conditions' : 'is_going_to_tellmission'
        },

        {
            'trigger' : 'advance',
            'source' : 'tellmission',
            'dest' : 'notrasher',
            'conditions' : 'is_going_to_notrasher'
        },

        {
            'trigger' : 'advance',
            'source' : 'askmission',
            'dest' : 'quiz',
            'conditions' : 'is_going_to_quiz'
        },
        
        {
            'trigger' : 'advance',
            'source' : 'quiz',
            'dest' : 'practice',
            'conditions' : 'is_going_to_practice'
        },

        {
            'trigger' : 'advance',
            'source' : 'practice',
            'dest' : 'practicemore',
            'conditions' : 'is_going_to_practicemore'
        },

        {
            'trigger' : 'advance',
            'source' :[
                'quiz',
                'practice',
                'practicemore',
                ],
            'dest' : 'quizstart',
            'conditions' : 'is_going_to_quizstart'
        },

        {
            'trigger' : 'advance',
            'source' : 'tellmission',
            'dest' : 'quiz',
            'conditions' : 'is_going_to_quiz'
        },

        {
            'trigger' : 'advance',
            'source' : 'quiz',
            'dest' : 'quizstart',
        },

        {
            'trigger' : 'advance',
            'source' : 'quizstart',
            'dest' : 'quizstart'
        },

        {
            'trigger' : 'go_final',
            'source' : 'quizstart',
            'dest' : 'final'
        },

        {
            'trigger' : 'go_trash',
            'source' : 'quizstart',
            'dest' : 'notrasher'
        },

        {
            'trigger' : 'advance',
            'source' : 'askwhy',
            'dest' : 'askpressure',
            'conditions':'is_going_to_askpressure'
        },

        {
            'trigger' : 'advance',
            'source' : 'askwhy',
            'dest' : 'ososos',
            'conditions' : 'is_going_to_OS'
        },

        {
            'trigger' : 'advance',
            'source' : 'ososos',
            'dest' : 'keepAddress',
            'conditions' : 'is_going_to_keepAddress'   
        },

        {
            'trigger' : 'advance',
            'source' : 'ososos',
            'dest': 'askwhatyoudo',
            'conditions' : 'is_going_to_askwhatyoudo'
        },

        {
            'trigger' : 'advance',
            'source' : 'keepAddress',
            'dest' : 'BePatient'
        },

        {
            'trigger' : 'advance',
            'source' : 'BePatient',
            'dest' : 'BePatient'
        },

        {
            'trigger' : 'advance',
            'source' : 'askdicision',
            'dest': 'notrasher',
            'conditions':'is_going_to_notrasher'
        },

        {   
            'trigger' : 'advance',
            'source' : 'askpressure',
            'dest' : 'tips',
            'conditions' : 'is_going_to_tips'
        },

        {
            'trigger' : 'advance',
            'source' : 'askpressure',
            'dest' : 'retarded',
            'conditions' : 'is_going_to_retarded'
        },

        {
            'trigger' : 'advance',
            'source' : 'retarded',
            'dest' : 'askwhatyoudo',
            'conditions' : 'is_going_to_askwhatyoudo'
        },

        {
            'trigger' : 'advance',
            'source' : 'askwhatyoudo',
            'dest' : 'guao',
        },

        {
            'trigger' : 'advance',
            'source' : 'tips',
            'dest' : 'tip1',
            'conditions' : 'is_going_to_tip1'
        },

        {
            'trigger' : 'advance',
            'source' : 'tips',
            'dest' : 'tip2',
            'conditions' : 'is_going_to_tip2'     
        },

        {
            'trigger' : 'advance',
            'source' : 'tips',
            'dest' : 'tip3',
            'conditions' : 'is_going_to_tip3'
        },

        {
            'trigger' : 'advance',
            'source' : 'tips',
            'dest' : 'another',
            'conditions' : 'is_going_to_another'
        },

        {
            'trigger' : 'advance',
            'source' : 'tip1',
            'dest' : 'another',
            'conditions' : 'is_going_to_another'
        },

        {
            'trigger' : 'advance',
            'source' : 'tip2',
            'dest' : 'another',
            'conditions' : 'is_going_to_another'
        },
        
        {
            'trigger' : 'advance',
            'source' : 'tip3',
            'dest' : 'another',
            'conditions' : 'is_going_to_another'
        },

        {
            'trigger':'advance',
            'source' : 'tip1',
            'dest' : 'guao'
        },

        {
            'trigger':'advance',
            'source' : 'tip2',
            'dest' : 'guao'
        },

        {
            'trigger':'advance',
            'source' : 'tip3',
            'dest' : 'guao'
        },

        {
            'trigger' : 'advance',
            'source' : 'another',
            'dest' : 'guao'
        },

    ],
    initial='user',
#    auto_transitions=False,
#    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/mybot', methods=['POST'])
def mybot():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
