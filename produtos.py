import discord
from discord.ext import commands
import qrcode
from io import BytesIO

class produtos_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.produtos = {
            '1': {'nome': 'Produto 1', 'preco': 10.0},
            '2': {'nome': 'Produto 2', 'preco': 20.0},
            '3': {'nome': 'Produto 3', 'preco': 30.0},
        }

    @commands.command(name="listarprodutos", help="Lista todos os produtos disponíveis para compra.")
    async def listar_produtos(self, ctx):
        embed = discord.Embed(title="Produtos Disponíveis", color=discord.Color.green())
        for codigo, produto in self.produtos.items():
            embed.add_field(name=f"{codigo}: {produto['nome']}", value=f"Preço: R$ {produto['preco']:.2f}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="comprar", help="Compra um produto pelo seu código.")
    async def comprar(self, ctx, codigo_produto: str):
        if codigo_produto not in self.produtos:
            await ctx.send("Produto não encontrado.")
            return

        produto = self.produtos[codigo_produto]
        await ctx.send(f"Você selecionou o produto {produto['nome']} por R$ {produto['preco']:.2f}. Envie o pagamento via PIX para o QR code abaixo.")

        qr_code_image = self.generate_qr_code(f"Pagamento para {produto['nome']} no valor de R$ {produto['preco']:.2f}")
        qr_code_file = discord.File(qr_code_image, filename="qrcode.png")
        await ctx.send(file=qr_code_file)

    def generate_qr_code(self, content):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(content)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_byte_array = BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)

        return img_byte_array
