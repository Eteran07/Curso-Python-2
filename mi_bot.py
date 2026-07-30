import telebot # Importamos el manual de Telegram
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Guardamos la llave maestra en una variable (Usa el tuyo propio)
TOKEN = "8548252535:AAEr_WIIJ72uEmQ37Us4jNq038LcGeb_Ews" 

# Creamos el objeto bot, dándole el Token para que pueda conectarse
bot = telebot.TeleBot(TOKEN)






#HANDLER


# El "sensor" que escucha el comando /start
@bot.message_handler(commands=['start'])
def enviar_bienvenida(mensaje):
    # La respuesta que dará el bot
    bot.reply_to(mensaje, "¡Hola! Soy un bot creado con Python. ¿En qué te ayudo?")
















#BOTONES O MENU INTERACTIVO


from telebot.types import ReplyKeyboardMarkup, KeyboardButton

@bot.message_handler(commands=['menu'])
def mostrar_menu(mensaje):
    # Creamos el contenedor del teclado
    teclado = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Creamos los botones
    btn_saldo = KeyboardButton("Consultar Saldo")
    btn_ayuda = KeyboardButton("Ayuda")
    
    # Añadimos los botones al teclado
    teclado.add(btn_saldo, btn_ayuda)
    
    # Enviamos el mensaje junto con el teclado
    bot.reply_to(mensaje, "Elige una opción:", reply_markup=teclado)






















#CONVERSACIONES CONTINUAS


@bot.message_handler(commands=['registro'])
def pedir_nombre(mensaje):
    # Hacemos la primera pregunta
    msg = bot.reply_to(mensaje, "¿Cuál es tu nombre?")
    # Le decimos al bot que espere el próximo mensaje y lo mande a 'guardar_nombre'
    bot.register_next_step_handler(msg, guardar_nombre)

def guardar_nombre(mensaje):
    nombre = mensaje.text
    bot.reply_to(mensaje, f"¡Mucho gusto, {nombre}!")




















#ESCUCHA ACTIVA BOT



print("El bot está encendido y escuchando...")

# El café
bot.infinity_polling() 