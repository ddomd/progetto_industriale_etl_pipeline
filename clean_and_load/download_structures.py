from typing import Set
import requests
import xml.etree.ElementTree as ET


def get_structure(datastructure: str) -> Set[str]:

    dimensions = set()

    response = requests.get(
        f"https://esploradati.istat.it/SDMXWS/rest/datastructure/IT1/{datastructure}",
    )

    # Apro il file dove ho salvato la chiamata XML e setto un puntatore al primo livello dei tag XML
    root = ET.fromstring(response.text)

    # sono i namespace di SDMXML che servono per scorrere il file ricevuto
    namespaces = {
        "structure": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
        "common": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common",
    }

    # Cerca nel file XML tutti i tag che contengono <structure:Dimension> e li salva in un array
    matching_elements = root.findall(".//structure:Dimension", namespaces)

    # cicla tutti i tag salvati
    for elem in matching_elements:
        enumeration = elem.find(".//structure:Enumeration", namespaces)

        # controlla che la lista non sia vuota
        if enumeration is not None:
            ref = enumeration.find(".//Ref", namespaces)

            if ref is not None:
                id = ref.get("id")

                if id != "CL_CORREZ":
                    dimensions.add(id)

    return dimensions
