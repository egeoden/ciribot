import disnake 
from disnake.ext import commands



class Avatar(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.slash_command(name="avatar", description="sleş")
    async def avatar(self,inter,member: disnake.Member):
        embed = disnake.Embed(
            title= f"{member} kullanıcısının avatarı",
            description = "\n",
            color = member.top_role.color
        )
        embed.set_image(url=member.display_avatar.url)
        await inter.response.send_message(embed = embed)

def setup(client):
    client.add_cog(Avatar(client))