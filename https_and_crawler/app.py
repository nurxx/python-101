import sys
from view.interface import View

class WebCrawlerApp:

    @classmethod
    def start(cls):
        View.search()

if __name__=='__main__':
    WebCrawlerApp.start()
