class Config:
    def __init__(self):
        self._base_url = "http://devmh-admin.bhitest.com/"
        self._test_data = "C:\\Users\\rgarg\\PycharmProjects\\MattamyHomes\\Data\\TestData.xlsx"

    @property
    def base_url(self):
        return self._base_url

    @property
    def testDataFile(self):
        return self._test_data
