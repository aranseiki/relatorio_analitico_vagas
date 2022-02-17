# Relatório analítico de vagas



## Introdução
#### Esse projeto tem como propósito a divulgação do resultado de um teste de processo seletivo.
#### No processo seletivo foi solicitado realizar um script de automação que faz raspagem de dados da página de vagas do site da Cadmus.



# Pré-requisitos
#### Como pré-requisito da execução do script é necessário ter um navegador compatível com as tecnologias mencionadas, assim como as mesmas: 

* Visual Studio Code
* Python 3.10
* Selenium WebDriver
* WebDriver do navegador



# Instalação das dependências

* Visual Studio Code: 
  #### Para a instalação do Visual Studio Code siga os passos contido no link abaixo: 
  #### https://code.visualstudio.com/docs/setup/windows
  
* Python
  #### Para a instalação do Python siga os passos contigo no link abaixo: 
  #### https://python.org.br/instalacao-windows/#:~:text=O%20processo%20de%20instala%C3%A7%C3%A3o%20%C3%A9%20bem%20simples.%201.,--version.%20Este%20comando%20retornar%C3%A1%20a%20vers%C3%A3o%20do%20
  
* SeleniumWebDriver e WebDriver do navegador 
  #### Para a instalação do SeleniumWebDriver siga os passos contigo no link abaixo:
  #### https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/
  
  #### Para a instalação do WebDriver do navegador siga os passos contigo no link abaixo:
  #### https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
  


# Executando o script
#### Clone esse projeto em alguma pasta de sua preferência
#### Abra o Visual Studio Code nessa pasta;
#### Abra o terminal do sistema dentro do Visual Studio Code. Copie a sequência de código abaixo no terminal dentro do VSCode e pressione Enter:
``` python -m venv venv ```
``` & ./venv/Scripts/Activate.ps1 ```
``` python -m pip install -r requirements_dev.txt ```
#### Execute o comando abaixo para efetivamente colocar em produção o script: 
``` python .\main.py ```

#### Ao final do processo será gerado um log conforme consta na documentação. Você pode obter os detalhes do processo, logs e muito mais acessando a pasta documentação dentro deste projeto.

# Autores
Allan de Oliveira Almeida
