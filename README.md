# Gerador de Assinaturas de E-mail — Automação com Python e Excel

Automatiza a criação de assinaturas visuais (cartões de contato) a partir de um modelo de imagem e dados em planilha Excel. Ideal para gerar assinaturas personalizadas com nome, cargo e telefones de forma massiva.

---

##  Tecnologias utilizadas

- **Python**  
- Bibliotecas:
  - `Pillow` (PIL fork) para manipulação de imagem (texto sobre template) :contentReference[oaicite:2]{index=2}  
  - `openpyxl` para leitura de planilha Excel (`.xlsx`) :contentReference[oaicite:3]{index=3}  
  - Fonte customizada via `ttf_opensans` (OpenSans Bold e Regular)

---

##  Funcionalidades principais

- 🆔 **Geração automática de assinaturas visuais** em formato PNG.
-  Leitura de dados (nome, cargo, telefones) da planilha Excel.
-  Renderização de texto sobre imagem modelo (template) usando `Pillow`.
-  Formatação inteligente de telefones: DDD em regular, número em negrito.
-  Personalização de cores: o cargo aparece em verde escuro (`#004039`).
-  Nomes geram automaticamente nomes de arquivo seguros (ex.: `Primeiro-Ultimo.png`).
-  Cria uma pasta de saída automaticamente com os cartões gerados.
-  Logs no terminal indicam progresso e pulam linhas sem nome.

---
