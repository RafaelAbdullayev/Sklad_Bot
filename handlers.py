from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as md
import os
from utils import create_doc

class Form(StatesGroup):
    doc_name = State() 
    doc_number = State() 
    doc_date = State()
    Name_client = State() 
    Name_client_organization = State() 
    addres_client = State()
    Payment_account_client = State() 
    name_of_the_bank_client = State() 
    bic_bank_client = State()
    phone_client = State() 

async def cmd_start(message: types.Message):
    await Form.doc_name.set()
    await message.answer("Здравствуйте! Вас приветствует телеграмм бот заполнения документов.")
    await message.answer("Введите название документа.")

async def document_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['doc_name'] = message.text
    await Form.next()
    await message.answer("Введите номер документа?")

async def document_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['doc_number'] = message.text
    await Form.next()
    await message.answer("Введите дату документа в формате дд.мм.гг?")

async def process_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['doc_date'] = message.text
    await Form.next()
    await message.answer("Введите имя клиента?")

async def clientele_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Name_client'] = message.text
    await Form.next()
    await message.answer("Введите название организации клиента?")

async def company_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Name_client_organization'] = message.text
    await Form.next()
    await message.answer("Введите адрес клиента?")

async def address_clientele(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['addres_client'] = message.text
    await Form.next()
    await message.answer("Введите номер расчетного счета клиента?")

async def payment_account_clientele(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Payment_account_client'] = message.text
    await Form.next()
    await message.answer("Введите название банка клиента?")

async def clientele_name_bank(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_of_the_bank_client'] = message.text
    await Form.next()
    await message.answer("Введите BIC банка клиента?")

async def clientele_bic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bic_bank_client'] = message.text
    await Form.next()
    await message.answer("Введите телефонный номер клиента?")

async def process_save(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_client'] = message.text
        await message.answer(md.text(
            md.text('Название документа: ', data['doc_name']),
            md.text('Номер документа: ', data['doc_number']),
            md.text('Дата документа: ', data['doc_date']),
            md.text('Имя клиента: ', data['Name_client']),
            md.text('Название организации клиента: ', data['Name_client_organization']),
            md.text('Адрес клиента: ', data['addres_client']),
            md.text('Рассчетный счет клиента: ', data['Payment_account_client']),
            md.text('Название банка клиента: ', data['name_of_the_bank_client']),
            md.text('BIC банка клиента: ', data['bic_bank_client']),
            md.text('Телефонный номер клиента: ', data['phone_client']),
            sep='\n',
        ))
    f_path = create_doc(data)
    with open(f_path, 'rb') as doc:
        await message.answer_document(doc)
    os.remove(f_path)
    await state.finish()
