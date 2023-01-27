from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from time import sleep
from getpass import getpass
from pwinput import pwinput

class main:
    def __init__(self):
        self.browser = Firefox()
        self.username, self.password = main.get_id()
        self.Courses = {"Electromagnétisme " : "https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1589",
               "lignes de transmission" :"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1595",
               "Architecture des systèmes":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1583",
               "Capteurs et métrologie":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1505",
               "DDRS": "https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=2661",
               "Electronique analogique":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1577",
               "Energie":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1517",
               "Engagement étudiant":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=971",
               "Entreprise et management":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1559",
               "Language C":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1541",
               "Mathematiques":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1553",
               "Physique":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1511",
               "Projet Elec-Info":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1571",
               "Projet VHDL":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1529",
               "Anglais":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=3461",
               "Système asservis":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1565",
               "VHDL":"https://moodle-sciences-22.sorbonne-universite.fr/course/view.php?id=1535"}

    def get_id():
        username = input("Username: ")
        password = pwinput("Password: ")
        return username, password

    def Login(self, course):
            self.browser.get(course)
            try:
                username_field = self.browser.find_element("id", "username")
                password_field = self.browser.find_element("id", "password")
                login_button = self.browser.find_element("name", "submit")
                username_field.send_keys(self.username)
                password_field.send_keys(self.password)
                login_button.click()
            except:
                return 0

    def CheckCourses(self):
        homework = {}
        for course in self.Courses:
            self.Login(self.Courses[course])
            #sleep(0.1)
            CourseSoup = BeautifulSoup(self.browser.page_source, 'html.parser')
            if "Devoir" in CourseSoup.get_text():
                print("Il y a un devoir à rendre dans le cours " + course)
                homework[course] = self.Courses[course]
        return homework
    
    def GetHomework(self):
        print(self.CheckCourses())
        self.browser.close()
    
if __name__ == "__main__":
    main().Login("https://auth.sorbonne-universite.fr/cas/login?service=https%3A%2F%2Fmoodle-sciences-22.sorbonne-universite.fr%2Flogin%2Findex.php%3FauthCAS%3DCAS")
    main().GetHomework()