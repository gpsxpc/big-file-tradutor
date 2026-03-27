# 🌐 Big File Tradutor

> 🐍 Script Python para traduzir arquivos de texto grandes de qualquer idioma para outro, utilizando a API gratuita do Google Translate.

Para contornar os limites de tamanho da API, o arquivo é automaticamente dividido em pedaços (_chunks_) menores, traduzidos individualmente e depois remontados em um único arquivo de saída. ✂️➡️🌍

---

## 📁 Estrutura do projeto

```
big-file-tradutor/
└── Translator_02.py   # Script principal de tradução
```

---

## ⚙️ Requisitos

- 🐍 Python 3.x
- 📦 Biblioteca [`googletrans`](https://pypi.org/project/googletrans/)

```bash
pip install googletrans==4.0.0-rc1
```

---

## 🔍 Como funciona

O script expõe duas funções principais:

| Função | Descrição |
|---|---|
| `translate_text(text, dest_language)` | 🔤 Traduz uma string diretamente para o idioma de destino e retorna o texto traduzido. |
| `translate_large_file(input_file, output_file, dest_language, chunk_size=5000)` | 📄 Lê um arquivo de texto, divide-o em pedaços de até `chunk_size` caracteres (padrão: 5 000), traduz cada pedaço e salva o resultado em `output_file`. |

### 🔄 Fluxo de execução

1. 📖 O arquivo de entrada é lido inteiro na memória.
2. ✂️ O conteúdo é dividido em pedaços de `chunk_size` caracteres.
3. 🌐 Cada pedaço é enviado individualmente para a API do Google Translate.
4. 💾 Os pedaços traduzidos são concatenados e gravados no arquivo de saída.

---

## 🚀 Como usar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/gpsxpc/big-file-tradutor.git
cd big-file-tradutor
```

### 2️⃣ Instale as dependências

```bash
pip install googletrans==4.0.0-rc1
```

### 3️⃣ Ajuste os parâmetros no script

Abra o arquivo `Translator_02.py` e edite as variáveis no final do script:

```python
input_file    = "input.txt"   # 📂 Caminho do arquivo de entrada
output_file   = "output.txt"  # 💾 Caminho do arquivo de saída
dest_language = "pt"          # 🌍 Código do idioma de destino
```

### 4️⃣ Execute o script

```bash
python Translator_02.py
```

✅ O arquivo traduzido será salvo no caminho definido em `output_file`.

---

## 🌍 Códigos de idioma suportados

Alguns exemplos de códigos de idioma aceitos pela API do Google Translate:

| Código | Idioma |
|---|---|
| `pt` | 🇧🇷 Português |
| `en` | 🇺🇸 Inglês |
| `es` | 🇪🇸 Espanhol |
| `fr` | 🇫🇷 Francês |
| `de` | 🇩🇪 Alemão |
| `it` | 🇮🇹 Italiano |
| `ja` | 🇯🇵 Japonês |
| `zh-cn` | 🇨🇳 Chinês Simplificado |

📚 Para a lista completa, consulte a [documentação do googletrans](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages).

---

## 🛠️ Personalizando o tamanho dos pedaços

Por padrão, o texto é dividido em pedaços de **5 000 caracteres**. Se necessário, ajuste o parâmetro `chunk_size` na chamada da função:

```python
translate_large_file(input_file, output_file, dest_language, chunk_size=3000)
```

> 💡 Valores menores reduzem a chance de erros na API; valores maiores diminuem o número de requisições.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! 🎉 Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

## 📄 Licença

Este projeto é licenciado sob a Licença MIT – veja o arquivo [LICENSE](LICENSE) para detalhes.

