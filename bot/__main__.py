from uvloop import install
from bot import app, aiosession, event_loop




async def main():
      await app.start()
      
      await idle()
      await aiosession.close()
      await app.stop()
      
      
if __name__ == "__main__":
    LOGGER("Ubot").info("Starting  Ubot")
    install()
    event_loop.run_until_complete(main())