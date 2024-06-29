import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # if message.content == "hello":
    #     await message.reply("Hello!")
    # elif message.content == "bye":
    #     await message.reply("Bye!")
        
    await cl.Message(
        content = f"Received : {message.content}",
    ).send()