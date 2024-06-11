import re

# Mapeamento de instruções Smali para C
smali_to_c = {
    "const": "=",
    "move": "=",
    "add": "+=",
    "sub": "-=",
    "mul": "*=",
    "div": "/=",
    "return": "return"
}

# Mapeamento de funções estáticas conhecidas
static_functions = {
    "Lcom/example/MyClass;->myStaticMethod(I)V": "my_static_method"
}

# Função para converter uma linha de Smali para C
def convert_line(line):
    # Remover comentários
    line = re.sub(r'#.*', '', line).strip()
    if not line:
        return ""
    
    # Separar a instrução e os operandos
    parts = re.split(r'\s+', line)
    instruction = parts[0]
    operands = parts[1:]
    
    # Converter a instrução
    if instruction in smali_to_c:
        if instruction == "const":
            return f"int {operands[0]} {smali_to_c[instruction]} {operands[1]};"
        elif instruction == "move":
            return f"{operands[0]} {smali_to_c[instruction]} {operands[1]};"
        elif instruction in ["add", "sub", "mul", "div"]:
            return f"{operands[0]} {smali_to_c[instruction]} {operands[1]};"
        elif instruction == "return":
            return f"return {operands[0]};"
    elif instruction == "invoke-static":
        function_call = operands[-1]
        if function_call in static_functions:
            function_name = static_functions[function_call]
            args = ", ".join(operands[:-1])
            return f"{function_name}({args});"
        else:
            return f"// {line}  // Função estática não mapeada"
    
    return f"// {line}  // Instrução não mapeada"

# Função principal para converter código Smali para C
def convert_smali_to_c(smali_code):
    c_code = "#include <stdio.h>\n\n"
    
    # Adicionar declarações de funções estáticas
    for func in static_functions.values():
        c_code += f"void {func}(int);\n"
    
    c_code += "\nint main() {\n"
    
    for line in smali_code.splitlines():
        c_line = convert_line(line)
        if c_line:
            c_code += "    " + c_line + '\n'
    
    c_code += "\n    return 0;\n}\n"
    
    return c_code
