from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import os
from time import sleep
from .models import Tarifa


class TestUser(StaticLiveServerTestCase):

    # construtor da conexao
    @classmethod
    def setUpClass(cls):
        # criando database de teste
        Tarifa.objects.create(DDD_origem='011', DDD_destino='016', preco_por_minuto=1.90)
        Tarifa.objects.create(DDD_origem='016', DDD_destino='011', preco_por_minuto=2.90)
        Tarifa.objects.create(DDD_origem='011', DDD_destino='017', preco_por_minuto=1.70)
        Tarifa.objects.create(DDD_origem='017', DDD_destino='011', preco_por_minuto=2.70)
        Tarifa.objects.create(DDD_origem='011', DDD_destino='018', preco_por_minuto=0.90)
        Tarifa.objects.create(DDD_origem='018', DDD_destino='011', preco_por_minuto=1.90)

        super().setUpClass()
        # Chrome Driver init
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
        # preenchimento e formulario
        self.selenium.get('%s%s' % (self.live_server_url, '/consultar_ligacao/'))
        ddd_origem = self.selenium.find_element_by_name("DDD_origem")
        ddd_origem.send_keys('011')
        ddd_destino = self.selenium.find_element_by_name('DDD_destino')
        ddd_destino.send_keys('017')
        tempo = self.selenium.find_element_by_name('tempo')
        tempo.send_keys('80')
        plano = self.selenium.find_element_by_name('plano_falemais')
        plano.send_keys('FaleMais 60')
        # click de botao de consulta
        self.selenium.find_element_by_xpath('/html/body/form/button').click()

        sleep(2)
        
        try:
            preco = self.selenium.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[5]').text
            self.assertEqual(preco, '37.40')
        except:
            self.fail()

    def test_valid_call_zero(self):
        """
        confere se o formulario retorna valor nulo quando o tempo de chamada e menor que o tempo do Plano FaleMais
        """
        # preenchimento de formulario
        self.selenium.get('%s%s' % (self.live_server_url, '/consultar_ligacao/'))
        ddd_origem = self.selenium.find_element_by_name("DDD_origem")
        ddd_origem.send_keys('011')
        ddd_destino = self.selenium.find_element_by_name('DDD_destino')
        ddd_destino.send_keys('017')
        tempo = self.selenium.find_element_by_name('tempo')
        tempo.send_keys('80')
        plano = self.selenium.find_element_by_name('plano_falemais')
        plano.send_keys('FaleMais 120')
        # click de botao de consulta
        self.selenium.find_element_by_xpath('/html/body/form/button').click()

        sleep(2)

        try:
            preco = self.selenium.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[5]').text
            self.assertEqual(preco, '0.00')
        except:
            self.fail()

    def test_invalid_call_same_ddd(self):
        """
        confere se o formulario retorna consulta invalida para valores iguais de DDD
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultar_ligacao/'))
        # preenchimento do formulario
        ddd_origem = self.selenium.find_element_by_name("DDD_origem")
        ddd_origem.send_keys('017')
        ddd_destino = self.selenium.find_element_by_name('DDD_destino')
        ddd_destino.send_keys('017')
        tempo = self.selenium.find_element_by_name('tempo')
        tempo.send_keys('80')
        plano = self.selenium.find_element_by_name('plano_falemais')
        plano.send_keys('FaleMais 60')
        # click de botao
        self.selenium.find_element_by_xpath('/html/body/form/button').click()

        try:
            consulta_invalida = self.selenium.find_element_by_xpath('/html/body/div/h2').text
            self.assertEqual(consulta_invalida, 'Consulta Invalida')
        except:
            self.fail()


    def test_invalid_call_no_capital(self):
        """
        confere se o formulario retorna consulta invalida para uma operacao tal que nem a origem e destino sao 011
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/consultar_ligacao/'))
        # preenchimento do formulario
        ddd_origem = self.selenium.find_element_by_name("DDD_origem")
        ddd_origem.send_keys('017')
        ddd_destino = self.selenium.find_element_by_name('DDD_destino')
        ddd_destino.send_keys('018')
        tempo = self.selenium.find_element_by_name('tempo')
        tempo.send_keys('80')
        plano = self.selenium.find_element_by_name('plano_falemais')
        plano.send_keys('FaleMais 60')
        # click de botao
        self.selenium.find_element_by_xpath('/html/body/form/button').click()

        try:
            consulta_invalida = self.selenium.find_element_by_xpath('/html/body/div/h2').text
            self.assertEqual(consulta_invalida, 'Consulta Invalida')
        except:
            self.fail()
