# There are two ways to achieve polymorphism:
#Inheritance and Duck typing


class Email:                                                         #send is (common interface)
    def send(self):
        print("sending email")              #different obj1

class SMS:
    def send(self):
        print("Sending SMS")       #doj2

class WhatsApp:
    def send(Self):
        print("Sending Whatsapp messgae")           #doj3



def notify(service):
    service.send()

notify(Email())
notify(SMS())
notify(WhatsApp())