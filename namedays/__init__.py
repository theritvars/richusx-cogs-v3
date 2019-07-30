from .namedays import Namedays, check_file, check_folder

def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(Namedays())