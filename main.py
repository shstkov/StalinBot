from interactions import User
from interactions import Permissions
import roles
from interactions.models import Intents
from interactions import (
    Client,
    OptionType,
    Role,
    SlashContext,
    slash_option,
    slash_command,
)
from os import getenv
from dotenv import load_dotenv

load_dotenv()
token = getenv("bot_token")
bot = Client(intents=Intents.ALL)


@slash_command(
    name="образоватьнквд",
    description="Верные нашей родине смогут исполнять свой священный долг!",
)
@slash_option(
    name="role",
    description="Верные нашей родине",
    required=True,
    opt_type=OptionType.ROLE,
)
async def setup_nkvd(ctx: SlashContext, role: Role):
    if ctx.author.has_permission(Permissions.ADMINISTRATOR):
        roles.setup_nkvd_role(role)
        await ctx.send(
            "Товарищи! Хочу всех поздравить с отличнейшим событием - образование НКВД! Ура товарищи!"
        )
        await ctx.send("https://klipy.com/gifs/stalin-memy")
    else:
        await ctx.send("Товарищь! А не много ли вы себе позволяете?")


@slash_command(
    name="образоватьгулаг",
    description="Неверные нашей родине будут наказаны!",
)
@slash_option(
    name="role",
    description="Неверные нашей родине",
    required=True,
    opt_type=OptionType.ROLE,
)
async def setup_gulag(ctx: SlashContext, role: Role):
    if await roles.check_nkvd(ctx, ctx.author):
        roles.setup_gulag_role(role)
        await ctx.send(
            "Товарищи! Отныне все неверные нашему величайшему государству будут отправляться в ГУЛАГ! Ура товарищи!"
        )
        await ctx.send("https://klipy.com/gifs/stalin-soviet-2")


@slash_command(
    name="вгулаг",
    description="Неверный нашей родине будет наказан!",
)
@slash_option(
    name="user",
    description="Неверный нашей родине",
    required=True,
    opt_type=OptionType.USER,
)
async def into_gulag(ctx: SlashContext, user: User):
    if await roles.check_gulag(ctx) is False:
        return
    if await roles.check_nkvd(ctx, ctx.author):
        await user.send(
            "https://tenor.com/view/%D0%BC%D1%83%D0%B4%D0%B8%D0%BB%D0%B0-%D1%81%D1%81%D1%81%D1%80-ussr-stalin-mudila-gif-16990551258572186886"
        )
        for member in ctx.guild.members:
            if member.user == user:
                await member.add_role(roles.gulag_role)
                break
        await ctx.send(
            f"{user.display_name} был сослан в гулаг! Ура товарищи! Туда ему дорога!"
        )
        await ctx.send(
            "https://tenor.com/view/%D0%BC%D1%83%D0%B4%D0%B8%D0%BB%D0%B0-%D1%81%D1%81%D1%81%D1%80-ussr-stalin-mudila-gif-16990551258572186886"
        )


bot.start(token)
