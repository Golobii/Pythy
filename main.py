from discord.ext import tasks, commands
import discord
from discord.utils import find
import asyncio
import time
import calendar
import random
import requests
import praw
import json
import numpy as np

from commands import juje
from commands import urnik as ur
import encryption as enc
print("Imported!")

env = open(".env", "r").read().split("\n")
TOKEN = env[0]
PASSWORD_REDDIT = env[1]
CLIENT_SECRET = env[2]

reddit = praw.Reddit(
	client_id="H-KKMwdm9rZm9g",
	client_secret=CLIENT_SECRET,
	user_agent="LMGTFY (by u/golobii)",
	username="golobii",
	password=PASSWORD_REDDIT
)
switch = None
switch2 = None
iteration = 0

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

key = enc.load_key()

def isint(num):
	try:
		int(num)
		str(num)
		return True
	except ValueError:
		return False



async def my_background_task(client):
	await client.wait_until_ready()
	while True:
		current_time = time.time()
		current_time = time.localtime(current_time)
		current_time = time.strftime("%H:%M", current_time)
		user = client.get_user(485111024404660235)
		if current_time == "21:45" or current_time == "12:00":
			await user.send(f'{user.mention} tablete!')
			await asyncio.sleep(60)
		elif current_time == "08:00":
			user = client.get_user(691930634733748226)
			await user.send("Mornin babessss!")
			await asyncio.sleep(60)
		else:
			await asyncio.sleep(5)


async def my_background_task2(message, x):
	global switch
	switch = True
	while switch:
		await message.channel.send(x)
		x += 1
		await asyncio.sleep(5)
	return

client.loop.create_task(my_background_task(client))


async def periodic():
	while True:

		await asyncio.sleep(15)


@client.event
async def on_ready():
	print("Bot: {0.user}".format(client) + " is online!")
	welcome_channel = client.get_channel(749324560859529236)
	f = open("secret", "r").read()
	await welcome_channel.send(f)
	while True:
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="visual studio is the best!"))
		await asyncio.sleep(60)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="py help"))
		await asyncio.sleep(60)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="I hope you are feeling good!"))
		await asyncio.sleep(60)
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="skrrrrrrrrrr"))
		await asyncio.sleep(60)

	loop = asyncio.get_event_loop()
	task = loop.create_task(periodic())
	try:
		loop.run_until_complete(task)
	except asyncio.CancelledError:
		pass


def check(author, kanal):
	def inner_check(message):
		return message.author == author and message.channel == kanal
	return inner_check


def reddit_embed(chosen_subreddit):
	subreddit = reddit.subreddit(str(chosen_subreddit))
	random_submission = subreddit.random()
	memeEmbed = discord.Embed(title=str(random_submission.title),
							  url="https://www.reddit.com" + str(random_submission.permalink), color=0x00ffff)
	memeEmbed.set_image(url=str(random_submission.url))
	memeEmbed.set_footer(text=f"{random_submission.comments}")
	memeEmbed.set_footer(
		text=f"From r/{subreddit.display_name} by: u/{random_submission.author}❤ \n {random_submission.upvote_ratio * 100}% upvote ratio👍 | {random_submission.num_comments}💬")
	return memeEmbed


def reddit_embed_hot(chosen_subreddit, kanal):
	subreddit = reddit.subreddit(chosen_subreddit)
	random_number = random.randint(1, 250)
	for submission in reddit.subreddit(chosen_subreddit).hot(limit=random_number):
		random_submission = submission
	memeEmbed = discord.Embed(title=str(random_submission.title),
							  url="https://www.reddit.com" + str(random_submission.permalink), color=0x00ffff)
	memeEmbed.set_image(url=str(random_submission.url))
	memeEmbed.set_footer(text=f"{random_submission.comments}")
	memeEmbed.set_footer(
		text=f"From r/{subreddit.display_name} by: u/{random_submission.author}❤ \n {random_submission.score}👍 | {random_submission.num_comments}💬")
	if random_submission.over_18:
		if kanal.is_nsfw():
			return memeEmbed
		else:
			memeEmbed = discord.Embed(
				title="This isn't a NSFW channel!", color=0xff0000)
			return memeEmbed
	else:
		return memeEmbed


@client.event
async def on_guild_join(guild):
	welcome_channel = client.get_channel(749324560859529236)

	# ignore this
	await welcome_channel.send('I have been added to {}!'.format(guild.name))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.lower() == "me_irl":
		embedVar = reddit_embed(message.content)
		await message.channel.send(embed=embedVar)

	if message.mentions:
		for mention in message.mentions:
			if mention == client.user.mention:
				pass
			elif mention == message.author:
				pass
			else:
				f = open("afk", "r")
				ludeki = f.read()
				ludeki = ludeki.split(";")
				for ludek in ludeki:
					ludek_reason = ludek.split(",")
					ludek = ludek_reason[0]
					if ludek == str(mention):
						await message.channel.send(f"{mention} is afk! ``{ludek_reason[1]}``")
					else:
						pass
				f.close()

	if message.content.startswith("py"):
		# DONT FORGET TO CHANGE DA PREFIX!

		command = message.content.lower()
		command = command.split(" ")
		if len(command) < 1:
			embedVar = discord.Embed(title="Error:", color=0xff0000)
			embedVar.add_field(name="No command specified:",
							   value="Please check if you're writing the command correctly!", inline=False)
			await message.channel.send(embed=embedVar)
		else:
			command = command[1]

			if command == "help":
				embedVar = discord.Embed(
					title="How to use:", url="https://discord.com/oauth2/authorize?client_id=771315216654008330&scope=bot&permissions=8", color=0x00ffff)
				embedVar.set_thumbnail(
					url="https://cdn.discordapp.com/avatars/771315216654008330/aec8ee04fa7d7b6179a3415dad50e5a4.webp?size=1024")
				embedVar.add_field(
					name="TypeRacer!", value="To play TypeRacer simply type ``py type``!", inline=False)
				embedVar.add_field(
					name="Guess!", value="Type ``py guess`` and start guessing!", inline=False)
				embedVar.add_field(
					name="Coming soon", value="More minigames coming soon.", inline=False)
				embedVar.add_field(
					name="Movie Suggestions!", value="If you are bored and dont know what to do, type ``py movie popular`` to get one popular movie or type ``py movie top`` to get one of the top rated movies!", inline=False)
				embedVar.add_field(
					name="Reddit!", value="``py reddit (subreddit)``", inline=False)
				embedVar.add_field(
					name="Subreddit!", value="Get a description of your favourite subreddits by typing ``py reddit_description (subreddit)``", inline=False)
				embedVar.set_footer(text="Hope you have a great day!")
				msg = await message.channel.send(embed=embedVar)
				await msg.add_reaction("🤍")

			if command == "urnik":
				try:
					razred = message.content.split(" ")[2].upper()
					test = ur.urnik_by_razred(razred)
				except IndexError:
					test = ur.urnik_by_razred("1.B")
				await message.channel.send(embed=test)

			if command == "count":
				client.loop.create_task()
				my_background_task2(message, 1)
				if command == "stop":
					global switch
					switch = False

			if command == "afk":
				try:
					command = message.content.split(" ")[2]
				except:
					command = False
				if command:
					f = open("afk", "w+")
					ludeki = f.read()
					ludeki = ludeki.split(";")
					back = ""
					if command == "remove":
						s = False
						for ludek in ludeki:
							ludek_name = ludek.split(",")[0]
							if ludek_name == str(message.author):
								await message.channel.send("Welcome back!")
								s = True
							else:
								back = back + ludek
						f.write(back)
						f.close()
						if s != True:
							await message.channel.send("You're not on the afk list!")

				else:
					f = open("afk", "r")
					ludeki = f.read()
					ludeki = ludeki.split(";")
					already = False
					for ludek in ludeki:
						ludek = ludek.split(",")[0]
						if ludek == str(message.author):
							already = True
							break
					f.close()
					if already == True:
						await message.channel.send("You're on the afk list already!")
					else:
						try:
							reason = message.content.split(" ")[2]
						except:
							reason = None
						if reason != None:
							pass
						else:
							reason = "No reason provided"
						f = open("afk", "a")
						f.write(f"{message.author},{reason};")
						f.close()
						await message.channel.send("Added to afk!")

			if command == "encrypt":
				await message.delete()
				x = 2
				i = 0
				mesidz = ''
				while i < len(message.content.split(" ")) - 2:
					i += 1
					word = message.content.split(" ")[x]
					if i == len(message.content.split(" ")) - 2:
						pass
					else:
						word = word + " "
					mesidz += word
					x += 1
				encrypted_message = enc.encrypt(key, mesidz)
				await message.channel.send(encrypted_message)
			if command == "decrypt":
				x = 2
				i = 0
				mesidz = ''
				while i < len(message.content.split(" ")) - 4:
					i += 1
					word = message.content.split(" ")[x]
					if i == len(message.content.split(" ")) - 4:
						pass
					else:
						word = word + " "
					mesidz += word
					x += 1
				key3 = message.content.split(" ")
				key3 = key3[3: len(message.content)]
				key3 = key3[0] + " " + key3[1]
				decrypted_message = enc.decrypt(key3, mesidz)
				await message.channel.send(decrypted_message)

			if command == "reddit":
				kanal = message.channel
				chosen_subreddit = message.content.lower()
				chosen_subreddit = chosen_subreddit.split(" ")
				chosen_subreddit = chosen_subreddit[2]
				embedVar = reddit_embed_hot(chosen_subreddit, kanal)

				await message.channel.send(embed=embedVar)

			if command == "reddit_description":

				chosen_subreddit = message.content.lower()
				chosen_subreddit = chosen_subreddit.split(" ")
				chosen_subreddit = chosen_subreddit[2]
				subreddit = reddit.subreddit(str(chosen_subreddit))

				pfp = juje.getpfp("r/" + str(subreddit))

				mods = []
				rules_list = []
				modEmbed = discord.Embed(title="Moderation:", color=0x00ffff)

				unix_timestamp = int(subreddit.created_utc)
				utc_time = time.gmtime(unix_timestamp)
				local_time = time.localtime(unix_timestamp)
				creation = (time.strftime("%Y-%m-%d %H:%M:%S", local_time))
				creation_unix = (time.strftime(
					"%Y-%m-%d %H:%M:%S+00:00 (UTC)", utc_time))

				for moderator in subreddit.moderator():
					mods.append(f"u/{moderator}")
				for rule in subreddit.rules:
					rules_list.append(f"{rule}")

				embedVar = discord.Embed(
					title=f"r/{subreddit.display_name}", url="https://www.reddit.com/r/" + subreddit.display_name + "/", color=0x00ffff)
				embedVar.set_thumbnail(url=pfp)
				embedVar.add_field(name="Number of subscribers:",
								   value=f"{subreddit.subscribers}", inline=False)
				embedVar.add_field(name="Is over 18?",
								   value=f"{subreddit.over18}", inline=False)
				embedVar.add_field(name="Is the user a subscriber?",
								   value=f"{subreddit.user_is_subscriber}", inline=False)
				embedVar.add_field(name="Whether the spoiler tag feature is enabled.",
								   value=f"{subreddit.spoilers_enabled}", inline=False)
				if str(subreddit.public_description) == "":
					pass
				else:
					embedVar.add_field(
						name="Public description:", value=f"{subreddit.public_description}", inline=False)
				embedVar.add_field(name="Subreddit id:",
								   value=f"``{subreddit.id}``", inline=False)
				embedVar.add_field(
					name="Created on:", value=f"{creation}\n{creation_unix}", inline=False)
				embedVar.set_footer(text=f"{subreddit.title}")

				await message.channel.send(embed=embedVar)

				modEmbed.add_field(
					name="Mods:", value=f"```{mods}```", inline=False)
				modEmbed.add_field(
					name="Rules:", value=f"```{rules_list}```", inline=False)
				await message.channel.send(embed=modEmbed)

				# make it better

			if command == "compliment":
				with open("compliments.txt", "r") as compliment:
					compliment = compliment.read()
					selection = compliment.split("\n")
					compliment = random.choice(selection)

				mention = message.mentions

				clovek = message.author.mention if mention == [] else mention[0].mention
				await message.channel.send(f"{clovek}, {compliment}")

			if command == "guess":
				await message.channel.send("Guess!")

				selection = range(1, 11)
				number = random.choices(selection)
				print(number)
				tries = 3

				while tries > 0:
					message = await client.wait_for("message")
					answer = message.content
					print(number)

					if '[' + answer + ']' == str(number):
						selection = [
							'You got it!', 'Nice job!', 'Great guess! You guessed it.', 'A point for you!']
						selection = random.choices(selection)
						await message.channel.send(selection)
						break
					else:
						await message.channel.send("Nope!")
						tries -= 1
						await message.channel.send(f"{tries} tries left!")

			elif command == "type":
				number_of_tries = "x"
				kanal = message.channel
				player = message.author

				while type(number_of_tries) != "int":
					await message.channel.send("Choose your difficulty (easy, medium, hard): ")

					message = await client.wait_for("message", check=check(player, kanal))

					if message.content == "easy":
						number_of_tries = 5
						# multiplier zato, da boš za različno dolge besede meu različno cajta (basically rasiszem za besede)
						time_multiplier = 0.90
						# manjši k je multiplier, manj maš časa (ampak samo če mam matematko 2)
						await message.channel.send('Difficulty set, type "start" to begin!')
						break
					elif message.content == "medium":
						number_of_tries = 3
						time_multiplier = 0.60
						await message.channel.send('Difficulty set, type "start" to begin!')
						break
					elif message.content == "hard":
						number_of_tries = 1
						time_multiplier = 0.30
						await message.channel.send('Difficulty set, type "start" to begin!')
						break
					elif message.content == "quit":
						await message.channel.send('Quit!')
						break
					else:
						# stvar k te odjebe tut če nočš da te odjebe
						await message.channel.send('Unknown command! Please select a difficulty.')

				while number_of_tries > 0:
					score = 0
					message = await client.wait_for("message", check=check(player, kanal))

					if message.content == "help":
						await message.channel.send("help")
					if message.content == "quit":
						await message.channel.send("Exiting...")
						break
					if message.content == "start" and score == 0:
						await message.channel.send("Ready!")
						time.sleep(1)
						await message.channel.send("Set!")
						time.sleep(1)
						await message.channel.send("Go!")
						time.sleep(1)
						while number_of_tries > -1:  # to je gavno k te dejansko sprašuje za za shit
							with open("words.txt", "r") as random_word:
								random_word = random_word.read()
								selection = random_word.split("\n")
								random_word = random.choice(selection)

							# koda k zračuna timeout iz dolžine stringa k ga gor dobimo in difficultija
							dolžina = len(random_word)
							cajt = dolžina * time_multiplier

							# cajt_ms = cajt * 1000

							await message.channel.send("Please write: ``" + random_word + ('``'))

							start_time = time.time()
							try:  # to je treba tko dt ker stvar k ti pove kdaj ti zmanjka časa ti u usta odfuka exception ko se leto zgodi
								message = await client.wait_for("message", check=check(player, kanal), timeout=cajt)

							except asyncio.exceptions.TimeoutError:
								embedVar = discord.Embed(
									title="You ran out of time! ⏱️", color=0xff0000)
								await message.channel.send(embed=embedVar)
								number_of_tries -= 1
								await message.channel.send("**" + str(number_of_tries) + " tries left!**")

							else:  # če ti ne zmanka časa te nebi smeu odfukat

								answer = message.content
								answer_time = time.time()
								# uporab advanced 2nd grade odštevanje da zračuna kok cajta s rabu za odgovor
								took_time = answer_time - start_time
								took_time *= 1000

								if message.author == client.user:
									return
								if answer == "quit":
									await message.channel.send("Exiting...")
									await message.channel.send("**Your score: " + str(score) + "**")
									break
								if answer == random_word:
									await message.channel.send("You got it!")
									score += 1
								else:
									await message.channel.send("oops...")
									number_of_tries -= 1
									await message.channel.send("**" + str(number_of_tries) + " tries left!**")
							if number_of_tries == 0:
								await message.channel.send("**Your score: " + str(score) + "**")
								break

print("Connecting to servers...")
client.run(TOKEN)
