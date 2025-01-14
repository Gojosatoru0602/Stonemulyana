import os
import shutil

import git
from pyrogram import filters

from StoneXMusic import app


@app.on_message(filters.command(["downloadrepo"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text(
            "ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ɢɪᴛʜᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴜʀʟ ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ. ᴇxᴀᴍᴘʟᴇ: /downloadrepo ʀᴇᴘᴏ ᴜʀʟ "
        )
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɢɪᴛʜᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ.")


def download_and_zip_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{repo_name}"

        # Clone the repository
        repo = git.Repo.clone_from(repo_url, repo_path)

        # Create a zip file of the repository
        shutil.make_archive(repo_path, "zip", repo_path)

        return f"{repo_path}.zip"
    except Exception as e:
        print(f"ᴇʀʀᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀɴᴅ ᴢɪᴘᴘɪɴɢ ɢɪᴛʜᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
