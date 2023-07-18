import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import navigation.constants as const
import getpass


class Navigation(webdriver.Firefox):
    def __init__(self, driver_path=const.GECKODRIVER_PATH,
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.FirefoxOptions()
        super(Navigation, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def router_login(self):
        username = input("input router username: ")
        password = getpass.getpass("Enter router password: ")
        router_login = "http://" + username + ":" + password + "@192.168.1.1/"
        self.get(router_login)
        print("Login success")

    def access_router_backup_menu(self):
        self.get(const.ROUTER_BACKUP_URL)

    def router_save_conf(self):
        self.find_element(By.ID, "backup").click()

    def switch_login(self):
        self.get(const.SWITCH_URL)
        self.input_login_1()

    def input_login_1(self):
        login_element_0 = self.find_element(By.ID, "password")
        login_element_1 = self.find_element(By.ID, "loginBtn")
        switch_pas = getpass.getpass("Enter Password: ")
        login_element_0.send_keys(switch_pas)
        login_element_1.click()

    def access_maintenance_tab(self):
        menu_bar_element_0 = self.find_element(By.XPATH,
            '//*[@id="System_Maintenance"]'
        )
        menu_bar_element_0.click()

    def access_maintenance_menu(self):
        menu_column_element_0 = self.find_element(By.NAME,
            "lv5"
        )
        menu_column_element_0.click()

    def save_conf(self):
        save_conf_button = self.find_element(By.ID,
            "btn_Save"
        )
        save_conf_button.click()
