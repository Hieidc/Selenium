from tabnanny import check
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
# navegar até o site
driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(1)
driver.execute_script("window.scrollTo(0, 1500);")
sleep(1)
# Desafio 1
carros = driver.find_elements(By.XPATH, "//input[@name='carros']")
carros[1].click()
carros[3].click()
carros[4].click()
sleep(3)
# Desafio 2
motos = driver.find_elements(By.XPATH, "//input[@name='motos']")
for moto in motos:
    moto.click()
sleep(3)

input('')
driver.close()