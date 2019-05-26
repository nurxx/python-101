import requests
from bs4 import BeautifulSoup
from pprint import pprint
from sqlalchemy.orm import sessionmaker
import pandas
from collections import Counter
from sys import path
path.append('../')
from database.database_layer import Database, Domain


class Crawler:
    def __init__(self,current_url,database):
        self.url = current_url
        self.db = Database(database)
        self.session_maker = sessionmaker(bind=self.db.engine)
        self.session = self.session_maker()

    def save_to_database(self,obj):
        try:
            self.session.add(obj)
        except Exception:
            print('Oops! Failed while saving to database!')
        else:
            self.session.commit()

    def do_exist_in_database(self,current_url):
        tuples = self.session.query(Domain.domain)\
                                    .filter(Domain.domain == current_url)

        return tuples.count() != 0

    @staticmethod
    def get_server(url):
        try:
            response = requests.head(url)
            return response.headers['server']
        except Exception as err:
            print('Oops! Error while getting DNS!')


    '''
    Getting internal links of a website using 
    level order traversal
    '''

    def get_internal_links(self):
        if self.url is None:
            return

        queue = list()
        queue.append(self.url)

        while len(queue):

            n = len(queue)
            
            while n:
                current_url = queue[0]
                queue.pop(0)
                if not self.do_exist_in_database(current_url):
                    server = self.get_server(current_url)
                    obj = Domain(domain=current_url,server=server)
                    self.save_to_database(obj)
                response = requests.get(current_url)
                soup = BeautifulSoup(response.text,'html.parser')
                links = soup.find_all('a')
                suffix = '.bg/'
                try:
                    for link in links:
                        link = link.get('href','')
                        if link.startswith('http://') and suffix in link:
                            index = link.find(suffix)
                            domain = link[:(index + len(suffix))]
                            queue.append(domain)
                        n = n-1
                except Exception as err:
                    pass

    def get_all_servers_from_db(self):
        try:
            servers = self.session.query(Domain.server).all()
            return [server for server, in results]
        except Exception as err:
            print('Error occured while getting all servers from database!')

    def make_histogram_of_results(self):
        servers = self.get_all_servers_from_db()
        histogram = Counter(servers)
        keys = list(histogram.keys())
        values = list(histogram.values())

        X = list(range(len(keys)))

        plt.bar(X, list(histogram.values()), align="center")
        plt.xticks(X, keys)

        plt.title(".bg servers")
        plt.xlabel("Server")
        plt.ylabel("Count")

        plt.savefig("histogram.png")

