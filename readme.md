# Recicla EG - Plataforma de Gestão de Resíduos e Coleta Inteligente

**Projeto Integrador - 8º Semestre de Engenharia de Software**

## 🌍 Visão Geral e Alinhamento ONU (ODS)
O **Recicla EG** é uma aplicação web desenvolvida para mitigar o descarte irregular de resíduos, criando uma ponte digital entre munícipes (colaboradores) e pontos de coleta. A arquitetura do sistema foi projetada para atender a dois Objetivos de Desenvolvimento Sustentável (ODS) da ONU:

* **ODS 11 (Cidades e Comunidades Sustentáveis):** Atua diretamente na Meta 11.6, facilitando a gestão de resíduos sólidos municipais e melhorando a infraestrutura de zeladoria da região.
* **ODS 12 (Consumo e Produção Responsáveis):** Atende à Meta 12.5, promovendo a economia circular ao rastrear categorias de resíduos (plásticos, eletrônicos, etc.) e conectar a demanda residencial aos ecopontos corretos.

## 💻 Arquitetura e Tecnologias
O sistema segue o padrão de arquitetura Monolítica MVC (Model-View-Controller) simplificada, focando em alta coesão e baixo acoplamento, estruturado para fácil manutenção e escalabilidade.
* **Backend:** Python com **Flask** (Framework WSGI leve, modular e performático).
* **ORM:** **SQLAlchemy**, garantindo segurança contra Injeção de SQL e facilidade na modelagem relacional dos dados.
* **Banco de Dados:** **SQLite**, encapsulando os dados localmente para facilitar a implantação, testes automatizados e validação do MVP em ambientes acadêmicos.

## Funcionalidades

A aplicação permite que os usuários:
- Se cadastrem como **coletores** ou **colaboradores**.
- Visualizem e cadastrem **pontos de coleta** de recicláveis.
- Acompanhem o progresso do sistema de reciclagem na sua região.
- Colaboradores podem se cadastrar com endereços para receber a coleta em suas casas.

## 🚀 Como Executar o Projeto Localmente

1. Clone este repositório:
   ```bash
   git clone [https://github.com/seuusuario/reciclagem.git](https://github.com/seuusuario/reciclagem.git)
   cd reciclagem
   ´´´

2. Crie e ative um ambiente virtual (recomendado):
   ´´´bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ´´´

3. Instale as dependências:
   ´´´bash
   pip install -r requirements.txt
   ´´´

4. Inicialize o banco de dados e rode a aplicação:
   ```bash
   flask run
   ´´´
