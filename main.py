from model_Apriori import Apriori
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from GUI import Ui_MainWindow
from model_Apriori import Apriori
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Apriori.clicked.connect(self.da_Doc)
        self.uic.Apriori.clicked.connect(self.Apriori)
        self.xuLy()
        self.modelApriori=Apriori('Data/user_rating.csv', 0.08)
    def xuLy(self):
        from BLL import BLL
        bll = BLL('Data/user_rating.csv')
        items = bll.id_User()
        for item in items:
            self.uic.list_User.addItem('User: '+str(item))
    def da_Doc(self):
        from BLL import BLL
        bll = BLL('Data/user_rating.csv')
        id = int(self.uic.list_User.currentItem().text().replace('User: ', ''))
        self.books = bll.da_Doc(id)
        self.uic.list_SachDoc.clear()
        for book in self.books:
            self.uic.list_SachDoc.addItem(str(book))
    def Apriori(self):
        lst = self.books
        results = self.modelApriori.rules(lst)
        self.uic.list_Sach.clear()
        for result in results[:15]:
            self.uic.list_Sach.addItem(str(result))
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


