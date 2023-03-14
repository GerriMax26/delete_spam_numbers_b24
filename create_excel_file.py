import xlsxwriter
import os

def writer_file (array_numbers: list) -> None:
   """Creates an excel file with phone numbers"""
   
   path = os.path.abspath(os.path.dirname(__file__)) + '\spam_contacts.xlsx'
   
   book = xlsxwriter.Workbook(path)
   
   page = book.add_worksheet('page_1')
            
   page.set_column("A:A", 15)

   row: int = 0 
   column: int = 0
    
   for item in array_numbers:
       
      page.write(row, column, item)
      row += 1
   
   book.close()