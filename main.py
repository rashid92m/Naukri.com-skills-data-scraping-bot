from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# nukri_url = input("Enter Choice  : 1-updateProfile, 2-fetch skill from URL")
nukri_url = input('Enter URL : ')
raw_css_Article = '#root > div.search-result-container > div.content > section.listContainer.fleft > div.list > article'
raw_xpath_ul_skills = '/html/body/div[1]/div[3]/div[2]/section[2]/div[2]/article[1]/ul/li[1]'
raw_xpath_jobtitle = '/html/body/div[1]/div[3]/div[2]/section[2]/div[2]/article[11]/div[1]/div[1]/a'
path = r'C:\Users\Rashid mohammad\Documents\PYTHON DEVELOPMENT\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(url=nukri_url)
driver.maximize_window()
skillsList =[]

xpath_nextButton = '/html/body/div[1]/div[3]/div[2]/section[2]/div[3]/a[2]'
skillsDict = {}
def CountArticle():
    # MaxJobCount = len(driver.find_elements_by_css_selector(raw_css_Article))
    # print(f"article count on this page = {MaxJobCount}")
    return 12


def freq():
    # gives set of unique words
    unique_words = set(skillsList)

    for words in unique_words:
        skillsDict[words] = skillsList.count(words)
    sorted_dict = {}
    sorted_keys = sorted(skillsDict, key=skillsDict.get)  # [1, 3, 2]

    for w in sorted_keys:

        sorted_dict[w] = skillsDict[w]

    print(sorted_dict)

def collectSkillofCurrentPage():
    maxlimit = CountArticle()
    for i in range(1,maxlimit+1):
        xpath_ul_skills = f'/html/body/div[1]/div[3]/div[2]/section[2]/div[2]/article[{i}]/ul'
        ul_skills = driver.find_element_by_xpath(xpath_ul_skills)
        skills_items = ul_skills.find_elements_by_tag_name("li")
        for item in skills_items:
            skillsList.append(item.text)
def clickNext():
    # driver.execute_script("window.scrollTo(0, 5000)")
    time.sleep(1)
    driver.find_element_by_xpath(xpath_nextButton).click()

for i in range (0,10):
    driver.implicitly_wait(15)  # seconds
    collectSkillofCurrentPage()
    clickNext()

freq()
driver.quit()


