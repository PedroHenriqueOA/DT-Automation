from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from whats_automation import sendWppMsg


def loginDT(driver, dt_user, dt_pass):
    driver.get("https://tsi-app.com/planejamento-operacional_1")
    driver.implicitly_wait(1000)
    driver.find_element(By.ID, "username").send_keys(dt_user)
    driver.find_element(By.ID, "password").send_keys(dt_pass)
    driver.find_element(By.NAME, "send").click()


def iframe_test(driver):
    # -----------------IFRAME TEST------------------------------

    from selenium.webdriver.common.by import By


def encontrar_caminho(driver, caminho=[]):
    if driver.find_elements(By.ID, "qtdlider"):
        print("Caminho:", caminho)
        return True

    frames = driver.find_elements(By.TAG_NAME, "iframe")

    for i, frame in enumerate(frames):
        driver.switch_to.frame(frame)

        if encontrar_caminho(driver, caminho + [i]):
            return True

        driver.switch_to.parent_frame()

    return False


# iframes = driver.find_elements(By.TAG_NAME, "iframe")
# print(f"IFRAMES: {len(iframes)}")

# for i, iframe in enumerate(iframes):
#     print(i, iframe.get_attribute("src"))
# -----------------IFRAME TEST------------------------------


def openKey(site, date_plan, hour_plan, workers_quantity, dt_user, dt_pass):

    driver = webdriver.Firefox()

    # ------------LOGIN----------------------------
    loginDT(driver, dt_user, dt_pass)

    # ------------VARIABLES---------------------
    cliente = "Shopee LTDA"
    demand1d8 = (
        "/html/body/div[1]/div/div/div/div/form/div[7]/div/div/div/div/ul/li[1]/a"
    )
    demand3d8 = (
        "/html/body/div[1]/div/div/div/div/form/div[7]/div/div/div/div/ul/li[2]/a"
    )
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
    # ActionChains(driver).send_keys(Keys.TAB).perform()
    # -----------------------------SUBMIT--------------------------------------------
    driver.find_element(By.ID, "submitF").click()

    # ------------------------NEXT PAGE  --------------------------------------------------
    driver.implicitly_wait(1000)

    # ----------------------Preencher demanda-----------------------------
    driver.find_element(By.CSS_SELECTOR, "[data-id='jornada_plan']").click()
    driver.implicitly_wait(1000)
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
    ).click()
    # ----------------------Confirmar Solicitação--------------------
    driver.implicitly_wait(1000)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/a").click()
    driver.implicitly_wait(1000)

    # -----------------------Capturar Informações------------------------

    # chave = driver.find_element(By.ID, "chave_pedido").text
    # time = driver.find_element(By.CSS_SELECTOR, "[data-id='time_pedido']").text
    # coordenador = driver.find_element(By.ID, "coordenador_pedido").text

    # -------------------------Save------------------------------

    # driver.implicitly_wait(1000)
    # driver.find_element(By.ID, "submitF").click()
    # driver.implicitly_wait(1000)

    # ------------------------Inserir Quantidade Advisor------------------------------------

    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div[2]/div/div/div[1]/div/form/div[18]/div[2]/div/table/tbody/tr/td[4]/a[1]",
    ).click()
    driver.implicitly_wait(1000)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(workers_quantity).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # driver.switch_to.frame(6)
    # qtdlider = driver.find_element(By.ID, "qtdlider")
    # # qtdlider.click()
    # qtdlider.send_keys(workers_quantity)
    # driver.find_element(By.ID, "submitF").click()
    # driver.find_element(By.CLASS_NAME, "close").click()
    # --------------------------Gravar Informações------------------------------

    # sendWppMsg("+5575999207767", chave + coordenador + time)
    # driver.quit()
