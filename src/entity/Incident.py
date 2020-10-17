from typing import Dict

class Incident(object):
    __title = ''
    __link = ''
    __pub_date = ''
    __description = ''
    __type = ''
    __subtype = ''
    __region = ''
    __city = ''
    __department = ''
    __state = ''

    def set_title(self, title: str):
        self.__title = title

    def set_link(self, link: str):
        self.__link = link

    def set_pub_date(self, pub_date: str):
        self.__pub_date = pub_date

    def set_description(self, description: str):
        self.__description = description

    def set_type(self, type: str):
        self.__type = type

    def set_subtype(self, subtype: str):
        self.__subtype = subtype

    def set_region(self, region: str):
        self.__region = region

    def set_city(self, city: str):
        self.__city = city

    def set_department(self, department: str):
        self.__department = department

    def set_state(self, state: str):
        self.__state = state

    def get_link(self) -> str:
        return self.__link

    def get_data(self) -> Dict[str, str]:
        return {
            'title': self.__title,
            'link': self.__link,
            'pub_date': self.__pub_date,
            'description': self.__description,
            'type': self.__type,
            'subtype': self.__subtype,
            'region': self.__region,
            'city': self.__city,
            'department': self.__department,
            'state': self.__state
        }
