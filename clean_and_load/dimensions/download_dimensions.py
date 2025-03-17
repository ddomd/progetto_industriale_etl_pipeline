from download_operations.download import download_list
from dimensions.parse_dimensions import parse_codelist


def download_dimensions(dimensions):
    url_list = [
        f"https://esploradati.istat.it/SDMXWS/rest/codelist/IT1/{code}"
        for code in dimensions
    ]

    codelist = download_list(url_list)

    return parse_codelist(codelist)
