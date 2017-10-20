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
			'Hewwo {0.author.mention} OwO'
			+ '\nMy name is bitch-bot~'
			+ '\nI respond to:'
			+ '\n\t/hello'
			+ '\n\t/help'
			+ '\n\t/bigboss'
			+ '\n\t/pissonme'
			+ '\n\t/pussy [day optional]'
			.format(message))

	if message.content.startswith('/hello'):
		await client.send_message(message.channel, 
			'Hewwo {0.author.mention} OwO'.format(message))

	if message.content.startswith('/bigboss'):
		await client.send_message(message.channel, 
			'No one will ever be as ruggedly handsome as big boss, nor will '
			+ 'they fuck as hard. it\'s just something you have to accept '
			+ 'and move on')

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
			'No offense but... it\'s {} '
			+ '*rips wax strip off my pussy*'.format(msg))

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	today = calendar.day_name[date.today().weekday()]
	await client.send_message(client.get_channel('370994252915671050'),
		'No offense but... it\'s {} *rips wax strip off my pussy*'.format(today))
	print('!')

client.run('MzcwNjM2NzQzMDg0NDc0MzY5.DMvFkA.6_YuYKfKAqh7JCWN8cnsMdSMNZw')
