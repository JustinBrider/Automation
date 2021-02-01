# coding: utf-8
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:
#
# Created:     09/07/2020
# Copyright:   (c)  2020
# Licence:
#-------------------------------------------------------------------------------

import unittest
import time
from datetime import datetime
import HtmlTestRunner
import conf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Edge
from selenium.common.exceptions import NoSuchElementException

class ASP(unittest.TestCase):

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

    def test_02_aFF(self):
        self.driver.find_element_by_xpath("//*[@id='analyseSitu-header']/h5/button").click()


    def test_03_TCAS(self):
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='analyse-past-situation-page-heading']/span").get_attribute("innerHTML"), "a")
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='searchNavbar']/div/div/div[1]/div/label/h5/span").get_attribute("innerHTML"), "b")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-analyse-past-situation/div/div[1]/form/h2/span").get_attribute("innerHTML"), "c")
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='searchNavbar']/div/div/div[2]/div/label/h5/span").get_attribute("innerHTML"), "d")
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='searchNavbar']/div/div/div[3]/div/label/h5/span").text, "e")
        self.assertEquals(self.driver.find_element_by_xpath("//*[@id='timerNote']/span").text, "* f")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-analyse-past-situation/div/div[2]/rgs-chart-container/div/div/div[1]/span[1]/span").get_attribute("innerHTML"), "g")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-analyse-past-situation/div/div[3]/rgs-chart-container/div/div/div[1]/span[1]/span").get_attribute("innerHTML"), "h")
        self.assertEquals(self.driver.find_element_by_xpath("/html/body/jhi-main/div[2]/div/div[2]/rgs-analyse-past-situation/div/div[4]/rgs-chart-container/div/div/div[1]/span[1]/span").get_attribute("innerHTML"), "i")


    def test_04_CAS(self):
        self.driver.find_element_by_id("apsDatePicker")
        self.driver.find_element_by_xpath("//*[@id='apsTimePicker']/table/tbody/tr[2]/td[1]/input")
        self.driver.find_element_by_xpath("//*[@id='apsTimePicker']/table/tbody/tr[2]/td[3]/input")
        self.driver.find_element_by_xpath("//*[@id='apsTimePicker']/table/tbody/tr[2]/td[5]/input")
        self.driver.find_element_by_id("apsTimer")

    def test_05_BAS(self):
        list = [1, 2, 3, 4]
        self.driver.find_element_by_xpath("//*[@id='apsExportBtn']")
        i = 1
        for l in list:
            self.driver.find_element_by_xpath("//*[@id='searchNavbar']/div/div/div[4]/div/button["+str(i)+"]")
            i += 1

    def test_06_nH(self):
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
