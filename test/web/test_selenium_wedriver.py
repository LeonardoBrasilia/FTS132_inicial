# 1 Importar Bibliotecas
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest


# 2 Classe
class Test_Selenium_Webdriver():

    # Definição de Início - Executa antes do teste
    def setup_method(self, method):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome(
            'C:/Users/corre/PycharmProjects/fts132_inicial/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O Selenium vai esperar até 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegador

    # Definição de Fim - Executa depois do teste
    def teardown_method(self, method):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    @pytest.mark.parametrize('termo, curso, preco', [
        ('mantis', 'Mantis', 'R$ 59,99'),
        ('ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])
    def testar_comprar_curso_mantis_com_click_na_lupa(self, termo, curso, preco):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        # O Selenium clica no botão da lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
    # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O Selenium pressiona a tecla Enter
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
        # O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'


