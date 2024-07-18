from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class GoogleFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, form_data):
    	name, contact_number, email, address, pin_code, dob, gender = form_data
    	width = self.driver.execute_script("return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth );")
    	height = self.driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    	
    	# Set the window size to match the entire webpage
    	self.driver.set_window_size(width, height)
    	# Find the full page element (usually 'body') and capture the screenshot
    	full_page = self.driver.find_element(By.TAG_NAME, "body")
    	full_page.screenshot("screenshots/before_filling.png")
    	#self.driver.save_screenshot('before_filling.png')
    	
    	full_name = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i1']")
    	contact_number_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i5']")
    	email_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i9']")
    	full_address_field = self.driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i13']")
    	pin_code_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i17']")
    	dob_field = self.driver.find_element(By.XPATH, "//input[@type='date']")
    	gender_field = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i26']")
    	captcha = self.driver.find_element(By.XPATH, "//input[@aria-labelledby='i30']")
    	
    	print("----------------pass--------------")
    	
    	full_name.send_keys(name)
    	contact_number_field.send_keys(contact_number)
    	email_field.send_keys(email)
    	full_address_field.send_keys(address)
    	pin_code_field.send_keys(pin_code)
    	dob_field.send_keys(dob)
    	gender_field.send_keys(gender)
    	captcha.send_keys("GNFPYC")
    	
    	full_page = self.driver.find_element(By.TAG_NAME, "body")
    	full_page.screenshot("screenshots/after_filling.png")
    	#self.driver.save_screenshot('after_filling.png')
    	
    	#time.sleep(3)
    	submit_button = self.driver.find_element(By.XPATH, "//div[@aria-label='Submit']")
    	submit_button.click()
    	
    	full_page = self.driver.find_element(By.TAG_NAME, "body")
    	full_page.screenshot("screenshots/after_submitting.png")
    	#self.driver.save_screenshot('after_submitting.png')

def test_submit_google_form(form_data):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Use headless mode for running in the background
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    gform = GoogleFormPage(driver)
    gform.open()
    #time.sleep(5)
    gform.fill_form(form_data)
    #time.sleep(2)
    driver.quit()

if __name__ == "__main__":
	form_data = ("John Doe", "1234567890", "john.doe@example.com", "123 Main St, City, Country", "123456", "24-01-1990", "Male")
	#a=time.time()
	test_submit_google_form(form_data)
	#time.time()-a
