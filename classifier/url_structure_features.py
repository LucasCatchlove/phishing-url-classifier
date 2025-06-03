from url_parse_utils import split_url_into_sections
from static_data import URL_SECTIONS, SYMBOL_NAME_TO_SYMBOL

def get_quantity_features(extracted_sections):
    qty_features = {}
    for section_name, section in zip(URL_SECTIONS, extracted_sections): 
        for symbol_name, symbol in SYMBOL_NAME_TO_SYMBOL.items():
            qty_features[f"qty_{symbol_name}_{section_name}"] = section.count(symbol)
    return qty_features

def get_section_length_features(extracted_sections):
    length_features = {}
    for section_name, section in zip(URL_SECTIONS, extracted_sections):
        length_features[f"{section_name}_length"] = len(section)
    return length_features
        
def extract_length_url_feature(url):
    return {"length_url": len(url)}

def get_structural_features(url):
    extracted_sections = split_url_into_sections(url)
    extract_length_url_feature(url) | get_quantity_features(extracted_sections) | get_section_length_features(extracted_sections)