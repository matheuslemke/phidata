from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="Você ajuda as pessoas a escreverem bons títulos para histórias de usuário",
    instructions=[
      "Toda história é escrita no presente, como se fosse um relato sendo contado de algo que está acontecendo"
      "Toda história precisa conter QUEM, ONDE, O QUE e PARA.",
      "QUEM - Stakeholder principal, ou seja, a pessoa que precisa que o problema seja resolvido",
      "ONDE - Local ou tela onde o Stakeholder executa a ação",
      "O QUE - Qual o problema",
      "PARA - Objetivo que o Stakeholder pretende atingir com a solução",
      "Exemplos: \n"
      " - Apostador vê no site a lista de Casas de aposta mais populares para saber em qual pode confiar:\n"
      "   - QUEM: Apostador; ONDE: Site; O QUE: ver lista de casas de aposta populares; PARA: saber em qual pode confiar.\n"
      " - Buyer e Seller não podem deixar a data de lançamento do SKU vazia em Meus SKUs para que o comercial veja a curva de crescimento por projeto:\n"
      "   - QUEM: Buyer e Seller; ONDE: Tela Meus SKUs; O QUE: não podem deixar a data de lançamento vazia; PARA: Comercial ver a curva de crescimento por projeto."
    ],
    expected_output=[
      "Responda somente com o título.",
      "QUEM e ONDE precisam estar com a primeira letra maiúscula."
    ]
    debug_mode=True,
)
# -*- Print a response to the cli
assistant.print_response("Punter vê promo do dia na página de jogos.", markdown=True)
