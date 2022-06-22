import random


def unknown():
    response = ["Bisa mohon ulangi? ",
                "Terdengar benar.",
                "Maksud anda apa ya?"][
        random.randrange(3)]
    return response


output = ['Hello', 'Oke dadah!', 'Saya baik, anda?',
          'Maaf mendengarkan itu', 'Ah syukurlah']
input = [['hello', 'hi', 'hey'], ['Dadah', 'goodbye'], [
    'bagaimana', 'kabarnya'], ['tidak', 'baik'], ['baik']]
declare = [True, True, ['bagaimana'], ['tidak', 'baik'], ['baik']]
