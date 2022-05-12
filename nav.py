# markups.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnA = KeyboardButton('OUTROS')
btnB = KeyboardButton('ATIVAR ASSINATURA')
subMenuOne = ReplyKeyboardMarkup(resize_keyboard = True)
subMenuOne.add(btnB)
subMenuOne.add(btnA)

btnB = KeyboardButton('SUPORTE')
subMenuTre = ReplyKeyboardMarkup(resize_keyboard = True)
subMenuTre.add(btnB)


btnB = KeyboardButton('MENSAL')
btnA = KeyboardButton('VITALICIO')
subMenuTo = ReplyKeyboardMarkup(resize_keyboard = True)
subMenuTo.add(btnB)
subMenuTo.add(btnA)


btnA = KeyboardButton('ENTRAR NO GRUPO GRATUITO')
btnB = KeyboardButton('ATIVAR ASSINATURA')
btnC = KeyboardButton('SUPORTE')
#btnB = KeyboardButton('QUERO AJUDA COM OUTRA COISA')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnA)
mainMenu.add(btnB)
mainMenu.add(btnC)
