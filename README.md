# 📊 Dashboard de Salários na Área de Dados

Dashboard interativo desenvolvido em Python para análise de salários na área de dados, permitindo explorar informações sobre cargos, senioridade, tipos de contrato, tamanho das empresas e modalidades de trabalho.

O projeto foi desenvolvido utilizando Streamlit para a interface web, Pandas para manipulação dos dados e Plotly para visualizações interativas.

---

## 🚀 Funcionalidades

- Visualização de métricas gerais da base de dados
- Filtros dinâmicos por:
  - Ano
  - Senioridade
  - Tipo de Contrato
  - Tamanho da Empresa
- Ranking dos cargos com maiores salários médios
- Distribuição salarial por faixa de renda
- Proporção dos modelos de trabalho (remoto, híbrido e presencial)
- Mapa mundial com média salarial para o cargo de Data Scientist
- Tabela interativa com os dados filtrados

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly

---

## 📂 Estrutura do Projeto

```bash
.
├── app.py
├── requirements.txt
├── ProjetoSI.ipynb
└── README.md
```

---

## 📈 Fonte dos Dados

Os dados são carregados diretamente de um arquivo CSV dentro do repositório, com o nome "mental_health_workplace":

```python
mental_health_workplace
```

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SouzaKaique/Atv-Dados-SI.git
```

### 2. Acessar a pasta do projeto

```bash
cd ProjetoSI
```

### 3. Criar um ambiente virtual (opcional)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
streamlit run app.py
```

Após a execução, o Streamlit disponibilizará um endereço local semelhante a:

```text
http://localhost:8501
```

Abra o endereço no navegador para acessar o dashboard.

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido durante uma imersão em Python e Análise de Dados, com o objetivo de aplicar conceitos de:

- Manipulação de dados com Pandas
- Visualização de dados
- Desenvolvimento de dashboards interativos
- Análise exploratória de dados
- Publicação de aplicações Python

---

## 👨‍💻 Autor

Kaique

- GitHub: https://github.com/SouzaKaique
- LinkedIn: https://www.linkedin.com/in/kaique-souzaa/

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado.
