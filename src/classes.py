from abc import ABC, abstractmethod
from utils import decimal_translation, binary_translation, class_calculation, mask_calculation


class IpTranslation(ABC):
    """ Translate IP addresses. """
    def __init__(self, ip: str):
        """ Constructor class """
        self.ip = ip

    @abstractmethod
    def translation(self):
        print(self.ip)

    @abstractmethod
    def get_class(self):
        pass

    @abstractmethod
    def get_mask(self):
        pass

    @abstractmethod
    def get_net(self):
        pass


class BinaryTranslation(IpTranslation):

    def translation(self):
        decimal_ip = self.ip.split('.')
        return binary_translation(decimal_ip)

    def get_class(self):
        ip_address = self.ip
        return class_calculation(ip_address)

    def get_mask(self):
        ip_address = self.ip
        return mask_calculation(class_calculation(ip_address))

    def get_net(self):
        ip_address = self.ip


class DecimalTranslation(IpTranslation):
    def translation(self):
        binary_ip = self.ip.split('.')
        return decimal_translation(binary_ip)

    def get_class(self):
        ip_address = self.translation()
        return class_calculation(ip_address)

    def get_mask(self):
        ip_address = self.ip
        return mask_calculation(class_calculation(ip_address))

    def get_net(self):
        ip_address = self.ip
        return()


