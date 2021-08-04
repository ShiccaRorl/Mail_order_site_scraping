from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

##Html Elementのハイライト
def hhlight(element):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("background: white; border: 1px solid blue;")
    time.sleep(.3)
    apply_style(original_style)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) 
    driver.set_page_load_timeout(5)
    driver.set_script_timeout(5)
    driver.get('https://www.google.com/')

    ## こんな感じに、要素を検索して、作った関数に要素を渡すと指定したCSSが適用されて、
    ## どの要素が選択されているのかわかるようになります
    search_box = driver.find_element_by_name("q")
    hhlight(search_box)