import logging
from time import sleep

import requests

logging.getLogger().setLevel(logging.INFO)

INTERVALO_DE_TEMPO = 1

def verificar_temperatura():
    while True:
        logging.info("Checando temperatura....")

        try:
            temperatura = requests.get("http://localhost:5006/temperatura").json()

            if len(temperatura) == 0:
                logging.info("Não tem medicões de temperatura ainda...")
                sleep(INTERVALO_DE_TEMPO)
                continue

            temperatura_interna = temperatura[0]["temperatura_interna"]

            if temperatura_interna > 60:
                logging.warning(
                    f"Possível incêndio a temperatura é de {temperatura_interna}"
                    "graus, chame os bombeiros! #socorro"
                )
            else:
                logging.info(
                    f"Tudo ok a temperatura é de {temperatura_interna}"
                    " graus, vida que segue... #paz"
                )
        except Exception as err:
            logging.warning(f"Erro: {err}")

        sleep(INTERVALO_DE_TEMPO)

if __name__ == "__main__":
    verificar_temperatura()
