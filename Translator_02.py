from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text

def translate_large_file(input_file, output_file, dest_language, chunk_size=5000):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Dividir o texto em pedaços menores
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    translated_chunks = []
    for chunk in chunks:
        translated_chunks.append(translate_text(chunk, dest_language))

    # Concatenar os pedaços traduzidos de volta em um único texto
    translated_text = ''.join(translated_chunks)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

# Exemplo de uso
input_file = "input.txt"  # Nome do arquivo de entrada
output_file = "output.txt"  # Nome do arquivo de saída
dest_language = "pt"  # Código do idioma de destino (ex: 'pt' para português)

translate_large_file(input_file, output_file, dest_language)
