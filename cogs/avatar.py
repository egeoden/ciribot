import disnake 
from disnake.ext import commands



class Avatar(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.slash_command(name="avatar", description="sleş")
    async def avatar(self,inter):
        embed = disnake.Embed(
            title= f"{inter.author} kullanıcısının avatarı",
            description = "\n",
            color = inter.author.top_role.color
        )
        embed.set_image(url=inter.author.display_avatar.url)
        await inter.response.send_message(embed = embed)

def setup(client):
    client.add_cog(Avatar(client))