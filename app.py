from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Definir tipos para Endereço e Empresa
class AddressType(graphene.ObjectType):
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    postal_code = graphene.String()

class CompanyType(graphene.ObjectType):
    name = graphene.String()
    industry = graphene.String()

# Definir o tipo de Usuário (UserType)
class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    age = graphene.Int()
    address = graphene.Field(AddressType)  # Relacionamento com AddressType
    company = graphene.Field(CompanyType)  # Relacionamento com CompanyType

# Dados fixos de 5 usuários
USERS = [
    UserType(
        id=1,
        name="Alice Johnson",
        email="alice.johnson@example.com",
        phone="+1234567890",
        age=28,
        address=AddressType(
            street="123 Maple Street",
            city="Springfield",
            state="IL",
            postal_code="62701"
        ),
        company=CompanyType(
            name="Tech Solutions",
            industry="Software"
        )
    ),
    UserType(
        id=2,
        name="Bob Brown",
        email="bob.brown@example.com",
        phone="+1234567891",
        age=35,
        address=AddressType(
            street="456 Oak Avenue",
            city="Chicago",
            state="IL",
            postal_code="60601"
        ),
        company=CompanyType(
            name="Data Innovations",
            industry="Data Science"
        )
    ),
    UserType(
        id=3,
        name="Charlie Davis",
        email="charlie.davis@example.com",
        phone="+1234567892",
        age=42,
        address=AddressType(
            street="789 Pine Road",
            city="Los Angeles",
            state="CA",
            postal_code="90001"
        ),
        company=CompanyType(
            name="Creative Solutions",
            industry="Marketing"
        )
    ),
    UserType(
        id=4,
        name="Dana White",
        email="dana.white@example.com",
        phone="+1234567893",
        age=30,
        address=AddressType(
            street="321 Birch Lane",
            city="New York",
            state="NY",
            postal_code="10001"
        ),
        company=CompanyType(
            name="Design Co.",
            industry="Design"
        )
    ),
    UserType(
        id=5,
        name="Eve Black",
        email="eve.black@example.com",
        phone="+1234567894",
        age=25,
        address=AddressType(
            street="654 Cedar Street",
            city="Austin",
            state="TX",
            postal_code="73301"
        ),
        company=CompanyType(
            name="Marketing Pros",
            industry="Marketing"
        )
    )
]

# Criar uma consulta para retornar uma lista de usuários
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_users(self, info):
        # Retorna os 5 usuários definidos manualmente
        return USERS

    def resolve_user(self, info, id):
        # Buscar um único usuário pelo ID
        return next((user for user in USERS if user.id == id), None)

# Definir o schema GraphQL
schema = graphene.Schema(query=Query)

# Configurar o Flask
app = Flask(__name__)

# Configurar a rota do GraphQL
app.add_url_rule(
    "/graphql", 
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run()
