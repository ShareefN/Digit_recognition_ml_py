from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from time import sleep
import requests

# https://towardsdatascience.com/how-to-build-a-dataset-for-an-image-classifier-from-scratch-d2506e30468d

url_toscrap = "https://turo.com/ca/en-us/car-rental/montreal-qc/ford/mustang/702436?searchId=OD83L624"

# Define the driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Access the url of the page to scrap
driver.get(url_toscrap)

# Collect all the informations on the page
source_data = driver.page_source
soup = bs(source_data, features="html.parser")

# collect the number of pictures
extract_nbrpictures = soup.find("div", {"class": "fullScreenCarousel-count"})
if extract_nbrpictures != None:
    zoom_picturecarousel = extract_nbrpictures.text
    count_pictures = int(zoom_picturecarousel.split("of")[1].replace(" ", ""))
    print(f"There is {count_pictures} pictures on this offer")
    # For each picture
    for i in range(count_pictures):
        # Scroll on the carousel
        python_button = driver.find_elements_by_xpath(
            "//i[@class='fullScreenCarousel-navigation--next']")[0]
        python_button.click()

        source_data = driver.page_source
        soup = bs(source_data, features="html.parser")

        details_picture = soup.find(
            'img', {'class': 'vehicleCarouselImage-image'}, src=True)

        if(details_picture['src']):
            link_picture = details_picture["src"]
            print(f'Image Link: {link_picture}')

            response = get('https://d1zgdcrdir5wgt.cloudfront.net/media/vehicle/images/cfdc_Ig-RVGMr0XISzdR_w.1440x700.jpg')
            if response.ok:
                img_data = response.content
            # Save the picture in a file (picturei.jpg)
            with open(f"picture{i}.jpg", 'wb') as file:
                file.write(img_data)


sleep(2)

# Stop the driver
driver.close()
