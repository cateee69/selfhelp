"""os module for reboot"""
import os

# sys module for kill & reboot
import sys

# json module for checker
import json

# discord.py-self that the whole bot is based on
import discord


class MyClient(discord.Client):
    """definding our class"""

    async def on_ready(self, ):
        """so i can see when the bot is online"""
        print(
            "Logged on as",
            self.user,
        )

    async def on_message(
        self,
        message,
    ):
        """most command shit"""
        # don't respond to ourselves
        if (message.author == self.user):
            return
        if (message.content.lower() == "tos!discum"):
            embed = discord.Embed(
                title="discum",
                description=(
                    "this command shows you the proper way to install discum"),
                color=0xB400EB,
            )
            embed.set_author(name="selfhelp")
            embed.add_field(
                name=("if pip doesn't work"),
                value=("try `python -m pip`"),
                inline=False,
            )
            embed.add_field(
                name=("to install discum"),
                value=
                ("you should use this `python -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum`\nif that doesn't work download git"
                 ),
                inline=False,
            )
            embed.add_field(
                name=("git link"),
                value=
                "[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)",
                inline=False,
            )
            await message.channel.send(embed=embed)
        if (message.content.lower() == "tos!help"):
            embed = discord.Embed(
                title=("help command"),
                description=("basic help menu"),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            embed.add_field(
                name="tos!general",
                value=("useful & general purpose commands"),
                inline=False,
            )
            embed.add_field(
                name="tos!errors",
                value=("some errors people have when using dmdmgo"),
                inline=False,
            )
            embed.add_field(
                name=("tos!status "),
                value=("for invalid status code errors"),
                inline=False,
            )
            embed.add_field(
                name="tos!tutorials",
                value=
                ("explanations of stuff & some 'tutorials(not emplemented yet )'"
                 ),
                inline=False,
            )
            embed.add_field(
                name="tos!oldhelp",
                value=("deprecate help menu"),
                inline=False,
            )
            await message.channel.send(embed=embed)
        if (message.content.lower() == "tos!general"):
            embed = discord.Embed(
                title=("general "),
                description=("some useful commands"),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            embed.add_field(
                name="tos!build",
                value=(
                    "creates message.json \nfor usage do tos!build urmessage"),
                inline=False,
            )
            embed.add_field(
                name="tos!validate",
                value=("validates jsons(message.json)"),
                inline=False,
            )
            embed.add_field(
                name="tos!ping",
                value=("Check the bot's ping"),
                inline=False,
            )
            embed.add_field(
                name="tos!reboot",
                value=("reboots the bot"),
                inline=False,
            )
            embed.add_field(
                name="tos!kill",
                value=("stops the bot"),
                inline=True,
            )
            await message.channel.send(embed=embed)
        if (message.content.lower() == "tos!errors"):
            embed = discord.Embed(
                title=(
                    "errors(some errors people have excluding status codes)"),
                description=(
                    "(some errors people have excluding status codes)"),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            embed.add_field(
                name="padding",
                value=
                ("its dmdgo fault prolly trying to decompress gz/tr using brotli"
                 ),
                inline=False,
            )
            embed.add_field(
                name=("tokens sleeping"),
                value=
                ("your token is rate limited its gonna stop for 13 minuts or whatever is in the config and no its not banned"
                 ),
                inline=True,
            )
            embed.add_field(
                name=("invalid character e"),
                value=
                ("if its while joining you are getting cloudflare ratelimited\nif its while while mass dming try to disable check mutual"
                 ),
                inline=True,
            )
            await message.channel.send(embed=embed)
        if message.content.lower().startswith("tos!build"):
            form = message.content.replace(
                "tos!build ",
                "",
            )
            form = form.replace(
                "\n",
                r"\n",
            )
            await message.channel.send(f"""```{{
    "content" : "{form}"
}}```""")
        if (message.content.lower() == "tos!reboot"):
            if (message.author.id == 862282426860699678):
                embed = discord.Embed(
                    title=("reboot "),
                    description=("the bot has been rebooted"),
                    color=0xB400EB,
                )
                embed.set_author(
                    name="selfhelp",
                    icon_url=
                    "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
                )
                await message.channel.send(embed=embed)
                os.system("python t.py")
                sys.exit()
            else:
                embed = discord.Embed(
                    title=("reboot "),
                    description=("rebooting failed"),
                    color=0xB400EB,
                )
                embed.set_author(
                    name="selfhelp",
                    icon_url=
                    "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
                )
                embed.add_field(
                    name="reason",
                    value=("command executed by a non authorized member"),
                    inline=True,
                )
                await message.channel.send(embed=embed)
        if (message.content.lower() == "tos!kill"):
            if (message.author.id == 862282426860699678):
                embed = discord.Embed(
                    title=("kill command"),
                    description=("the bot has been killed"),
                    color=0xB400EB,
                )
                embed.set_author(
                    name="selfhelp",
                    icon_url=
                    "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
                )
                await message.channel.send(embed=embed)
                sys.exit()
            else:
                embed = discord.Embed(
                    title=("kill command"),
                    description=("killing failed"),
                    color=0xB400EB,
                )
                embed.set_author(
                    name="selfhelp",
                    icon_url=
                    "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
                )
                embed.add_field(
                    name="reason",
                    value=("command executed by a non authorized member"),
                    inline=True,
                )
                await message.channel.send(embed=embed)
        if message.content.startswith("tos!validate"):
            await message.channel.send("validating....")
            file = message.content.replace(
                "tos!validate ",
                "",
            )
            try:
                json.loads(file)
            except ValueError as err:
                await message.channel.send(f"Invalid JSON: {err}"
                                           )  # in case json is invalid
            else:
                await message.channel.send("Valid JSON")
        if (message.content.lower() == "tos!e"):
            embed = discord.Embed(
                title=("error invalid character e"),
                description=(
                    "you are being cloudflare ratelimited try using a vpn/proxy"
                ),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            await message.channel.send(embed=embed)
        if (message.content.lower() == "<@924234682973962312>"):
            embed = discord.Embed(
                title=("basic introduction"),
                description=
                ("hi im selfhelp i am going to help you run dmdgo\nto start and see commands u can run do tos!help to show some of the commands or tos!inf to see all the commands"
                 ),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            await message.channel.send(embed=embed)
        if (message.content.lower() == "tos!rate_limit_delay"):
            embed = discord.Embed(
                title=("ratelimit delay"),
                description=
                ("Duration in seconds to wait when Discord rate limits sending DMs"
                 ),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            await message.channel.send(embed=embed)
        if (message.content.lower() == "individual_delay"):
            embed = discord.Embed(
                title=("individual delay"),
                description=
                ("Duration in seconds between 2 consecutive messages from a single discord token"
                 ),
                color=0xB400EB,
            )
            embed.set_author(
                name="selfhelp",
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            await message.channel.send(embed=embed)
        if ("tos!status" == message.content.lower()):
            embed = discord.Embed(
                title=("status codes "),
                description=(
                    "explanations of various errors(404/403/400/401)etc. "),
                color=0xB400EB,
            )
            embed.set_author(
                name=("selfhelp "),
                icon_url=
                "https://cdn.discordapp.com/avatars/924234682973962312/69121357c1d0a67836120c6bc496836d.png?size=2048",
            )
            embed.add_field(
                name="400",
                value=
                ("Error 400 is a malformed request and is a fault at your end. Either the channel IDs are wrong / the token is trying to DM itself. Or your message is empty (Empty messages can't be sent on discord) stuff like that."
                 ),
                inline=False,
            )
            embed.add_field(
                name="401",
                value=
                ("invalid token locked/disabled (yes you cant unlock a locked token)"
                 ),
                inline=False,
            )
            embed.add_field(
                name="403",
                value=
                ("403 arrises due to several reasons - You're blocked by the reciever, you don't share a mutual server with them, you're phone locked, you're email locked, You haven't completed member screening, reciever's DMs are closed, etc"
                 ),
                inline=False,
            )
            embed.add_field(
                name="405",
                value=
                ("Error 405 usually happens when you try to do something that can't be done normally on discord, based on how the program works, this might arise if your tokens get locked/ disabled"
                 ),
                inline=False,
            )
            embed.add_field(
                name="404",
                value=
                ("you probably put the whole invite instead of the code if the invite is discord.gg/selfbot the code is selfbot"
                 ),
                inline=False,
            )
            await message.channel.send(embed=embed)
        if ("tos!padding" == message.content.lower()):
            await message.channel.send(
                "The error simply tells you that the buffer represented by the stream is not properly compressed, so it cannot be decompressed\nbasicly its badly compressed\nyou can try to run dmdgo again "
            )
        if ("tos!ping" == message.content.lower()):
            await message.channel.send(f"pong {round(self.latency, 1)}")
        if ("tos!install" == message.content.lower()):
            await message.channel.send(
                "to install on windows you need to download the exe from releases \nhttps://github.com/V4NSH4J/discord-mass-DM-GO/releases/latest\ndownload windows and extract it \nput ur ids, tokens, and run the exe "
            )
        if ("tos!scrape" == message.content.lower()):
            await message.channel.send(
                "make sure u have python installed and run pip install discum after that run the python file in the scraper folder edit the file using notepad or smth put there channel id server id and token for easier usage use https://cdn.discordapp.com/attachments/905132747549458452/906659591620788244/member_id_scraper.py "
            )
        if ("tos!xyliase" == message.content.lower()):
            await message.channel.send("xyliase is shit dont buy")
        if ("exordium" in message.content.lower()):
            await message.channel.send(
                "exordium is a scammer if u bought smth u got scammed")
        if ("tos!404" == message.content.lower()):
            await message.channel.send(
                "put only the code not the whole invite \n https://discord.gg/selfbot > selfbot"
            )
        if ("tos!405" == message.content.lower()):
            await message.channel.send(
                "method not allowed you probably tried to do a post request when u r supposed to do a get etc"
            )
        if ("tos!400" == message.content.lower()):
            await message.channel.send(
                "99% of the times you've entered wrong member IDs Error 400 is a malformed request and is a fault at your end. Either the channel IDs are wrong / the token is trying to DM itself. Or your message is empty (Empty messages can't be sent on discord) stuff like that. "
            )
        if ("tos!sleep" == message.content.lower()):
            await message.channel.send(
                "your token is rate limited its gonna stop for 13 minuts or whatever is in the config and no its not banned "
            )
        if ("tos!virus" == message.content.lower()):
            await message.channel.send("""```
It's not a virus it's just that the source code gets seen as it which
it isn't, read more about it here:
<https://go.dev/doc/faq#virus>```""")
        print(
            message.content.lower(),
            message.author,
        )
        if ("tos!oldhelp" == message.content.lower()):
            embed = discord.Embed(
                title=("help command"),
                description=("shows you the commands you can run"),
                color=0xB400EB,
            )
            embed.set_author(name="selfhelp")
            embed.add_field(
                name="tos!xyliase",
                value=("check it ur self "),
                inline=False,
            )
            embed.add_field(
                name="tos!404",
                value=("if u have error 404 in joiner"),
                inline=False,
            )
            embed.add_field(
                name="tos!scrape",
                value=("shows you how to scrape"),
                inline=False,
            )
            embed.add_field(
                name="tos!405",
                value=("if u had error 405"),
                inline=False,
            )
            embed.add_field(
                name="tos!400",
                value=("shows u what to do if u have error 400"),
                inline=False,
            )
            embed.add_field(
                name="tos!sleep",
                value=("what to do to do if tokens are sleeping"),
                inline=False,
            )
            embed.add_field(
                name="tos!virus",
                value=("if ur anti virus flags dmd go"),
                inline=False,
            )
            embed.add_field(
                name="tos!selfhelp",
                value=(r"steps to fix anything ur self¯\_(ツ)_/¯"),
                inline=False,
            )
            embed.add_field(
                name="tos!install",
                value=("steps for installing dmdgo"),
                inline=False,
            )
            embed.add_field(
                name="tos!403",
                value=("if u have error 403"),
                inline=False,
            )
            embed.add_field(
                name="tos!ping",
                value=("shows bot ping"),
                inline=False,
            )
            embed.add_field(
                name=("tos! padding"),
                value=("padding if u have padding error"),
                inline=False,
            )
            embed.add_field(
                name="tos!build",
                value=
                ("helps you to make message.json for usage do tos!build the message"
                 ),
                inline=False,
            )
            embed.add_field(
                name="tos!status",
                value=(" if you have errors like 403 405 401"),
                inline=False,
            )
            embed.add_field(
                name="tos!individual_delay",
                value=("shows you what is individual_delay"),
                inline=False,
            )
            embed.add_field(
                name="tos!rate_limit_delay",
                value=("shows you whats ratelimit delay"),
                inline=False,
            )
            embed.add_field(
                name="tos!validate",
                value=("validates message.json to check if its valid or no"),
                inline=False,
            )
            embed.add_field(
                name="tos!e",
                value=("if you got error invalid character e while joining "),
                inline=False,
            )
            embed.set_footer(text=("i am following tos"))

            await message.channel.send(embed=embed)
        if ("tos!403" == message.content.lower()):
            await message.channel.send(
                "if you got it while joining/bypassing the server has phone verification and u need phone verified tokens "
            )
        if ("tos!selfhelp" == message.content.lower()):
            await message.channel.send("""
Steps for selfhelp:
step 1: read the readme.md https://github.com/V4NSH4J/discord-mass-DM-GO scroll down a little bit
step 2: read thereadme.md again
step 3: watch the video https://youtu.be/3m56RTbThbg
step 4: try it even when you dont know whats going on
step 5: try it again but this time follow each step of the video
step 7: wait a day and start from step 1 again
step 8: once youre done with step 7 once and still dont know how to run it you come here and ask for help
> message by siegfried""")


client = (MyClient())
client.run("token")
