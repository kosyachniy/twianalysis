import vk_api, time

vk=vk_api.VkApi(token='44177b16755f6d96acf4fae0a8dd0700472f1e473943769aea355c3b1cfab3c446c981b2990345b60a4cb')
vk.auth()

send=lambda user, cont: vk.method('messages.send', {'user_id':user, 'message':cont})
read=lambda user: [i['body'] if not i['read_state'] else '' for i in vk.method('messages.get', {'user_id':user})['items']][::-1]