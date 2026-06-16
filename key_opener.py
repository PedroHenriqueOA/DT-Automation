from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


# ------------VARIABLES-------------------
dt_user = "05855880583"
dt_pass = "DT123@"
cliente = "Shopee LTDA"
site = ""
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
# ---------------------------Fill First Form--------------------------------------
# Preenche o campo de cliente
driver.implicitly_wait(1000)
cliente_button = driver.find_element(
    By.CSS_SELECTOR,
    "html body div.margin-5px div.cards-form div.divmargin div#SOLICITACAO div form#new.form.has-validation-callback div.floatLeft.L40 div.input-group.divmargin div.custom-select div.btn-group.bootstrap-select.show-tick.open button.btn.dropdown-toggle.bs-placeholder.btn-selectbox",
)
cliente_button.click()
driver.implicitly_wait(1000)
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[1]/div/div/div/div/div/input"
).send_keys(cliente)
