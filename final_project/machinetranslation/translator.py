""" This module is used to translate text from english to french and from french to english"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# french_text = json.dumps(translate, indent=2, ensure_ascii=False)
def english_to_french(english_text):
    """ This method translates english text to french"""
    translate = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    my_list = []
    for i in translate.values():
        my_list.append(i)
    french_text = my_list[0][0]['translation']
    return french_text

def french_to_english(french_text):
    """This method translates french text to english"""
    translate = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    my_list = []
    for i in translate.values():
        my_list.append(i)
    english_text = my_list[0][0]['translation']
    return english_text
