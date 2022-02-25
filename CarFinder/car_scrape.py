import requests, re, time
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/75.0.3770.80 Safari/537.36"
}

make = "toyota"
model = "rav4"
zip = # zipcode :D
state = "state abbreviation"
city = "city"
maxPrice = 14500
maxMileage = 130000
awd_4wd = True
radius=100
minYear = 2009
maxYear = 2012

if awd_4wd == True:
    usedcars_drive = "awd-4wd/"
else:
    usedcars_drive = ""


usedcars_url = "https://www.usedcars.com/buy/make-"+make+"/model-"+model+"/state-"+state.upper()+"/city-"+(city[0].upper()+city[1:].lower())+"/zipcode-"+str(zip)+"/priceMax-"+str(maxPrice)+"/driveTypes-"+str(usedcars_drive)+"/includeNationalDeliveryPrograms-false/mileageMax-"+str(maxMileage)+"/pageSize-1000/radius-"+str(radius)+"/sortBy-Lowest_price/yearMax-"+str(maxYear)+"/yearMin-"+str(minYear)
auto_url = "https://www.autotrader.com/cars-for-sale/all-cars/"+usedcars_drive+make+"/"+model+"/"+city+"-"+state+"-"+str(zip)+"?dma=&maxMileage="+str(maxMileage)+"&vhrTypes=NO_ACCIDENTS&searchRadius="+str(radius)+"&location=&maxPrice="+str(maxPrice)+"&marketExtension=include&startYear="+str(minYear)+"&endYear="+str(maxYear)+"&isNewSearch=false&showAccelerateBanner=false&sortBy=derivedpriceASC&numRecords=1000"

print(usedcars_url)
print(auto_url)
