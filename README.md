# API de gestão de produtos/fornecedores com estoque

#API-REST básica de um sitema de gerenciamento de estoque feito com base em estudos com o Gemini, que foi o "orientador pessoal para tirar dúvidas" e mostrar como montar uma estrutura profissional com boas práticas de segurança (Token) nativo da prórpia DRF.

## Como funciona?

* **Utilização de autenticação por Token:** O sistema gera um token de acesso para usuários autenticados, assim os endpoints mais "protegidos" são acessados por pessoas autorizadas.
*  **Permissão de acesso:** Somente usuários logados podem acessar o PUT, POST E DELETE, os demais somente o GET limitados pela configuração feita no Serializer de cada Model.
* **Crud full para:**
*  `Produtos - categorias - Fornecedores - Estoques`
*  A estrutura foi feita em partes separadas (`core`, `produtos`, `accounts`) separando a responsabilidade de cada um e com fácil possibilidade de expansão futura(escalabilidade) e os dados sensiveis estão ocultos com um arquivo externo que não foi upadado junto ao projeto.

## Tecnologias usadas para desenvolvimento
<table>
  <tr>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" alt="Python" title="Python"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" width="40" alt="Django" title="Django"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-original.svg" width="40" alt="DRF" title="Django REST Framework"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original-wordmark.svg" width="40" alt="MySQL" title="MySQL"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" width="40" alt="Git" title="Git"/></td>
    <td valign="top"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" width="40" alt="GitHub" title="GitHub"/></td>
  </tr>
</table>

  
