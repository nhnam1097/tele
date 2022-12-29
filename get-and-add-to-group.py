from telethon import TelegramClient
from telethon import utils
from telethon import types
from telethon.tl.functions.channels import InviteToChannelRequest
# For normal chats
from telethon.tl.functions.messages import AddChatUserRequest
import socks

# Remember to use your own values from my.telegram.org!
api_id = 
api_hash = ''
proxys = {
    'proxy_type': 'http', # (mandatory) protocol to use (see above)
    'addr': '',      # (mandatory) proxy IP address
    'port': 8080,           # (mandatory) proxy port number
    'username': '',      # (optional) username if the proxy requires auth
    'password': '',      # (optional) password if the proxy requires auth
    'rdns': True            # (optional) whether to use remote or local resolve, default remote
}
client = TelegramClient('anon', api_id, api_hash, proxy=proxys)

async def main():
    # Getting information about yourself

    channelGet = await client.get_entity('')
    # real_id, peer_type = utils.resolve_id(497136388)
    users = await client.get_participants(channelGet)
    print(users[0])

    channel = await client.get_entity('')
    print(channel)
    await client(InviteToChannelRequest(
    channel,
    [users[0]]
))

    # for user in users:
    #     if user.username is not None:
    #         print(user)
#     userAdd = await client.get_entity('shjnnosuke97')
    # channel = await client.get_entity('https://t.me/airdropgem6')
#     print(userAdd)
#     print(channel)
#     await client(InviteToChannelRequest(
#     channel,
#     [userAdd.id]
# ))

    



with client:
    client.loop.run_until_complete(main())