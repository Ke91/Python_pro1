import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def dato(ctx):
    datos = [
        "🌍 En América Latina, más de 100 millones de personas están expuestas a niveles peligrosos de contaminación del aire.",
        "🌊 Cada año, más de 8 millones de toneladas de plástico terminan en los océanos. Gran parte proviene de ríos en zonas urbanas de Latinoamérica.",
        "🚮 El río Riachuelo en Argentina es uno de los más contaminados del mundo, con décadas de desechos industriales y domésticos.",
        "🗑 En muchas ciudades latinoamericanas, solo se recicla entre el 1% y el 10% de la basura generada.",
        "🔥 La quema de basura a cielo abierto es común en áreas rurales, lo que genera gases tóxicos y enfermedades respiratorias.",
        "🌱 Plantar árboles urbanos puede reducir hasta un 30% de la contaminación del aire en zonas densamente pobladas.",
        "🚯 La contaminación del suelo afecta la agricultura en muchas zonas rurales de México, Colombia y Perú, reduciendo la calidad de los alimentos."
        "💧 Más de 36 millones de personas en Latinoamérica no tienen acceso a agua potable debido a la contaminación de fuentes naturales.",
        "🌫️ En ciudades como Ciudad de México, Santiago o Bogotá, la contaminación del aire supera con frecuencia los límites recomendados por la OMS.",
        "🛢️ La contaminación por derrames de petróleo afecta comunidades indígenas y ecosistemas en países como Ecuador, Venezuela y Perú.",
        "🚫 El 70% de las aguas residuales en América Latina se vierten sin tratamiento, contaminando ríos y mares.",
        "🐢 En países costeros como Costa Rica o Colombia, se han encontrado microplásticos en estómagos de peces, tortugas y aves marinas.",
        "🌍 Si todos los habitantes del planeta vivieran como lo hace un ciudadano promedio en Brasil o Argentina, necesitaríamos más de 1.5 planetas para sostener ese estilo de vida.",
        "🌿 En algunos países, se están promoviendo ciudades verdes, como Curitiba (Brasil), ejemplo mundial en transporte público ecológico.",
        "🔥 La deforestación en la Amazonía brasileña y peruana libera millones de toneladas de CO₂, acelerando el cambio climático.",
        "🌾 La contaminación de suelos agrícolas por plaguicidas afecta tanto la biodiversidad como la salud de agricultores y consumidores.",
        "🦠 La exposición prolongada a la contaminación atmosférica está relacionada con enfermedades respiratorias como asma, especialmente en jóvenes."
    ]
    await ctx.send(random.choice(datos))
#si xD
@bot.command()
async def per(ctx):
    datos_peru = [
        "🇵🇪 En Perú, el 85% de las aguas residuales se vierten sin tratamiento, contaminando ríos como el Rímac y el Mantaro.",
        "🌊 El lago Titicaca sufre graves problemas de contaminación por aguas residuales, metales pesados y basura.",
        "🏭 La minería informal contamina suelos y ríos con mercurio, especialmente en la región de Madre de Dios.",
        "🚮 En Lima, se generan más de 8 mil toneladas de basura al día; gran parte termina en botaderos informales.",
        "🔥 La quema de residuos sólidos en zonas urbanas de Perú contribuye a la contaminación del aire.",
        "🌫️ La ciudad de Lima tiene una de las peores calidades de aire de América Latina en épocas de invierno.",
        "🗑️ En muchas comunidades rurales, no existen sistemas de recolección de residuos, lo que genera contaminación local.",
        "🛢️ El derrame de petróleo en la Amazonía peruana ha contaminado fuentes de agua y ha afectado comunidades indígenas.",
        "📉 Solo el 1.9% de los residuos generados en Perú se reciclan, según datos del Ministerio del Ambiente.",
        "🌿 La deforestación ilegal en la Amazonía peruana contribuye al cambio climático y la pérdida de biodiversidad."
    ]

    await ctx.send(random.choice(datos_peru))

@bot.command()
async def arg(ctx):
    datos_argentina = [
        "🇦🇷 El Riachuelo es uno de los ríos más contaminados de América Latina, con altos niveles de plomo y sustancias tóxicas.",
        "🌫️ La contaminación del aire en Buenos Aires supera frecuentemente los límites recomendados por la OMS.",
        "🚯 Solo alrededor del 10% de los residuos sólidos urbanos se reciclan en Argentina.",
        "🏞️ En zonas rurales, el uso excesivo de agroquímicos contamina suelos y fuentes de agua subterránea.",
        "🔥 La quema de residuos a cielo abierto es una práctica común en muchas provincias, generando gases tóxicos.",
        "🌊 En la costa atlántica, la contaminación por plásticos afecta a especies marinas como tortugas y aves.",
        "🧪 El agua subterránea en algunas regiones, como Santiago del Estero, contiene niveles peligrosos de arsénico.",
        "🚗 Las emisiones de vehículos en ciudades grandes contribuyen significativamente al smog urbano.",
        "📉 En muchas ciudades no existen políticas activas para separar residuos o incentivar el reciclaje.",
        "🌳 La deforestación en el norte argentino, especialmente en Salta y Chaco, está destruyendo ecosistemas nativos."
    ]

    await ctx.send(random.choice(datos_argentina))

@bot.command()
async def col(ctx):
    datos_colombia = [
        "🇨🇴 En Colombia, el río Bogotá está gravemente contaminado por vertidos industriales y domésticos.",
        "🌫️ Las ciudades como Bogotá y Medellín enfrentan altos niveles de contaminación del aire, especialmente en épocas secas.",
        "🛢️ El conflicto armado ha dificultado el monitoreo y control de la contaminación por minería ilegal, especialmente en la región del Amazonas.",
        "🌿 La deforestación en la Amazonía colombiana sigue en aumento, impulsada por la expansión de la ganadería y la minería.",
        "🏭 La industria del petróleo ha generado importantes derrames en los ríos de la región del Casanare, afectando ecosistemas locales.",
        "📊 Solo el 17% de los residuos generados en Colombia son reciclados adecuadamente, según datos oficiales.",
        "🚯 En las playas de la costa Caribe, el plástico es una de las principales amenazas para la vida marina.",
        "🌱 El Gobierno ha propuesto varias iniciativas para restaurar las zonas deforestadas, pero la tasa de reforestación sigue siendo insuficiente.",
        "🚗 El transporte vehicular es una de las principales fuentes de contaminación en las grandes ciudades como Cali y Barranquilla.",
        "🔥 Las quemas agrícolas, aunque comunes, afectan la calidad del aire y contribuyen al cambio climático."
    ]

    await ctx.send(random.choice(datos_colombia))    

token = ''

bot.run(token)