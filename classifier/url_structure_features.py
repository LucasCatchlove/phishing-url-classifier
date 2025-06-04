from url_parse_utils import split_url_into_sections
from static_data import SYMBOL_NAME_TO_GENERAL_URL_SYMBOL, URL_SECTIONS, SYMBOL_NAME_TO_SYMBOL

def get_quantity_features_by_section(extracted_sections):
    qty_features = {}
    for section_name, section in zip(URL_SECTIONS, extracted_sections): 
        for symbol_name, symbol in SYMBOL_NAME_TO_SYMBOL.items():
            qty_features[f"qty_{symbol_name}_{section_name}"] = section.count(symbol)
    return qty_features

def get_quantity_vowels_by_section(extracted_sections):
    vowels = "aeiouAEIOU"
    vowel_features = {}
    
    for section_name, section in zip(URL_SECTIONS, extracted_sections):
        vowel_count = sum(1 for char in section if char in vowels)
        vowel_features[f"qty_vowels_{section_name}"] = vowel_count
    
    return vowel_features

def get_quantity_features_by_url(url):
    qty_url_features = {}
    for symbol_name, symbol in SYMBOL_NAME_TO_GENERAL_URL_SYMBOL.items(): 
        qty_url_features[f"qty_{symbol_name}_url"] = url.count(symbol)
    return qty_url_features

def get_section_length_features(extracted_sections):
    length_features = {}
    for section_name, section in zip(URL_SECTIONS, extracted_sections):
        length_features[f"{section_name}_length"] = len(section)
    return length_features
        
def extract_length_url_feature(url):
    return {"length_url": len(url)}

def get_structural_features(url) -> dict[str, any]:
    extracted_sections = split_url_into_sections(url)
    length_features = extract_length_url_feature(url)
    quantity_url_features = get_quantity_features_by_url(url)
    quantity_features = get_quantity_features_by_section(extracted_sections)
    quantity_vowel_features = get_quantity_vowels_by_section(extracted_sections)
    section_length_features = get_section_length_features(extracted_sections)
    return length_features | quantity_features | section_length_features | quantity_url_features | quantity_vowel_features