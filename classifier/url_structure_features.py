from static_data import SECTIONS, SYMBOL_NAME_TO_SYMBOL

def extract_quantity_features(extracted_sections):
    qty_features = {}
    for section_name, section in zip(SECTIONS, extracted_sections): 
        for symbol_name, symbol in SYMBOL_NAME_TO_SYMBOL.items():
            qty_features[f"qty_{symbol_name}_{section_name}"] = section.count(symbol)
    return qty_features

def extract_section_length_features(extracted_sections):
    length_features = {}
    for section_name, section in zip(SECTIONS, extracted_sections):
        length_features[f"{section_name}_length"] = len(section)
    return length_features
        
def extract_length_url_feature(url):
    return {"length_url": len(url)}