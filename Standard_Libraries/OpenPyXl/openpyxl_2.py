from openpyxl import Workbook


# this is how we create a new workbook
wb = Workbook()

ws = wb.active

# this is how we get or set a title for our sheet
ws.title = "Data"

# this appends to the first empty row of the workbook(each item in different columns)
ws.append(["Omid", "is", "Great", "!"])
ws.append(["Omid", "is", "Great", "!"])
ws.append(["Omid", "is", "Great", "!"])
ws.append(["Omid", "is", "Great", "!"])
ws.append(["end"])

wb.save(r"./test.xlsx")
 