import telebot

CHAVE_API = "5134645934:AAH4alrNC1JoGWXG7GQ5RvFhgik3FvaFoLk"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(Commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id,"Boa tarde, estou te encaminhando o telefone do nosso advogado lider na area Trabalhista DDD (xx) xxxxx-xxxx")

@bot.message_handler(Commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id,"Boa tarde, estou te encaminhando o telefone do nosso advogado lider na area Civil DDD (xx) xxxxx-xxxx")

@bot.message_handler(Commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id,"Boa tarde, estou te encaminhando o telefone do nosso advogado lider na area Maritima DDD (xx) xxxxx-xxxx")

@bot.message_handler(Commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id,"Segue abaixo o numero da nossa recepcao!")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
  Escolha uma opção para continuar (Clique no item):
    /opcao1 Advogados de direito Trabalhistas
    /opcao2 Advogados de direito Civis
    /opcao3 Advogads de direito Maritimos
    Responder qualquer outra coisa não ira ter resposta, clique em uma opção valida
    /opcao4 Falar com a  Recepcao;  """

    bot.reply_to(mensagem, "Olá aqui é Claudia da Ruy de Mello Miller")


bot.polling()