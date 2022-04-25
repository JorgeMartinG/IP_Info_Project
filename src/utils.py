import logging
import datetime

NUMBERS = (128, 64, 32, 16, 8, 4, 2, 1)
MASKS = ('255.0.0.0', '255.255.0.0', '255.255.255.0')

# - Project Functions:


def binary_translation(decimal_ip: list) -> str:
    """ Translate binary IP address into decimal IP address
        params: Decimal_ip
        return: Binary IP address """
    binary_ip = []
    for byte in decimal_ip:
        result = int(byte)
        for value in NUMBERS:
            result -= value
            if result < 0:
                binary_ip.append(0)
                result += value
            else:
                binary_ip.append(1)
        binary_ip.append('.')
    binary_ip = binary_ip
    ip_address = ''.join(str(bit) for bit in binary_ip)
    return ip_address[:-1]


def decimal_translation(binary_ip: list) -> str:
    """ Translate decimal IP address into binary IP address
        params: Binary ip
        return: decimal IP address """
    binary_bytes = [byte[::-1] for byte in binary_ip]
    decimal_byte = []
    decimal_bytes = []
    for byte in binary_bytes:
        for index, bit in enumerate(list(byte)):
            bit = int(bit) * (2 ** int(index))
            decimal_byte.append(bit)
        decimal_bytes.append(sum(decimal_byte))
        decimal_byte.clear()
    ip_address = '.'.join(str(byte) for byte in decimal_bytes)
    return ip_address


def class_calculation(ip_address: str) -> str:
    """ Calulate IP class of an IP
        params: ip_address
        return: ip_class """
    ip_bytes = ip_address.split('.')
    if int(ip_bytes[0]) <= 127:
        class_ip = 'A'
    elif int(ip_bytes[0]) <= 191:
        class_ip = 'B'
    elif int(ip_bytes[0]) <= 223:
        class_ip = 'C'
    elif int(ip_bytes[0]) < 239:
        class_ip = 'D'
    else:
        class_ip = 'E'
    return class_ip


def mask_calculation(class_ip: str) -> str:
    """ Calulate IP Mask of an IP
        params: class_ip
        return: ip_mask """
    if class_ip == 'A':
        ip_mask = MASKS[0]
    elif class_ip == 'B':
        ip_mask = MASKS[1]
    elif class_ip == 'C':
        ip_mask = MASKS[2]
    else:
        ip_mask = 'N/A'
    return ip_mask




