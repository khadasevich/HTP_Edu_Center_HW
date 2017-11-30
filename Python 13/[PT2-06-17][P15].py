#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module that searches for Александр Солодуха at yahoo.com, google.com, banana.by, tut.by, Wikipedia """

from selenium import webdriver
import logging
import json
import time
import sys


class Configurator(object):
    """Class which allows to set which browser to use during execution and which pages script should visit"""

    def __init__(self, new_browser='Firefox'):
        """Constructor for new searches, by default I'm using the FireFox browser"""
        self.project_path = r'/home/alex/PycharmProjects/newborn/'
        self.exec_path = self.project_path + r'geckodriver'
        self.new_browser = new_browser
        self.email = None
        self.password = None
        self.js = None
        self.search_path = ('https://www.yahoo.com/',
                            'https://www.google.by/',
                            'https://banana.by/',
                            'https://www.tut.by/',
                            'https://ru.wikipedia.org/')
        self.twitter_path = 'https://twitter.com/solodukha'
        self.auth_data_opening()
        self.change_of_exec_path()

    def auth_data_opening(self):
        """Opening and reading data"""
        with open('autho_data.txt') as configure:
            self.js = json.load(configure)
            for key in self.js:
                self.email = self.js[key]["email"]
                self.password = self.js[key]["password"]

    def change_of_exec_path(self):
        """Changes exec path in according to browser"""
        if self.new_browser == 'Chrome':
            self.exec_path = self.project_path + r'chromedriver'


class Searcher(object):
    """Creates new session of search"""

    def __init__(self, browser_name, path_to_file):
        """Creates new session of web driver connection"""
        self.browser = None
        self.browser_name = browser_name
        self.path_to_driver = path_to_file
        self.input_field = None
        self.select_of_browser()

    def select_of_browser(self):
        """Selects which browser will in use"""
        self.browser = webdriver.Firefox(executable_path=self.path_to_driver)
        if self.browser_name == 'Chrome':
            self.browser = webdriver.Chrome(executable_path=self.path_to_driver)

    def solodukha_search(self, search_path):
        """Searches mentions of solodukha in the internet"""
        self.browser.maximize_window()
        self.browser.get(search_path)
        self.browser.implicitly_wait(30)
        self.searching_element(search_path)
        self.input_field.send_keys(u'Александр Солодуха')
        self.input_field.submit()

    def searching_element(self, search_path):
        """ Searches input field """
        if search_path == 'https://www.yahoo.com/':
            self.input_field = self.browser.find_element_by_xpath("//*[@id='uh-search-box']")
        elif search_path == 'https://www.google.by/':
            self.input_field = self.browser.find_element_by_xpath("//*[@id='lst-ib']")
        elif search_path == 'https://banana.by/':
            self.input_field = self.browser.find_element_by_xpath("//*[@id='searchinput']")
        elif search_path == 'https://www.tut.by/':
            self.input_field = self.browser.find_element_by_xpath("//*[@id='search_from_str']")
        else:
            self.input_field = self.browser.find_element_by_xpath("//*[@id='searchInput']")

    def browser_closing(self):
        """Closes browser after search"""
        self.browser.quit()


class TwitterSearcher(object):
    """Class for search in the twitter"""
    logger = logging.getLogger(__name__)
    logfile = "followers.txt.log"

    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.INFO)

    logger.addHandler(screen_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    def __init__(self, browser_name, path_to_file):
        """Creates new session of web driver connection"""
        self.browser = None
        self.browser_name = browser_name
        self.path_to_driver = path_to_file
        self.input_field = None
        self.select_of_browser()

    def select_of_browser(self):
        """Selects which browser will in use"""
        self.browser = webdriver.Firefox(executable_path=self.path_to_driver)
        if self.browser_name == 'Chrome':
            self.browser = webdriver.Chrome(executable_path=self.path_to_driver)

    def solodukha_twitter(self, search_path):
        """Opens Solodukha's page on Twitter"""
        start_time = time.strftime('%x %X %p')
        self.browser.get(search_path)
        self.browser.implicitly_wait(30)
        quantity_element = \
            self.browser.find_element_by_xpath(
                "/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]")
        quantity = quantity_element.get_attribute('data-count')
        self.browser.quit()
        self.logger.debug("[{} - {} - {}]".format(start_time, self.browser_name, quantity))


if __name__ == '__main__':
    new = Configurator()
    search = Searcher(new.new_browser, new.exec_path)
    for element in new.search_path:
        search.solodukha_search(element)
    time.sleep(2)
    search.browser_closing()
    twitter = TwitterSearcher(new.new_browser, new.exec_path)
    twitter.solodukha_twitter(new.twitter_path)
