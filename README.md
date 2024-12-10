##Testar via Navegador
Acesse http://127.0.0.1:5000/graphql para usar a interface GraphiQL. Experimente as queries abaixo:

Obter todos os usuários:
```bash
query {
    users {
        id
        name
        email
        phone
        age
        address {
            street
            city
            state
            postal_code
        }
        company {
            name
            industry
        }
    }
}

```
