name: Problem Report
description: File a problem report
title: "[PR]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Utilize o formulário abaixo para realizar a abertura do Problem Report
  - type: input
    id: contato
    attributes:
      label: Informação de Contato
      description: Como podemos entrar em contato com você para falarmos do PR?
      placeholder: ex. email@example.com
    validations:
      required: false
  - type: textarea
    id: Descrição
    attributes:
      label: Qual foi o problema encontrado?
      description: Quando o problema foi encontrado, o que esperava além do problema?
      placeholder: Mostre o que aconteceu! (Screenshots)
      value: "A bug happened!"
    validations:
      required: true
  - type: dropdown
    id: version
    attributes:
      label: Versão
      description: Qual versão da plataforma o erro ocorreu?
      options:
        - OctaX V4.3 
        - OctaX V4.299
        - RobotFX V0.17.296
        - RobotFX V0.20.8 
    validations:
      required: true
  - type: dropdown
    id: ambiente
    attributes:
      label: Qual ambiente o problema foi encontrado?
      multiple: true
      options:
        - Homologação
        - Desenvolvimento
        - Produção
  - type: dropdown
    id: severity
    attributes:
      label: Severidade
      description: Qual a severidade do problema? 
      options:
        - Crítica
        - Não-Crítica
    validations:
      required: true
  - type: dropdown
    id: priority
    attributes:
      label: Prioridade
      description: Qual a prioridade do problema?
      multiple: true
      options:
        - Alta prioridade
        - Média prioridade
        - Baixa prioridade