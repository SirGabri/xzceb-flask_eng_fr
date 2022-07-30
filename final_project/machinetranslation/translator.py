"""Necessary modules for the final project """
from gettext import translation
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


#Create the translator instance.
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
#My translator location is London
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    """Returns a string. Translates a english string to french"""
    translation = language_translator.translate(text=english_text, model_id='en-fr')
    dic = translation.result["translations"][0]
    french_text = dic["translation"]
    return french_text


def french_to_english(french_text):
    """Returns a string. Translates a french string to english"""
    translation = language_translator.translate(text=french_text, model_id='fr-en')
    dic = translation.result["translations"][0]
    english_text = dic["translation"]
    return english_text

