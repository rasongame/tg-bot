from aiogram import types


async def start_msg(message: types.Message):
    msg = """
    Some things here...
    """
    await message.answer(msg)
    return

async def help_msg(message: types.Message):
    msg = """
    Some things here
    """
    await message.answer(msg)
    return