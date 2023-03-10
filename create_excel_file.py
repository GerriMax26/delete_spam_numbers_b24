import xlsxwriter

def writer_file (function_name):
    
    book = xlsxwriter.Workbook(r"C:/Users/admin/Desktop/delete_spam_numbers_b24/spam_contacts.xlsx")
    page = book.add_worksheet('page_1')
            
    page.set_column("A:A", 15)

    row = 0 
    column = 0
    
    for item in function_name:
       page.write(row, column, item)
       row+=1
    book.close()