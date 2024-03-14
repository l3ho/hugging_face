import speech_recognition as sr
import pyaudio


class speech_rec():
    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.audio_txt = ""

    def start_listening(self):
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
        self.stop_listening = self.r.listen_in_background(self.m, callback=self.callback)

    def callback(self, recognizer, audio):
        try:
            self.audio_txt=recognizer.recognize_google(audio, language='pl-pl')
        except Exception as ee:
            pass

    def stop_to_listen(self):
        self.stop_listening()

def main():
    r= sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
    stop_listening = r.listen_in_background(m, callback=callback)

    # srec = sr.speech_rec()
    # print("start")
    # srec.start_listening()
    # tmp1 = srec.audio_txt
    # for ii in range(100):
    #     tmp1 = srec.audio_txt
    #     time.sleep(1)
    #     if tmp1 != srec.audio_txt:
    #         print(srec.audio_txt)
    # print("stop")
    # srec.stop_listening()

