class EmailNotifier:
    def send(self,msg):
        print(msg)

class SMSNotifier:
    def send(self,msg):
        print(msg)

def notify(obj):
    obj.send("Hello User")

notify(EmailNotifier())
notify(SMSNotifier())