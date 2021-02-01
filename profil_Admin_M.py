#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:
#
# Created:     27/07/2020
# Copyright:   (c)  2020
# Licence:
#-------------------------------------------------------------------------------
import unittest
import time, random
from datetime import datetime
import HtmlTestRunner
import conf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Edge
from selenium.common.exceptions import NoSuchElementException

class AM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge(executable_path=conf.edge_driver_path)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_01_connexion(self):
        self.driver.get(conf.webSite)
        self.driver.find_element_by_id("login").click()
        self.driver.find_element_by_name("username").send_keys()
        self.driver.find_element_by_name("password").send_keys()
        self.driver.find_element_by_xpath("//form[@role='form']//*[@class='btn btn-primary']").click()

    def test_02_aDM(self):
        self.driver.find_element_by_xpath("//*[@id='functional-admin-header']/h5/button").click()

    def test_03_TS(self):
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div"
        self.assertEquals(self.driver.find_element_by_id("configuration-page-heading").text, "A")

        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[1]/div[1]/div/h2/span").text, "A")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[1]/div[2]/div/h2").text, "B")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[2]/div[1]/div/h2/span").text, "C")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[2]/div[2]/div/h2/span").text, "D")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[3]/div/div/h2/span").text, "F")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[4]/div/div/h2/span").text, "G")

        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[5]/button/span").text, "Enregistrer")

    def test_04_GTR(self):
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[1]/div/div/div/h5/span").text, "Mode*")
        i = 1
        j = 0
        list = ["automatique", "permanent", "Affichage permanent"]
        for l in list:
            self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[1]/div/div/div/div["+str(i)+"]/div/label").text, l)
            self.driver.find_element_by_id("displayAreaStateRadio_"+str(j))
            i += 1
            j += 1

        text = "* l'écran du mur."
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[1]/div/div/div/label/span").text, text)


    def test_05_FI(self):
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[2]/div/div[1]/div/label/h5/span").text, "A")
        self.driver.find_element_by_id("a")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[2]/div/div[1]/div/div/div/div/span/span").text, "B")

        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[2]/div/div[3]/div/label/h5/span").text, "C")
        self.driver.find_element_by_id("b")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[1]/div[2]/div/div[3]/div/div/div/div/span/span").text, "D")

    def test_06_GMD(self):
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[1]/div/div/div/label[1]/h5/span").text, "E")
        self.driver.find_element_by_id("c")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[1]/div/div/div/div[1]/div/div/span/span").text, "F")

        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[1]/div/div/div/label[2]/h5/span").text, "G")
        self.driver.find_element_by_id("d")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[1]/div/div/div/div[2]/div/div/span/span").text, "H")

    def test_07_Alarme(self):
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[2]/div/div/div/h5/span").text, "I")

        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[2]/div/div/div/div[1]/label/span").text, "Oui")
        self.driver.find_element_by_id("e")

        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[2]/div[2]/div/div/div/div[2]/label/span").text, "Non")
        self.driver.find_element_by_id("f")

    def test_08_CH(self):
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[3]/div/div/div/div[1]"
        xpath_2 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[3]/div/div/div/div"
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"/h5/span").text, "Activation")
        self.driver.find_element_by_id("g")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"/div[1]/label/span").text, "Oui")
        self.driver.find_element_by_id("h")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"/div[2]/label/span").text, "Non")

        self.assertEquals(self.driver.find_element_by_xpath(xpath_2+"[2]/div/h5/span").text, "Date de début")
        self.driver.find_element_by_id("i")
        self.driver.find_element_by_xpath(xpath_2+"[2]/div/div/div[2]/timepicker/table/tbody/tr[2]/td[1]/input")
        self.driver.find_element_by_xpath(xpath_2+"[2]/div/div/div[2]/timepicker/table/tbody/tr[2]/td[3]/input")
        self.assertEquals(self.driver.find_element_by_xpath(xpath_2+"[2]/div/div/div[1]/div/div/span/span").text, "Date")

        self.assertEquals(self.driver.find_element_by_xpath(xpath_2+"[3]/div/h5/span").text, "Date de fin")
        self.driver.find_element_by_id("j")
        self.driver.find_element_by_xpath("//*[@id='importBehaviourChangeEndHour']/table/tbody/tr[2]/td[1]/input")
        self.driver.find_element_by_xpath("//*[@id='importBehaviourChangeEndHour']/table/tbody/tr[2]/td[3]/input")

        self.assertEquals(self.driver.find_element_by_xpath(xpath_2+"[3]/div/div/div[1]/div/div/span/span").text, "Date")

    def test_09_AD(self):
        list = ["faible", "moyenne", "forte", "très forte"]
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div[4]/div/div/div["
        i = 1
        j = 0
        for l in list:
            self.assertEquals(self.driver.find_element_by_xpath(xpath_1+str(i)+"]/div/div[1]/h5/span").text, l)
            self.assertEquals(self.driver.find_element_by_xpath(xpath_1+str(i)+"]/div/div[2]/h5").text, "Couleur associée")
            self.driver.find_element_by_id("helperAreaGravity_"+str(j))
            self.driver.find_element_by_id("opacity2_"+str(j))
            i += 1
            j += 1

    def test_10_MAD(self):
        time.sleep(10)
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div"
        list = ["15 minutes",
        "15 minutes : tous",
        "5 minutes",
        "1 minute"]
        j = 0
        for l in list:
            rand = random.randint(1,100)
            self.driver.find_element_by_id("helperAreaGravity_"+str(j)).clear()
            self.driver.find_element_by_id("helperAreaGravity_"+str(j)).send_keys(l+" Test modification : "+str(rand))
            list_2 = []
            list_2.append(self.driver.find_element_by_id("helperAreaGravity_"+str(j)).text)
            j += 1
        self.driver.find_element_by_xpath(xpath_1+"[5]/button/span").click()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='toast-container']/div/div").text, "C")
        self.driver.find_element_by_xpath("//*[@id='increments-header']/h5/button").click()
        self.driver.find_element_by_xpath("//*[@id='functional-admin-header']/h5/button").click()
        i = 0
        for l2 in list_2:
            print(self.driver.find_element_by_id("helperAreaGravity_"+str(i)).text)
            self.assertEquals(self.driver.find_element_by_id("helperAreaGravity_"+str(i)).text, l2)
            i += 1


    def test_11_MCSFI(self):
        #1500
        time.sleep(10)
        id = "ThresholdInput"
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div"
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("-3")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[1]/div[2]/div/div[2]/span").text, "A")
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("1500")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='toast-container']/div/div").text, "B")
        self.driver.find_element_by_xpath("//*[@id='frequencyGaps-header']/h5/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='functional-admin-header']/h5/button").click()
        self.assertEquals(self.driver.find_element_by_id(id).get_attribute("value"), "1500")


    def test_12_MCSMFI(self):
        #1500
        time.sleep(10)
        id = "ThresholdInput"
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div"
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("-3")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='toast-container']/div/div").text, "c")
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("1500")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='toast-container']/div/div").text, "c")
        self.driver.find_element_by_xpath("//*[@id='analyseSitu-header']/h5/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='functional-admin-header']/h5/button").click()
        self.assertEquals(self.driver.find_element_by_id(id).get_attribute("value"), "1500")

    def test_13_MCFAGMD(self):
        #172800
        time.sleep(10)
        id = "DetectionInput"
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div"
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("-251")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[2]/div[1]/div/div/div/div[3]/span").text, "A")
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("0")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[2]/div[1]/div/div/div/div[3]/span").text, "B")
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("172800")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='toast-container']/div/div").text, "c")
        self.driver.find_element_by_xpath("//*[@id='analyseSitu-header']/h5/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='functional-admin-header']/h5/button").click()
        self.assertEquals(self.driver.find_element_by_id(id).get_attribute("value"), "172800")

    def test_14_MCDMGMD(self):
        #3600
        time.sleep(10)
        id = "DetectionInput"
        xpath_1 = "/html/body/jhi-main/div[2]/div/div[2]/rgs-functional-admin/div/div/form/div"
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("-100")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[2]/div[1]/div/div/div/div[3]/span").text, "A")
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("0")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        self.assertEquals(self.driver.find_element_by_xpath(xpath_1+"[2]/div[1]/div/div/div/div[3]/span").text, "C")
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys("3600")
        self.driver.find_element_by_xpath(xpath_1+"[5]/button").click()
        time.sleep(3)
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='toast-container']/div/div").text, "B")
        self.driver.find_element_by_xpath("//*[@id='analyseSitu-header']/h5/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='functional-admin-header']/h5/button").click()
        self.assertEquals(self.driver.find_element_by_id(id).get_attribute("value"), "3600")

    def test_15_navbarHaut(self):
        self.driver.find_element_by_xpath("/html/body/jhi-main/div[1]/rgs-navbar/nav/div[1]/a").click()
        self.driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/div/rgs-record-notification[1]/div/a/div[2]")
        self.driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/div/rgs-record-notification[2]/div/a/div[2]")
        self.driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[2]/span/span")
        self.driver.find_element_by_xpath("//*[@id='logout']")
        self.driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[4]/a")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
