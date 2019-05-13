class German:
    def greet(self):
        return "Hallo!"

    def bye(self):
        return "Tschüss!"

class Translator:
    _response_greetings = {
    'Hallo!':'Γεια σου!',
    'Tschüss!': 'Τα λέμε!'
    }

    def __init__(self,german):
        self.current_speaker = german 

class Greek:
    def __init__(self,german_to_greek):
        self.translator = german_to_greek

    def greet(self):
        return self.translator._response_greetings[self.translator.current_speaker.greet()]

    def bye(self):
        return self.translator._response_greetings[self.translator.current_speaker.bye()]

def main():
    speaker1 = German()
    translator = Translator(speaker1)
    speaker2 = Greek(translator)

    print(speaker1.greet())
    print(speaker2.greet())

    print(speaker1.bye())
    print(speaker2.bye())

if __name__=='__main__':
    main()
