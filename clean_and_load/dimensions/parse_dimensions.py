from typing import List
import pandas as pd
import xml.etree.ElementTree as ET


def parse_code(codelist: str):
    codes = {}
    # Apro il file dove ho salvato la chiamata XML e setto un puntatore al primo livello dei tag XML
    root = ET.fromstring(codelist)

    # sono i namespace di SDMXML che servono per scorrere il file ricevuto
    namespaces = {
        "structure": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
        "common": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common",
        "xml": "http://www.w3.org/XML/1998/namespace",
    }

    # Cerca nel file XML tutti i tag che contengono <structure:Dataflow> e li salva in un array
    matching_elements = root.findall(".//structure:Code", namespaces)

    # cicla tutti i tag salvati
    for elem in matching_elements:
        # mi salvo per ognuno l'id in una variabile perche' corrispondono ai dataflow da cui dovremmo poi estrarre i dati
        id_attr = elem.get("id")

        # gli specifico di aggiungere i dati all'oggetto codelist solo se l'id che mi ero salvato contiene
        # la stringa 122_54 perche' e' la sequenza che corrisponde alla sezione sul turismo
        name_elem = elem.find(f'common:Name[@xml:lang="it"]', namespaces).text

        # salvo nell'oggetto quello che ho trovato in forma id - nome del dataflow
        if name_elem is not None:
            codes[id_attr] = name_elem

    series = pd.Series(codes)
    df = series.reset_index()
    df.columns = ["id", "nome"]
    return df


def parse_codelist(codelist: List[str]) -> List[pd.DataFrame]:
    codes = []

    for code in codelist:
        codes.append(parse_code(code))

    return codes
