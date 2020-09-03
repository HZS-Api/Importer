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

    def get_title(self) -> str:
        return self.__title

    def get_link(self) -> str:
        return self.__link

    def get_pub_date(self) -> str:
        return self.__pub_date

    def get_description(self) -> str:
        return self.__description

    def get_type(self) -> str:
        return self.__type

    def get_subtype(self) -> str:
        return self.__subtype

    def get_region(self) -> str:
        return self.__region

    def get_city(self) -> str:
        return self.__city

    def get_department(self) -> str:
        return self.__department

    def get_state(self) -> str:
        return self.__state
