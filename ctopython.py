import re

def convert_variable_declaration(line):
    line = re.sub(r'\bint\s+', '', line)
    line = re.sub(r'\bfloat\s+', '', line)
    line = re.sub(r'\bchar\s+', '', line)
    line = re.sub(r';', '', line)  # Remove semicolons
    line = re.sub(r'\bdouble\s+', '', line)
    return line

def convert_control_structures(line):
    line = re.sub(r'\bif\s*\((.*?)\)\s*{', r'if \1:', line)
    line = re.sub(r'\belse\s*{', r'else:', line)
    line = re.sub(r'\bfor\s*\((.*?);(.*?);(.*?)\)\s*{', lambda m: f"for {m.group(1).strip()} in range({m.group(2).strip()}):", line)
    line = re.sub(r'\bwhile\s*\((.*?)\)\s*{', r'while \1:', line)
    line = re.sub(r'}', '', line)  # Remove closing braces
    return line

def convert_functions(line):
    line = re.sub(r'\bvoid\s+(\w+)\s*\((.*?)\)\s*{', r'def \1(\2):', line)
    line = re.sub(r'\bint\s+(\w+)\s*\((.*?)\)\s*{', r'def \1(\2):', line)
    line = re.sub(r'\bfloat\s+(\w+)\s*\((.*?)\)\s*{', r'def \1(\2):', line)
    line = re.sub(r'\bchar\s+(\w+)\s*\((.*?)\)\s*{', r'def \1(\2):', line)
    line = re.sub(r'\bdouble\s+(\w+)\s*\((.*?)\)\s*{', r'def \1(\2):', line)
    line = re.sub(r'\breturn\b', 'return', line)
    return line

def convert_parameters(line):
    line = re.sub(r'\bint\s+', '', line)
    line = re.sub(r'\bfloat\s+', '', line)
    line = re.sub(r'\bchar\s+', '', line)
    line = re.sub(r'\bdouble\s+', '', line)
    return line

def convert_c_to_python_code(c_code_lines):
    python_code_lines = []
    for line in c_code_lines:
        if '(' in line and ')' in line and '{' in line:
            line = convert_parameters(line)
        line = convert_variable_declaration(line)
        line = convert_control_structures(line)
        line = convert_functions(line)
        python_code_lines.append(line)
    return python_code_lines

def convert_c_to_python(c_code):
    c_code_lines = c_code.split('\n')
    python_code_lines = convert_c_to_python_code(c_code_lines)
    python_code = '\n'.join(python_code_lines)
    return python_code
