from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
import os
from runner import alive

ch = 904359885909688411

sched = AsyncIOScheduler(timezone='Asia/Bangkok')

def c_d(teach, link):
	return "**Teacher** : " + teach + "\n**Link** : " + link

async def kim():
	chan = client.get_channel(ch)
	res = discord.Embed(title="EN32102", description=c_d("Somanat/Kimberly", "https://meet.google.com/lookup/aqwjoc5qw4?authuser=0&hs=179"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def social():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SO32103/SO32202", description=c_d("Weerarat", "https://meet.google.com/dqz-jefg-got?authuser=0&hs=179"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def niwpong():
	chan = client.get_channel(ch)
	res = discord.Embed(title="MA32202", description=c_d("Woratep", "https://us02web.zoom.us/j/6463824790?pwd=ZmRZcU1NT1RaRW12M24wRXRKM2c4UT09"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def com():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32182/SC30289", description=c_d("Yuwadee", "https://meet.google.com/fkc-sogg-uhp?authuser=0&hs=179"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def bio():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32244", description=c_d("Kwanjai", "https://meet.google.com/lookup/dk4vbsauko"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def chem():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32224", description=c_d("Trakool", "https://meet.google.com/lookup/fs2mb4nn6o"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def thai():
	chan = client.get_channel(ch)
	res = discord.Embed(title="TH32102", description=c_d("Sutchai", "https://meet.google.com/kay-kpqp-ebr?authuser=0&hs=179"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def art():
	chan = client.get_channel(ch)
	res = discord.Embed(title="AR32102", description=c_d("Kittisak", "https://meet.google.com/lookup/fmpewevwuz"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def health():
	chan = client.get_channel(ch)
	res = discord.Embed(title="HP32102", description=c_d("Chantawat", "None"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def parinya():
	chan = client.get_channel(ch)
	res = discord.Embed(title="MA23112", description=c_d("Parinya", "https://meet.google.com/shw-upvo-yjw?authuser=0"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def phy():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32204", description=c_d("Paitoon", "https://meet.google.com/ixf-snzt-jtx"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def history():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SO32104", description=c_d("Nisalai", "https://meet.google.com/lookup/eywcabf4ya"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def homeroom():
	chan = client.get_channel(ch)
	res = discord.Embed(title="Homeroom", description=c_d("Trakool/Natapon", "https://meet.google.com/lookup/fs2mb4nn6o"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def phy2():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32112", description=c_d("Ornanong", "https://meet.google.com/bgd-dnhk-tvw?authuser=0&hs=179"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def eng():
	chan = client.get_channel(ch)
	res = discord.Embed(title="EN32202", description=c_d("Waraporn", "https://meet.google.com/lookup/dcxdxsg2bj"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def iot():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32283", description=c_d("Wattana", "https://meet.google.com/nqm-xxko-jcf"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def ot():
	chan = client.get_channel(ch)
	res = discord.Embed(title="OT32102", description=c_d("Amornrat", "None"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def eng2():
	chan = client.get_channel(ch)
	res = discord.Embed(title="OT32102", description=c_d("Somanat", "https://meet.google.com/lookup/a2nnrqnvnc"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def soccer():
	chan = client.get_channel(ch)
	res = discord.Embed(title="HP30204", description=c_d("Ekkaluk", "None"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def project():
	chan = client.get_channel(ch)
	res = discord.Embed(title="SC32284", description=c_d("Natapon", "https://meet.google.com/acb-sinx-vkg"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def guid():
	chan = client.get_channel(ch)
	res = discord.Embed(title="DA30904", description=c_d("Thanapon", "https://meet.google.com/lookup/ct3fpumjpt"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

async def john():
	chan = client.get_channel(ch)
	res = discord.Embed(title="EN30020", description=c_d("Waraporn/John", "https://meet.google.com/lookup/htnhbx2gv5"), color=discord.Color.from_rgb(255, 203, 251))
	await chan.send(embed=res)

# Monday
sched.add_job(kim, 'cron', day_of_week='mon', hour=8, minute=15)
sched.add_job(social, 'cron', day_of_week='mon', hour=8, minute=55)
sched.add_job(niwpong, 'cron', day_of_week='mon', hour=9, minute=45)
sched.add_job(com, 'cron', day_of_week='mon', hour=10, minute=25)
sched.add_job(bio, 'cron', day_of_week='mon', hour=11, minute=45)
sched.add_job(chem, 'cron', day_of_week='mon', hour=13, minute=15)
sched.add_job(thai, 'cron', day_of_week='mon', hour=13, minute=55)
sched.add_job(art, 'cron', day_of_week='mon', hour=14, minute=35)

# Tuesday
sched.add_job(health, 'cron', day_of_week='tue', hour=8, minute=15)
sched.add_job(parinya, 'cron', day_of_week='tue', hour=8, minute=55)
sched.add_job(phy, 'cron', day_of_week='tue', hour=9, minute=45)
sched.add_job(social, 'cron', day_of_week='tue', hour=11, minute=45)
sched.add_job(history, 'cron', day_of_week='tue', hour=12, minute=35)
sched.add_job(niwpong, 'cron', day_of_week='tue', hour=13, minute=15)

# Wednesday
sched.add_job(homeroom, 'cron', day_of_week='wed', hour=8, minute=15)
sched.add_job(phy2, 'cron', day_of_week='wed', hour=8, minute=55)
sched.add_job(eng, 'cron', day_of_week='wed', hour=10, minute=25)
sched.add_job(niwpong, 'cron', day_of_week='wed', hour=11, minute=45)
sched.add_job(thai, 'cron', day_of_week='wed', hour=12, minute=35)
sched.add_job(iot, 'cron', day_of_week='wed', hour=13, minute=15)

# Thursday
sched.add_job(parinya, 'cron', day_of_week='thu', hour=8, minute=15)
sched.add_job(ot, 'cron', day_of_week='thu', hour=8, minute=55)
sched.add_job(chem, 'cron', day_of_week='thu', hour=9, minute=45)
sched.add_job(eng2, 'cron', day_of_week='thu', hour=11, minute=45)
sched.add_job(soccer, 'cron', day_of_week='thu', hour=12, minute=35)
sched.add_job(bio, 'cron', day_of_week='thu', hour=13, minute=15)
sched.add_job(project, 'cron', day_of_week='thu', hour=13, minute=55)

# Friday
sched.add_job(phy2, 'cron', day_of_week='fri', hour=8, minute=15)
sched.add_job(guid, 'cron', day_of_week='fri', hour=8, minute=55)
sched.add_job(com, 'cron', day_of_week='fri', hour=9, minute=45)
sched.add_job(parinya, 'cron', day_of_week='fri', hour=10, minute=25)
sched.add_job(john, 'cron', day_of_week='fri', hour=11, minute=45)
sched.add_job(niwpong, 'cron', day_of_week='fri', hour=12, minute=35)
sched.add_job(phy, 'cron', day_of_week='fri', hour=13, minute=55)
sched.start()
client = discord.Client()

@client.event
async def on_ready():
	print('hello world')

alive()
client.run(os.environ['TOKEN'])