from typing import Callable, Coroutine, Dict, List, Union
from interactions import Client, Member, OptionType, Permissions, Role, SlashCommand, SlashCommandOption, SlashContext, User
import roles

async def send_to_gulag(member: Member):
    await member.remove_roles(member.roles)
    await member.add_role(roles.get_gulag_role())
    await member.send("https://tenor.com/view/%D0%BC%D1%83%D0%B4%D0%B8%D0%BB%D0%B0-%D1%81%D1%81%D1%81%D1%80-ussr-stalin-mudila-gif-16990551258572186886")

async def shoot(member: Member):
    await member.send("https://klipy.com/gifs/stalin-photoshop-1")
    await member.ban(reason="РАССТРЕЛЯН")
    
def is_user_on_gulag(member: Member) -> bool:
    return member.has_role(roles.get_gulag_role())

def is_it_stalin(ctx: SlashContext, user: User) -> bool:
    return ctx.bot.get_member(ctx.bot.user.id, ctx.guild_id) is user.client.get_member(user.id, ctx.guild_id)

async def gulag_init(ctx: SlashContext, role: Role):
    print(f"{ctx.author.display_name} called command gulag_init")
    roles.setup_gulag_role(role)
    await ctx.send("Товарищи! Отныне все неверные нашему величайшему государству будут отправляться в ГУЛАГ! Ура товарищи!")
    await ctx.send("https://klipy.com/gifs/stalin-soviet-2")

async def to_gulag(ctx: SlashContext, user: User):
    print(f"{ctx.author.display_name} called command send_to_gulag for {user.display_name}")
    if roles.check_gulag_role is None:
        await ctx.send("Товарищь! С радостью бы его отправил, только вот ГУЛАГа нету!")
        return
    if is_user_on_gulag(user.client.get_member(user.id, ctx.guild_id)):
        await ctx.send("Товарищь! Так он уже в ГУЛАГе!")
        await ctx.send("https://klipy.com/gifs/stalin-joseph")
        return
    if is_it_stalin(ctx, user):
        await ctx.send("Товарищь! Вы ничего не попутали? В ГУЛАГ!")
        await ctx.send("https://tenor.com/view/%D0%BC%D1%83%D0%B4%D0%B8%D0%BB%D0%B0-%D1%81%D1%81%D1%81%D1%80-ussr-stalin-mudila-gif-16990551258572186886")
        await send_to_gulag(ctx.author)
        return
    await send_to_gulag(user.client.get_member(user.id, ctx.guild_id))
    await ctx.send(f"{user.display_name} был отправлен в ГУЛАГ! Это победа товарищи! Ура!")
    await ctx.send("https://tenor.com/view/%D0%BC%D1%83%D0%B4%D0%B8%D0%BB%D0%B0-%D1%81%D1%81%D1%81%D1%80-ussr-stalin-mudila-gif-16990551258572186886")

async def to_shoot(ctx: SlashContext, user: User):
    print(f"{ctx.author.display_name} called command shoot for {user.display_name}")
    if is_it_stalin(ctx, user):
        await ctx.send("Ох, товарищь! Это было зря...")
        await ctx.send("https://klipy.com/gifs/stalin-photoshop-1")
        await shoot(ctx.author)
        return
    await shoot(user.client.get_member(user.id, ctx.guild_id))
    await ctx.send(f"{user.display_name} был расстрелян! Это величайшая победа нашей великой родины, товарищи! Ура!")
    await ctx.send("https://klipy.com/gifs/stalin-photoshop-1")

def new_cmd(bot: Client, name: str, desc: str, permission: Permissions, options: List[Union[SlashCommandOption, Dict]], callback: Callable[..., Coroutine]):
    bot.add_interaction(
        SlashCommand(
            name=name,
            description=desc,
            default_member_permissions=permission,
            options=options,
            callback=callback
        ),
    )

def init(bot: Client):
    # /организоватьгулаг [role]
    new_cmd(
        bot=bot,
        name="организоватьгулаг",
        desc="Неверные нашей великой родине будут наказаны!",
        permission=Permissions.ADMINISTRATOR,
        options=[
            SlashCommandOption(
                name="role",
                description="Неверные нашей родине",
                required=True,
                type=OptionType.ROLE
            )
        ],
        callback=gulag_init
    )

    # /отправитьвгулаг [user]
    new_cmd(
        bot=bot,
        name="отправитьвгулаг",
        desc="Неверные нашей великой родине будут наказаны!",
        permission=Permissions.ADMINISTRATOR,
        options=[
            SlashCommandOption(
                name="user",
                description="Неверный нашей родине",
                required=True,
                type=OptionType.USER
            )
        ],
        callback=to_gulag
    )
    # /освободитьизгулага [user]
    # /запугать [user] [time]
    # /расстрелять [user]
    new_cmd(
        bot=bot,
        name="расстрелять",
        desc="РАССТРЕЛЯТЬ!",
        permission=Permissions.ADMINISTRATOR,
        options=[
            SlashCommandOption(
                name="user",
                description="Неверный нашей родине",
                required=True,
                type=OptionType.USER
            )
        ],
        callback=to_shoot
    )
