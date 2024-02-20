from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho para o WebDriver. Substitua 'your_webdriver_path' pelo caminho do seu WebDriver.
webdriver_path = 'your_webdriver_path'
driver = webdriver.Chrome(webdriver_path)

try:
    # Substitua 'your_notion_page_url' pela URL da página do Notion que você deseja automatizar.
    driver.get('your_notion_page_url')
    
    # Exemplo: Esperar até que o título da página seja carregado
    WebDriverWait(driver, 10).until(
        EC.title_contains("Notion")
    )

    # Aqui você adicionaria mais interações com a página
    print("Página do Notion carregada com sucesso!")
    
finally:
    # Fechar o navegador após a execução
    driver.quit()
