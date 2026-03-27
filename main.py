import boto3
import os
import time

def salvar_no_dynamo():
    # O Codespaces pega as chaves direto das configurações do GitHub
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name='us-east-1' 
    )
    
    dynamodb = session.resource('dynamodb')
    tabela = dynamodb.Table('FinChatData')

    item = {
        'userId': 'usuario_github_codespace',
        'timestamp': int(time.time()),
        'description': 'Teste vindo da VM do GitHub',
        'amount': 99.90
    }

    try:
        tabela.put_item(Item=item)
        print("🚀 Sucesso! O dado saiu do GitHub e caiu na AWS!")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    salvar_no_dynamo()