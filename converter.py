import sys
import re

def convert_list(input_filepath, output_filepath):
    with open(input_filepath, 'r') as source_file, open(output_filepath, 'w') as target_file:
        pattern_server = r'server='
        pattern_bracket = r'['
        
        old_dns = r'/114.114.114.114'
        new_dns = r'/]https://dns.alidns.com/dns-query'
            
        for line in source_file:
            converted_line = re.sub(pattern_server, pattern_bracket, line)
            final_line = re.sub(old_dns, new_dns, converted_line)
            target_file.write(final_line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <input_file>")
        sys.exit(1)
        
    input_filepath = sys.argv[1]
    input_filename = input_filepath.split('/')[-1]
    input_filename = input_filename.split('.')[0]
    output_filename = f'{input_filename}_AdGuard.conf'
    output_filepath = f'./{output_filename}'
    
    convert_list(input_filepath, output_filepath)
