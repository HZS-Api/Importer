class Incident(object):
    __title = ''
    __link = ''
    __pub_date = ''

    def __init__(self, data):
        self.__title = data['title']
        self.__link = data['link']
        self.__pub_date = data['pub_date']

    def get_title(self):
        return self.__title

    def get_link(self):
        return self.__link

    def get_pub_date(self):
        return self.__pub_date
