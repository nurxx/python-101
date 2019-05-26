from sys import path
path.append('../')
from controller.controller import Crawler

class View:

    @classmethod
    def search(cls):
        print('#### Welcome to Panda Web Crawler! We are going to crawl the Bulgarian Web! ####')
        print('#### Get ready! Please, fill up the following ...')
        url = input('Your start url:> ')
        db = input('Your database:> ')
        crawler = Crawler(current_url=url, database=db)
        print('**** Saving all internal links of the website to database .... ****')
        crawler.get_internal_links()
        option = input('Do you want to save results to a histogram? [y/n]')
        # if option == 'y':
        crawler.make_histogram_of_results()
        print('Histogram is ready! Go check :)')
        # else:
            # pprint('~~~~ Goodbye! ~~~~')

