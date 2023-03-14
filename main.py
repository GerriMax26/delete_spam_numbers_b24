import os

from bitrix24 import *
from fast_bitrix24 import Bitrix
from dotenv import load_dotenv

from create_excel_file import writer_file


load_dotenv()

bx24 = Bitrix24(os.getenv('bx24'))
b = Bitrix(os.getenv('b'))


def create_array_numbers() -> list:
    """Сreates an array of numbers with the name spam to create a excel file"""
    
    array_all_data_numbers_spam: list = bx24.callMethod('crm.contact.list',
                    filter = { "%NAME": "спам" },
                    select=['NAME', 'PHONE'])

    array_number: list = [] 
    array_number_result: list = []

    for i in range(len(array_all_data_numbers_spam)):
        
        count_element = array_all_data_numbers_spam[i]
        array_number = count_element['PHONE']
        
        for j in array_number:
            array_number_result.append(j['VALUE'])

    for i in range(len(array_number_result)):
        array_number_result[i] = array_number_result[i].replace(' ','')
        array_number_result[i] = array_number_result[i].replace('-','')
        
    return array_number_result

def create_array_contacts() -> list:
    """Сreates an array of contacts with the name spam"""
    
    array_all_data_contacts: list = bx24.callMethod('crm.contact.list',
                    filter = { "%NAME": "спам" },
                    select=['NAME', 'PHONE'])
    
    return array_all_data_contacts


def get_id_contacts(array_all_data_contacts: list) -> list:
    """Creates an array of contact id"""
    
    array_id: list = []
    
    for id in array_all_data_contacts:
        array_id.append(id['ID'])
    
    return array_id        

def delete_contacts(array_id: list) -> None:
    """Deletes contacts from crm by their id"""
    
    dict_id: dict = {}
    
    for i in array_id:
        
        dict_id['ID'] = int(i)
        b.call('crm.contact.delete',dict_id)

def main() -> None:
    
    writer_file(create_array_numbers())
    delete_contacts(get_id_contacts(create_array_contacts()))


if __name__ == '__main__':
    main()
