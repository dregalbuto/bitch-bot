#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import datetime
from datetime import date
import calendar

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('/help'):
		await client.send_message(message.channel, 
			'Hewwo {0.author.mention} OwO'.format(message)
			+ '\nMy name is bitch-bot~'
			+ '\nI respond to:'
			+ '\n\t/hello'
			+ '\n\t/help'
			+ '\n\t/bigboss'
			+ '\n\t/pissonme'
			+ '\n\t/pussy [day optional]')

	if message.content.startswith('/hello'):
		await client.send_message(message.channel, 
			'Hewwo {0.author.mention} OwO'.format(message))

	if "hewwo" in message.content.lower():
		await client.send_message(message.channel, 'HEWWO?!')

	if message.content.startswith('/bigboss'):
		await client.send_message(message.channel, 
			'No one will ever be as ruggedly handsome as big boss, nor will '
			+ 'they fuck as hard. it\'s just something you have to accept '
			+ 'and move on')

	if message.content.startswith('/navyseal'):
			await client.send_message(message.channel,
			'What the fuck did you just fucking say about me, you little '
			+ 'bitch? I’ll have you know I graduated top of my class in the '
			+ 'Navy Seals, and I’ve been involved in numerous secret raids on '
			+ 'Al-Quaeda, and I have over 300 confirmed kills. I am trained '
			+ 'in gorilla warfare and I’m the top sniper in the entire US '
			+ 'armed forces. You are nothing to me but just another target. '
			+ 'I will wipe you the fuck out with precision the likes of which '
			+ 'has never been seen before on this Earth, mark my fucking '
			+ 'words. You think you can get away with saying that shit to me '
			+ 'over the Internet? Think again, fucker. As we speak I am '
			+ 'contacting my secret network of spies across the USA and your '
			+ 'IP is being traced right now so you better prepare for the '
			+ 'storm, maggot. The storm that wipes out the pathetic little '
			+ 'thing you call your life. You’re fucking dead, kid. I can be '
			+ 'anywhere, anytime, and I can kill you in over seven hundred '
			+ 'ways, and that’s just with my bare hands. Not only am I '
			+ 'extensively trained in unarmed combat, but I have access to '
			+ 'the entire arsenal of the United States Marine Corps and I '
			+ 'will use it to its full extent to wipe your miserable ass off '
			+ 'the face of the continent, you little shit. If only you could '
			+ 'have known what unholy retribution your little “clever” comment '
			+ 'was about to bring down upon you, maybe you would have held '
			+ 'your fucking tongue. But you couldn’t, you didn’t, and now '
			+ 'you’re paying the price, you goddamn idiot. I will shit fury '
			+ 'all over you and you will drown in it. You’re fucking dead, '
			+ 'kiddo.');

	if message.content.startswith('/pissonme'):
		await client.send_message(message.channel, 
			'PISS ON ME FUCKING PISS ON ME BUT DO IT IN THE ANTARCTIC SO THAT '
			+ 'THE PEE FREEZES IN MID AIR WHILE YOU ARE PISSING OFF A '
			+ 'BUILDING AND THE PISS TURNS TO SPEAR’S IMPALE ME WITH FROZEN '
			+ 'URINE AND THEN SHIT ON MY BUTT CORPSE IM A FAT GAY AND I WANT '
			+ ' TO GO TO ICE HELL FTW')

	if message.content.startswith('/pussy'):
		msg = message.content.lstrip('/pussy ') 
		if len(msg) < 1:
			await client.send_message(message.channel, 'What day is it?')
			msg = (await client.wait_for_message(author=message.author)).content
		await client.send_message(message.channel, 
			'No offense but... it\'s {} '.format(msg)
			+ '*rips wax strip off my pussy*')

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	today = calendar.day_name[date.today().weekday()]
	await client.send_message(client.get_channel('370994252915671050'),
		'No offense but... it\'s {} '.format(today)
		+ '*rips wax strip off my pussy*')
	print('!')

client.run('MzcwNjM2NzQzMDg0NDc0MzY5.DMvFkA.6_YuYKfKAqh7JCWN8cnsMdSMNZw')
