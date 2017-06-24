import tweepy, datetime, csv
from re import findall
from subprocess import getoutput
from time import time, sleep

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def test_speed():
	print("Testing...")
	speeds = getoutput(['speedtest-cli', '--simple'])
	print("\nTest completed.")
	return findall(r'(\d+\.\d+)', speeds)

def format_data(data, down_speed, up_speed, isp, cidade):
	if float(data[0]) > 100:
		return (1, "Ei {}, por que meu ping está {} ms aqui em {}".format(isp, data[0]), cidade)
	elif float(data[1]) < down_speed*0.75 or float(data[2]) < up_speed*0.75: 
		return (1, "Ei {}, por que minha internet está em {1}down e {2}up quando pago por {1}down/{2}up? Aqui em {}".format(isp, data[1], data[2], cidade))
	return (0, "Ok.")

def send_tweet(tweet_formatado):
	try:
		api.update_status(tweet_formatado)
		print("Tweet enviado!")
	except:
		print("Erro ao enviar tweet!")

def input_handle():
	while(1):
		isp_handle = input("Twitter do provedor de internet: ")
		cidade = input("Sua cidade: ")
		user_input = input("Seu download/upload, em Mbit/s, separados por /: ").split("/")
		try:
			down = float(user_input[0])
			up = float(user_input[1])
			break
		except ValueError:
			print("Input fora de padrão. Entre com valores em Mbit/s.")
	return (down, up, isp_handle, cidade)

def spreadsheet_output(data):
	time_stamp = time()
	date = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
	out_file = open("data.csv", 'a+')
	writer = csv.writer(out_file)
	writer.writerow((isp, date, data[0], data[1], data[2]))
	out_file.close()

if __name__ == '__main__':
	down, up, isp, cidade = input_handle()
	while(1):
		data = test_speed()
		spreadsheet_output(data)
		print("Ping: {}\nDownload: {}\nUpload: {}".format(data[0], data[1], data[2]))
		status, tweet = format_data(data, down, up, isp, cidade)
		if(status):
			send_tweet(tweet)
		else:
			print("Internet normal.")
		sleep(900)