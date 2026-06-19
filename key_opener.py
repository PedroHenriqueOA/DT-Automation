from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def openKey(site, date_plan, hour_plan, workers_quantity):

    driver = webdriver.Firefox()

    # ------------LOGIN----------------------------
    loginDT(dt_user, dt_pass)

    # ------------VARIABLES---------------------
    dt_user = "05855880583"
    dt_pass = "DT123@"
    cliente = "Shopee LTDA"
    demand1d8 = (
        "/html/body/div[1]/div/div/div/div/form/div[7]/div/div/div/div/ul/li[1]/a"
    )
    demand3d8 = "html body div.margin-5px div.cards-form div.divmargin div#SOLICITACAO div form#new.form.has-validation-callback div.floatLeft.L35 div.input-group.divmargin div.custom-select div.btn-group.bootstrap-select.show-tick.open div.dropdown-menu.open ul.dropdown-menu.inner li a"
    time = ""
    coordenador = ""
    chave = ""

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
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/form/div[1]/div/div/div/div/div/input",
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
    site_input = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div/div/form/div[2]/div/div/div/div/div/input",
    )
    site_input.send_keys(site)
    driver.implicitly_wait(1000)
    site_input.send_keys(Keys.ENTER)

    # ----------------------SKIPPING STUFF--------------------------------------------------------------------------------------

    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()

    # ----------------------------Preenche campo de data------------------------------
    ActionChains(driver).send_keys(date_plan).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    # ----------------------------Preenche campo de hora------------------------------
    ActionChains(driver).send_keys(hour_plan).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    # ----------------------------Preenche campo de quatidade------------------------------
    ActionChains(driver).send_keys(workers_quantity).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    # -----------------------------SUBMIT--------------------------------------------
    driver.find_element(By.ID, "submitF").click()

    # ------------------------NEXT PAGE  --------------------------------------------------
    driver.implicitly_wait(1000)

    # ----------------------Preencher demanda-----------------------------
    driver.find_element(By.CSS_SELECTOR, "[data-id='jornada_plan']").click()
    driver.find_element(By.XPATH, demand1d8).click()
    # -----------------------Confirmações---------------------------
    driver.find_element(By.ID, "p1_confirm_0").click()
    driver.find_element(By.ID, "p2_confirm_0").click()
    # -----------------------------SUBMIT--------------------------------------------
    driver.find_element(By.ID, "submitF").click()
    # -----------------------------Clica no olho--------------------------------------------
    driver.implicitly_wait(1000)
    driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/div/div/div/form/div[2]/div/span[3]/a"
    )
    # ----------------------Confirmar Solicitação--------------------
    driver.implicitly_wait(1000)

    # ActionChains(driver).send_keys(Keys.TAB)

    driver.quit


def loginDT(driver, dt_user, dt_pass):
    driver.get("https://tsi-app.com/planejamento-operacional_1")
    driver.implicitly_wait(1000)
    driver.find_element(By.ID, "username").send_keys(dt_user)
    driver.find_element(By.ID, "password").send_keys(dt_pass)
    driver.find_element(By.NAME, "send").click()
