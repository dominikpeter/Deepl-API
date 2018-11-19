
# coding: utf-8

import requests
import time
from random import randint
from requests.exceptions import ConnectionError, HTTPError


def timestamp():
    return int(round(time.time() * 1000))


def random_with_N_digits(n):
    range_start = 10**(n - 1)
    range_end = (10**n) - 1
    random_number = randint(range_start,
                            range_end)
    return random_number


class DeeplObject():
    def __init__(self,
                 sentence,
                 lang,
                 target_lang,
                 translation,
                 log_proba):
        self.sentence = sentence
        self.translation = translation
        self.log_proba = log_proba
        self.lang = lang
        self.target_lang = lang

    def __str__(self):
        return "[DeeplObject; Sentence: {}, Translation: {}]".format(
            self.sentence, self.translation
        )

    def extract(self, log_proba=True):
        if log_proba:
            l = list(zip(self.translation,
                         self.log_proba))
        else:
            l = self.translation
        return l

    def extract_first(self, log_proba=True):
        if log_proba:
            l = (self.translation[0],
                 self.log_proba[0])
        else:
            l = self.translation[0]
        return l


class Deepl():
    def __init__(self, n_trials=10):
        self.headers = {
            'Origin': 'https://www.deepl.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'text/plain',
            'Accept': '*/*',
            'Referer': 'https://www.deepl.com/translator',
            'Connection': 'keep-alive',
        }
        self.url = "https://www2.deepl.com/jsonrpc"
        self.n_errors = 0
        self.n_trials = 10

    def translate(self, sentence, target_lang, lang="auto"):
        if self.n_errors > self.n_trials:
            raise Exception('To many trials')
        else:
            id = random_with_N_digits(8)
            timestamp = timestamp()
            data = {
                "jsonrpc": "2.0",
                "method": "LMT_handle_jobs",
                "params": {"jobs": [
                    {"kind": "default",
                     "raw_en_sentence": sentence,
                     "raw_en_context_before": [],
                     "raw_en_context_after":[],
                     "quality":"fast"}
                ],
                    "lang": {"user_preferred_langs": ["DE", "EN", "FR"],
                             "source_lang_user_selected": lang,
                             "target_lang": target_lang},
                    "priority": -1,
                    "timestamp": timestamp},
                "id": id
            }
            try:
                response = requests.post(self.url,
                                         headers=self.headers,
                                         json=data)
            except (HTTPError, ConnectionError):
                print("Connection Error. Trying one more time...")
                self.n_errors += 1
                return self.translate(sentence, target_lang, lang)

            js = response.json()
            translation_js = js['result']['translations'][0]['beams']
            translation = [i['postprocessed_sentence'] for i in translation_js]
            log_proba = [i['totalLogProb'] for i in translation_js]
            deeplo = DeeplObject(sentence, lang,
                                 target_lang, translation,
                                 log_proba)
        return deeplo
