from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os
from time import sleep


class MySeleniumTests(StaticLiveServerTestCase):

    # construtor da conexao
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        driver = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + '/chromedriver_win32 (1)/chromedriver.exe')
        cls.selenium = driver
        cls.selenium.implicitly_wait(10)

    # destrutor da conexao
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_valid_call(self):
        """
        confere se o formulario esta calculando corretamente dado umconjunto valido de DDD's
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultar_ligacao/'))
        ddd_origem = self.selenium.find_element_by_name("DDD_origem")
        ddd_origem.send_keys('016')
        sleep(2)
        ddd_destino = self.selenium.find_element_by_name('DDD_destino')
        ddd_destino.send_keys('011')
        sleep(2)
        tempo = self.selenium.find_element_by_name('tempo')
        tempo.send_keys('80')
        sleep(2)
        plano = self.selenium.find_element_by_name('plano_falemais')
        plano.send_keys('FaleMais 60')
        sleep(2)
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        
        sleep(2)

        """preco = self.selenium.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[5]').get_attribute('value')
        print(preco)"""
