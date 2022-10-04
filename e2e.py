from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




def test_scores_service(url):
    my_drive = webdriver.Chrome(ChromeDriverManager().install())
    my_drive.get(url)
    WebDriverWait(my_drive, 15).until(
        EC.element_to_be_clickable(
            (By.ID, "score")))
    score = my_drive.find_element(By.ID, "score").text
    sleep(3)
    try:
        if 0 < int(score) < 1001:
            return True
        else:
            return False
    except:
        return False


def main_function():
    result = test_scores_service("http://127.0.0.1:8777")
    if result is True:
        return 0
    if result is False:
        return -1


print(main_function())
