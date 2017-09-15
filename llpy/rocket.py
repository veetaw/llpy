import requests

from llpy import LLpyException, Base
from llpy.constants import URL


class Rocket(Base):
    instance_name = ['rocket', 'rockets']
    def __get_the(self, query):
        return Base.__get_the(self, query)

    def search(self, query):
        try:
            return requests.get(URL + 'agency?name=' + query).json()['agencies']
        except Exception as e:
            raise LLpyException('search', str(e))


class RocketEvent(Base):
    instance_name = ['rocketevent', '']
    def __get_the(self, query):
        return Base.__get_the(self, query)


class RocketFamily(Base):
    instance_name = ['rocketfamily', 'RocketFamilies']
    def __get_the(self, query):
        return Base.__get_the(self, query)
