from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
from selenium import webdriver


from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.common.exceptions import NoSuchElementException
import os
import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

app=FastAPI()

class Item(BaseModel):
    user: str
    passw: str
    hasht: str
@app.put("/hey")
async def instag(item: Item):
    recieved=item.dict()
    driver =  webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get('https://instagram.com/')
    err=self.driver.find_element_by_xpath('//*[@class="_2Lks6"]').text
    return {err}