URL_SECTIONS = ["domain", "directory", "file", "parameters", "url"]

SYMBOL_NAME_TO_SYMBOL = {
    'and': '&',
    'asterisk': '*',
    'at': '@',
    'comma': ',',
    'dollar': '$',
    'dot': '.',
    'equal': '=',
    'exclamation': '!',
    'hashtag': '#',
    'hyphen': '-',
    'percent': '%',
    'plus': '+',
    'questionmark': '?',
    'slash': '/',
    'space': ' ',
    'tilde': '~',
    'underline': '_'
}

SYMBOL_NAME_TO_GENERAL_URL_SYMBOL = {
    'dot': '.',
    'hyphen': '-',
    'percent': '%',
    'slash': '/',
    'underline': '_'
}


FEATURE_LIST = [
    "qty_dot_url",
    "qty_hyphen_url",
    "qty_underline_url",
    "qty_slash_url",
    "qty_percent_url",
    # "qty_tld_url",
    "length_url",
    "qty_dot_domain",
    "qty_hyphen_domain",
    "qty_vowels_domain",
    "domain_length",
    "qty_dot_directory",
    "qty_hyphen_directory",
    "qty_underline_directory",
    "qty_slash_directory",
    "qty_questionmark_directory",
    "qty_equal_directory",
    "qty_at_directory",
    "qty_and_directory",
    "qty_exclamation_directory",
    "qty_space_directory",
    "qty_tilde_directory",
    "qty_comma_directory",
    "qty_plus_directory",
    "qty_asterisk_directory",
    "qty_hashtag_directory",
    "qty_dollar_directory",
    "qty_percent_directory",
    "directory_length",
    "qty_dot_file",
    "qty_hyphen_file",
    "qty_underline_file",
    "qty_slash_file",
    "qty_questionmark_file",
    "qty_equal_file",
    "qty_at_file",
    "qty_and_file",
    "qty_exclamation_file",
    "qty_space_file",
    "qty_tilde_file",
    "qty_comma_file",
    "qty_plus_file",
    "qty_asterisk_file",
    "qty_hashtag_file",
    "qty_dollar_file",
    "qty_percent_file",
    "file_length",
    "time_response",
    # "domain_spf",
    "asn_ip",
    "time_domain_activation",
    "time_domain_expiration",
    "qty_ip_resolved",
    "qty_nameservers",
    "qty_mx_servers",
    "ttl_hostname",
    "tls_ssl_certificate",
    "qty_redirects",
]


#might not need these, but worth keeping given the effort put into compiling them

# #features labels
# # Attributes based on the whole URL properties (Table 1)
# url_properties_attributes = [
#     "qty_dot_url",
#     "qty_hyphen_url",
#     "qty_underline_url",
#     "qty_slash_url",
#     "qty_questionmark_url",
#     "qty_equal_url",
#     "qty_at_url",
#     "qty_and_url",
#     "qty_exclamation_url",
#     "qty_space_url",
#     "qty_tilde_url",
#     "qty_comma_url",
#     "qty_plus_url",
#     "qty_asterisk_url",
#     "qty_hashtag_url",
#     "qty_dollar_url",
#     "qty_percent_url",
#     "qty_tld_url",
#     "length_url",
#     "email_in_url",
# ]

# # Attributes based on the domain properties (Table 2)
# domain_properties_attributes = [
#     "qty_dot_domain",
#     "qty_hyphen_domain",
#     "qty_underline_domain",
#     "qty_slash_domain",
#     "qty_questionmark_domain",
#     "qty_equal_domain",
#     "qty_at_domain",
#     "qty_and_domain",
#     "qty_exclamation_domain",
#     "qty_space_domain",
#     "qty_tilde_domain",
#     "qty_comma_domain",
#     "qty_plus_domain",
#     "qty_asterisk_domain",
#     "qty_hashtag_domain",
#     "qty_dollar_domain",
#     "qty_percent_domain",
#     "qty_vowels_domain",
#     "domain_length",
#     "domain_in_ip",
#     "server_client_domain",
# ]

# # Attributes based on the URL directory properties (Table 3)
# directory_properties_attributes = [
#     "qty_dot_directory",
#     "qty_hyphen_directory",
#     "qty_underline_directory",
#     "qty_slash_directory",
#     "qty_questionmark_directory",
#     "qty_equal_directory",
#     "qty_at_directory",
#     "qty_and_directory",
#     "qty_exclamation_directory",
#     "qty_space_directory",
#     "qty_tilde_directory",
#     "qty_comma_directory",
#     "qty_plus_directory",
#     "qty_asterisk_directory",
#     "qty_hashtag_directory",
#     "qty_dollar_directory",
#     "qty_percent_directory",
#     "directory_length",
# ]

# # Attributes based on the URL file properties (Table 4)
# file_properties_attributes = [
#     "qty_dot_file",
#     "qty_hyphen_file",
#     "qty_underline_file",
#     "qty_slash_file",
#     "qty_questionmark_file",
#     "qty_equal_file",
#     "qty_at_file",
#     "qty_and_file",
#     "qty_exclamation_file",
#     "qty_space_file",
#     "qty_tilde_file",
#     "qty_comma_file",
#     "qty_plus_file",
#     "qty_asterisk_file",
#     "qty_hashtag_file",
#     "qty_dollar_file",
#     "qty_percent_file",
#     "file_length",
# ]

# # Attributes based on the URL parameter properties (Table 5)
# parameter_properties_attributes = [
#     "qty_dot_params",
#     "qty_hyphen_params",
#     "qty_underline_params",
#     "qty_slash_params",
#     "qty_questionmark_params",
#     "qty_equal_params",
#     "qty_at_params",
#     "qty_and_params",
#     "qty_exclamation_params",
#     "qty_space_params",
#     "qty_tilde_params",
#     "qty_comma_params",
#     "qty_plus_params",
#     "qty_asterisk_params",
#     "qty_hashtag_params",
#     "qty_dollar_params",
#     "qty_percent_params",
#     "params_length",
#     "tld_present_params",
#     "qty_params",
# ]

# # Attributes based on URL resolving data and external services (Table 6)
# resolving_external_attributes = [
#     "time_response",
#     "domain_spf",
#     "asn_ip",
#     "time_domain_activation",
#     "time_domain_expiration",
#     "qty_ip_resolved",
#     "qty_nameservers",
#     "qty_mx_servers",
#     "ttl_hostname",
#     "tls_ssl_certificate",
#     "qty_redirects",
#     "url_google_index",
#     "domain_google_index",
#     "url_shortened"
# ]

