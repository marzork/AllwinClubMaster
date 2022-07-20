import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from Controller.controlDao import connectDao
from aiogram.types.message import ContentType
from aiogram.utils import executor
import threading, nav
from datetime import date
from woocommerce import API
import datetime,time,telebot
from Controller.controlEnum import MENSAGE
from telegram import ParseMode, User
from googletrans import Translator
from Controller.controlConfig import  controlValue, MsgTo
from Controller.controlDao import connectDao

from googletrans import Translator
translator = Translator()

	
logging.basicConfig(level=logging.INFO)
ACTIVCATALAGVip = ['TODOS','EURAUD','AUDNZD','GBPNZD','USDCAD','AUDJPY','GBPCAD','GBPAUD','EURUSD','EURGBP','GBPJPY','EURJPY','GBPUSD','USDJPY','AUDCAD',"USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'NZDUSD','USDCHF','AUDUSD','EOSUSD','XRPUSD','ETHUSD','LTCUSD','BTCUSD','USDJPY-OTC','AUDCAD-OTC','EURUSD-OTC','EURGBP-OTC','USDCHF-OTC','EURJPY-OTC','NZDUSD-OTC','GBPUSD-OTC','GBPJPY-OTC','EURCAD']
#1856618899:AAGHq3wJkjNqtO5NiasW8jkaKJg6GOcubw0
#5205191564:AAHlQzCk2TQBqMtsd0QGDB8FcQTH3aL-GGw
API_TOKEN = '5205191564:AAHlQzCk2TQBqMtsd0QGDB8FcQTH3aL-GGw'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

def dateTimeFormat(dateTime):
	dateTime= dateTime.split('T')
	time = dateTime[1]
	date = dateTime[0].split('-')
	date = date[2]+'/'+date[1]+'/'+date[0]
	return date+' '+time

def Sheac(email):
	
	if True:
		email = int(email)
		wcapi = API(
			url="https://allwinclub.vip",
			consumer_key='ck_a897889fddd55e8a0e3f35fcbac97e0c048f2c8c',
			consumer_secret='cs_fd98e918b2ff4a04abb0c715fa6449704f00f196',
			version="wc/v3"
		)
		a = wcapi.get("subscriptions/"+str(email)).json()
		if "ID inválido" in str(a):
			a = wcapi.get("orders/"+str(email)).json()
			if "ID inválido" in str(a):
				return False
			else:
				if a['status'] in ['processing','completed']:
					return a['order_key'][12:],a['date_modified'], a['total'],a['order_key'],a['billing']['email'],a['line_items'][0]['name'],a['line_items'][0]['product_id'],'active'
				else:
					return None,None,None, None,None,None,None,None,None
		else:
			if a['status'] in ['processing','active']:
				return a['order_key'][12:],a['date_modified'], a['total'],a['order_key'],a['billing']['email'],a['line_items'][0]['name'],a['line_items'][0]['product_id'],'active'
			return None,None,None, None,None,None,None,None,None

def validateCod(email):
	try:
		ass = ''
		if True:
			wcapi = API(
				url="https://allwinclub.vip",
				consumer_key='ck_a897889fddd55e8a0e3f35fcbac97e0c048f2c8c',
				consumer_secret='cs_fd98e918b2ff4a04abb0c715fa6449704f00f196',
				version="wc/v3"
			)
			a = wcapi.get("subscriptions/"+str(email)).json()
			if "ID inválido" in str(a):
				a = wcapi.get("orders/"+str(email)).json()
				if "ID inválido" in str(a):
					return False, 'Invalido'
				else:
					#dataFormat = a['date_created'].split('-')
					#pri_date = datetime.date(int(dataFormat[0]),int(dataFormat[1]),int(dataFormat[2][:-9]))	
					#dataFormat = str(datetime.datetime.now()).split('-')
					#second_date = datetime.date(int(dataFormat[0]),int(dataFormat[1]),int(dataFormat[2][:-16]))
					
					if str(a['line_items'][0]['product_id']) in ['27195','27197','27194']:
						if a['status'] in ['processing','completed']:
							return True,''
						else:
							return False, 'active'
					else:
						return False,'Produto não permitido: '+str(a['line_items'][0]['product_id'])
			else:
				
				if str(a['line_items'][0]['product_id']) in ['536','531','535']:
					if a['status'] in ['processing','active']:
						return True,''
					else:
						return False,'Produto não permitido: '+str(a['line_items'][0]['product_id'])
				return False,'Produto não permitido: '+str(a['line_items'][0]['product_id'])
	except Exception as e:
		#print(e)
		return False,''

def validateEmail(email,senha):
	if True:
		wcapi = API(
			url="https://allwinclub.vip",
			consumer_key='ck_a897889fddd55e8a0e3f35fcbac97e0c048f2c8c',
			consumer_secret='cs_fd98e918b2ff4a04abb0c715fa6449704f00f196',
			version="wc/v3"
		)
		a = wcapi.get("subscriptions/"+str(senha)).json()

		if "ID inválido" in str(a):
			a = wcapi.get("orders/"+str(senha)).json()
			#print(a)
			if "ID inválido" in str(a):
				return False
			else:
				if str(a['line_items'][0]['product_id']) in ['27195','27197','27194']:
					if email.lower() == a['billing']['email'].lower():
						return True
					else:
						return False
				return False
		else:
			if str(a['line_items'][0]['product_id']) in ['535','536','531']:
				if email.lower() == a['billing']['email'].lower():
					return True
				else:
					return False
			return False
			
	else:
		return False
def is_int(d):
	try:
		int(d)
		return d
	except ValueError:
		return False
	except TypeError:
		return False
def is_float(d):
	try:
		float(d)
		return d
	except ValueError:
		return False
	except TypeError:
		return False
def is_str(d):
	try:
		str(d)
		return d
	except ValueError:
		return False
	except TypeError:
		return False

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id, "Olá {0}, seja bem vindo ao nosso clube! Fui programado para te ajudar, então preciso cumprir meu objetivo! O que você deseja?".format(message.chat.first_name), reply_markup = nav.mainMenu) 


class Formsig(StatesGroup):
	email = State()
	upo = State()
	upt = State()
	upf = State()
	senha = State()
	finish = State()

@dp.message_handler(commands='dsda')
async def cmd_start(message: types.Message):
	await Formsig.email.set()
	await message.reply("Olá {0}, seja bem vindo ao nosso clube! Fui programado para te ajudar, então preciso cumprir meu objetivo! Qual o código da sua assinatura?\n(não utlize #, apenas o número) ".format(message.chat.first_name))
	await bot.send_photo(message.chat.id, photo=open('ph.jpg', 'rb'),caption='Você encontra esse código ao logar no seu perfil na plataforma https://allwinclub.vip/painel/subscriptions/ \n\nOBS: Você precisa fazer o Login primeiro.')
	

@dp.message_handler(state=Formsig.email)	
async def process_semail(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['email'] = message.text
	check, reaos = validateCod(message.text.replace('#',''))
	if check == False:
		await message.reply("STATUS: "+reaos+". tente novamente. /start")
		await state.finish()
	else:
		await Formsig.next()
		await message.reply("Isso ai {0}, Envie uma foto ou #print do cartão utilizado para a compra (visíveis apenas os 4 últimos dígitos e nome do titular) restante esconder/desenhar em cima.".format(message.chat.first_name))

@dp.message_handler(state=Formsig.upo, content_types=ContentType.ANY)
async def process_ban(message: types.PhotoSize, state: FSMContext):
	async with state.proxy() as data:
		if message.text:
			await state.finish()
		else:
			if message.content_type == 'photo':
				bots = telebot.TeleBot(API_TOKEN)
				file_info = bots.get_file(message.photo[0].file_id)
				namefile = str(datetime.datetime.now()).replace(' ','')
				namefile = namefile.replace('.','')
				namefile = namefile.replace(':','')
				namefile = namefile.replace('-','')
				downloaded_file = bots.download_file(file_info.file_path)
				with open(namefile+'.png', 'wb') as new_file:
					new_file.write(downloaded_file)
				data["upo"] = namefile+'.png'
				await Formsig.next()
				await message.reply("Ok, Foto do titular do cartão segurando documento de identidade, legível.")
			else:
				await state.finish()
		
		
@dp.message_handler(state=Formsig.upt, content_types=ContentType.ANY)
async def process_ban(message: types.PhotoSize, state: FSMContext):
	async with state.proxy() as data:
		if message.text:
			await state.finish()
		else:
			if message.content_type == 'photo':
				bots = telebot.TeleBot(API_TOKEN)
				file_info = bots.get_file(message.photo[0].file_id)
				namefile = str(datetime.datetime.now()).replace(' ','')
				namefile = namefile.replace('.','')
				namefile = namefile.replace(':','')
				namefile = namefile.replace('-','')
				downloaded_file = bots.download_file(file_info.file_path)
				with open(namefile+'.png', 'wb') as new_file:
					new_file.write(downloaded_file)
				data["upt"] = namefile+'.png'
				await Formsig.next()
				await message.reply("ok, Foto documento separado junto com um papel escrito Membro All Win Club.")
			else:
				await state.finish()
@dp.message_handler(state=Formsig.upf, content_types=ContentType.ANY)
async def process_ban(message: types.PhotoSize, state: FSMContext):
	async with state.proxy() as data:
		if message.text:
			await state.finish()
		else:
			if message.content_type == 'photo':
				bots = telebot.TeleBot(API_TOKEN)
				file_info = bots.get_file(message.photo[0].file_id)
				namefile = str(datetime.datetime.now()).replace(' ','')
				namefile = namefile.replace('.','')
				namefile = namefile.replace(':','')
				namefile = namefile.replace('-','')
				downloaded_file = bots.download_file(file_info.file_path)
				with open(namefile+'.png', 'wb') as new_file:
					new_file.write(downloaded_file)
				data["upf"] = namefile+'.png'
				await Formsig.next()
				await message.reply("Ok, Qual email do site?")
			else:
				await state.finish()
@dp.message_handler(state=Formsig.senha)
async def process_optionsdateTop(message: types.Message, state: FSMContext):
	markup = types.ReplyKeyboardRemove()
	async with state.proxy() as data:
		ss = message.text
		data['senha'] = ss
	if "cancelar" in message.text.lower():
		await message.reply("Ok, cancelado")
		await state.finish()
	if validateEmail(data['senha'],data['email'].replace('#','')):
		passd,date_c,valor,order_key,email,name,product_id,active = Sheac(data['email'].replace('#',''))
		if passd != None:
			sig, a = connectDao.insertAcc(str(email), str(passd), str(valor),str(order_key), str(name), str(product_id), str(active), 'LAB', str(message.chat.id), str(date_c), str(data['email']))
			if sig:
				await bot.send_photo(1406327626, photo=open(data["upo"], 'rb'), caption=str(message.chat.id)+' - cartão')
				await bot.send_photo(1406327626, photo=open(data["upt"], 'rb'), caption=str(message.chat.id)+' - identidade')
				await bot.send_photo(1406327626, photo=open(data["upf"], 'rb'), caption=str(message.chat.id)+' - documento separado junto com um papel')
				await bot.send_message(1406327626, str(data['senha'])+' - '+str(data['email'])+' - '+str(message.chat.id),parse_mode=ParseMode.HTML)
				
				await message.reply(''' 

🙅🏻 Bem Vindo ao Clube! 

O primeiro passo é se registrar na nossa plataforma de membros clicando AQUI (https://allwinclub.vip/):

O segundo passo é assistir TODOS OS VÍDEOS DO CAMINHO DA CONSISTÊNCIA (https://allwinclub.vip/o-caminho-da-consistencia)!

Temos muitas salas de sinais e estamos começando a trazer outros mercados para os nossos membros também, então você deve primeiro entender quais são os horários em que operamos em cada sala (https://allwinclub.vip/tour-pelas-salas-do-all-win-club/).

Clique no link de cada sala e opte por entrar, depois é só aguardar a sua aprovação como membro, não é um processo demorado.

CASO O TELEGRAM EXIBA A MENSAGEM DE QUE O NÚMERO DE TENTATIVAS ESGOTOU, AGUARDE ALGUNS MINUTOS E ENTRE NOS CANAIS RESTANTES.

OPERE A PRIMEIRA SEMANA SEGUINDO AS LIVES SEM GALE À 00:00 e 12:30. 

❇️ FOREX
  |
O mercado que movimenta 4 trilhões por dia. Melhor risco e recompensa.

https://t.me/+ozGq9aE7dQgwZTYx

❇️ OURO
  |
Sala de Sinais de pares XAU (Onça de Ouro) para Forex.

https://t.me/+tGwxaYUCh1g5Y2Jh

❇️ MAGWIN GREEN (AO VIVO)
  |
Lives SEM GALE de operação com o Phelippão.

https://t.me/+LvIkiEBNnUkxMDgx

❇️ MAGWIN BLUE [AO VIVO M1]
  |
Lives SEM GALE expiração para 1 minuto com o Ramon.

https://t.me/+MucIX-vEbUQ3MDQx

❇️ MAGWIN RED (AO VIVO)
  |
Lives SEM GALE com o Joab.

https://t.me/+XNZMaCDQBL8zMjM5

❇️ [LISTAS]
  |
Listas com tempo de expiração para 5 minutos.

https://t.me/+Q9ShiqPKzRNjMjUx

❇️ [OTC]
  |
Listas com tempo de expiração para 5 minutos para o mercado de OTC.

https://t.me/+5frS_yAiT7w5MjEx

❇️ M5 [24HR$]
  |
Sinais enviados 24HR$ com tempo de expiração para 5 minutos.

https://t.me/+FPn1vyRB_tQ4NGYx

❇️ M15 [24HR$]
  |
Sinais enviados 24HR$ com tempo de expiração para 15 minutos.

https://t.me/+r4osuUft1lE2MWEx

❇️ M30 [24HR$]
  |
Sinais enviados 24HR$ com tempo de expiração para 30 minutos.

https://t.me/+ohAFf3LLdIkyN2Nh

❇️ H1 [24HR$]
  |
Sinais enviados 24HR$ com tempo de expiração para 1 hora.

https://t.me/+h3kZfbQ5BPQwOTM5

❇️ NOTÍCIAS [24HR$]
  |
Todas as notícias que afetam o mercado e qual a força esperada delas.

https://t.me/+ymLty2CaC4wwYjBh

❇️ ESTUDOS
  |
Novidades, enquetes e comunicados.

https://t.me/+O5V7ASk2m6c0YWJh

❇️ MUITO IMPORTANTE
  |
Acompanhar os resultados dos membros para trocar ideias e interagirem entre si.

https://t.me/resultadosallwinclub

⚠️ Recomendo iniciar as operações fazendo entradas dentro de um gerenciamento conservador até pegar o ritmo.

- De 0.5% a 1% do valor da banca de entradas que vão até o Gale 2, buscando de 5 a 10% por dia.
- De 5 a 10% de Stop Win.
- De 7 a 10% de Stop Loss.

- De 2 a 5% do valor da banca para entradas SEM GALE.

APLICAR JUROS COMPOSTOS AO DIA! O VALOR REFERENTE A % SEMPRE AUMENTA DE ACORDO COM A BANCA. DIARIAMENTE.

⚠️ Assistir o curso é importante porque você se torna independente do horário do sinal, podendo pular os gales ou se posicionar em taxas melhores do que a da virada de vela.

⚠️ Salas 24HRs são para traders mais experientes, sugiro operar somente quando a assertividade estiver acima de 90%.
https://t.me/+Q9ShiqPKzRNjMjUx''',reply_markup=markup)
				await bot.send_video(message.chat.id, video=open('video.mp4', 'rb'),caption='Façam isso para conseguirem acompanhar todas as salas do clube!')
				await bot.send_animation(message.chat.id, animation=open('gif.mp4', 'rb'),caption='Façam isso para conseguirem acompanhar todas as salas do clube!')
				await message.reply('''ASSISTE TODO O CONTEÚDO DO CURSO ANTES DE OPERAR

ESCUTA O QUE EU FALO NOS ÁUDIOS

É importante pra que você obtenha os mesmos resultados dos outros membros

Por favor um passo de cada vez, temos muitas histórias de sucesso e todas elas seguiram exatamente o que passamos''',reply_markup=markup)
				await bot.send_audio(message.chat.id, audio=open('ouca_o_audio.ogg', 'rb'))
	
				await message.reply('''
				⚠️ ATENÇÃO ⚠️

Você adquiriu um de nossos planos, sabemos que no país em que vivemos é muito difícil se dispor de um valor fixo mensal, principalmente enquanto busca uma RENDA EXTRA, e é justamente por isso que decidimos proporcionar à você o VITALÍCIO do nosso clube após o pagamento de 3 mensalidades seguidas. Isso mesmo. NINGUÉM proporciona isso pra vocês, nosso foco é ajudar cada um, desta forma você fica no clube por 3 meses e garante o acesso para o resto da vida à todos os nossos recursos, salas, cursos e tudo que ainda está sendo desenvolvido.

TEMOS MUITAS NOVIDADES VINDO AÍ E QUEREMOS DE TODO O CORAÇÃO QUE VOCÊ FAÇA PARTE DISTO.

Membros inadimplentes são removidos automaticamente na data exata do vencimento de sua assinatura mensal, para garantir esta vantagem basta manter o pagamento em dia por três meses. Nada mais que isto. Automaticamente sua assinatura já será convertida em vitalícia.''',reply_markup=markup)

			else:
				await message.reply(a,reply_markup=markup)
		else:
			await message.reply("ERRO",reply_markup=markup)
		await state.finish()
	else:
		await message.reply("invalido, tente novamente. /start")
		await state.finish()



 #/nextremove retorna do banco de dados TODOS os próximos vencimentos DATA/NOME/ID DO PRODUTO | Comando 
@dp.message_handler(commands=['nextremove'])
async def command_start(message: types.Message):
	if str(message.from_user.id) in ['971655878','1406327626']:
		nextRemoveUsers = connectDao.nextRemove()
		await bot.send_message(message.from_user.id, "ID | EMAIL | DATA | ID PRODUTO", reply_markup = nav.mainMenu)
		for users in nextRemoveUsers:
			dataFormat = str(users[2]).split('-')
			dayNow = date.today()
			dates = datetime.date(int(dataFormat[0]),int(dataFormat[1]),int(dataFormat[2][:-9]))
			futuro = date.fromordinal(dates.toordinal()+31)
			if dayNow < futuro:
				await bot.send_message(message.from_user.id, str(users[0])+" | "+str(users[1])+" | "+str(dateTimeFormat(users[2]))+" | "+str(users[3]), reply_markup = nav.mainMenu) 
	else:
		
		await bot.send_message(message.from_user.id, 'Unauthorized') 
		
		 

 #/lastremove retorna do banco de dados TODOS os removidos DATA/NOME/ID DO PRODUTO. | Comando 
@dp.message_handler(commands=['lastremove'])
async def command_start(message: types.Message):
	if str(message.from_user.id) in ['971655878','1406327626']:
		lastRemoveUsers = connectDao.lastRemove()
		await bot.send_message(message.from_user.id, "ID | EMAIL | DATA | ID PRODUTO", reply_markup = nav.mainMenu)
		for users in lastRemoveUsers:
			await bot.send_message(message.from_user.id, str(users[0])+" | "+str(users[1])+" | "+str(dateTimeFormat(users[2]))+" | "+str(users[3]), reply_markup = nav.mainMenu) 
	else:
		await bot.send_message(message.from_user.id, 'Unauthorized')
		

 #/todayremove retorna do banco de dados TODOS os que SERÃO ou FORAM removidos hoje DATA/NOME/ID DO PRODUTO.
@dp.message_handler(commands=['todayremove'])
async def command_start(message: types.Message):
	if str(message.from_user.id) in ['971655878','1406327626']:
		dayNow = date.today()
		dayWhere =  str(dayNow).split('-')
		nextRemoveUsers = connectDao.todayRemove(dayWhere[2]+'/'+dayWhere[1]+'/'+dayWhere[0])
		await bot.send_message(message.from_user.id, "ID | EMAIL | DATA | ID PRODUTO", reply_markup = nav.mainMenu)
		for users in nextRemoveUsers:
			dataFormat = str(users[2]).split('-')
			dates = datetime.date(int(dataFormat[0]),int(dataFormat[1]),int(dataFormat[2][:-9]))
			futuro = date.fromordinal(dates.toordinal()+31)
			if dayNow == futuro:
				await bot.send_message(message.from_user.id, str(users[0])+" | "+str(users[1])+" | "+str(dateTimeFormat(users[2]))+" | "+str(users[3]), reply_markup = nav.mainMenu) 
			elif users[4] != None:
				await bot.send_message(message.from_user.id, str(users[0])+" | "+str(users[1])+" | "+str(dateTimeFormat(users[2]))+" | "+str(users[3]), reply_markup = nav.mainMenu)
	else:
		await bot.send_message(message.from_user.id, 'Unauthorized')

@dp.message_handler()	
async def bot_message(message: types.Message):
	# await bot.send_message(message.from_user.id, message.text) 
	if message.text == 'QUERO AJUDA COM OUTRA COISA':
		await message.reply("🌐",reply_markup=nav.subMenuOne)
	if message.text == 'OUTROS':
		await message.reply('Ok, como posso te ajudar?',reply_markup=nav.subMenuTre)
	if message.text == 'ENTRAR NO GRUPO GRATUITO':
		await message.reply('Ok, aqui vai o link do nosso grupo 100% gratuito, clique nele e depois em "Entrar no Canal" na parte inferior da sua tela: https://t.me/+VeWwXZ-N9dphMWMx')
	if message.text ==  'SUPORTE':
		await message.reply('Pode chamar o @marzork',reply_markup=nav.subMenuTre)
	if message.text == 'ATIVAR ASSINATURA':
		await message.reply("Que tipo de assinatura?",reply_markup=nav.subMenuTo)
	if message.text in ['TRIMESTRAL ALLWINCLUB','SEMESTRAL ALLWINCLUB','VITALICIO ALLWINCLUB']:
		await cmd_start(message)

if __name__ == '__main__':
	##print(datetime.datetime.now(),"ss")
	executor.start_polling(dp, skip_updates=True)
