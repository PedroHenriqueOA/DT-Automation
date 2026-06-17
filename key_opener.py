from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


# ------------VARIABLES-------------------
dt_user = "05855880583"
dt_pass = "DT123@"
cliente = "Shopee LTDA"
site = "HUB-LSP-60"
chave = ""
coordenador = ""
time = ""


# -----------------------DT LOGIN    ----------------------------------
driver.get("https://tsi-app.com/planejamento-operacional_1")
driver.implicitly_wait(1000)
driver.find_element(By.ID, "username").send_keys(dt_user)
driver.find_element(By.ID, "password").send_keys(dt_pass)
driver.find_element(By.NAME, "send").click()

# ---------------------OPEN NOVO PLANEJAMENTO-----------------------------
driver.get("https://tsi-app.com/planejamento-operacional_1")
driver.implicitly_wait(1000)

driver.find_element(
    By.XPATH, "/html/body/div[2]/section/div/div[1]/div/div[1]/a"
).click()
driver.implicitly_wait(1000)
# ---------------------------Fill First Form--------------------------------------
# ------ Preenche o campo de client-------
driver.switch_to.frame(10)
btn_cliente = cliente_button = driver.find_element(
    By.CSS_SELECTOR, "[data-id='cliente_plan']"
)

btn_cliente.click()
btn_cliente.click()

driver.implicitly_wait(1000)
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[1]/div/div/div/div/div/input"
).send_keys(cliente)
driver.implicitly_wait(1000)
driver.find_element(By.CSS_SELECTOR, ".active > a:nth-child(1)").click()
# -----------------IFRAME TEST------------------------------
# iframes = driver.find_elements(By.TAG_NAME, "iframe")
# print(f"IFRAMES: {len(iframes)}")

# for i, iframe in enumerate(iframes):
#     print(i, iframe.get_attribute("src"))
# -----------------IFRAME TEST------------------------------

# ------- Preenche o campo de site-----------------
btn_site = cliente_button = driver.find_element(
    By.CSS_SELECTOR, "[data-id='site_plan']"
)

btn_site.click()
# btn_site.click()

driver.implicitly_wait(1000)
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[2]/div/div/div/div/div/input"
).send_keys(site)
driver.implicitly_wait(1000)
driver.find_element(By.CSS_SELECTOR, ".active: > a:nth-child(1)").click()


driver.quit
