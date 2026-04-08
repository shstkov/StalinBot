from interactions import SlashContext
from interactions import Member
from interactions import Role

nkvd_role: Role = None
gulag_role: Role = None


def setup_nkvd_role(role: Role):
    global nkvd_role
    nkvd_role = role


def setup_gulag_role(role: Role):
    global gulag_role
    gulag_role = role


async def check_nkvd(ctx: SlashContext, member: Member) -> bool:
    if nkvd_role is None:
        await ctx.send(
            "Товарищь! Мы ничего с врагами народа не сможем сделать, пока у нас нет НКВД!"
        )
        return False
    if member.has_role(nkvd_role):
        return True
    else:
        await ctx.send("Товарищь! А не много ли вы себе позволяете?")
        return False


async def check_gulag(ctx: SlashContext) -> bool:
    if gulag_role is None:
        await ctx.send(
            "Товарищь! Мы ничего с врагами народа не сможем сделать, пока у нас нет ГУЛАГА!"
        )
        return False
    else:
        return True
