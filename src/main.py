#!/usr/bin/env python

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handlers import (
    constants,
    start_handler,
    rank_handler,
    help_handler,
)
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from models.player import Player

# Create an engine that connects to an in-memory SQLite database
engine = create_engine('sqlite:///players.db', echo=True)

# Define a base class using the declarative system
Base = declarative_base()
# Create the users table in the database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()

user1 = Player(tg_id=100, fortnite_username="el_fant0mas")
user2 = Player(tg_id=1110, fortnite_username="no_el_fant0mas")

# Add them to the session
session.add(user1)
session.add(user2)

# Commit the transaction to save the changes
session.commit()
# Query and print the users
players = session.query(Player).all()
for player in players:
    print(player)

# Close the session
session.close()

app = ApplicationBuilder().token(constants.TG_BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_handler.start))
app.add_handler(CommandHandler("help", help_handler.help))

app.run_polling()
