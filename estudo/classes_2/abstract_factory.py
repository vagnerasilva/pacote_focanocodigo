from abc import ABC, abstractmethod


class AbstractApiFortal(ABC):
    def __init__(self, token):
        self.token = token

    @abstractmethod
    def collect_data(self):
        pass


class AbstractApiCe(ABC):
    def __init__(self, token):
        self.token = token

    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def collect_data_by_city(self, city):
        pass


class ApiFortalTransport(AbstractApiCe):
    def collect_data(self):
        return f"Dados coletados ApiCeTransport por meio do token: {self.token}"

    def collect_data_by_city(self, city):
        return f"Dados coletados da cidade ApiCeTransport por meio do token: {self.token}"


class ApiFortalSecurity(AbstractApiFortal):
    def collect_data(self):
        return f"Dados coletados ApiFortalSecurity por meio do token: {self.token}"

    def collect_data_by_city(self, city):
        return f"Dados coletados da cidade ApiFortalSecurity por meio do token: {self.token}"


class AbstractAPIFactory(ABC):
    def __init__(self, token_fortal, token_ce):
        self.token_fortal = token_fortal
        self.token_ce = token_ce

    @abstractmethod
    def create_api_fortal(self):
        pass

    @abstractmethod
    def create_api_ce(self):
        pass


class TransportDataFactory(AbstractAPIFactory):
    def create_api_fortal(self):
            return ApiFortalTransport(self.token_fortal)
   
    def create_api_ce(self):
            return Api(self.token_ce)
      

class SecurityDataFactory(AbstractAPIFactory):
    def create_api_fortal(self):
            return ApiFortalSecurity(self.token_fortal)
   
    def create_api_ce(self):
            return ApiFortalSecurity(self.token_ce)