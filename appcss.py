from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR','--windows-size=800,600','--incognito']

    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'G:\\Storega\\Repositorio_Selenium',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app')

# tag(section,div,h4,button)
# class(.btn)
# combinação de class(.btn.btn-success)
# Id (#dropDownMenuButton)

# Para encontrar valores exatos
# input[class='form-check-input']
# Inicia com algum valor
# input[class^='form']
# finaliza com algum valor
# input[class$='input']
# Contem algum valor
# input[class*='check']

elemento_h2 = driver.find_element(By.CSS_SELECTOR,'h2')
elementos_form_chec = driver.find_element(By.CSS_SELECTOR,'input[class="form-check-input"]')

input('')
driver.close()