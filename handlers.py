from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from aiogram import Router, types, F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.utils.chat_action import ChatActionSender
from moviepy.editor import VideoFileClip
import ffmpeg
import subprocess
import os

router = Router()

FFMPEG_PATH = r'ffmpeg_file/bin/ffmpeg.exe'

@router.message(Command('start'))
async def cmd_start(msg: Message):
    await msg.answer('Привет!🖐\n Я могу сделать любую гифку для тебя☺\n'
                     'Для этого отправь мне видео:)')

@router.message(F.video)
async def on_send_video(msg: Message, bot: Bot):

    # Характеристики гифки
    await msg.reply('Спасибо! Сейчас все будет 🥰')

    video = msg.video
    file_info = await bot.get_file(video.file_id)

    video_path = f"{video.file_id}_input.mp4"
    gif_path = f"{video.file_id}_output.gif"

    await bot.download_file(file_info.file_path, video_path)

    # Настройки для уменьшения размера и продолжительности GIF
    input_args = {
        'ss': 0,
        't': 20
    }
    filter_args = 'scale=320:-1,fps=10'
    output_args = {
        'q:v': 10
    }
    async with ChatActionSender.upload_video(msg.from_user.id, bot) as action:
        ffmpeg.input(video_path, **input_args).output(gif_path, vf=filter_args, **output_args).run(cmd=FFMPEG_PATH)
        # Отправка GIF пользователю
        img = FSInputFile(gif_path)
        await msg.answer_document(img)

        os.remove(video_path)
        os.remove(gif_path)

@router.message(F.photo | F.audio | F.document)
async def notvideo_answer(msg: Message):
    await msg.answer(f'Думаю это не видео🤔')

@router.message(F.animation)
async def notvideo_answer(msg: Message):
    await msg.answer('Ухты, какая красота! 🥰❤')

