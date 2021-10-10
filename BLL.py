import pandas as pd
import numpy as np

class BLL():
    def __init__(self,url):
        self.url = url
    def id_User(self):
        data = pd.read_csv(self.url)
        return sorted(list(set(data.ID)))
    def da_Doc(self,id):
        data = pd.read_csv(self.url)
        return sorted(list(set(data[data.ID==id].Name)))

    def xuLy(self):
        from BLL import BLL
        bll = BLL('Data/user_rating.csv')
        items = bll.id_User()
        for item in items:
            self.list_User.addItem('User: '+str(item))

    # def xuLy(self):
    #     from BLL import BLL
    #     from PyQt5.QtWidgets import QListWidgetItem
    #     bll = BLL('Data/user_rating.csv')
    #     items = bll.id_User()
    #     for item in items:
    #         self.list_User.addItem('User: '+str(item))
    #     self.list_Use
    #
    #     id = int(self.list_User.currentItem().replace('User: ',''))
    #     temp = QListWidgetItem('User: '+str(items[2]))
    #     self.list_User.setCurrentItem(temp)
    #     books = bll.da_Doc(self.list_User.currentItem().text())
    #     for book in books:
    #         self.list_Sach_2.addItem(str(book))
