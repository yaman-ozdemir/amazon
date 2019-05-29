from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome('/home/yaman/PycharmProjects/untitled/venv/chromedriver')
browser.maximize_window()

#we should use webriver wait for all elements instead of browser.find_element.

#1. www.amazon.com sitesine gelecek ve anasayfanın açıldığını onaylayacak,
browser.get("https://www.amazon.com/")
webPageTitle = "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
assert browser.title in webPageTitle
print("You are on Amazon.com")

#2. Login ekranını açıp, bir kullanıcı ile login olacak,

# Let's use id instead of css selector
browser.find_element_by_css_selector("#nav-link-accountList").click()
browser.find_element_by_css_selector("#ap_email").send_keys("tezt1zs@gmail.com")
browser.find_element_by_css_selector("#ap_password").send_keys("112233445566")
browser.find_element_by_css_selector("#signInSubmit").click()

#3.Ekranın üstündeki Search alanına 'samsung' yazıp Ara butonuna tıklayacak
browser.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Samsung")
browser.find_element_by_css_selector(".nav-input").click()

#4. Gelen sayfada samsung icin sonuç bulunduğunu onaylayacak,
searchKeyword = browser.find_element_by_css_selector("#twotabsearchtextbox").text
searchKeywordResult = browser.find_element_by_css_selector(".a-color-state").text
assert searchKeyword in searchKeywordResult
print("Samsung Search Result")

#5.Arama sonuclarindan 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanın şu an gösterimde olduğunu onaylayacak,

# Shorter selector please
browser.find_element_by_css_selector(".a-pagination > li:nth-child(3)").click()
assert "2" in browser.find_element_by_css_selector(".a-selected").text
print("You are looking into Second Page")

#6.Üstten 3. ürünün içindeki 'Add to List' butonuna tıklayacak,
browser.find_element_by_css_selector("div[data-index='2'] .a-size-medium").click()
productName = browser.find_element_by_css_selector("#productTitle").text
browser.find_element_by_css_selector("#add-to-wishlist-button-submit").click()
time.sleep(2)
browser.find_element_by_css_selector(".a-icon-close").click()
time.sleep(2)

#7. Ekranın en üstündeki 'List' linkine tıklayacak içerisinden Wish listi seçecek,
wishListMenu = browser.find_element_by_css_selector(".nav-truncate")
hover = ActionChains(browser).move_to_element(wishListMenu)
hover.perform()
time.sleep(1)
#too looooong (try to use text link)
browser.find_element_by_css_selector("#nav-flyout-wl-items > div > a:nth-child(1) > span").click()

#8. Açılan sayfada bir önceki sayfada izlemeye alınmış ürünün bulunduğunu onaylayacak,
wishListProductName = browser.find_element_by_css_selector("h3.a-size-base").text
assert productName in wishListProductName
print("Product has found in Wish List")

#9. Favorilere alınan bu ürünün yanındaki 'Delete' butonuna basarak, favorilerimden çıkaracak,
browser.find_element_by_link_text("Delete item").click()
time.sleep(2)

#10. Sayfada bu ürünün artık favorilere alınmadığını onaylayacak.

#selector is too long
#take icon element and assert is_displayed()
deleteConfirmText = browser.find_element_by_css_selector(".a-row.a-spacing-none:nth-of-type(1)").text
assert deleteConfirmText in wishListProductName
print("Product deleted!")

time.sleep(1)
browser.quit()
