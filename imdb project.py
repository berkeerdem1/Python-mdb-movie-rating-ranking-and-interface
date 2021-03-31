import sys
import requests
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout
from bs4 import BeautifulSoup


url="http://www.imdb.com/chart/top"
response=requests.get(url)
html_content=response.content

soup=BeautifulSoup(html_content,"html.parser")

titles=soup.find_all("td",{"class":"titleColumn"})
ratings=soup.find_all("td",{"class":"ratingColumn"})

print(response)

class window(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.checkbox=QCheckBox("imdb movies and rating order")
        self.yazi_alani=QLabel("")
        self.buton=QPushButton("click")

        v_box=QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("")

        self.buton.clicked.connect(lambda: self.click(self.checkbox.isChecked(),self.yazi_alani))
        self.show()

    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("imdb movie and rating in the run section")
            for title, rating in zip(titles, ratings):
                print("title", title.text)
                print("rating", rating.text)
        else:
            yazi_alani.setText("Please,check the box to see the imdb movie and rating order!")

app=QApplication(sys.argv)
pencere=window()
sys.exit(app.exec_())