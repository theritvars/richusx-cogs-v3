from .namedays import Namedays, check_file, check_folder

async def setup(bot):
    check_folder()
    check_file()
    await bot.add_cog(Namedays(bot))