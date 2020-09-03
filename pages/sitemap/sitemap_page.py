import requests
from base.basepage import BasePage
from utilities.rw_file import ReadWriteFile


class SitemapPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.read = ReadWriteFile()
        self.driver = driver

    def verifySitemapUrl(self, url, resultSheetName):
        self.read.delete_excelSheet(resultSheetName)
        self.read.create_excelSheet(resultSheetName)
        row = 0
        urls = self.read.getXMLData(url, "url", "loc")
        for url in urls.values():
            r = requests.head(url)
            status = r.status_code
            if status != 200:
                row = row + 1
                self.read.write_excel(sheetToWrite=resultSheetName, row=row, column=1, cellValue=row)
                self.read.write_excel(sheetToWrite=resultSheetName, row=row, column=2, cellValue=url)
                self.read.write_excel(sheetToWrite=resultSheetName, row=row, column=3, cellValue=status)
        rows = self.read.count_excelRows(resultSheetName)
        columns = self.read.count_excelColumns(resultSheetName)
        if rows == 1 and columns == 1:
            return True
        else:
            return False
