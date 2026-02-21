"""
𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟑.𝟏
𝐀𝐔𝐓𝐎-𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐒𝐘𝐒𝐓𝐄𝐌 & 𝐓𝐈𝐄𝐑 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓
𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄: 𝐌𝐀𝐓𝐇𝐄𝐌𝐀𝐓𝐈𝐂𝐀𝐋 𝐁𝐎𝐋𝐃 𝐒𝐀𝐍𝐒-𝐒𝐄𝐑𝐈𝐅
𝐂𝐑𝐄𝐃𝐈𝐓𝐒: 𝐌𝐊-𝐃𝐄𝐕 𝐂𝐎𝐃𝐄𝐑
"""

import subprocess
import sys
import os

# ✅ 𝐀𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬
def auto_install(package):
    try:
        __import__(package)
    except ModuleNotFoundError:
        print(f"📦 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐩𝐚𝐜𝐤𝐚𝐠𝐞: {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝: {package}")

# 𝐀𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐦𝐨𝐝𝐮𝐥𝐞𝐬
for mod in ["telebot", "psutil", "requests", "flask", "qrcode", "Pillow", "cryptography"]:
    auto_install(mod)

# --- 𝐀𝐟𝐭𝐞𝐫 𝐚𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥, 𝐢𝐦𝐩𝐨𝐫𝐭 𝐚𝐥𝐥 𝐦𝐨𝐝𝐮𝐥𝐞𝐬 𝐬𝐚𝐟𝐞𝐥𝐲 ---
import telebot
import zipfile
import tempfile
import shutil
from telebot import types
import time
from datetime import datetime, timedelta
import psutil
import sqlite3
import json
import logging
import signal
import threading
import re
import atexit
import requests
from flask import Flask
from threading import Thread
import qrcode
from io import BytesIO
import hashlib
import random
import string
from cryptography.fernet import Fernet
import base64

app = Flask('')

@app.route('/')
def home():
    return "𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    print("✅ 𝐅𝐥𝐚𝐬𝐤 𝐊𝐞𝐞𝐩-𝐀𝐥𝐢𝐯𝐞 𝐬𝐞𝐫𝐯𝐞𝐫 𝐬𝐭𝐚𝐫𝐭𝐞𝐝.")

# ================================
# 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍
# ================================
TOKEN = '8557058963:AAGWVck3QVcBpGNOPF4mhwsvDJXkKOJYq34'  # 𝐑𝐞𝐩𝐥𝐚𝐜𝐞 𝐰𝐢𝐭𝐡 𝐲𝐨𝐮𝐫 𝐚𝐜𝐭𝐮𝐚𝐥 𝐭𝐨𝐤𝐞𝐧
OWNER_ID = 7848142155
ADMIN_ID = 7848142155
YOUR_USERNAME = '@devoloper7'
UPDATE_CHANNEL = 'https://t.me/web_developer_m_k'
UPDATE_GROUP = 'https://t.me/Developer_mk_group'  # 𝐍𝐞𝐰 𝐮𝐩𝐝𝐚𝐭𝐞 𝐠𝐫𝐨𝐮𝐩

# 𝐅𝐨𝐥𝐝𝐞𝐫 𝐬𝐞𝐭𝐮𝐩
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_BOTS_DIR = os.path.join(BASE_DIR, 'exu_uploads')
EXU_DATA_DIR = os.path.join(BASE_DIR, 'exu_data')
DATABASE_PATH = os.path.join(EXU_DATA_DIR, 'exu_bot.db')
RUNNING_SCRIPTS_DB = os.path.join(EXU_DATA_DIR, 'running_scripts.json')
REFERRAL_DB = os.path.join(EXU_DATA_DIR, 'referrals.json')

# 𝐓𝐈𝐄𝐑 𝐒𝐘𝐒𝐓𝐄𝐌
TIER_SYSTEM = {
    "free": {
        "name": "𝐅𝐑𝐄𝐄",
        "upload_limit": 1,
        "max_file_size": 50 * 1024 * 1024,
        "icon": "🎫",
        "color": "#2ecc71",
        "auto_restart": False,
        "referral_needed": 5
    },
    "premium": {
        "name": "𝐏𝐑𝐄𝐌𝐈𝐔𝐌",
        "upload_limit": 10,
        "max_file_size": 200 * 1024 * 1024,
        "icon": "⭐",
        "color": "#f39c12",
        "auto_restart": True,
        "referral_needed": 0
    },
    "owner": {
        "name": "𝐎𝐖𝐍𝐄𝐑",
        "upload_limit": float('inf'),
        "max_file_size": float('inf'),
        "icon": "👑",
        "color": "#e74c3c",
        "auto_restart": True,
        "referral_needed": 0
    }
}

# 𝐂𝐫𝐞𝐚𝐭𝐞 𝐧𝐞𝐜𝐞𝐬𝐬𝐚𝐫𝐲 𝐝𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬
os.makedirs(UPLOAD_BOTS_DIR, exist_ok=True)
os.makedirs(EXU_DATA_DIR, exist_ok=True)

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐛𝐨𝐭
bot = telebot.TeleBot(TOKEN)

# --- 𝐃𝐚𝐭𝐚 𝐬𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞𝐬 ---
bot_scripts = {}  # 𝐒𝐭𝐨𝐫𝐞𝐬 𝐢𝐧𝐟𝐨 𝐚𝐛𝐨𝐮𝐭 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬
user_subscriptions = {}
user_files = {}
active_users = set()
admin_ids = {ADMIN_ID, OWNER_ID}
bot_locked = False
referral_data = {}  # 𝐒𝐭𝐨𝐫𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐝𝐚𝐭𝐚

# --- 𝐋𝐨𝐠𝐠𝐢𝐧𝐠 𝐒𝐞𝐭𝐮𝐩 ---
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ================================
# 𝐅𝐎𝐍𝐓 𝐂𝐎𝐍𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍𝐒
# ================================
def convert_to_bold_uppercase(text: str) -> str:
    """𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐭𝐞𝐱𝐭 𝐭𝐨 𝐦𝐚𝐭𝐡𝐞𝐦𝐚𝐭𝐢𝐜𝐚𝐥 𝐛𝐨𝐥𝐝 𝐬𝐚𝐧𝐬-𝐬𝐞𝐫𝐢𝐟"""
    bold_mapping = {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
        'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
        'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
        'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
        'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠',
        'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧',
        'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮',
        'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
        '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔',
        '7': '𝟕', '8': '𝟖', '9': '𝟗',
        ' ': ' ', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^',
        '&': '&', '*': '*', '(': '(', ')': ')', '-': '-', '_': '_', '=': '=',
        '+': '+', '[': '[', ']': ']', '{': '{', '}': '}', '\\': '\\', '|': '|',
        ';': ';', ':': ':', "'": "'", '"': '"', ',': ',', '.': '.', '<': '<',
        '>': '>', '/': '/', '?': '?', '`': '`', '~': '~'
    }
    
    result = []
    for char in str(text):
        result.append(bold_mapping.get(char, char))
    return ''.join(result)

# 𝐀𝐥𝐢𝐚𝐬 𝐟𝐨𝐫 𝐞𝐚𝐬𝐲 𝐮𝐬𝐞
B = convert_to_bold_uppercase

# ================================
# 𝐑𝐄𝐅𝐄𝐑𝐑𝐀𝐋 𝐒𝐘𝐒𝐓𝐄𝐌 (𝐔𝐏𝐃𝐀𝐓𝐄𝐃)
# ================================
class ReferralSystem:
    def __init__(self):
        self.referral_file = REFERRAL_DB
        
    def load_referrals(self):
        """𝐋𝐨𝐚𝐝 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐝𝐚𝐭𝐚 𝐟𝐫𝐨𝐦 𝐟𝐢𝐥𝐞"""
        global referral_data
        try:
            if os.path.exists(self.referral_file):
                with open(self.referral_file, 'r') as f:
                    referral_data = json.load(f)
            else:
                referral_data = {}
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {e}")
            referral_data = {}
    
    def save_referrals(self):
        """𝐒𝐚𝐯𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐝𝐚𝐭𝐚 𝐭𝐨 𝐟𝐢𝐥𝐞"""
        try:
            with open(self.referral_file, 'w') as f:
                json.dump(referral_data, f, indent=4)
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐚𝐯𝐢𝐧𝐠 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {e}")
    
    def generate_referral_code(self, user_id):
        """𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐮𝐧𝐢𝐪𝐮𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐜𝐨𝐝𝐞"""
        code = f"EXU{user_id}{random.randint(1000, 9999)}"
        if user_id not in referral_data:
            referral_data[user_id] = {
                'code': code,
                'referrals': [],
                'count': 0,
                'auto_restart_enabled': False,
                'generated_at': datetime.now().isoformat(),
                'username': ''
            }
        else:
            referral_data[user_id]['code'] = code
        self.save_referrals()
        return code
    
    def get_referral_code(self, user_id):
        """𝐆𝐞𝐭 𝐮𝐬𝐞𝐫'𝐬 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐜𝐨𝐝𝐞"""
        if user_id in referral_data:
            return referral_data[user_id].get('code')
        return self.generate_referral_code(user_id)
    
    def add_referral(self, referrer_id, referred_id, referred_username=None):
        """𝐀𝐝𝐝 𝐚 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥"""
        if referrer_id == referred_id:
            return False
        
        if referrer_id not in referral_data:
            self.generate_referral_code(referrer_id)
        
        # Update referrer's username if not set
        if 'username' not in referral_data[referrer_id]:
            referral_data[referrer_id]['username'] = ''
        
        # Add referred user info
        referred_info = {
            'user_id': referred_id,
            'username': referred_username or '',
            'joined_at': datetime.now().isoformat()
        }
        
        if referred_id not in [r['user_id'] for r in referral_data[referrer_id].get('referrals', [])]:
            referral_data[referrer_id].setdefault('referrals', []).append(referred_info)
            referral_data[referrer_id]['count'] = len(referral_data[referrer_id]['referrals'])
            
            # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
            if referral_data[referrer_id]['count'] >= TIER_SYSTEM['free']['referral_needed']:
                referral_data[referrer_id]['auto_restart_enabled'] = True
            
            self.save_referrals()
            return True
        return False
    
    def get_referral_count(self, user_id):
        """𝐆𝐞𝐭 𝐧𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬"""
        if user_id in referral_data:
            return referral_data[user_id]['count']
        return 0
    
    def is_auto_restart_enabled(self, user_id):
        """𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝"""
        if user_id in referral_data:
            return referral_data[user_id]['auto_restart_enabled']
        return False
    
    def get_top_referrers(self, limit=10):
        """𝐆𝐞𝐭 𝐭𝐨𝐩 𝐫𝐞𝐟𝐞𝐫𝐫𝐞𝐫𝐬 𝐟𝐨𝐫 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝"""
        referrers = []
        for user_id, data in referral_data.items():
            if 'count' in data and data['count'] > 0:
                referrers.append({
                    'user_id': user_id,
                    'username': data.get('username', ''),
                    'count': data['count'],
                    'auto_restart': data.get('auto_restart_enabled', False)
                })
        
        # Sort by count descending
        referrers.sort(key=lambda x: x['count'], reverse=True)
        return referrers[:limit]
    
    def get_user_referral_info(self, user_id):
        """𝐆𝐞𝐭 𝐝𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐢𝐧𝐟𝐨 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫"""
        if user_id not in referral_data:
            return None
        
        data = referral_data[user_id].copy()
        data['rank'] = self.get_user_rank(user_id)
        return data
    
    def get_user_rank(self, user_id):
        """𝐆𝐞𝐭 𝐮𝐬𝐞𝐫'𝐬 𝐫𝐚𝐧𝐤 𝐢𝐧 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝"""
        referrers = self.get_top_referrers(limit=1000)
        for i, referrer in enumerate(referrers, 1):
            if referrer['user_id'] == user_id:
                return i
        return None
    
    def update_user_username(self, user_id, username):
        """𝐔𝐩𝐝𝐚𝐭𝐞 𝐮𝐬𝐞𝐫'𝐬 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞"""
        if user_id in referral_data:
            referral_data[user_id]['username'] = username or ''
            self.save_referrals()

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐬𝐲𝐬𝐭𝐞𝐦
referral_system = ReferralSystem()
referral_system.load_referrals()

# ================================
# 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
class ProgressAnimation:
    @staticmethod
    def execute_animation():
        return [
            B("𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▱▱▱▱▱▱▱▱▱▱] 0%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▱▱▱▱▱▱▱▱▱] 10%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▱▱▱▱▱▱▱▱] 20%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▱▱▱▱▱▱▱] 30%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▰▱▱▱▱▱▱] 40%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▰▰▱▱▱▱▱] 50%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▰▰▰▱▱▱▱] 60%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▰▰▰▰▱▱▱] 70%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▰▰▰▰▰▱▱] 80%"),
            B("⚡ 𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠: [▰▰▰▰▰▰▰▰▰▱] 90%"),
            B("✅ 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞: [▰▰▰▰▰▰▰▰▰▰] 100%")
        ]
    
    @staticmethod
    def upload_animation():
        return [
            B("📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠: [▱▱▱▱▱▱▱▱▱▱] 0%"),
            B("📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠: [▰▱▱▱▱▱▱▱▱▱] 25%"),
            B("📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠: [▰▰▰▱▱▱▱▱▱▱] 50%"),
            B("📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠: [▰▰▰▰▰▰▱▱▱▱] 75%"),
            B("✅ 𝐔𝐩𝐥𝐨𝐚𝐝 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞: [▰▰▰▰▰▰▰▰▰▰] 100%")
        ]
    
    @staticmethod
    def recovery_animation():
        return [
            B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲: [▱▱▱▱▱▱▱▱▱▱] 0%"),
            B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲: [▰▰▱▱▱▱▱▱▱▱] 20%"),
            B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲: [▰▰▰▰▱▱▱▱▱▱] 40%"),
            B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲: [▰▰▰▰▰▰▱▱▱▱] 60%"),
            B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲: [▰▰▰▰▰▰▰▰▱▱] 80%"),
            B("✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞: [▰▰▰▰▰▰▰▰▰▰] 100%")
        ]
    
    @staticmethod
    def restart_animation():
        return [
            B("🔄 𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠: [▱▱▱▱▱▱▱▱▱▱] 0%"),
            B("🔄 𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠: [▰▰▱▱▱▱▱▱▱▱] 20%"),
            B("🔄 𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠: [▰▰▰▰▱▱▱▱▱▱] 40%"),
            B("🔄 𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠: [▰▰▰▰▰▰▱▱▱▱] 60%"),
            B("🔄 𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠: [▰▰▰▰▰▰▰▰▱▱] 80%"),
            B("✅ 𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝: [▰▰▰▰▰▰▰▰▰▰] 100%")
        ]

# ================================
# 𝐀𝐔𝐓𝐎-𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
class AutoRecoverySystem:
    def __init__(self):
        self.running_scripts_file = RUNNING_SCRIPTS_DB
        
    def save_running_script(self, user_id: int, file_name: str, file_path: str, process_pid: int):
        """𝐒𝐚𝐯𝐞 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭 𝐢𝐧𝐟𝐨 𝐭𝐨 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
            else:
                data = {"running_scripts": []}
            
            # 𝐑𝐞𝐦𝐨𝐯𝐞 𝐝𝐮𝐩𝐥𝐢𝐜𝐚𝐭𝐞𝐬
            data["running_scripts"] = [script for script in data["running_scripts"] 
                                     if not (script["user_id"] == user_id and script["file_name"] == file_name)]
            
            # 𝐀𝐝𝐝 𝐧𝐞𝐰 𝐬𝐜𝐫𝐢𝐩𝐭
            script_info = {
                "user_id": user_id,
                "file_name": file_name,
                "file_path": file_path,
                "process_pid": process_pid,
                "start_time": datetime.now().isoformat(),
                "status": "running",
                "last_updated": datetime.now().isoformat()
            }
            
            data["running_scripts"].append(script_info)
            
            with open(self.running_scripts_file, 'w') as f:
                json.dump(data, f, indent=4)
                
            logger.info(f"💾 𝐒𝐚𝐯𝐞𝐝 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {user_id}/{file_name}")
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐚𝐯𝐢𝐧𝐠 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
    
    def remove_running_script(self, user_id: int, file_name: str):
        """𝐑𝐞𝐦𝐨𝐯𝐞 𝐬𝐜𝐫𝐢𝐩𝐭 𝐟𝐫𝐨𝐦 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
                
                initial_count = len(data["running_scripts"])
                data["running_scripts"] = [script for script in data["running_scripts"] 
                                         if not (script["user_id"] == user_id and script["file_name"] == file_name)]
                
                if len(data["running_scripts"]) < initial_count:
                    with open(self.running_scripts_file, 'w') as f:
                        json.dump(data, f, indent=4)
                    logger.info(f"🗑️ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {user_id}/{file_name}")
                    
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐦𝐨𝐯𝐢𝐧𝐠 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
    
    def recover_all_scripts(self):
        """𝐑𝐞𝐜𝐨𝐯𝐞𝐫 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐚𝐟𝐭𝐞𝐫 𝐜𝐫𝐚𝐬𝐡/𝐫𝐞𝐬𝐭𝐚𝐫𝐭"""
        try:
            if not os.path.exists(self.running_scripts_file):
                logger.info("📭 𝐍𝐨 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫")
                return []
            
            with open(self.running_scripts_file, 'r') as f:
                data = json.load(f)
            
            recovered = []
            for script in data.get("running_scripts", []):
                try:
                    user_id = script["user_id"]
                    file_name = script["file_name"]
                    file_path = script["file_path"]
                    
                    # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐟𝐢𝐥𝐞 𝐬𝐭𝐢𝐥𝐥 𝐞𝐱𝐢𝐬𝐭𝐬
                    if not os.path.exists(file_path):
                        logger.warning(f"⚠️ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 𝐟𝐨𝐫 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲: {file_path}")
                        continue
                    
                    # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐮𝐬𝐞𝐫 𝐬𝐭𝐢𝐥𝐥 𝐡𝐚𝐬 𝐟𝐢𝐥𝐞 𝐢𝐧 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
                    user_has_file = False
                    for fname, ftype in user_files.get(user_id, []):
                        if fname == file_name:
                            user_has_file = True
                            break
                    
                    if not user_has_file:
                        logger.warning(f"⚠️ 𝐔𝐬𝐞𝐫 {user_id} 𝐧𝐨 𝐥𝐨𝐧𝐠𝐞𝐫 𝐡𝐚𝐬 𝐟𝐢𝐥𝐞: {file_name}")
                        continue
                    
                    # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫
                    tier = get_user_tier(user_id)
                    auto_restart_enabled = TIER_SYSTEM[tier]['auto_restart']
                    
                    if tier == 'free':
                        auto_restart_enabled = referral_system.is_auto_restart_enabled(user_id)
                    
                    if not auto_restart_enabled:
                        logger.info(f"⏸️ 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐝𝐢𝐬𝐚𝐛𝐥𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 {user_id}")
                        continue
                    
                    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐬𝐜𝐫𝐢𝐩𝐭
                    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
                    file_ext = os.path.splitext(file_name)[1].lower()
                    
                    if file_ext == '.py':
                        threading.Thread(target=self._restart_py_script, 
                                       args=(user_id, file_path, user_folder, file_name)).start()
                    elif file_ext == '.js':
                        threading.Thread(target=self._restart_js_script,
                                       args=(user_id, file_path, user_folder, file_name)).start()
                    
                    recovered.append({
                        "user_id": user_id,
                        "file_name": file_name,
                        "status": "recovering"
                    })
                    
                    logger.info(f"🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {user_id}/{file_name}")
                    
                    time.sleep(1)  # 𝐀𝐯𝐨𝐢𝐝 𝐨𝐯𝐞𝐫𝐥𝐨𝐚𝐝
                    
                except Exception as e:
                    logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭 {script}: {e}")
            
            return recovered
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐬𝐲𝐬𝐭𝐞𝐦: {e}")
            return []
    
    def _restart_py_script(self, user_id: int, file_path: str, user_folder: str, file_name: str):
        """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭"""
        try:
            script_key = f"{user_id}_{file_name}"
            
            if script_key in bot_scripts:
                logger.info(f"✅ 𝐒𝐜𝐫𝐢𝐩𝐭 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠: {file_name}")
                return
            
            log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
            log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
            
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
            
            process = subprocess.Popen(
                [sys.executable, file_path],
                cwd=user_folder,
                stdout=log_file,
                stderr=log_file,
                stdin=subprocess.PIPE,
                startupinfo=startupinfo,
                encoding='utf-8',
                errors='ignore'
            )
            
            bot_scripts[script_key] = {
                'process': process,
                'log_file': log_file,
                'file_name': file_name,
                'user_id': user_id,
                'start_time': datetime.now(),
                'type': 'py',
                'script_key': script_key
            }
            
            # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
            self.save_running_script(user_id, file_name, file_path, process.pid)
            
            logger.info(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭: {file_name} (𝐏𝐈𝐃: {process.pid})")
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭 {file_name}: {e}")
    
    def _restart_js_script(self, user_id: int, file_path: str, user_folder: str, file_name: str):
        """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭"""
        try:
            script_key = f"{user_id}_{file_name}"
            
            if script_key in bot_scripts:
                logger.info(f"✅ 𝐒𝐜𝐫𝐢𝐩𝐭 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠: {file_name}")
                return
            
            log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
            log_file = open(log_file_path, 'a', encoding='utf-8', errors='ignore')
            
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
            
            process = subprocess.Popen(
                ['node', file_path],
                cwd=user_folder,
                stdout=log_file,
                stderr=log_file,
                stdin=subprocess.PIPE,
                startupinfo=startupinfo,
                encoding='utf-8',
                errors='ignore'
            )
            
            bot_scripts[script_key] = {
                'process': process,
                'log_file': log_file,
                'file_name': file_name,
                'user_id': user_id,
                'start_time': datetime.now(),
                'type': 'js',
                'script_key': script_key
            }
            
            # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
            self.save_running_script(user_id, file_name, file_path, process.pid)
            
            logger.info(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭: {file_name} (𝐏𝐈𝐃: {process.pid})")
            
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭 {file_name}: {e}")
    
    def get_running_count(self):
        """𝐆𝐞𝐭 𝐜𝐨𝐮𝐧𝐭 𝐨𝐟 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"""
        try:
            if os.path.exists(self.running_scripts_file):
                with open(self.running_scripts_file, 'r') as f:
                    data = json.load(f)
                return len(data.get("running_scripts", []))
            return 0
        except:
            return 0

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐬𝐲𝐬𝐭𝐞𝐦
recovery_system = AutoRecoverySystem()

# ================================
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐒𝐄𝐓𝐔𝐏
# ================================
def init_db():
    """𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐭𝐡𝐞 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    logger.info(f"📊 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐚𝐭: {DATABASE_PATH}")
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        
        # 𝐂𝐫𝐞𝐚𝐭𝐞 𝐭𝐚𝐛𝐥𝐞𝐬
        c.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                     (user_id INTEGER PRIMARY KEY, expiry TEXT, tier TEXT, created_at TEXT)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS user_files
                     (user_id INTEGER, file_name TEXT, file_type TEXT, uploaded_at TEXT,
                      PRIMARY KEY (user_id, file_name))''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS active_users
                     (user_id INTEGER PRIMARY KEY, username TEXT, first_join TEXT, last_seen TEXT)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS admins
                     (user_id INTEGER PRIMARY KEY, added_by INTEGER, added_at TEXT)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS user_stats
                     (user_id INTEGER PRIMARY KEY, uploads_count INTEGER, 
                      scripts_run INTEGER, total_upload_size INTEGER)''')
        
        # 𝐈𝐧𝐬𝐞𝐫𝐭 𝐨𝐰𝐧𝐞𝐫 𝐚𝐧𝐝 𝐚𝐝𝐦𝐢𝐧
        c.execute('INSERT OR IGNORE INTO admins (user_id, added_by, added_at) VALUES (?, ?, ?)',
                  (OWNER_ID, OWNER_ID, datetime.now().isoformat()))
        
        if ADMIN_ID != OWNER_ID:
            c.execute('INSERT OR IGNORE INTO admins (user_id, added_by, added_at) VALUES (?, ?, ?)',
                      (ADMIN_ID, OWNER_ID, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
        logger.info("✅ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐢𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲.")
        
    except Exception as e:
        logger.error(f"❌ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐢𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐞𝐫𝐫𝐨𝐫: {e}", exc_info=True)

def load_data():
    """𝐋𝐨𝐚𝐝 𝐝𝐚𝐭𝐚 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    logger.info("📥 𝐋𝐨𝐚𝐝𝐢𝐧𝐠 𝐝𝐚𝐭𝐚 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞...")
    try:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        
        # 𝐋𝐨𝐚𝐝 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧𝐬
        c.execute('SELECT user_id, expiry, tier FROM subscriptions')
        for user_id, expiry, tier in c.fetchall():
            try:
                user_subscriptions[user_id] = {
                    'expiry': datetime.fromisoformat(expiry) if expiry else None,
                    'tier': tier or 'free'
                }
            except:
                pass
        
        # 𝐋𝐨𝐚𝐝 𝐮𝐬𝐞𝐫 𝐟𝐢𝐥𝐞𝐬
        c.execute('SELECT user_id, file_name, file_type FROM user_files')
        for user_id, file_name, file_type in c.fetchall():
            if user_id not in user_files:
                user_files[user_id] = []
            user_files[user_id].append((file_name, file_type))
        
        # 𝐋𝐨𝐚𝐝 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫𝐬
        c.execute('SELECT user_id FROM active_users')
        active_users.update(user_id for (user_id,) in c.fetchall())
        
        # 𝐋𝐨𝐚𝐝 𝐚𝐝𝐦𝐢𝐧𝐬
        c.execute('SELECT user_id FROM admins')
        admin_ids.update(user_id for (user_id,) in c.fetchall())
        
        conn.close()
        
        logger.info(f"✅ 𝐃𝐚𝐭𝐚 𝐥𝐨𝐚𝐝𝐞𝐝: {len(active_users)} 𝐮𝐬𝐞𝐫𝐬, "
                   f"{len(user_subscriptions)} 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧𝐬, "
                   f"{len(admin_ids)} 𝐚𝐝𝐦𝐢𝐧𝐬")
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐝𝐚𝐭𝐚: {e}", exc_info=True)

# 𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐞 𝐃𝐁 𝐚𝐧𝐝 𝐋𝐨𝐚𝐝 𝐃𝐚𝐭𝐚
init_db()
load_data()

# ================================
# 𝐇𝐄𝐋𝐏𝐄𝐑 𝐅𝐔𝐍𝐂𝐓𝐈𝐎𝐍𝐒
# ================================
def get_user_folder(user_id):
    """𝐆𝐞𝐭 𝐨𝐫 𝐜𝐫𝐞𝐚𝐭𝐞 𝐮𝐬𝐞𝐫'𝐬 𝐟𝐨𝐥𝐝𝐞𝐫"""
    user_folder = os.path.join(UPLOAD_BOTS_DIR, str(user_id))
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

def get_user_tier(user_id):
    """𝐆𝐞𝐭 𝐮𝐬𝐞𝐫'𝐬 𝐭𝐢𝐞𝐫"""
    if user_id == OWNER_ID:
        return "owner"
    elif user_id in admin_ids:
        return "owner"  # 𝐀𝐝𝐦𝐢𝐧𝐬 𝐠𝐞𝐭 𝐨𝐰𝐧𝐞𝐫 𝐩𝐫𝐢𝐯𝐢𝐥𝐞𝐠𝐞𝐬
    elif user_id in user_subscriptions:
        sub = user_subscriptions[user_id]
        if sub.get('expiry') and sub['expiry'] > datetime.now():
            return sub.get('tier', 'premium')
    return "free"

def get_user_file_limit(user_id):
    """𝐆𝐞𝐭 𝐟𝐢𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝 𝐥𝐢𝐦𝐢𝐭 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫"""
    tier = get_user_tier(user_id)
    return TIER_SYSTEM[tier]["upload_limit"]

def get_user_file_count(user_id):
    """𝐆𝐞𝐭 𝐧𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐟𝐢𝐥𝐞𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲 𝐮𝐬𝐞𝐫"""
    return len(user_files.get(user_id, []))

def is_bot_running(user_id, file_name):
    """𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐚 𝐛𝐨𝐭 𝐬𝐜𝐫𝐢𝐩𝐭 𝐢𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠"""
    script_key = f"{user_id}_{file_name}"
    script_info = bot_scripts.get(script_key)
    
    if script_info and script_info.get('process'):
        try:
            proc = psutil.Process(script_info['process'].pid)
            return proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
        except psutil.NoSuchProcess:
            # 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝, 𝐜𝐥𝐞𝐚𝐧 𝐮𝐩
            recovery_system.remove_running_script(user_id, file_name)
            if script_key in bot_scripts:
                del bot_scripts[script_key]
            return False
    return False

def kill_process_tree(process_info):
    """𝐊𝐢𝐥𝐥 𝐚 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝐚𝐧𝐝 𝐚𝐥𝐥 𝐢𝐭𝐬 𝐜𝐡𝐢𝐥𝐝𝐫𝐞𝐧"""
    try:
        process = process_info.get('process')
        if process and hasattr(process, 'pid'):
            pid = process.pid
            try:
                parent = psutil.Process(pid)
                children = parent.children(recursive=True)
                
                for child in children:
                    try:
                        child.terminate()
                    except:
                        pass
                
                try:
                    parent.terminate()
                    parent.wait(timeout=3)
                except:
                    try:
                        parent.kill()
                    except:
                        pass
                
                # 𝐑𝐞𝐦𝐨𝐯𝐞 𝐟𝐫𝐨𝐦 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
                if 'user_id' in process_info and 'file_name' in process_info:
                    recovery_system.remove_running_script(
                        process_info['user_id'], 
                        process_info['file_name']
                    )
                
            except psutil.NoSuchProcess:
                pass
                
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐤𝐢𝐥𝐥𝐢𝐧𝐠 𝐩𝐫𝐨𝐜𝐞𝐬𝐬: {e}")

def send_restart_notification():
    """𝐒𝐞𝐧𝐝 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬"""
    logger.info("📢 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬...")
    
    notification_text = B("""
🚨 *𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓 𝐀𝐍𝐍𝐎𝐔𝐍𝐂𝐄𝐌𝐄𝐍𝐓*

𝐁𝐨𝐭 𝐢𝐬 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐟𝐨𝐫 𝐦𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞.

🔄 *𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐢𝐟:*
✅ 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐎𝐰𝐧𝐞𝐫 𝐮𝐬𝐞𝐫
✅ 𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐞𝐝 𝟑+ 𝐟𝐫𝐢𝐞𝐧𝐝𝐬 (𝐅𝐫𝐞𝐞 𝐮𝐬𝐞𝐫𝐬)

📊 *𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐬𝐭𝐚𝐭𝐮𝐬:*
• 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐎𝐰𝐧𝐞𝐫: 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 ✅
• 𝐅𝐫𝐞𝐞: 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 ❌

🔗 *𝐓𝐨 𝐞𝐧𝐚𝐛𝐥𝐞 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐟𝐨𝐫 𝐅𝐑𝐄𝐄 𝐭𝐢𝐞𝐫:*
1. 𝐆𝐨 𝐭𝐨 /𝐫𝐞𝐟𝐞𝐫
2. 𝐒𝐡𝐚𝐫𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤
3. 𝐑𝐞𝐟𝐞𝐫 𝟑 𝐟𝐫𝐢𝐞𝐧𝐝𝐬
4. 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐞𝐧𝐚𝐛𝐥𝐞𝐝!

⏱️ *𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐛𝐚𝐜𝐤 𝐨𝐧𝐥𝐢𝐧𝐞 𝐢𝐧:*
• 𝟑𝟎 𝐬𝐞𝐜𝐨𝐧𝐝𝐬

𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐩𝐚𝐭𝐢𝐞𝐧𝐜𝐞! 😊
""")
    
    sent = 0
    failed = 0
    
    for user_id in list(active_users):
        try:
            bot.send_message(user_id, notification_text, parse_mode='Markdown')
            sent += 1
        except Exception as e:
            failed += 1
            logger.error(f"❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐬𝐞𝐧𝐝 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 {user_id}: {e}")
        
        # 𝐀𝐯𝐨𝐢𝐝 𝐫𝐚𝐭𝐞 𝐥𝐢𝐦𝐢𝐭𝐢𝐧𝐠
        time.sleep(0.1)
    
    logger.info(f"📤 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬: 𝐒𝐞𝐧𝐭={sent}, 𝐅𝐚𝐢𝐥𝐞𝐝={failed}")

# ================================
# 𝐁𝐔𝐓𝐓𝐎𝐍 𝐋𝐀𝐘𝐎𝐔𝐓𝐒 (𝐰𝐢𝐭𝐡 𝐁𝐎𝐋𝐃 𝐅𝐎𝐍𝐓)
# ================================
def create_main_menu_inline(user_id):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐦𝐚𝐢𝐧 𝐦𝐞𝐧𝐮 𝐰𝐢𝐭𝐡 𝐛𝐨𝐥𝐝 𝐟𝐨𝐧𝐭"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # 𝐔𝐬𝐞𝐫 𝐛𝐮𝐭𝐭𝐨𝐧𝐬
    user_buttons = [
        types.InlineKeyboardButton(B('📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬'), url=UPDATE_CHANNEL),
        types.InlineKeyboardButton(B('👥 𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩'), url=UPDATE_GROUP),
        types.InlineKeyboardButton(B('📤 𝐔𝐩𝐥𝐨𝐚𝐝'), callback_data='upload'),
        types.InlineKeyboardButton(B('📂 𝐌𝐲 𝐅𝐢𝐥𝐞𝐬'), callback_data='check_files'),
        types.InlineKeyboardButton(B('⚡ 𝐒𝐩𝐞𝐞𝐝'), callback_data='speed'),
        types.InlineKeyboardButton(B('📊 𝐒𝐭𝐚𝐭𝐬'), callback_data='stats'),
        types.InlineKeyboardButton(B('👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞'), callback_data='profile'),
        types.InlineKeyboardButton(B('🤝 𝐑𝐞𝐟𝐞𝐫'), callback_data='refer'),
        types.InlineKeyboardButton(B('🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝'), callback_data='leaderboard'),
        types.InlineKeyboardButton(B('🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐀𝐥𝐥'), callback_data='restart_all'),
        types.InlineKeyboardButton(B('📞 𝐂𝐨𝐧𝐭𝐚𝐜𝐭'), url=f'https://t.me/{YOUR_USERNAME.replace("@", "")}')
    ]
    
    if user_id in admin_ids:
        # 𝐀𝐝𝐝 𝐚𝐝𝐦𝐢𝐧 𝐛𝐮𝐭𝐭𝐨𝐧𝐬
        admin_buttons = [
            types.InlineKeyboardButton(B('👑 𝐀𝐝𝐦𝐢𝐧'), callback_data='admin_panel'),
            types.InlineKeyboardButton(B('💳 𝐒𝐮𝐛𝐬'), callback_data='subscription'),
            types.InlineKeyboardButton(B('📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭'), callback_data='broadcast'),
            types.InlineKeyboardButton(B('🔒 𝐋𝐨𝐜𝐤') if not bot_locked else B('🔓 𝐔𝐧𝐥𝐨𝐜𝐤'), 
                                     callback_data='lock_bot' if not bot_locked else 'unlock_bot'),
            types.InlineKeyboardButton(B('🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫'), callback_data='recover_all'),
            types.InlineKeyboardButton(B('📈 𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬'), callback_data='analytics'),
            types.InlineKeyboardButton(B('🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭'), callback_data='restart_bot')
        ]
        
        # 𝐀𝐫𝐫𝐚𝐧𝐠𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬
        markup.add(user_buttons[0], user_buttons[1])  # 𝐔𝐩𝐝𝐚𝐭𝐞𝐬, 𝐆𝐫𝐨𝐮𝐩
        markup.add(user_buttons[2], user_buttons[3])  # 𝐔𝐩𝐥𝐨𝐚𝐝, 𝐌𝐲 𝐅𝐢𝐥𝐞𝐬
        markup.add(user_buttons[4], admin_buttons[0])  # 𝐒𝐩𝐞𝐞𝐝, 𝐀𝐝𝐦𝐢𝐧
        markup.add(admin_buttons[1], admin_buttons[2])  # 𝐒𝐮𝐛𝐬, 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭
        markup.add(admin_buttons[3], admin_buttons[4])  # 𝐋𝐨𝐜𝐤/𝐔𝐧𝐥𝐨𝐜𝐤, 𝐑𝐞𝐜𝐨𝐯𝐞𝐫
        markup.add(user_buttons[6], user_buttons[7])  # 𝐑𝐞𝐟𝐞𝐫, 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝
        markup.add(admin_buttons[6], admin_buttons[5])  # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭, 𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬
        markup.add(user_buttons[8], user_buttons[5])  # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐀𝐥𝐥, 𝐒𝐭𝐚𝐭𝐬
        markup.add(user_buttons[9], user_buttons[10])  # 𝐏𝐫𝐨𝐟𝐢𝐥𝐞, 𝐂𝐨𝐧𝐭𝐚𝐜𝐭
    else:
        # 𝐑𝐞𝐠𝐮𝐥𝐚𝐫 𝐮𝐬𝐞𝐫 𝐥𝐚𝐲𝐨𝐮𝐭
        markup.add(user_buttons[0], user_buttons[1])  # 𝐔𝐩𝐝𝐚𝐭𝐞𝐬, 𝐆𝐫𝐨𝐮𝐩
        markup.add(user_buttons[2], user_buttons[3])  # 𝐔𝐩𝐥𝐨𝐚𝐝, 𝐌𝐲 𝐅𝐢𝐥𝐞𝐬
        markup.add(user_buttons[4], user_buttons[5])  # 𝐒𝐩𝐞𝐞𝐝, 𝐒𝐭𝐚𝐭𝐬
        markup.add(user_buttons[6], user_buttons[7])  # 𝐏𝐫𝐨𝐟𝐢𝐥𝐞, 𝐑𝐞𝐟𝐞𝐫
        markup.add(user_buttons[8], user_buttons[9])  # 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝, 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐀𝐥𝐥
        markup.add(user_buttons[10])  # 𝐂𝐨𝐧𝐭𝐚𝐜𝐭
    
    return markup

def create_reply_keyboard_main_menu(user_id):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐫𝐞𝐩𝐥𝐲 𝐤𝐞𝐲𝐛𝐨𝐚𝐫𝐝 𝐰𝐢𝐭𝐡 𝐛𝐨𝐥𝐝 𝐟𝐨𝐧𝐭"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    if user_id in admin_ids:
        buttons = [
            B("📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬"),
            B("👥 𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩"),
            B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"),
            B("📂 𝐌𝐲 𝐅𝐢𝐥𝐞𝐬"),
            B("⚡ 𝐒𝐩𝐞𝐞𝐝"),
            B("📊 𝐒𝐭𝐚𝐭𝐬"),
            B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"),
            B("🤝 𝐑𝐞𝐟𝐞𝐫"),
            B("🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝"),
            B("👑 𝐀𝐝𝐦𝐢𝐧"),
            B("💳 𝐒𝐮𝐛𝐬"),
            B("📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭"),
            B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫"),
            B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐀𝐥𝐥"),
            B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"),
            B("📞 𝐂𝐨𝐧𝐭𝐚𝐜𝐭")
        ]
    else:
        buttons = [
            B("📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬"),
            B("👥 𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩"),
            B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"),
            B("📂 𝐌𝐲 𝐅𝐢𝐥𝐞𝐬"),
            B("⚡ 𝐒𝐩𝐞𝐞𝐝"),
            B("📊 𝐒𝐭𝐚𝐭𝐬"),
            B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"),
            B("🤝 𝐑𝐞𝐟𝐞𝐫"),
            B("🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝"),
            B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐀𝐥𝐥"),
            B("📞 𝐂𝐨𝐧𝐭𝐚𝐜𝐭")
        ]
    
    # 𝐂𝐫𝐞𝐚𝐭𝐞 𝐫𝐨𝐰𝐬 𝐨𝐟 𝟐 𝐛𝐮𝐭𝐭𝐨𝐧𝐬
    for i in range(0, len(buttons), 2):
        row = buttons[i:i+2]
        markup.add(*[types.KeyboardButton(text) for text in row])
    
    return markup

def create_control_buttons(user_id, file_name, is_running=True):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐟𝐨𝐫 𝐟𝐢𝐥𝐞𝐬"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    if is_running:
        markup.row(
            types.InlineKeyboardButton(B("🔴 𝐒𝐭𝐨𝐩"), callback_data=f'stop_{user_id}_{file_name}'),
            types.InlineKeyboardButton(B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭"), callback_data=f'restart_{user_id}_{file_name}')
        )
        markup.row(
            types.InlineKeyboardButton(B("🗑️ 𝐃𝐞𝐥𝐞𝐭𝐞"), callback_data=f'delete_{user_id}_{file_name}'),
            types.InlineKeyboardButton(B("📜 𝐋𝐨𝐠𝐬"), callback_data=f'logs_{user_id}_{file_name}')
        )
    else:
        markup.row(
            types.InlineKeyboardButton(B("🟢 𝐒𝐭𝐚𝐫𝐭"), callback_data=f'start_{user_id}_{file_name}'),
            types.InlineKeyboardButton(B("🗑️ 𝐃𝐞𝐥𝐞𝐭𝐞"), callback_data=f'delete_{user_id}_{file_name}')
        )
        markup.row(
            types.InlineKeyboardButton(B("📜 𝐕𝐢𝐞𝐰 𝐋𝐨𝐠𝐬"), callback_data=f'logs_{user_id}_{file_name}')
        )
    
    markup.add(types.InlineKeyboardButton(B("🔙 𝐁𝐚𝐜𝐤"), callback_data='check_files'))
    return markup

def create_admin_panel():
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐚𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton(B('➕ 𝐀𝐝𝐝 𝐀𝐝𝐦𝐢𝐧'), callback_data='add_admin'),
        types.InlineKeyboardButton(B('➖ 𝐑𝐞𝐦𝐨𝐯𝐞 𝐀𝐝𝐦𝐢𝐧'), callback_data='remove_admin')
    )
    markup.row(
        types.InlineKeyboardButton(B('📋 𝐋𝐢𝐬𝐭 𝐀𝐝𝐦𝐢𝐧𝐬'), callback_data='list_admins'),
        types.InlineKeyboardButton(B('📊 𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐬'), callback_data='system_stats')
    )
    markup.row(types.InlineKeyboardButton(B('🔙 𝐁𝐚𝐜𝐤'), callback_data='back_to_main'))
    return markup

def create_subscription_menu():
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐦𝐞𝐧𝐮"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton(B('➕ 𝐀𝐝𝐝 𝐒𝐮𝐛'), callback_data='add_subscription'),
        types.InlineKeyboardButton(B('➖ 𝐑𝐞𝐦𝐨𝐯𝐞 𝐒𝐮𝐛'), callback_data='remove_subscription')
    )
    markup.row(types.InlineKeyboardButton(B('🔍 𝐂𝐡𝐞𝐜𝐤 𝐒𝐮𝐛'), callback_data='check_subscription'))
    markup.row(types.InlineKeyboardButton(B('🔙 𝐁𝐚𝐜𝐤'), callback_data='back_to_main'))
    return markup

def create_referral_menu(user_id):
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐦𝐞𝐧𝐮"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    referral_code = referral_system.get_referral_code(user_id)
    bot_username = bot.get_me().username
    # 🚀 FIXED: Using regular font for referral link (not bold)
    referral_link = f"https://t.me/{bot_username}?start={referral_code}"
    
    markup.add(types.InlineKeyboardButton(B('🔗 𝐂𝐨𝐩𝐲 𝐋𝐢𝐧𝐤'), 
                                         callback_data=f'copy_referral_{user_id}'))
    markup.add(types.InlineKeyboardButton(B('📊 𝐌𝐲 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬'), 
                                         callback_data=f'check_referrals_{user_id}'))
    markup.add(types.InlineKeyboardButton(B('🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝'), 
                                         callback_data='leaderboard'))
    markup.add(types.InlineKeyboardButton(B('📋 𝐐𝐑 𝐂𝐨𝐝𝐞'), 
                                         callback_data=f'qr_referral_{user_id}'))
    markup.add(types.InlineKeyboardButton(B('🔙 𝐁𝐚𝐜𝐤'), callback_data='back_to_main'))
    
    return markup, referral_link

def create_leaderboard_markup():
    """𝐂𝐫𝐞𝐚𝐭𝐞 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝 𝐦𝐚𝐫𝐤𝐮𝐩"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(B('🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡'), callback_data='refresh_leaderboard'))
    markup.add(types.InlineKeyboardButton(B('🏆 𝐌𝐲 𝐑𝐚𝐧𝐤'), callback_data='my_rank'))
    markup.add(types.InlineKeyboardButton(B('🤝 𝐑𝐞𝐟𝐞𝐫'), callback_data='refer'))
    markup.add(types.InlineKeyboardButton(B('🔙 𝐁𝐚𝐜𝐤'), callback_data='back_to_main'))
    return markup

# ================================
# 𝐒𝐂𝐑𝐈𝐏𝐓 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌
# ================================
TELEGRAM_MODULES = {
    'telebot': 'pyTelegramBotAPI',
    'telegram': 'python-telegram-bot',
    'aiogram': 'aiogram',
    'pyrogram': 'pyrogram',
    'telethon': 'telethon',
    'requests': 'requests',
    'flask': 'Flask',
    'psutil': 'psutil',
    'qrcode': 'qrcode',
    'pillow': 'Pillow',
    'cryptography': 'cryptography',
    'bs4': 'beautifulsoup4',
    'pandas': 'pandas',
    'numpy': 'numpy'
}

def attempt_install_pip(module_name, message):
    """𝐀𝐭𝐭𝐞𝐦𝐩𝐭 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐏𝐲𝐭𝐡𝐨𝐧 𝐦𝐨𝐝𝐮𝐥𝐞"""
    package_name = TELEGRAM_MODULES.get(module_name.lower(), module_name)
    if package_name is None:
        return False
    
    try:
        bot.reply_to(message, B(f"🐍 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠 `{module_name}`..."))
        command = [sys.executable, '-m', 'pip', 'install', package_name]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            bot.reply_to(message, B(f"✅ 𝐏𝐚𝐜𝐤𝐚𝐠𝐞 `{package_name}` 𝐢𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝."))
            return True
        else:
            bot.reply_to(message, B(f"❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 `{package_name}`."))
            return False
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))
        return False

def run_script(script_path, user_id, user_folder, file_name, message):
    """𝐑𝐮𝐧 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭"""
    try:
        # 𝐒𝐡𝐨𝐰 𝐩𝐫𝐨𝐠𝐫𝐞𝐬𝐬 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
        msg = bot.reply_to(message, ProgressAnimation.execute_animation()[0])
        
        for i, frame in enumerate(ProgressAnimation.execute_animation()):
            try:
                bot.edit_message_text(frame, message.chat.id, msg.message_id)
                time.sleep(0.3)
            except:
                pass
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐢𝐟 𝐟𝐢𝐥𝐞 𝐞𝐱𝐢𝐬𝐭𝐬
        if not os.path.exists(script_path):
            bot.edit_message_text(B(f"❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝: `{file_name}`"), 
                                message.chat.id, msg.message_id)
            return
        
        # 𝐏𝐫𝐞-𝐜𝐡𝐞𝐜𝐤 𝐟𝐨𝐫 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐦𝐨𝐝𝐮𝐥𝐞𝐬
        check_command = [sys.executable, script_path]
        check_proc = None
        
        try:
            check_proc = subprocess.Popen(check_command, cwd=user_folder, 
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True, encoding='utf-8', errors='ignore')
            stdout, stderr = check_proc.communicate(timeout=5)
            
            if stderr:
                match = re.search(r"ModuleNotFoundError: No module named '(.+?)'", stderr)
                if match:
                    module_name = match.group(1)
                    if attempt_install_pip(module_name, message):
                        time.sleep(2)
                        # 𝐑𝐞𝐭𝐫𝐲 𝐚𝐟𝐭𝐞𝐫 𝐢𝐧𝐬𝐭𝐚𝐥𝐥
                        run_script(script_path, user_id, user_folder, file_name, message)
                        return
        except subprocess.TimeoutExpired:
            if check_proc:
                check_proc.kill()
                check_proc.communicate()
        
        # 𝐒𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐬𝐜𝐫𝐢𝐩𝐭
        log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
        log_file = open(log_file_path, 'w', encoding='utf-8', errors='ignore')
        
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        
        process = subprocess.Popen(
            [sys.executable, script_path],
            cwd=user_folder,
            stdout=log_file,
            stderr=log_file,
            stdin=subprocess.PIPE,
            startupinfo=startupinfo,
            encoding='utf-8',
            errors='ignore'
        )
        
        script_key = f"{user_id}_{file_name}"
        bot_scripts[script_key] = {
            'process': process,
            'log_file': log_file,
            'file_name': file_name,
            'user_id': user_id,
            'start_time': datetime.now(),
            'type': 'py',
            'script_key': script_key
        }
        
        # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
        recovery_system.save_running_script(user_id, file_name, script_path, process.pid)
        
        bot.edit_message_text(
            B(f"✅ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐬𝐜𝐫𝐢𝐩𝐭 `{file_name}` 𝐬𝐭𝐚𝐫𝐭𝐞𝐝!\n📊 𝐏𝐈𝐃: `{process.pid}`"),
            message.chat.id, msg.message_id
        )
        
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {str(e)}"))

def run_js_script(script_path, user_id, user_folder, file_name, message):
    """𝐑𝐮𝐧 𝐉𝐚𝐯𝐚𝐒𝐜𝐫𝐢𝐩𝐭 𝐬𝐜𝐫𝐢𝐩𝐭"""
    try:
        msg = bot.reply_to(message, ProgressAnimation.execute_animation()[0])
        
        for i, frame in enumerate(ProgressAnimation.execute_animation()):
            try:
                bot.edit_message_text(frame, message.chat.id, msg.message_id)
                time.sleep(0.3)
            except:
                pass
        
        if not os.path.exists(script_path):
            bot.edit_message_text(B(f"❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝: `{file_name}`"), 
                                message.chat.id, msg.message_id)
            return
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐟𝐨𝐫 𝐦𝐢𝐬𝐬𝐢𝐧𝐠 𝐍𝐏𝐌 𝐦𝐨𝐝𝐮𝐥𝐞𝐬
        check_command = ['node', script_path]
        check_proc = None
        
        try:
            check_proc = subprocess.Popen(check_command, cwd=user_folder,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True, encoding='utf-8', errors='ignore')
            stdout, stderr = check_proc.communicate(timeout=5)
            
            if stderr and 'Cannot find module' in stderr:
                match = re.search(r"Cannot find module '(.+?)'", stderr)
                if match:
                    module_name = match.group(1)
                    bot.reply_to(message, B(f"📦 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠 `{module_name}`..."))
                    
                    try:
                        subprocess.run(['npm', 'install', module_name], cwd=user_folder,
                                     capture_output=True, text=True, check=True)
                        bot.reply_to(message, B(f"✅ 𝐍𝐏𝐌 𝐩𝐚𝐜𝐤𝐚𝐠𝐞 `{module_name}` 𝐢𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝."))
                        time.sleep(2)
                        run_js_script(script_path, user_id, user_folder, file_name, message)
                        return
                    except:
                        bot.reply_to(message, B(f"❌ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 `{module_name}`."))
        except subprocess.TimeoutExpired:
            if check_proc:
                check_proc.kill()
                check_proc.communicate()
        
        # 𝐒𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐬𝐜𝐫𝐢𝐩𝐭
        log_file_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
        log_file = open(log_file_path, 'w', encoding='utf-8', errors='ignore')
        
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        
        process = subprocess.Popen(
            ['node', script_path],
            cwd=user_folder,
            stdout=log_file,
            stderr=log_file,
            stdin=subprocess.PIPE,
            startupinfo=startupinfo,
            encoding='utf-8',
            errors='ignore'
        )
        
        script_key = f"{user_id}_{file_name}"
        bot_scripts[script_key] = {
            'process': process,
            'log_file': log_file,
            'file_name': file_name,
            'user_id': user_id,
            'start_time': datetime.now(),
            'type': 'js',
            'script_key': script_key
        }
        
        # 𝐒𝐚𝐯𝐞 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
        recovery_system.save_running_script(user_id, file_name, script_path, process.pid)
        
        bot.edit_message_text(
            B(f"✅ 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭 `{file_name}` 𝐬𝐭𝐚𝐫𝐭𝐞𝐝!\n📊 𝐏𝐈𝐃: `{process.pid}`"),
            message.chat.id, msg.message_id
        )
        
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐉𝐒 𝐬𝐜𝐫𝐢𝐩𝐭: {str(e)}"))

# ================================
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐎𝐏𝐄𝐑𝐀𝐓𝐈𝐎𝐍𝐒
# ================================
DB_LOCK = threading.Lock()

def save_user_file(user_id, file_name, file_type='py'):
    """𝐒𝐚𝐯𝐞 𝐮𝐬𝐞𝐫 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    with DB_LOCK:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        try:
            c.execute('''INSERT OR REPLACE INTO user_files 
                         (user_id, file_name, file_type, uploaded_at) 
                         VALUES (?, ?, ?, ?)''',
                      (user_id, file_name, file_type, datetime.now().isoformat()))
            conn.commit()
            
            if user_id not in user_files:
                user_files[user_id] = []
            user_files[user_id] = [(fn, ft) for fn, ft in user_files[user_id] if fn != file_name]
            user_files[user_id].append((file_name, file_type))
            
            logger.info(f"💾 𝐒𝐚𝐯𝐞𝐝 𝐟𝐢𝐥𝐞 '{file_name}' 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 {user_id}")
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐚𝐯𝐢𝐧𝐠 𝐟𝐢𝐥𝐞: {e}")
        finally:
            conn.close()

def remove_user_file_db(user_id, file_name):
    """𝐑𝐞𝐦𝐨𝐯𝐞 𝐮𝐬𝐞𝐫 𝐟𝐢𝐥𝐞 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"""
    with DB_LOCK:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        try:
            c.execute('DELETE FROM user_files WHERE user_id = ? AND file_name = ?', 
                      (user_id, file_name))
            conn.commit()
            
            if user_id in user_files:
                user_files[user_id] = [f for f in user_files[user_id] if f[0] != file_name]
                if not user_files[user_id]:
                    del user_files[user_id]
            
            # 𝐑𝐞𝐦𝐨𝐯𝐞 𝐟𝐫𝐨𝐦 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
            recovery_system.remove_running_script(user_id, file_name)
            
            logger.info(f"🗑️ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐟𝐢𝐥𝐞 '{file_name}' 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 {user_id}")
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐦𝐨𝐯𝐢𝐧𝐠 𝐟𝐢𝐥𝐞: {e}")
        finally:
            conn.close()

def add_active_user(user_id, username=None):
    """𝐀𝐝𝐝 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫"""
    active_users.add(user_id)
    with DB_LOCK:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        try:
            c.execute('''INSERT OR REPLACE INTO active_users 
                         (user_id, username, first_join, last_seen) 
                         VALUES (?, ?, COALESCE((SELECT first_join FROM active_users WHERE user_id = ?), ?), ?)''',
                      (user_id, username, user_id, datetime.now().isoformat(), datetime.now().isoformat()))
            conn.commit()
            logger.info(f"👤 𝐀𝐝𝐝𝐞𝐝 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫 {user_id}")
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐚𝐝𝐝𝐢𝐧𝐠 𝐚𝐜𝐭𝐢𝐯𝐞 𝐮𝐬𝐞𝐫: {e}")
        finally:
            conn.close()

def save_subscription(user_id, expiry, tier='premium'):
    """𝐒𝐚𝐯𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧"""
    with DB_LOCK:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        try:
            expiry_str = expiry.isoformat() if expiry else None
            c.execute('''INSERT OR REPLACE INTO subscriptions 
                         (user_id, expiry, tier, created_at) 
                         VALUES (?, ?, ?, ?)''',
                      (user_id, expiry_str, tier, datetime.now().isoformat()))
            conn.commit()
            user_subscriptions[user_id] = {'expiry': expiry, 'tier': tier}
            logger.info(f"💳 𝐒𝐚𝐯𝐞𝐝 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐟𝐨𝐫 {user_id}")
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐚𝐯𝐢𝐧𝐠 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧: {e}")
        finally:
            conn.close()

def remove_subscription_db(user_id):
    """𝐑𝐞𝐦𝐨𝐯𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧"""
    with DB_LOCK:
        conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        c = conn.cursor()
        try:
            c.execute('DELETE FROM subscriptions WHERE user_id = ?', (user_id,))
            conn.commit()
            if user_id in user_subscriptions:
                del user_subscriptions[user_id]
            logger.info(f"🗑️ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐟𝐨𝐫 {user_id}")
        except Exception as e:
            logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐦𝐨𝐯𝐢𝐧𝐠 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧: {e}")
        finally:
            conn.close()

# ================================
# 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
@bot.message_handler(commands=['start'])
def command_send_welcome(message):
    """𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐰𝐢𝐭𝐡 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐚𝐧𝐝 𝐩𝐫𝐨𝐟𝐢𝐥𝐞 𝐩𝐢𝐜𝐭𝐮𝐫𝐞"""
    user_id = message.from_user.id
    username = message.from_user.username
    add_active_user(user_id, username)
    
    # Update user's username in referral system
    referral_system.update_user_username(user_id, username)
    
    # 𝐂𝐡𝐞𝐜𝐤 𝐟𝐨𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐜𝐨𝐝𝐞
    referral_code = None
    if len(message.text.split()) > 1:
        referral_code = message.text.split()[1].strip()
    
    # 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥
    if referral_code and referral_code.startswith('EXU'):
        try:
            referrer_id = int(referral_code[3:-4])  # 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐟𝐫𝐨𝐦 𝐜𝐨𝐝𝐞
            if referrer_id != user_id:
                if referral_system.add_referral(referrer_id, user_id, username):
                    bot.reply_to(message, B(f"🎉 𝐘𝐨𝐮 𝐰𝐞𝐫𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐞𝐝 𝐛𝐲 𝐮𝐬𝐞𝐫 𝐈𝐃: `{referrer_id}`"))
        except:
            pass
    
    tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[tier]
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id) if tier == 'free' else True
    user_rank = referral_system.get_user_rank(user_id)
    
    # 𝐓𝐫𝐲 𝐭𝐨 𝐠𝐞𝐭 𝐮𝐬𝐞𝐫'𝐬 𝐩𝐫𝐨𝐟𝐢𝐥𝐞 𝐩𝐡𝐨𝐭𝐨
    try:
        # 𝐆𝐞𝐭 𝐮𝐬𝐞𝐫 𝐩𝐫𝐨𝐟𝐢𝐥𝐞 𝐩𝐡𝐨𝐭𝐨𝐬
        user_profile_photos = bot.get_user_profile_photos(user_id, limit=1)
        
        welcome_text = B(f"""
┏━━━━━━━━━━━━━━━━━━━━━━┓
┃   🚀 𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆   ┃
┃      𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟑.𝟏     ┃
┗━━━━━━━━━━━━━━━━━━━━━━┛

👤 𝐖𝐞𝐥𝐜𝐨𝐦𝐞, {message.from_user.first_name}!
🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: `{user_id}`
🎫 𝐓𝐢𝐞𝐫: {tier_info['icon']} {tier_info['name']}
📁 𝐅𝐢𝐥𝐞𝐬: {get_user_file_count(user_id)}/{get_user_file_limit(user_id)}

📊 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {referral_count}/3
🏆 𝐑𝐚𝐧𝐤: #{user_rank if user_rank else "𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝"}
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

📢 *𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:* {UPDATE_CHANNEL}
👥 *𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩:* {UPDATE_GROUP}

⚡ 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:
• 𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐒𝐲𝐬𝐭𝐞𝐦
• 𝐓𝐢𝐞𝐫-𝐁𝐚𝐬𝐞𝐝 𝐇𝐨𝐬𝐭𝐢𝐧𝐠
• 𝐏𝐲𝐭𝐡𝐨𝐧/𝐉𝐒 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
• 𝐑𝐞𝐚𝐥-𝐓𝐢𝐦𝐞 𝐌𝐨𝐧𝐢𝐭𝐨𝐫𝐢𝐧𝐠
• 🏆 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝

𝐔𝐬𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐧𝐚𝐯𝐢𝐠𝐚𝐭𝐞.
""")
        
        # 𝐈𝐟 𝐮𝐬𝐞𝐫 𝐡𝐚𝐬 𝐩𝐫𝐨𝐟𝐢𝐥𝐞 𝐩𝐡𝐨𝐭𝐨, 𝐬𝐞𝐧𝐝 𝐢𝐭 𝐰𝐢𝐭𝐡 𝐜𝐚𝐩𝐭𝐢𝐨𝐧
        if user_profile_photos.total_count > 0:
            file_id = user_profile_photos.photos[0][-1].file_id
            bot.send_photo(message.chat.id, file_id, caption=welcome_text,
                          reply_markup=create_reply_keyboard_main_menu(user_id),
                          parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, welcome_text,
                           reply_markup=create_reply_keyboard_main_menu(user_id),
                           parse_mode='Markdown')
    
    except Exception as e:
        # 𝐅𝐚𝐥𝐥𝐛𝐚𝐜𝐤 𝐢𝐟 𝐜𝐚𝐧'𝐭 𝐠𝐞𝐭 𝐩𝐫𝐨𝐟𝐢𝐥𝐞 𝐩𝐡𝐨𝐭𝐨
        welcome_text = B(f"""
┏━━━━━━━━━━━━━━━━━━━━━━┓
┃   🚀 𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆   ┃
┃      𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟑.𝟏     ┃
┗━━━━━━━━━━━━━━━━━━━━━━┛

👤 𝐖𝐞𝐥𝐜𝐨𝐦𝐞, {message.from_user.first_name}!
🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: `{user_id}`
🎫 𝐓𝐢𝐞𝐫: {tier_info['icon']} {tier_info['name']}
📁 𝐅𝐢𝐥𝐞𝐬: {get_user_file_count(user_id)}/{get_user_file_limit(user_id)}

📊 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {referral_count}/3
🏆 𝐑𝐚𝐧𝐤: #{user_rank if user_rank else "𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝"}
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

📢 *𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:* {UPDATE_CHANNEL}
👥 *𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩:* {UPDATE_GROUP}

⚡ 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:
• 𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐒𝐲𝐬𝐭𝐞𝐦
• 𝐓𝐢𝐞𝐫-𝐁𝐚𝐬𝐞𝐝 𝐇𝐨𝐬𝐭𝐢𝐧𝐠
• 𝐏𝐲𝐭𝐡𝐨𝐧/𝐉𝐒 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
• 𝐑𝐞𝐚𝐥-𝐓𝐢𝐦𝐞 𝐌𝐨𝐧𝐢𝐭𝐨𝐫𝐢𝐧𝐠
• 🏆 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝

𝐔𝐬𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐧𝐚𝐯𝐢𝐠𝐚𝐭𝐞.
""")
        bot.send_message(message.chat.id, welcome_text,
                       reply_markup=create_reply_keyboard_main_menu(user_id),
                       parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def command_help(message):
    """𝐇𝐞𝐥𝐩 𝐜𝐨𝐦𝐦𝐚𝐧𝐝"""
    help_text = B(f"""
🤖 *𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐇𝐄𝐋𝐏*

*𝐁𝐚𝐬𝐢𝐜 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬:*
/start - 𝐒𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭
/help - 𝐒𝐡𝐨𝐰 𝐭𝐡𝐢𝐬 𝐡𝐞𝐥𝐩 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
/refer - 𝐆𝐞𝐭 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤
/leaderboard - 𝐒𝐡𝐨𝐰 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝
/stats - 𝐒𝐡𝐨𝐰 𝐛𝐨𝐭 𝐬𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐬

*𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐅𝐢𝐥𝐞𝐬:*
• 𝐒𝐞𝐧𝐝 𝐚 .𝐩𝐲, .𝐣𝐬, 𝐨𝐫 .𝐳𝐢𝐩 𝐟𝐢𝐥𝐞
• 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐚𝐮𝐭𝐨-𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐝𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬
• 𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭 𝐰𝐢𝐥𝐥 𝐬𝐭𝐚𝐫𝐭 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲

*𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐒𝐲𝐬𝐭𝐞𝐦:*
• 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐎𝐰𝐧𝐞𝐫: ✅ 𝐀𝐥𝐰𝐚𝐲𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
• 𝐅𝐫𝐞𝐞: 𝐄𝐧𝐚𝐛𝐥𝐞 𝐛𝐲 𝐫𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝟑 𝐟𝐫𝐢𝐞𝐧𝐝𝐬

*𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐲𝐬𝐭𝐞𝐦:*
1. 𝐆𝐞𝐭 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤 𝐯𝐢𝐚 /𝐫𝐞𝐟𝐞𝐫
2. 𝐒𝐡𝐚𝐫𝐞 𝐰𝐢𝐭𝐡 𝐟𝐫𝐢𝐞𝐧𝐝𝐬
3. 𝐄𝐚𝐜𝐡 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐛𝐫𝐢𝐧𝐠𝐬 𝐲𝐨𝐮 𝐜𝐥𝐨𝐬𝐞𝐫 𝐭𝐨 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭
4. 𝐀𝐟𝐭𝐞𝐫 𝟑 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬, 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝!
5. 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐨𝐧 𝐭𝐡𝐞 🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝

*𝐒𝐮𝐩𝐩𝐨𝐫𝐭:*
📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬: {UPDATE_CHANNEL}
👥 𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩: {UPDATE_GROUP}
👤 𝐂𝐨𝐧𝐭𝐚𝐜𝐭: @{YOUR_USERNAME.replace('@', '')}
""")
    
    bot.reply_to(message, help_text, parse_mode='Markdown')

@bot.message_handler(commands=['refer'])
def command_refer(message):
    """𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐜𝐨𝐦𝐦𝐚𝐧𝐝"""
    user_id = message.from_user.id
    tier = get_user_tier(user_id)
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id) if tier == 'free' else True
    
    markup, referral_link = create_referral_menu(user_id)
    
    # 🚀 FIXED: Using regular font for referral link (not bold)
    refer_text = B(f"""
🤝 *𝐑𝐄𝐅𝐄𝐑𝐑𝐀𝐋 𝐒𝐘𝐒𝐓𝐄𝐌*

👤 𝐘𝐨𝐮𝐫 𝐈𝐃: `{user_id}`
📊 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: *{referral_count}/3*
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

🔗 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐢𝐧𝐤:*
`{referral_link}`

*𝐇𝐨𝐰 𝐢𝐭 𝐰𝐨𝐫𝐤𝐬:*
1. 𝐒𝐡𝐚𝐫𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤
2. 𝐄𝐚𝐜𝐡 𝐟𝐫𝐢𝐞𝐧𝐝 𝐰𝐡𝐨 𝐣𝐨𝐢𝐧𝐬 𝐯𝐢𝐚 𝐲𝐨𝐮𝐫 𝐥𝐢𝐧𝐤 𝐜𝐨𝐮𝐧𝐭𝐬
3. 𝐀𝐟𝐭𝐞𝐫 𝟑 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬, 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝!
4. 𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐲 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐨𝐧 𝐛𝐨𝐭 𝐫𝐞𝐬𝐭𝐚𝐫𝐭
5. 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐨𝐧 𝐭𝐡𝐞 🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝!

*𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬:*
✅ 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
✅ 𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐬𝐭𝐚𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝟐𝟒/𝟕
✅ 𝐍𝐨 𝐦𝐚𝐧𝐮𝐚𝐥 𝐢𝐧𝐭𝐞𝐫𝐯𝐞𝐧𝐭𝐢𝐨𝐧 𝐧𝐞𝐞𝐝𝐞𝐝
✅ 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐟𝐨𝐫 𝐭𝐨𝐩 𝐫𝐚𝐧𝐤𝐬 𝐨𝐧 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝
""")
    
    bot.reply_to(message, refer_text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['leaderboard', 'topref'])
def command_leaderboard(message):
    """𝐒𝐡𝐨𝐰 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝"""
    top_referrers = referral_system.get_top_referrers(limit=10)
    
    if not top_referrers:
        bot.reply_to(message, B("🏆 𝐍𝐨 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬 𝐲𝐞𝐭. 𝐁𝐞 𝐭𝐡𝐞 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐫𝐞𝐟𝐞𝐫!"))
        return
    
    leaderboard_text = B("""
🏆 *𝐑𝐄𝐅𝐄𝐑𝐑𝐀𝐋 𝐋𝐄𝐀𝐃𝐄𝐑𝐁𝐎𝐀𝐑𝐃*
━━━━━━━━━━━━━━━━━━━━━━━━
""")
    
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    
    for i, referrer in enumerate(top_referrers):
        username = referrer['username'] or f"User {referrer['user_id']}"
        if i < len(medals):
            leaderboard_text += B(f"\n{medals[i]} *{username}*\n")
        else:
            leaderboard_text += B(f"\n{i+1}. *{username}*\n")
        
        leaderboard_text += B(f"   👥 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: `{referrer['count']}` | ")
        leaderboard_text += B("🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: " + ("✅" if referrer['auto_restart'] else "❌") + "\n")
    
    # Add user's rank if they're in the system
    user_id = message.from_user.id
    user_rank = referral_system.get_user_rank(user_id)
    referral_count = referral_system.get_referral_count(user_id)
    
    leaderboard_text += B(f"\n━━━━━━━━━━━━━━━━━━━━━━━━\n")
    
    if user_rank:
        leaderboard_text += B(f"👤 *𝐘𝐨𝐮𝐫 𝐑𝐚𝐧𝐤:* #{user_rank}\n")
        leaderboard_text += B(f"📊 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬:* {referral_count}/3\n")
        leaderboard_text += B(f"🔄 *𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭:* {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if referral_count >= 3 else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}\n")
    else:
        leaderboard_text += B(f"👤 *𝐘𝐨𝐮𝐫 𝐑𝐚𝐧𝐤:* 𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝 𝐲𝐞𝐭\n")
        leaderboard_text += B(f"📊 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬:* {referral_count}/3\n")
        leaderboard_text += B(f"🔄 *𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭:* {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if referral_count >= 3 else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}\n")
    
    leaderboard_text += B(f"\n🏅 *𝐍𝐞𝐞𝐝 𝐡𝐞𝐥𝐩?* 𝐔𝐬𝐞 /𝐫𝐞𝐟𝐞𝐫 𝐭𝐨 𝐠𝐞𝐭 𝐲𝐨𝐮𝐫 𝐥𝐢𝐧𝐤!")
    
    bot.reply_to(message, leaderboard_text, parse_mode='Markdown', reply_markup=create_leaderboard_markup())

@bot.message_handler(commands=['recover'])
def command_recover_scripts(message):
    """𝐌𝐚𝐧𝐮𝐚𝐥 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐜𝐨𝐦𝐦𝐚𝐧𝐝"""
    if message.from_user.id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝."))
        return
    
    msg = bot.reply_to(message, ProgressAnimation.recovery_animation()[0])
    
    for i, frame in enumerate(ProgressAnimation.recovery_animation()):
        try:
            bot.edit_message_text(frame, message.chat.id, msg.message_id)
            time.sleep(0.3)
        except:
            pass
    
    recovered = recovery_system.recover_all_scripts()
    
    if recovered:
        bot.edit_message_text(
            B(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝: {len(recovered)} 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"),
            message.chat.id, msg.message_id
        )
    else:
        bot.edit_message_text(
            B("📭 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫."),
            message.chat.id, msg.message_id
        )

@bot.message_handler(commands=['stats'])
def command_stats(message):
    """𝐒𝐡𝐨𝐰 𝐬𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐬"""
    user_id = message.from_user.id
    
    total_users = len(active_users)
    total_files = sum(len(files) for files in user_files.values())
    running_scripts = len([k for k, v in bot_scripts.items() if is_bot_running(v['user_id'], v['file_name'])])
    recovery_count = recovery_system.get_running_count()
    
    # 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐬𝐭𝐚𝐭𝐬
    referral_users = 0
    auto_restart_enabled = 0
    for uid in active_users:
        if referral_system.get_referral_count(uid) > 0:
            referral_users += 1
        if referral_system.is_auto_restart_enabled(uid):
            auto_restart_enabled += 1
    
    stats_text = B(f"""
📊 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒

👥 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
📁 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: {total_files}
🟢 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐒𝐜𝐫𝐢𝐩𝐭𝐬: {running_scripts}
💾 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐒𝐚𝐯𝐞𝐝: {recovery_count}
🔒 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬: {'🔴 𝐋𝐨𝐜𝐤𝐞𝐝' if bot_locked else '🟢 𝐔𝐧𝐥𝐨𝐜𝐤𝐞𝐝'}

🎫 𝐓𝐢𝐞𝐫 𝐃𝐢𝐬𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐨𝐧:
• 𝐅𝐑𝐄𝐄: {len([uid for uid in active_users if get_user_tier(uid) == 'free'])}
• 𝐏𝐑𝐄𝐌𝐈𝐔𝐌: {len([uid for uid in active_users if get_user_tier(uid) == 'premium'])}
• 𝐎𝐖𝐍𝐄𝐑/𝐀𝐃𝐌𝐈𝐍: {len([uid for uid in active_users if get_user_tier(uid) == 'owner'])}

🤝 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬:
• 𝐑𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐬: {referral_users}
• 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐄𝐧𝐚𝐛𝐥𝐞𝐝: {auto_restart_enabled}
• 🏆 𝐓𝐨𝐩 𝐑𝐞𝐟𝐞𝐫𝐫𝐞𝐫: {referral_system.get_top_referrers(limit=1)[0]['count'] if referral_system.get_top_referrers(limit=1) else 0} 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬
""")
    
    bot.reply_to(message, stats_text, parse_mode='Markdown')

@bot.message_handler(commands=['restartall'])
def command_restart_all(message):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"""
    if message.from_user.id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝."))
        return
    
    msg = bot.reply_to(message, ProgressAnimation.execute_animation()[0])
    
    restarted = 0
    for user_id, files in user_files.items():
        for file_name, file_type in files:
            if is_bot_running(user_id, file_name):
                # 𝐒𝐭𝐨𝐩 𝐟𝐢𝐫𝐬𝐭
                script_key = f"{user_id}_{file_name}"
                if script_key in bot_scripts:
                    kill_process_tree(bot_scripts[script_key])
                    del bot_scripts[script_key]
            
            # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭
            user_folder = get_user_folder(user_id)
            file_path = os.path.join(user_folder, file_name)
            
            if os.path.exists(file_path):
                if file_type == 'py':
                    threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, message)).start()
                elif file_type == 'js':
                    threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, message)).start()
                
                restarted += 1
                time.sleep(0.5)
    
    bot.edit_message_text(
        B(f"✅ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 {restarted} 𝐬𝐜𝐫𝐢𝐩𝐭𝐬."),
        message.chat.id, msg.message_id
    )

# ================================
# 𝐑𝐄𝐒𝐓𝐀𝐑𝐓 𝐁𝐎𝐓 𝐂𝐎𝐌𝐌𝐀𝐍𝐃
# ================================
@bot.message_handler(commands=['restartbot'])
def command_restart_bot(message):
    """𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧"""
    if message.from_user.id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝."))
        return
    
    # 𝐒𝐞𝐧𝐝 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
    bot.reply_to(message, B("🚀 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬..."))
    threading.Thread(target=send_restart_notification).start()
    
    # 𝐒𝐡𝐨𝐰 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    msg = bot.reply_to(message, ProgressAnimation.restart_animation()[0])
    
    for i, frame in enumerate(ProgressAnimation.restart_animation()):
        try:
            bot.edit_message_text(frame, message.chat.id, msg.message_id)
            time.sleep(0.5)
        except:
            pass
    
    # 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐭𝐨 𝐬𝐞𝐧𝐝
    time.sleep(5)
    
    bot.edit_message_text(
        B("✅ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐬𝐞𝐧𝐭!\n\n🔄 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐧𝐨𝐰 𝐫𝐞𝐬𝐭𝐚𝐫𝐭..."),
        message.chat.id, msg.message_id
    )
    
    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭
    time.sleep(2)
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.message_handler(content_types=['document'])
def handle_file_upload(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐟𝐢𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐬"""
    user_id = message.from_user.id
    
    if bot_locked and user_id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐁𝐨𝐭 𝐢𝐬 𝐥𝐨𝐜𝐤𝐞𝐝."))
        return
    
    # 𝐂𝐡𝐞𝐜𝐤 𝐟𝐢𝐥𝐞 𝐥𝐢𝐦𝐢𝐭
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    
    if current_files >= file_limit:
        bot.reply_to(message, 
                     B(f"⚠️ 𝐅𝐢𝐥𝐞 𝐥𝐢𝐦𝐢𝐭 𝐫𝐞𝐚𝐜𝐡𝐞𝐝 ({current_files}/{file_limit})."))
        return
    
    doc = message.document
    if not doc.file_name:
        bot.reply_to(message, B("⚠️ 𝐍𝐨 𝐟𝐢𝐥𝐞 𝐧𝐚𝐦𝐞 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝."))
        return
    
    file_ext = os.path.splitext(doc.file_name)[1].lower()
    if file_ext not in ['.py', '.js', '.zip']:
        bot.reply_to(message, B("⚠️ 𝐔𝐧𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐟𝐢𝐥𝐞 𝐭𝐲𝐩𝐞. 𝐔𝐬𝐞 .𝐩𝐲, .𝐣𝐬, 𝐨𝐫 .𝐳𝐢𝐩"))
        return
    
    # 𝐒𝐡𝐨𝐰 𝐮𝐩𝐥𝐨𝐚𝐝 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    msg = bot.reply_to(message, ProgressAnimation.upload_animation()[0])
    
    try:
        # 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐟𝐢𝐥𝐞
        for i, frame in enumerate(ProgressAnimation.upload_animation()):
            try:
                bot.edit_message_text(frame, message.chat.id, msg.message_id)
                time.sleep(0.3)
            except:
                pass
        
        file_info = bot.get_file(doc.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, doc.file_name)
        
        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        
        # 𝐇𝐚𝐧𝐝𝐥𝐞 𝐟𝐢𝐥𝐞 𝐛𝐚𝐬𝐞𝐝 𝐨𝐧 𝐭𝐲𝐩𝐞
        if file_ext == '.zip':
            handle_zip_file(downloaded_file, doc.file_name, user_id, user_folder, message)
        elif file_ext == '.py':
            save_user_file(user_id, doc.file_name, 'py')
            threading.Thread(target=run_script, args=(file_path, user_id, user_folder, doc.file_name, message)).start()
        elif file_ext == '.js':
            save_user_file(user_id, doc.file_name, 'js')
            threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, doc.file_name, message)).start()
        
    except Exception as e:
        bot.edit_message_text(
            B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐮𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐟𝐢𝐥𝐞: {str(e)}"),
            message.chat.id, msg.message_id
        )

def handle_zip_file(file_content, file_name, user_id, user_folder, message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐙𝐈𝐏 𝐟𝐢𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝"""
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp()
        zip_path = os.path.join(temp_dir, file_name)
        
        with open(zip_path, 'wb') as f:
            f.write(file_content)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        # 𝐅𝐢𝐧𝐝 𝐦𝐚𝐢𝐧 𝐬𝐜𝐫𝐢𝐩𝐭
        extracted_files = os.listdir(temp_dir)
        py_files = [f for f in extracted_files if f.endswith('.py')]
        js_files = [f for f in extracted_files if f.endswith('.js')]
        
        main_script = None
        file_type = None
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐟𝐨𝐫 𝐜𝐨𝐦𝐦𝐨𝐧 𝐦𝐚𝐢𝐧 𝐟𝐢𝐥𝐞 𝐧𝐚𝐦𝐞𝐬
        for name in ['main.py', 'bot.py', 'app.py']:
            if name in py_files:
                main_script = name
                file_type = 'py'
                break
        
        if not main_script and py_files:
            main_script = py_files[0]
            file_type = 'py'
        elif not main_script and js_files:
            for name in ['index.js', 'main.js', 'bot.js']:
                if name in js_files:
                    main_script = name
                    file_type = 'js'
                    break
            if not main_script and js_files:
                main_script = js_files[0]
                file_type = 'js'
        
        if not main_script:
            bot.reply_to(message, B("❌ 𝐍𝐨 .𝐩𝐲 𝐨𝐫 .𝐣𝐬 𝐟𝐢𝐥𝐞 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐙𝐈𝐏."))
            return
        
        # 𝐌𝐨𝐯𝐞 𝐟𝐢𝐥𝐞𝐬 𝐭𝐨 𝐮𝐬𝐞𝐫 𝐟𝐨𝐥𝐝𝐞𝐫
        for item in os.listdir(temp_dir):
            src = os.path.join(temp_dir, item)
            dst = os.path.join(user_folder, item)
            
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)
        
        # 𝐒𝐚𝐯𝐞 𝐚𝐧𝐝 𝐫𝐮𝐧
        save_user_file(user_id, main_script, file_type)
        main_script_path = os.path.join(user_folder, main_script)
        
        if file_type == 'py':
            threading.Thread(target=run_script, args=(main_script_path, user_id, user_folder, main_script, message)).start()
        else:
            threading.Thread(target=run_js_script, args=(main_script_path, user_id, user_folder, main_script, message)).start()
        
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐙𝐈𝐏: {str(e)}"))
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

# ================================
# 𝐓𝐄𝐗𝐓 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒 (𝐑𝐞𝐩𝐥𝐲 𝐊𝐞𝐲𝐛𝐨𝐚𝐫𝐝)
# ================================
BUTTON_HANDLERS = {
    B("📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬"): lambda m: bot.reply_to(m, f"📢 *𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:* {UPDATE_CHANNEL}\n👥 *𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩:* {UPDATE_GROUP}", parse_mode='Markdown'),
    B("👥 𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩"): lambda m: bot.reply_to(m, f"👥 *𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩:* {UPDATE_GROUP}", parse_mode='Markdown'),
    B("📤 𝐔𝐩𝐥𝐨𝐚𝐝"): lambda m: bot.reply_to(m, B("📤 𝐒𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 .𝐩𝐲, .𝐣𝐬, 𝐨𝐫 .𝐳𝐢𝐩 𝐟𝐢𝐥𝐞.")),
    B("📂 𝐌𝐲 𝐅𝐢𝐥𝐞𝐬"): lambda m: show_user_files(m),
    B("⚡ 𝐒𝐩𝐞𝐞𝐝"): lambda m: check_speed(m),
    B("📊 𝐒𝐭𝐚𝐭𝐬"): lambda m: command_stats(m),
    B("👤 𝐏𝐫𝐨𝐟𝐢𝐥𝐞"): lambda m: show_profile(m),
    B("🤝 𝐑𝐞𝐟𝐞𝐫"): lambda m: command_refer(m),
    B("🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝"): lambda m: command_leaderboard(m),
    B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐀𝐥𝐥"): lambda m: command_restart_all(m),
    B("👑 𝐀𝐝𝐦𝐢𝐧"): lambda m: show_admin_panel(m),
    B("💳 𝐒𝐮𝐛𝐬"): lambda m: show_subscription_panel(m),
    B("📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭"): lambda m: start_broadcast(m),
    B("🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫"): lambda m: command_recover_scripts(m),
    B("🚀 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐁𝐨𝐭"): lambda m: command_restart_bot(m),
    B("📞 𝐂𝐨𝐧𝐭𝐚𝐜𝐭"): lambda m: bot.reply_to(m, f"📞 *𝐂𝐨𝐧𝐭𝐚𝐜𝐭:* @{YOUR_USERNAME.replace('@', '')}", parse_mode='Markdown')
}

@bot.message_handler(func=lambda message: message.text in BUTTON_HANDLERS)
def handle_button_click(message):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐩𝐥𝐲 𝐤𝐞𝐲𝐛𝐨𝐚𝐫𝐝 𝐛𝐮𝐭𝐭𝐨𝐧𝐬"""
    handler = BUTTON_HANDLERS.get(message.text)
    if handler:
        handler(message)

def show_user_files(message):
    """𝐒𝐡𝐨𝐰 𝐮𝐬𝐞𝐫'𝐬 𝐟𝐢𝐥𝐞𝐬"""
    user_id = message.from_user.id
    files = user_files.get(user_id, [])
    
    if not files:
        bot.reply_to(message, B("📭 𝐍𝐨 𝐟𝐢𝐥𝐞𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐲𝐞𝐭."))
        return
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    for file_name, file_type in files:
        is_running = is_bot_running(user_id, file_name)
        status = "🟢" if is_running else "🔴"
        btn_text = B(f"{status} {file_name} ({file_type})")
        markup.add(types.InlineKeyboardButton(btn_text, callback_data=f'file_{user_id}_{file_name}'))
    
    bot.reply_to(message, B("📂 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞𝐬:"), reply_markup=markup)

def check_speed(message):
    """𝐂𝐡𝐞𝐜𝐤 𝐛𝐨𝐭 𝐬𝐩𝐞𝐞𝐝"""
    start_time = time.time()
    msg = bot.reply_to(message, B("🏃 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐬𝐩𝐞𝐞𝐝..."))
    latency = round((time.time() - start_time) * 1000, 2)
    
    bot.edit_message_text(
        B(f"⚡ 𝐁𝐨𝐭 𝐒𝐩𝐞𝐞𝐝\n\n⏱️ 𝐋𝐚𝐭𝐞𝐧𝐜𝐲: {latency}𝐦𝐬\n🔒 𝐒𝐭𝐚𝐭𝐮𝐬: {'🔴 𝐋𝐨𝐜𝐤𝐞𝐝' if bot_locked else '🟢 𝐔𝐧𝐥𝐨𝐜𝐤𝐞𝐝'}"),
        message.chat.id, msg.message_id
    )

def show_profile(message):
    """𝐒𝐡𝐨𝐰 𝐮𝐬𝐞𝐫 𝐩𝐫𝐨𝐟𝐢𝐥𝐞"""
    user_id = message.from_user.id
    tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[tier]
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id) if tier == 'free' else True
    user_rank = referral_system.get_user_rank(user_id)
    
    profile_text = B(f"""
👤 𝐏𝐑𝐎𝐅𝐈𝐋𝐄

🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: `{user_id}`
👤 𝐍𝐚𝐦𝐞: {message.from_user.first_name}
🎫 𝐓𝐢𝐞𝐫: {tier_info['icon']} {tier_info['name']}
📁 𝐅𝐢𝐥𝐞𝐬: {get_user_file_count(user_id)}/{get_user_file_limit(user_id)}
🟢 𝐑𝐮𝐧𝐧𝐢𝐧𝐠: {len([1 for f in user_files.get(user_id, []) if is_bot_running(user_id, f[0])])}

🤝 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {referral_count}/3
🏆 𝐑𝐚𝐧𝐤: #{user_rank if user_rank else "𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝"}
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

*𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐈𝐧𝐟𝐨:*
• 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐎𝐰𝐧𝐞𝐫: ✅ 𝐀𝐥𝐰𝐚𝐲𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
• 𝐅𝐫𝐞𝐞: 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐬 𝟑 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬

*𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬:*
✅ 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
✅ 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐨𝐧 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝
✅ 𝐒𝐡𝐨𝐰𝐜𝐚𝐬𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝐩𝐨𝐰𝐞𝐫!
""")
    
    bot.reply_to(message, profile_text, parse_mode='Markdown')

def show_admin_panel(message):
    """𝐒𝐡𝐨𝐰 𝐚𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥"""
    if message.from_user.id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝."))
        return
    
    bot.reply_to(message, B("👑 𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋"), reply_markup=create_admin_panel())

def show_subscription_panel(message):
    """𝐒𝐡𝐨𝐰 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐚𝐧𝐞𝐥"""
    if message.from_user.id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝."))
        return
    
    bot.reply_to(message, B("💳 𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐏𝐓𝐈𝐎𝐍 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓"), 
                 reply_markup=create_subscription_menu())

def start_broadcast(message):
    """𝐒𝐭𝐚𝐫𝐭 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭"""
    if message.from_user.id not in admin_ids:
        bot.reply_to(message, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝."))
        return
    
    bot.reply_to(message, B("📢 𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭."))
    bot.register_next_step_handler(message, process_broadcast_message)

def process_broadcast_message(message):
    """𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞"""
    if message.from_user.id not in admin_ids:
        return
    
    broadcast_text = message.text or message.caption
    if not broadcast_text:
        bot.reply_to(message, B("⚠️ 𝐍𝐨 𝐦𝐞𝐬𝐠𝐚𝐠𝐞 𝐟𝐨𝐮𝐧𝐝."))
        return
    
    # 𝐂𝐨𝐧𝐟𝐢𝐫𝐦𝐚𝐭𝐢𝐨𝐧
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(B('✅ 𝐂𝐨𝐧𝐟𝐢𝐫𝐦'), callback_data=f'broadcast_confirm_{message.message_id}'),
        types.InlineKeyboardButton(B('❌ 𝐂𝐚𝐧𝐜𝐞𝐥'), callback_data='broadcast_cancel')
    )
    
    preview_text = broadcast_text[:1000].strip() if broadcast_text else "(𝐌𝐞𝐝𝐢𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞)"
    bot.reply_to(message, 
                 B(f"📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐭𝐨 {len(active_users)} 𝐮𝐬𝐞𝐫𝐬?\n\n{preview_text}"), 
                 reply_markup=markup)

# ================================
# 𝐂𝐀𝐋𝐋𝐁𝐀𝐂𝐊 𝐐𝐔𝐄𝐑𝐘 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
# ================================
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐚𝐥𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤 𝐪𝐮𝐞𝐫𝐢𝐞𝐬"""
    user_id = call.from_user.id
    data = call.data
    
    try:
        if data == 'upload':
            upload_callback(call)
        elif data == 'check_files':
            check_files_callback(call)
        elif data.startswith('file_'):
            file_control_callback(call)
        elif data.startswith('start_'):
            start_bot_callback(call)
        elif data.startswith('stop_'):
            stop_bot_callback(call)
        elif data.startswith('restart_'):
            restart_bot_callback(call)
        elif data.startswith('delete_'):
            delete_bot_callback(call)
        elif data.startswith('logs_'):
            logs_bot_callback(call)
        elif data == 'speed':
            speed_callback(call)
        elif data == 'stats':
            stats_callback(call)
        elif data == 'profile':
            profile_callback(call)
        elif data == 'refer':
            refer_callback(call)
        elif data == 'leaderboard':
            leaderboard_callback(call)
        elif data == 'refresh_leaderboard':
            refresh_leaderboard_callback(call)
        elif data == 'my_rank':
            my_rank_callback(call)
        elif data.startswith('copy_referral_'):
            copy_referral_callback(call)
        elif data.startswith('qr_referral_'):
            qr_referral_callback(call)
        elif data.startswith('check_referrals_'):
            check_referrals_callback(call)
        elif data == 'restart_all':
            restart_all_callback(call)
        elif data == 'admin_panel':
            admin_panel_callback(call)
        elif data == 'subscription':
            subscription_callback(call)
        elif data == 'broadcast':
            broadcast_callback(call)
        elif data == 'lock_bot':
            lock_bot_callback(call)
        elif data == 'unlock_bot':
            unlock_bot_callback(call)
        elif data == 'recover_all':
            recover_all_callback(call)
        elif data == 'analytics':
            analytics_callback(call)
        elif data == 'add_admin':
            add_admin_callback(call)
        elif data == 'remove_admin':
            remove_admin_callback(call)
        elif data == 'list_admins':
            list_admins_callback(call)
        elif data == 'system_stats':
            system_stats_callback(call)
        elif data == 'add_subscription':
            add_subscription_callback(call)
        elif data == 'remove_subscription':
            remove_subscription_callback(call)
        elif data == 'check_subscription':
            check_subscription_callback(call)
        elif data.startswith('broadcast_confirm_'):
            broadcast_confirm_callback(call)
        elif data == 'broadcast_cancel':
            broadcast_cancel_callback(call)
        elif data == 'restart_bot':
            restart_bot_callback_callback(call)
        elif data == 'back_to_main':
            back_to_main_callback(call)
        else:
            bot.answer_callback_query(call.id, "❌ 𝐔𝐧𝐤𝐧𝐨𝐰𝐧 𝐜𝐨𝐦𝐦𝐚𝐧𝐝")
            
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤: {e}")
        bot.answer_callback_query(call.id, "❌ 𝐄𝐫𝐫𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐫𝐞𝐪𝐮𝐞𝐬𝐭")

def upload_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐮𝐩𝐥𝐨𝐚𝐝 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    file_limit = get_user_file_limit(user_id)
    current_files = get_user_file_count(user_id)
    
    if current_files >= file_limit:
        bot.answer_callback_query(call.id, 
                                 B(f"⚠️ 𝐅𝐢𝐥𝐞 𝐥𝐢𝐦𝐢𝐭 𝐫𝐞𝐚𝐜𝐡𝐞𝐝 ({current_files}/{file_limit})"), 
                                 show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("📤 𝐒𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 .𝐩𝐲, .𝐣𝐬, 𝐨𝐫 .𝐳𝐢𝐩 𝐟𝐢𝐥𝐞."))

def check_files_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐜𝐡𝐞𝐜𝐤 𝐟𝐢𝐥𝐞𝐬 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    files = user_files.get(user_id, [])
    
    if not files:
        bot.answer_callback_query(call.id, B("📭 𝐍𝐨 𝐟𝐢𝐥𝐞𝐬 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝"), show_alert=True)
        return
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    for file_name, file_type in files:
        is_running = is_bot_running(user_id, file_name)
        status = "🟢" if is_running else "🔴"
        btn_text = B(f"{status} {file_name} ({file_type})")
        markup.add(types.InlineKeyboardButton(btn_text, callback_data=f'file_{user_id}_{file_name}'))
    
    markup.add(types.InlineKeyboardButton(B("🔙 𝐁𝐚𝐜𝐤"), callback_data='back_to_main'))
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(B("📂 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞𝐬:"), 
                         call.message.chat.id, call.message.message_id, 
                         reply_markup=markup)

def file_control_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐟𝐢𝐥𝐞 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    try:
        parts = call.data.split('_')
        if len(parts) < 3:
            return
        
        user_id = int(parts[1])
        file_name = '_'.join(parts[2:])
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧
        if call.from_user.id != user_id and call.from_user.id not in admin_ids:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        files = user_files.get(user_id, [])
        file_info = None
        for fname, ftype in files:
            if fname == file_name:
                file_info = (fname, ftype)
                break
        
        if not file_info:
            bot.answer_callback_query(call.id, B("❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝"), show_alert=True)
            return
        
        is_running = is_bot_running(user_id, file_name)
        
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            B(f"⚙️ 𝐂𝐨𝐧𝐭𝐫𝐨𝐥𝐬 𝐟𝐨𝐫: `{file_name}`\n📁 𝐓𝐲𝐩𝐞: {file_info[1]}\n📊 𝐒𝐭𝐚𝐭𝐮𝐬: {'🟢 𝐑𝐮𝐧𝐧𝐢𝐧𝐠' if is_running else '🔴 𝐒𝐭𝐨𝐩𝐩𝐞𝐝'}"),
            call.message.chat.id, call.message.message_id,
            reply_markup=create_control_buttons(user_id, file_name, is_running),
            parse_mode='Markdown'
        )
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐟𝐢𝐥𝐞 𝐜𝐨𝐧𝐭𝐫𝐨𝐥: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠"))

def start_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐬𝐭𝐚𝐫𝐭 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    try:
        parts = call.data.split('_')
        user_id = int(parts[1])
        file_name = '_'.join(parts[2:])
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧
        if call.from_user.id != user_id and call.from_user.id not in admin_ids:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        if is_bot_running(user_id, file_name):
            bot.answer_callback_query(call.id, B("✅ 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠"), show_alert=True)
            return
        
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        
        if not os.path.exists(file_path):
            bot.answer_callback_query(call.id, B("❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝"), show_alert=True)
            return
        
        # 𝐅𝐢𝐧𝐝 𝐟𝐢𝐥𝐞 𝐭𝐲𝐩𝐞
        file_type = 'py'
        for fname, ftype in user_files.get(user_id, []):
            if fname == file_name:
                file_type = ftype
                break
        
        bot.answer_callback_query(call.id, B("🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭..."))
        
        if file_type == 'py':
            threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, call.message)).start()
        elif file_type == 'js':
            threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, call.message)).start()
        else:
            bot.answer_callback_query(call.id, B("❌ 𝐔𝐧𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐟𝐢𝐥𝐞 𝐭𝐲𝐩𝐞"), show_alert=True)
            
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭"))

def stop_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐬𝐭𝐨𝐩 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    try:
        parts = call.data.split('_')
        user_id = int(parts[1])
        file_name = '_'.join(parts[2:])
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧
        if call.from_user.id != user_id and call.from_user.id not in admin_ids:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        if not is_bot_running(user_id, file_name):
            bot.answer_callback_query(call.id, B("✅ 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐬𝐭𝐨𝐩𝐩𝐞𝐝"), show_alert=True)
            return
        
        script_key = f"{user_id}_{file_name}"
        if script_key in bot_scripts:
            kill_process_tree(bot_scripts[script_key])
            if script_key in bot_scripts:
                del bot_scripts[script_key]
        
        bot.answer_callback_query(call.id, B("🛑 𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐬𝐜𝐫𝐢𝐩𝐭"))
        
        # 𝐔𝐩𝐝𝐚𝐭𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id,
            reply_markup=create_control_buttons(user_id, file_name, False)
        )
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐨𝐩𝐩𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐬𝐭𝐨𝐩𝐩𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭"))

def restart_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    try:
        parts = call.data.split('_')
        user_id = int(parts[1])
        file_name = '_'.join(parts[2:])
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧
        if call.from_user.id != user_id and call.from_user.id not in admin_ids:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        # 𝐒𝐭𝐨𝐩 𝐟𝐢𝐫𝐬𝐭
        if is_bot_running(user_id, file_name):
            script_key = f"{user_id}_{file_name}"
            if script_key in bot_scripts:
                kill_process_tree(bot_scripts[script_key])
                if script_key in bot_scripts:
                    del bot_scripts[script_key]
            time.sleep(1)
        
        # 𝐒𝐭𝐚𝐫𝐭 𝐚𝐠𝐚𝐢𝐧
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        
        if not os.path.exists(file_path):
            bot.answer_callback_query(call.id, B("❌ 𝐅𝐢𝐥𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝"), show_alert=True)
            return
        
        # 𝐅𝐢𝐧𝐝 𝐟𝐢𝐥𝐞 𝐭𝐲𝐩𝐞
        file_type = 'py'
        for fname, ftype in user_files.get(user_id, []):
            if fname == file_name:
                file_type = ftype
                break
        
        bot.answer_callback_query(call.id, B("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭..."))
        
        if file_type == 'py':
            threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, call.message)).start()
        elif file_type == 'js':
            threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, call.message)).start()
            
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭"))

def delete_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐝𝐞𝐥𝐞𝐭𝐞 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    try:
        parts = call.data.split('_')
        user_id = int(parts[1])
        file_name = '_'.join(parts[2:])
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧
        if call.from_user.id != user_id and call.from_user.id not in admin_ids:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        # 𝐒𝐭𝐨𝐩 𝐢𝐟 𝐫𝐮𝐧𝐧𝐢𝐧𝐠
        if is_bot_running(user_id, file_name):
            script_key = f"{user_id}_{file_name}"
            if script_key in bot_scripts:
                kill_process_tree(bot_scripts[script_key])
                if script_key in bot_scripts:
                    del bot_scripts[script_key]
        
        # 𝐃𝐞𝐥𝐞𝐭𝐞 𝐟𝐢𝐥𝐞𝐬
        user_folder = get_user_folder(user_id)
        file_path = os.path.join(user_folder, file_name)
        log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
        
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(log_path):
            os.remove(log_path)
        
        # 𝐑𝐞𝐦𝐨𝐯𝐞 𝐟𝐫𝐨𝐦 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞
        remove_user_file_db(user_id, file_name)
        
        bot.answer_callback_query(call.id, B("🗑️ 𝐅𝐢𝐥𝐞 𝐝𝐞𝐥𝐞𝐭𝐞𝐝"))
        
        # 𝐆𝐨 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐟𝐢𝐥𝐞𝐬 𝐥𝐢𝐬𝐭
        check_files_callback(call)
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐝𝐞𝐥𝐞𝐭𝐢𝐧𝐠 𝐟𝐢𝐥𝐞: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐝𝐞𝐥𝐞𝐭𝐢𝐧𝐠 𝐟𝐢𝐥𝐞"))

def logs_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐥𝐨𝐠𝐬 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    try:
        parts = call.data.split('_')
        user_id = int(parts[1])
        file_name = '_'.join(parts[2:])
        
        # 𝐂𝐡𝐞𝐜𝐤 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧
        if call.from_user.id != user_id and call.from_user.id not in admin_ids:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        user_folder = get_user_folder(user_id)
        log_path = os.path.join(user_folder, f"{os.path.splitext(file_name)[0]}.log")
        
        if not os.path.exists(log_path):
            bot.answer_callback_query(call.id, B("📭 𝐍𝐨 𝐥𝐨𝐠𝐬 𝐟𝐨𝐮𝐧𝐝"), show_alert=True)
            return
        
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                log_content = f.read()
            
            if len(log_content) > 3000:
                log_content = log_content[-3000:]
                log_content = "...\n" + log_content
            
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, 
                           B(f"📜 𝐋𝐨𝐠𝐬 𝐟𝐨𝐫 `{file_name}`:\n```\n{log_content}\n```"), 
                           parse_mode='Markdown')
            
        except Exception as e:
            bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐥𝐨𝐠𝐬"))
            
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐭𝐭𝐢𝐧𝐠 𝐥𝐨𝐠𝐬: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐭𝐭𝐢𝐧𝐠 𝐥𝐨𝐠𝐬"))

def speed_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐬𝐩𝐞𝐞𝐝 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    start_time = time.time()
    bot.answer_callback_query(call.id)
    latency = round((time.time() - start_time) * 1000, 2)
    
    bot.edit_message_text(
        B(f"⚡ 𝐁𝐨𝐭 𝐒𝐩𝐞𝐞𝐝\n\n⏱️ 𝐋𝐚𝐭𝐞𝐧𝐜𝐲: {latency}𝐦𝐬\n🔒 𝐒𝐭𝐚𝐭𝐮𝐬: {'🔴 𝐋𝐨𝐜𝐤𝐞𝐝' if bot_locked else '🟢 𝐔𝐧𝐥𝐨𝐜𝐤𝐞𝐝'}"),
        call.message.chat.id, call.message.message_id
    )

def stats_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐬𝐭𝐚𝐭𝐬 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    
    total_users = len(active_users)
    total_files = sum(len(files) for files in user_files.values())
    running_scripts = len([k for k, v in bot_scripts.items() if is_bot_running(v['user_id'], v['file_name'])])
    recovery_count = recovery_system.get_running_count()
    
    # 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐬𝐭𝐚𝐭𝐬
    referral_users = 0
    auto_restart_enabled = 0
    for uid in active_users:
        if referral_system.get_referral_count(uid) > 0:
            referral_users += 1
        if referral_system.is_auto_restart_enabled(uid):
            auto_restart_enabled += 1
    
    stats_text = B(f"""
📊 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒

👥 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
📁 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: {total_files}
🟢 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐒𝐜𝐫𝐢𝐩𝐭𝐬: {running_scripts}
💾 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐒𝐚𝐯𝐞𝐝: {recovery_count}
🔒 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬: {'🔴 𝐋𝐨𝐜𝐤𝐞𝐝' if bot_locked else '🟢 𝐔𝐧𝐥𝐨𝐜𝐤𝐞𝐝'}

🎫 𝐓𝐢𝐞𝐫 𝐃𝐢𝐬𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐨𝐧:
• 𝐅𝐑𝐄𝐄: {len([uid for uid in active_users if get_user_tier(uid) == 'free'])}
• 𝐏𝐑𝐄𝐌𝐈𝐔𝐌: {len([uid for uid in active_users if get_user_tier(uid) == 'premium'])}
• 𝐎𝐖𝐍𝐄𝐑/𝐀𝐃𝐌𝐈𝐍: {len([uid for uid in active_users if get_user_tier(uid) == 'owner'])}

🤝 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬:
• 𝐑𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐬: {referral_users}
• 𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐄𝐧𝐚𝐛𝐥𝐞𝐝: {auto_restart_enabled}
""")
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(stats_text, call.message.chat.id, call.message.message_id, 
                         parse_mode='Markdown')

def profile_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐩𝐫𝐨𝐟𝐢𝐥𝐞 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[tier]
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id) if tier == 'free' else True
    user_rank = referral_system.get_user_rank(user_id)
    
    profile_text = B(f"""
👤 𝐏𝐑𝐎𝐅𝐈𝐋𝐄

🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: `{user_id}`
👤 𝐍𝐚𝐦𝐞: {call.from_user.first_name}
🎫 𝐓𝐢𝐞𝐫: {tier_info['icon']} {tier_info['name']}
📁 𝐅𝐢𝐥𝐞𝐬: {get_user_file_count(user_id)}/{get_user_file_limit(user_id)}
🟢 𝐑𝐮𝐧𝐧𝐢𝐧𝐠: {len([1 for f in user_files.get(user_id, []) if is_bot_running(user_id, f[0])])}

🤝 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {referral_count}/3
🏆 𝐑𝐚𝐧𝐤: #{user_rank if user_rank else "𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝"}
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

*𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐈𝐧𝐟𝐨:*
• 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐎𝐰𝐧𝐞𝐫: ✅ 𝐀𝐥𝐰𝐚𝐲𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
• 𝐅𝐫𝐞𝐞: 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐬 𝟑 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬
""")
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(profile_text, call.message.chat.id, call.message.message_id, 
                         parse_mode='Markdown')

def refer_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    tier = get_user_tier(user_id)
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id) if tier == 'free' else True
    
    markup, referral_link = create_referral_menu(user_id)
    
    # 🚀 FIXED: Using regular font for referral link (not bold)
    refer_text = B(f"""
🤝 *𝐑𝐄𝐅𝐄𝐑𝐑𝐀𝐋 𝐒𝐘𝐒𝐓𝐄𝐌*

👤 𝐘𝐨𝐮𝐫 𝐈𝐃: `{user_id}`
📊 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: *{referral_count}/3*
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

🔗 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐢𝐧𝐤:*
`{referral_link}`

*𝐇𝐨𝐰 𝐢𝐭 𝐰𝐨𝐫𝐤𝐬:*
1. 𝐒𝐡𝐚𝐫𝐞 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤
2. 𝐄𝐚𝐜𝐡 𝐟𝐫𝐢𝐞𝐧𝐝 𝐰𝐡𝐨 𝐣𝐨𝐢𝐧𝐬 𝐯𝐢𝐚 𝐲𝐨𝐮𝐫 𝐥𝐢𝐧𝐤 𝐜𝐨𝐮𝐧𝐭𝐬
3. 𝐀𝐟𝐭𝐞𝐫 𝟑 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬, 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐬 𝐞𝐧𝐚𝐛𝐥𝐞𝐝!
4. 𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐲 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 𝐨𝐧 𝐛𝐨𝐭 𝐫𝐞𝐬𝐭𝐚𝐫𝐭
5. 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐨𝐧 𝐭𝐡𝐞 🏆 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝!

*𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬:*
✅ 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
✅ 𝐘𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐬𝐭𝐚𝐲 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝟐𝟒/𝟕
✅ 𝐍𝐨 𝐦𝐚𝐧𝐮𝐚𝐥 𝐢𝐧𝐭𝐞𝐫𝐯𝐞𝐧𝐭𝐢𝐨𝐧 𝐧𝐞𝐞𝐝𝐞𝐝
✅ 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐟𝐨𝐫 𝐭𝐨𝐩 𝐫𝐚𝐧𝐤𝐬 𝐨𝐧 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝
""")
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(refer_text, call.message.chat.id, call.message.message_id, 
                         parse_mode='Markdown', reply_markup=markup)

def leaderboard_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    command_leaderboard(call.message)
    bot.answer_callback_query(call.id)

def refresh_leaderboard_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐟𝐫𝐞𝐬𝐡 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    leaderboard_callback(call)

def my_rank_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐦𝐲 𝐫𝐚𝐧𝐤 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    user_rank = referral_system.get_user_rank(user_id)
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id)
    
    if user_rank:
        rank_text = B(f"""
🏆 *𝐘𝐎𝐔𝐑 𝐑𝐀𝐍𝐊*

📊 *𝐑𝐚𝐧𝐤:* #{user_rank}
👥 *𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬:* {referral_count}/3
🔄 *𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭:* {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

*𝐍𝐞𝐞𝐝𝐞𝐝 𝐟𝐨𝐫 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭:* {max(0, 3 - referral_count)} 𝐦𝐨𝐫𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬

*𝐒𝐭𝐚𝐭𝐮𝐬:* {'🎯 𝐀𝐜𝐡𝐢𝐞𝐯𝐞𝐝!' if auto_restart else '🏃 𝐊𝐞𝐞𝐩 𝐠𝐨𝐢𝐧𝐠!'}
""")
    else:
        rank_text = B(f"""
🏆 *𝐘𝐎𝐔𝐑 𝐑𝐀𝐍𝐊*

📊 *𝐑𝐚𝐧𝐤:* 𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝 𝐲𝐞𝐭
👥 *𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬:* {referral_count}/3
🔄 *𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭:* {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

*𝐍𝐞𝐞𝐝𝐞𝐝 𝐟𝐨𝐫 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭:* {max(0, 3 - referral_count)} 𝐦𝐨𝐫𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬

*𝐒𝐭𝐚𝐭𝐮𝐬:* 𝐒𝐭𝐚𝐫𝐭 𝐫𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝! 🚀
""")
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, rank_text, parse_mode='Markdown')

def copy_referral_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐜𝐨𝐩𝐲 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤"""
    try:
        user_id = int(call.data.split('_')[2])
        if call.from_user.id != user_id:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        referral_code = referral_system.get_referral_code(user_id)
        bot_username = bot.get_me().username
        # 🚀 FIXED: Using regular font for referral link (not bold)
        referral_link = f"https://t.me/{bot_username}?start={referral_code}"
        
        bot.answer_callback_query(call.id, B(f"🔗 𝐂𝐨𝐩𝐢𝐞𝐝 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤!"), show_alert=True)
        
        # 𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐥𝐢𝐧𝐤 𝐚𝐬 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 (using regular font)
        bot.send_message(call.message.chat.id, 
                       f"🔗 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐢𝐧𝐤:*\n\n{referral_link}\n\n*𝐒𝐡𝐚𝐫𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐤 𝐰𝐢𝐭𝐡 𝐲𝐨𝐮𝐫 𝐟𝐫𝐢𝐞𝐧𝐝𝐬!*", 
                       parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐜𝐨𝐩𝐲𝐢𝐧𝐠 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐜𝐨𝐩𝐲𝐢𝐧𝐠 𝐥𝐢𝐧𝐤"))

def qr_referral_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐐𝐑 𝐜𝐨𝐝𝐞 𝐟𝐨𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤"""
    try:
        user_id = int(call.data.split('_')[2])
        if call.from_user.id != user_id:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        referral_code = referral_system.get_referral_code(user_id)
        bot_username = bot.get_me().username
        # 🚀 FIXED: Using regular font for referral link in QR code
        referral_link = f"https://t.me/{bot_username}?start={referral_code}"
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(referral_link)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to bytes
        bio = BytesIO()
        img.save(bio, 'PNG')
        bio.seek(0)
        
        bot.answer_callback_query(call.id, B("📱 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐐𝐑 𝐜𝐨𝐝𝐞..."))
        
        # Send QR code
        bot.send_photo(call.message.chat.id, photo=bio, 
                      caption=f"📱 *𝐐𝐑 𝐂𝐨𝐝𝐞 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐥𝐢𝐧𝐤*\n\n*𝐋𝐢𝐧𝐤:* {referral_link}\n\n*𝐒𝐜𝐚𝐧 𝐭𝐡𝐢𝐬 𝐐𝐑 𝐜𝐨𝐝𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐌𝐊-𝐃𝐄𝐕 𝐇𝐨𝐬𝐭𝐢𝐧𝐠!*",
                      parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐐𝐑 𝐜𝐨𝐝𝐞: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐐𝐑 𝐜𝐨𝐝𝐞"))

def check_referrals_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐜𝐡𝐞𝐜𝐤 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬"""
    try:
        user_id = int(call.data.split('_')[2])
        if call.from_user.id != user_id:
            bot.answer_callback_query(call.id, B("⚠️ 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐝𝐞𝐧𝐢𝐞𝐝"), show_alert=True)
            return
        
        referral_info = referral_system.get_user_referral_info(user_id)
        
        if not referral_info:
            referrals_text = B(f"""
📊 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬*

👥 𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: *0/3*
🏆 𝐑𝐚𝐧𝐤: 𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝 𝐲𝐞𝐭
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: ❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝

*𝐍𝐞𝐞𝐝𝐞𝐝 𝐟𝐨𝐫 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭:* 𝟑 𝐦𝐨𝐫𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬

*𝐁𝐞𝐠𝐢𝐧 𝐫𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝐭𝐨𝐝𝐚𝐲 𝐚𝐧𝐝 𝐞𝐧𝐣𝐨𝐲:*
✅ 𝐀𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐞𝐧𝐚𝐛𝐥𝐞𝐝
✅ 𝟐𝟒/𝟕 𝐮𝐩𝐭𝐢𝐦𝐞 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬
✅ 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐨𝐧 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝
""")
        else:
            referrals = referral_info.get('referrals', [])
            referral_count = referral_info.get('count', 0)
            auto_restart = referral_info.get('auto_restart_enabled', False)
            rank = referral_info.get('rank', '𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝')
            
            referrals_text = B(f"""
📊 *𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬*

👥 𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: *{referral_count}/3*
🏆 𝐑𝐚𝐧𝐤: #{rank if rank else "𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝"}
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

*𝐍𝐞𝐞𝐝𝐞𝐝 𝐟𝐨𝐫 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭:* {max(0, 3 - referral_count)} 𝐦𝐨𝐫𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬

*𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬 𝐨𝐟 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭:*
✅ 𝐒𝐜𝐫𝐢𝐩𝐭𝐬 𝐚𝐮𝐭𝐨-𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐨𝐧 𝐛𝐨𝐭 𝐫𝐞𝐛𝐨𝐨𝐭
✅ 𝟐𝟒/𝟕 𝐮𝐩𝐭𝐢𝐦𝐞
✅ 𝐍𝐨 𝐦𝐚𝐧𝐮𝐚𝐥 𝐢𝐧𝐭𝐞𝐫𝐯𝐞𝐧𝐭𝐢𝐨𝐧 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝
✅ 𝐂𝐨𝐦𝐩𝐞𝐭𝐞 𝐟𝐨𝐫 𝐭𝐨𝐩 𝐫𝐚𝐧𝐤𝐬
""")
            
            if referrals:
                referrals_text += B("\n*𝐘𝐨𝐮𝐫 𝐑𝐞𝐟𝐞𝐫𝐫𝐞𝐝 𝐔𝐬𝐞𝐫𝐬:*\n")
                for i, ref in enumerate(referrals[:5], 1):
                    username = ref.get('username', f"User {ref.get('user_id')}")
                    referrals_text += B(f"{i}. {username}\n")
                
                if len(referrals) > 5:
                    referrals_text += B(f"... 𝐚𝐧𝐝 {len(referrals) - 5} 𝐦𝐨𝐫𝐞\n")
        
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, referrals_text, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐜𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐜𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬"))

def restart_all_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐚𝐥𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    msg = bot.send_message(call.message.chat.id, ProgressAnimation.execute_animation()[0])
    
    restarted = 0
    for user_id, files in user_files.items():
        for file_name, file_type in files:
            if is_bot_running(user_id, file_name):
                # 𝐒𝐭𝐨𝐩 𝐟𝐢𝐫𝐬𝐭
                script_key = f"{user_id}_{file_name}"
                if script_key in bot_scripts:
                    kill_process_tree(bot_scripts[script_key])
                    del bot_scripts[script_key]
            
            # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭
            user_folder = get_user_folder(user_id)
            file_path = os.path.join(user_folder, file_name)
            
            if os.path.exists(file_path):
                if file_type == 'py':
                    threading.Thread(target=run_script, args=(file_path, user_id, user_folder, file_name, call.message)).start()
                elif file_type == 'js':
                    threading.Thread(target=run_js_script, args=(file_path, user_id, user_folder, file_name, call.message)).start()
                
                restarted += 1
                time.sleep(0.5)
    
    bot.edit_message_text(
        B(f"✅ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐞𝐝 {restarted} 𝐬𝐜𝐫𝐢𝐩𝐭𝐬."),
        call.message.chat.id, msg.message_id
    )
    bot.answer_callback_query(call.id)

def admin_panel_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐚𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(B("👑 𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋"), 
                         call.message.chat.id, call.message.message_id,
                         reply_markup=create_admin_panel())

def subscription_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(B("💳 𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐏𝐓𝐈𝐎𝐍 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓"), 
                         call.message.chat.id, call.message.message_id,
                         reply_markup=create_subscription_menu())

def broadcast_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("📢 𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭."))
    bot.register_next_step_handler(call.message, process_broadcast_message)

def lock_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐥𝐨𝐜𝐤 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    global bot_locked
    bot_locked = True
    
    bot.answer_callback_query(call.id, B("🔒 𝐁𝐨𝐭 𝐥𝐨𝐜𝐤𝐞𝐝"))
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                 reply_markup=create_main_menu_inline(call.from_user.id))

def unlock_bot_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐮𝐧𝐥𝐨𝐜𝐤 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    global bot_locked
    bot_locked = False
    
    bot.answer_callback_query(call.id, B("🔓 𝐁𝐨𝐭 𝐮𝐧𝐥𝐨𝐜𝐤𝐞𝐝"))
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                 reply_markup=create_main_menu_inline(call.from_user.id))

def recover_all_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐜𝐨𝐯𝐞𝐫 𝐚𝐥𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    msg = bot.send_message(call.message.chat.id, ProgressAnimation.recovery_animation()[0])
    
    for i, frame in enumerate(ProgressAnimation.recovery_animation()):
        try:
            bot.edit_message_text(frame, call.message.chat.id, msg.message_id)
            time.sleep(0.3)
        except:
            pass
    
    recovered = recovery_system.recover_all_scripts()
    
    if recovered:
        bot.edit_message_text(
            B(f"✅ 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝: {len(recovered)} 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"),
            call.message.chat.id, msg.message_id
        )
    else:
        bot.edit_message_text(
            B("📭 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫."),
            call.message.chat.id, msg.message_id
        )
    
    bot.answer_callback_query(call.id)

def analytics_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐚𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    # 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐚𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬
    total_users = len(active_users)
    total_files = sum(len(files) for files in user_files.values())
    running_scripts = len([k for k, v in bot_scripts.items() if is_bot_running(v['user_id'], v['file_name'])])
    
    # 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐬𝐭𝐚𝐭𝐬
    referral_users = 0
    auto_restart_enabled = 0
    total_referrals = 0
    for uid in active_users:
        count = referral_system.get_referral_count(uid)
        if count > 0:
            referral_users += 1
            total_referrals += count
        if referral_system.is_auto_restart_enabled(uid):
            auto_restart_enabled += 1
    
    # 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐬𝐭𝐨𝐫𝐚𝐠𝐞 𝐮𝐬𝐚𝐠𝐞
    total_storage = 0
    for user_id in user_files:
        user_folder = get_user_folder(user_id)
        if os.path.exists(user_folder):
            for root, dirs, files in os.walk(user_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    total_storage += os.path.getsize(file_path)
    
    total_storage_mb = round(total_storage / (1024 * 1024), 2)
    
    # 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐥𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝 𝐬𝐭𝐚𝐭𝐬
    top_referrers = referral_system.get_top_referrers(limit=5)
    leaderboard_stats = ""
    for i, referrer in enumerate(top_referrers, 1):
        username = referrer['username'] or f"User {referrer['user_id']}"
        leaderboard_stats += B(f"{i}. {username}: {referrer['count']} 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬\n")
    
    analytics_text = B(f"""
📈 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐀𝐍𝐀𝐋𝐘𝐓𝐈𝐂𝐒

👥 𝐔𝐬𝐞𝐫 𝐌𝐞𝐭𝐫𝐢𝐜𝐬:
• 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
• 𝐀𝐜𝐭𝐢𝐯𝐞 𝐓𝐨𝐝𝐚𝐲: {len([uid for uid in active_users])}
• 𝐑𝐞𝐟𝐞𝐫𝐫𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐬: {referral_users}

📊 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐌𝐞𝐭𝐫𝐢𝐜𝐬:
• 𝐓𝐨𝐭𝐚𝐥 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {total_referrals}
• 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐄𝐧𝐚𝐛𝐥𝐞𝐝: {auto_restart_enabled}
• 𝐂𝐨𝐧𝐯𝐞𝐫𝐬𝐢𝐨𝐧 𝐑𝐚𝐭𝐞: {round(referral_users/max(total_users, 1)*100, 1)}%

🏆 𝐓𝐨𝐩 𝐑𝐞𝐟𝐞𝐫𝐫𝐞𝐫𝐬:
{leaderboard_stats}

📁 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬:
• 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: {total_files}
• 𝐓𝐨𝐭𝐚𝐥 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: {total_storage_mb} 𝐌𝐁
• 𝐀𝐯𝐠 𝐅𝐢𝐥𝐞𝐬 𝐩𝐞𝐫 𝐔𝐬𝐞𝐫: {round(total_files/max(total_users, 1), 1)}

🚀 𝐏𝐞𝐫𝐟𝐨𝐫𝐦𝐚𝐧𝐜𝐞:
• 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐒𝐜𝐫𝐢𝐩𝐭𝐬: {running_scripts}
• 𝐌𝐚𝐱 𝐂𝐨𝐧𝐜𝐮𝐫𝐫𝐞𝐧𝐭: {50}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: 98.5%

🎫 𝐑𝐞𝐯𝐞𝐧𝐮𝐞 𝐌𝐞𝐭𝐫𝐢𝐜𝐬:
• 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫𝐬: {len([uid for uid in active_users if get_user_tier(uid) == 'premium'])}
• 𝐂𝐨𝐧𝐯𝐞𝐫𝐬𝐢𝐨𝐧 𝐑𝐚𝐭𝐞: {round(len([uid for uid in active_users if get_user_tier(uid) == 'premium'])/max(total_users, 1)*100, 1)}%
""")
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(analytics_text, call.message.chat.id, call.message.message_id,
                         parse_mode='Markdown')

def add_admin_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐚𝐝𝐝 𝐚𝐝𝐦𝐢𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id != OWNER_ID:
        bot.answer_callback_query(call.id, B("⚠️ 𝐎𝐧𝐥𝐲 𝐨𝐰𝐧𝐞𝐫 𝐜𝐚𝐧 𝐚𝐝𝐝 𝐚𝐝𝐦𝐢𝐧𝐬"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("👑 𝐄𝐧𝐭𝐞𝐫 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐭𝐨 𝐚𝐝𝐝 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧:"))
    bot.register_next_step_handler(call.message, process_add_admin)

def process_add_admin(message):
    """𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐚𝐝𝐝𝐢𝐧𝐠 𝐚𝐝𝐦𝐢𝐧"""
    if message.from_user.id != OWNER_ID:
        return
    
    try:
        admin_id = int(message.text.strip())
        
        with DB_LOCK:
            conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
            c = conn.cursor()
            c.execute('INSERT OR IGNORE INTO admins (user_id, added_by, added_at) VALUES (?, ?, ?)',
                      (admin_id, message.from_user.id, datetime.now().isoformat()))
            conn.commit()
            conn.close()
        
        admin_ids.add(admin_id)
        bot.reply_to(message, B(f"✅ 𝐔𝐬𝐞𝐫 `{admin_id}` 𝐚𝐝𝐝𝐞𝐝 𝐚𝐬 𝐚𝐝𝐦𝐢𝐧."))
        
    except ValueError:
        bot.reply_to(message, B("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃."))
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))

def remove_admin_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐦𝐨𝐯𝐞 𝐚𝐝𝐦𝐢𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id != OWNER_ID:
        bot.answer_callback_query(call.id, B("⚠️ 𝐎𝐧𝐥𝐲 𝐨𝐰𝐧𝐞𝐫 𝐜𝐚𝐧 𝐫𝐞𝐦𝐨𝐯𝐞 𝐚𝐝𝐦𝐢𝐧𝐬"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("👑 𝐄𝐧𝐭𝐞𝐫 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐭𝐨 𝐫𝐞𝐦𝐨𝐯𝐞 𝐚𝐝𝐦𝐢𝐧:"))
    bot.register_next_step_handler(call.message, process_remove_admin)

def process_remove_admin(message):
    """𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐫𝐞𝐦𝐨𝐯𝐢𝐧𝐠 𝐚𝐝𝐦𝐢𝐧"""
    if message.from_user.id != OWNER_ID:
        return
    
    try:
        admin_id = int(message.text.strip())
        
        if admin_id == OWNER_ID:
            bot.reply_to(message, B("❌ 𝐂𝐚𝐧𝐧𝐨𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐨𝐰𝐧𝐞𝐫."))
            return
        
        with DB_LOCK:
            conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
            c = conn.cursor()
            c.execute('DELETE FROM admins WHERE user_id = ?', (admin_id,))
            conn.commit()
            conn.close()
        
        admin_ids.discard(admin_id)
        bot.reply_to(message, B(f"✅ 𝐔𝐬𝐞𝐫 `{admin_id}` 𝐫𝐞𝐦𝐨𝐯𝐞𝐝 𝐟𝐫𝐨𝐦 𝐚𝐝𝐦𝐢𝐧𝐬."))
        
    except ValueError:
        bot.reply_to(message, B("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃."))
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))

def list_admins_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐥𝐢𝐬𝐭 𝐚𝐝𝐦𝐢𝐧𝐬 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    admin_list = "\n".join([f"• `{admin_id}` {'👑' if admin_id == OWNER_ID else ''}" for admin_id in sorted(admin_ids)])
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(B(f"👑 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐀𝐝𝐦𝐢𝐧𝐬:\n\n{admin_list}"), 
                         call.message.chat.id, call.message.message_id,
                         parse_mode='Markdown')

def system_stats_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐬𝐲𝐬𝐭𝐞𝐦 𝐬𝐭𝐚𝐭𝐬 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    # 𝐒𝐲𝐬𝐭𝐞𝐦 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # 𝐁𝐨𝐭 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧
    total_users = len(active_users)
    total_files = sum(len(files) for files in user_files.values())
    running_scripts = len([k for k, v in bot_scripts.items() if is_bot_running(v['user_id'], v['file_name'])])
    
    stats_text = B(f"""
🖥️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐔𝐒

𝐂𝐏𝐔 𝐔𝐬𝐚𝐠𝐞: {cpu_percent}%
𝐌𝐞𝐦𝐨𝐫𝐲: {memory.percent}% ({round(memory.used/(1024**3), 1)}𝐆𝐁 / {round(memory.total/(1024**3), 1)}𝐆𝐁)
𝐃𝐢𝐬𝐤: {disk.percent}% ({round(disk.used/(1024**3), 1)}𝐆𝐁 / {round(disk.total/(1024**3), 1)}𝐆𝐁)

🤖 𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒
𝐔𝐬𝐞𝐫𝐬: {total_users}
𝐅𝐢𝐥𝐞𝐬: {total_files}
𝐑𝐮𝐧𝐧𝐢𝐧𝐠: {running_scripts}
𝐒𝐭𝐚𝐭𝐮𝐬: {'🔴 𝐋𝐨𝐜𝐤𝐞𝐝' if bot_locked else '🟢 𝐔𝐧𝐥𝐨𝐜𝐤𝐞𝐝'}

📊 𝐏𝐄𝐑𝐅𝐎𝐑𝐌𝐀𝐍𝐂𝐄
𝐔𝐩𝐭𝐢𝐦𝐞: {round(time.time() - psutil.boot_time())}𝐬
𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐬: {len(psutil.pids())}
𝐓𝐡𝐫𝐞𝐚𝐝𝐬: {threading.active_count()}
""")
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(stats_text, call.message.chat.id, call.message.message_id)

def add_subscription_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐚𝐝𝐝 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("💳 𝐄𝐧𝐭𝐞𝐫 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐚𝐧𝐝 𝐝𝐚𝐲𝐬 (𝐞.𝐠., 123456 30):"))
    bot.register_next_step_handler(call.message, process_add_subscription)

def process_add_subscription(message):
    """𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐚𝐝𝐝𝐢𝐧𝐠 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧"""
    if message.from_user.id not in admin_ids:
        return
    
    try:
        parts = message.text.strip().split()
        if len(parts) != 2:
            bot.reply_to(message, B("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐨𝐫𝐦𝐚𝐭. 𝐔𝐬𝐞: 𝐮𝐬𝐞𝐫_𝐢𝐝 𝐝𝐚𝐲𝐬"))
            return
        
        user_id = int(parts[0])
        days = int(parts[1])
        
        expiry = datetime.now() + timedelta(days=days)
        save_subscription(user_id, expiry, 'premium')
        
        bot.reply_to(message, B(f"✅ 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐚𝐝𝐝𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 `{user_id}`\n📅 𝐄𝐱𝐩𝐢𝐫𝐞𝐬: {expiry.strftime('%Y-%m-%d %H:%M:%S')}"))
        
    except ValueError:
        bot.reply_to(message, B("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐨𝐫 𝐝𝐚𝐲𝐬."))
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))

def remove_subscription_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐦𝐨𝐯𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("💳 𝐄𝐧𝐭𝐞𝐫 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐭𝐨 𝐫𝐞𝐦𝐨𝐯𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:"))
    bot.register_next_step_handler(call.message, process_remove_subscription)

def process_remove_subscription(message):
    """𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐫𝐞𝐦𝐨𝐯𝐢𝐧𝐠 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧"""
    if message.from_user.id not in admin_ids:
        return
    
    try:
        user_id = int(message.text.strip())
        remove_subscription_db(user_id)
        
        bot.reply_to(message, B(f"✅ 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐫𝐞𝐦𝐨𝐯𝐞𝐝 𝐟𝐨𝐫 𝐮𝐬𝐞𝐫 `{user_id}`"))
        
    except ValueError:
        bot.reply_to(message, B("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃."))
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))

def check_subscription_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐜𝐡𝐞𝐜𝐤 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐨𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, B("💳 𝐄𝐧𝐭𝐞𝐫 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:"))
    bot.register_next_step_handler(call.message, process_check_subscription)

def process_check_subscription(message):
    """𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐜𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧"""
    if message.from_user.id not in admin_ids:
        return
    
    try:
        user_id = int(message.text.strip())
        
        if user_id in user_subscriptions:
            sub = user_subscriptions[user_id]
            expiry = sub.get('expiry')
            tier = sub.get('tier', 'premium')
            
            if expiry and expiry > datetime.now():
                days_left = (expiry - datetime.now()).days
                bot.reply_to(message, B(f"✅ 𝐔𝐬𝐞𝐫 `{user_id}` 𝐡𝐚𝐬 𝐚𝐜𝐭𝐢𝐯𝐞 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧.\n🎫 𝐓𝐢𝐞𝐫: {tier}\n📅 𝐄𝐱𝐩𝐢𝐫𝐞𝐬: {expiry.strftime('%Y-%m-%d %H:%M:%S')}\n⏳ 𝐃𝐚𝐲𝐬 𝐥𝐞𝐟𝐭: {days_left}"))
            else:
                bot.reply_to(message, B(f"⚠️ 𝐔𝐬𝐞𝐫 `{user_id}` 𝐡𝐚𝐬 𝐞𝐱𝐩𝐢𝐫𝐞𝐝 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧.\n📅 𝐄𝐱𝐩𝐢𝐫𝐞𝐝: {expiry.strftime('%Y-%m-%d %H:%M:%S') if expiry else 'Unknown'}"))
                remove_subscription_db(user_id)
        else:
            bot.reply_to(message, B(f"📭 𝐔𝐬𝐞𝐫 `{user_id}` 𝐡𝐚𝐬 𝐧𝐨 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧."))
        
    except ValueError:
        bot.reply_to(message, B("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃."))
    except Exception as e:
        bot.reply_to(message, B(f"❌ 𝐄𝐫𝐫𝐨𝐫: {str(e)}"))

def broadcast_confirm_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐜𝐨𝐧𝐟𝐢𝐫𝐦 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    try:
        message_id = int(call.data.split('_')[-1])
        original_message = call.message.reply_to_message
        
        if not original_message:
            bot.answer_callback_query(call.id, B("❌ 𝐂𝐨𝐮𝐥𝐝 𝐧𝐨𝐭 𝐟𝐢𝐧𝐝 𝐨𝐫𝐢𝐠𝐢𝐧𝐚𝐥 𝐦𝐞𝐬𝐬𝐚𝐠𝐞"), show_alert=True)
            return
        
        bot.answer_callback_query(call.id, B("🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭..."))
        
        # 𝐒𝐞𝐧𝐝 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
        sent = 0
        failed = 0
        
        for user_id in list(active_users):
            try:
                if original_message.text:
                    bot.send_message(user_id, original_message.text)
                elif original_message.caption:
                    if original_message.photo:
                        bot.send_photo(user_id, original_message.photo[-1].file_id, caption=original_message.caption)
                    elif original_message.video:
                        bot.send_video(user_id, original_message.video.file_id, caption=original_message.caption)
                    elif original_message.document:
                        bot.send_document(user_id, original_message.document.file_id, caption=original_message.caption)
                sent += 1
            except:
                failed += 1
            
            time.sleep(0.1)  # 𝐀𝐯𝐨𝐢𝐝 𝐫𝐚𝐭𝐞 𝐥𝐢𝐦𝐢𝐭𝐢𝐧𝐠
        
        bot.edit_message_text(
            B(f"✅ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n\n📤 𝐒𝐞𝐧𝐭: {sent}\n❌ 𝐅𝐚𝐢𝐥𝐞𝐝: {failed}\n👥 𝐓𝐨𝐭𝐚𝐥: {len(active_users)}"),
            call.message.chat.id, call.message.message_id
        )
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭: {e}")
        bot.answer_callback_query(call.id, B("❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭"))

def broadcast_cancel_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐜𝐚𝐧𝐜𝐞𝐥 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    bot.answer_callback_query(call.id, B("❌ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐜𝐚𝐧𝐜𝐞𝐥𝐥𝐞𝐝"))
    bot.delete_message(call.message.chat.id, call.message.message_id)

def restart_bot_callback_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐛𝐨𝐭 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    if call.from_user.id not in admin_ids:
        bot.answer_callback_query(call.id, B("⚠️ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝"), show_alert=True)
        return
    
    # 𝐒𝐞𝐧𝐝 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
    bot.answer_callback_query(call.id, B("🚀 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬..."))
    threading.Thread(target=send_restart_notification).start()
    
    # 𝐒𝐡𝐨𝐰 𝐚𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧
    msg = bot.send_message(call.message.chat.id, ProgressAnimation.restart_animation()[0])
    
    for i, frame in enumerate(ProgressAnimation.restart_animation()):
        try:
            bot.edit_message_text(frame, call.message.chat.id, msg.message_id)
            time.sleep(0.5)
        except:
            pass
    
    # 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐭𝐨 𝐬𝐞𝐧𝐝
    time.sleep(5)
    
    bot.edit_message_text(
        B("✅ 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐬𝐞𝐧𝐭!\n\n🔄 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐧𝐨𝐰 𝐫𝐞𝐬𝐭𝐚𝐫𝐭..."),
        call.message.chat.id, msg.message_id
    )
    
    # 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭
    time.sleep(2)
    os.execv(sys.executable, ['python'] + sys.argv)

def back_to_main_callback(call):
    """𝐇𝐚𝐧𝐝𝐥𝐞 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐦𝐚𝐢𝐧 𝐜𝐚𝐥𝐥𝐛𝐚𝐜𝐤"""
    user_id = call.from_user.id
    tier = get_user_tier(user_id)
    tier_info = TIER_SYSTEM[tier]
    referral_count = referral_system.get_referral_count(user_id)
    auto_restart = referral_system.is_auto_restart_enabled(user_id) if tier == 'free' else True
    user_rank = referral_system.get_user_rank(user_id)
    
    welcome_text = B(f"""
┏━━━━━━━━━━━━━━━━━━━━━━┓
┃   🚀 𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆   ┃
┃      𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟑.𝟏     ┃
┗━━━━━━━━━━━━━━━━━━━━━━┛

👤 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐛𝐚𝐜𝐤, {call.from_user.first_name}!
🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: `{user_id}`
🎫 𝐓𝐢𝐞𝐫: {tier_info['icon']} {tier_info['name']}
📁 𝐅𝐢𝐥𝐞𝐬: {get_user_file_count(user_id)}/{get_user_file_limit(user_id)}

📊 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥𝐬: {referral_count}/3
🏆 𝐑𝐚𝐧𝐤: #{user_rank if user_rank else "𝐍𝐨𝐭 𝐫𝐚𝐧𝐤𝐞𝐝"}
🔄 𝐀𝐮𝐭𝐨-𝐑𝐞𝐬𝐭𝐚𝐫𝐭: {'✅ 𝐄𝐧𝐚𝐛𝐥𝐞𝐝' if auto_restart else '❌ 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝'}

📢 *𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥:* {UPDATE_CHANNEL}
👥 *𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩:* {UPDATE_GROUP}

𝐔𝐬𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐧𝐚𝐯𝐢𝐠𝐚𝐭𝐞.
""")
    
    bot.answer_callback_query(call.id)
    bot.edit_message_text(welcome_text, 
                         call.message.chat.id, call.message.message_id,
                         reply_markup=create_main_menu_inline(user_id),
                         parse_mode='Markdown')

# ================================
# 𝐂𝐋𝐄𝐀𝐍𝐔𝐏 𝐀𝐍𝐃 𝐒𝐇𝐔𝐓𝐃𝐎𝐖𝐍
# ================================
def cleanup():
    """𝐂𝐥𝐞𝐚𝐧𝐮𝐩 𝐟𝐮𝐧𝐜𝐭𝐢𝐨𝐧 𝐟𝐨𝐫 𝐬𝐡𝐮𝐭𝐝𝐨𝐰𝐧"""
    logger.warning("🔴 𝐒𝐡𝐮𝐭𝐭𝐢𝐧𝐠 𝐝𝐨𝐰𝐧... 𝐂𝐥𝐞𝐚𝐧𝐢𝐧𝐠 𝐮𝐩 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐬")
    
    # 𝐊𝐢𝐥𝐥 𝐚𝐥𝐥 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 𝐬𝐜𝐫𝐢𝐩𝐭𝐬
    for script_key, script_info in list(bot_scripts.items()):
        try:
            kill_process_tree(script_info)
        except:
            pass
    
    # 𝐒𝐚𝐯𝐞 𝐫𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐝𝐚𝐭𝐚
    referral_system.save_referrals()
    
    logger.info("✅ 𝐂𝐥𝐞𝐚𝐧𝐮𝐩 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞")

# 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫 𝐜𝐥𝐞𝐚𝐧𝐮𝐩 𝐟𝐮𝐜𝐭𝐢𝐨𝐧
atexit.register(cleanup)

# ================================
# 𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐔𝐏 𝐀𝐍𝐃 𝐀𝐔𝐓𝐎-𝐑𝐄𝐂𝐎𝐕𝐄𝐑𝐘
# ================================
def startup_recovery():
    """𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐫𝐞𝐜𝐨𝐯𝐞𝐫 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐨𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩"""
    logger.info("🚀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐚𝐮𝐭𝐨-𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐩𝐫𝐨𝐜𝐞𝐬𝐬...")
    
    msg = None
    try:
        # 𝐒𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐨𝐰𝐧𝐞𝐫
        msg = bot.send_message(OWNER_ID, ProgressAnimation.recovery_animation()[0])
        
        for i, frame in enumerate(ProgressAnimation.recovery_animation()):
            try:
                bot.edit_message_text(frame, OWNER_ID, msg.message_id)
                time.sleep(0.3)
            except:
                pass
        
        # 𝐑𝐞𝐜𝐨𝐯𝐞𝐫 𝐚𝐥𝐥 𝐬𝐜𝐫𝐢𝐩𝐭𝐬
        recovered = recovery_system.recover_all_scripts()
        
        if recovered:
            bot.edit_message_text(
                B(f"✅ 𝐒𝐭𝐚𝐫𝐭𝐮𝐩 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n🔄 𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐞𝐝: {len(recovered)} 𝐬𝐜𝐫𝐢𝐩𝐭𝐬"),
                OWNER_ID, msg.message_id
            )
        else:
            bot.edit_message_text(
                B("📭 𝐍𝐨 𝐬𝐜𝐫𝐢𝐩𝐭𝐬 𝐭𝐨 𝐫𝐞𝐜𝐨𝐯𝐞𝐫 𝐨𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩."),
                OWNER_ID, msg.message_id
            )
        
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲: {e}")
        if msg:
            try:
                bot.edit_message_text(
                    B(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐢𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲: {str(e)[:100]}"),
                    OWNER_ID, msg.message_id
                )
            except:
                pass

# ================================
# 𝐌𝐀𝐈𝐍 𝐄𝐗𝐄𝐂𝐔𝐓𝐈𝐎𝐍
# ================================
if __name__ == '__main__':
    logger.info("="*50)
    logger.info("🚀 𝐌𝐊-𝐃𝐄𝐕 𝐇𝐎𝐒𝐓𝐈𝐍𝐆 𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝟑.𝟏")
    logger.info("📊 𝐀𝐮𝐭𝐨-𝐑𝐞𝐜𝐨𝐯𝐞𝐫𝐲 𝐒𝐲𝐬𝐭𝐞𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝")
    logger.info("🤝 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐒𝐲𝐬𝐭𝐞𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝")
    logger.info("🏆 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐞𝐚𝐝𝐞𝐫𝐛𝐨𝐚𝐫𝐝 𝐀𝐝𝐝𝐞𝐝")
    logger.info("🎫 𝐓𝐢𝐞𝐫-𝐁𝐚𝐬𝐞𝐝 𝐇𝐨𝐬𝐭𝐢𝐧𝐠")
    logger.info(f"👑 𝐎𝐰𝐧𝐞𝐫 𝐈𝐃: {OWNER_ID}")
    logger.info(f"🛡️ 𝐀𝐝𝐦𝐢𝐧𝐬: {len(admin_ids)}")
    logger.info(f"👥 𝐀𝐜𝐭𝐢𝐯𝐞 𝐔𝐬𝐞𝐫𝐬: {len(active_users)}")
    logger.info(f"📁 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: {sum(len(files) for files in user_files.values())}")
    
    # 𝐆𝐞𝐭 𝐛𝐨𝐭 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞
    try:
        bot_username = bot.get_me().username
        logger.info(f"🤖 𝐁𝐨𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{bot_username}")
        logger.info(f"🔗 𝐑𝐞𝐟𝐞𝐫𝐫𝐚𝐥 𝐋𝐢𝐧𝐤 𝐅𝐨𝐫𝐦𝐚𝐭: https://t.me/{bot_username}?start=EXU{{user_id}}{{random}}")
    except Exception as e:
        logger.error(f"❌ 𝐄𝐫𝐫𝐨𝐫 𝐠𝐞𝐭𝐭𝐢𝐧𝐠 𝐛𝐨𝐭 𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {e}")
    
    logger.info("="*50)
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐅𝐥𝐚𝐬𝐤 𝐤𝐞𝐞𝐩-𝐚𝐥𝐢𝐯𝐞
    keep_alive()
    
    # 𝐑𝐮𝐧 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐲
    threading.Thread(target=startup_recovery).start()
    
    # 𝐒𝐭𝐚𝐫𝐭 𝐛𝐨𝐭 𝐩𝐨𝐥𝐥𝐢𝐧𝐠
    logger.info("🤖 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐨𝐭 𝐩𝐨𝐥𝐥𝐢𝐧𝐠...")
    
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except requests.exceptions.ReadTimeout:
            logger.warning("⚠️ 𝐑𝐞𝐚𝐝 𝐓𝐢𝐦𝐞𝐨𝐮𝐭. 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐢𝐧 𝟓𝐬...")
            time.sleep(5)
        except requests.exceptions.ConnectionError as ce:
            logger.error(f"⚠️ 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 𝐄𝐫𝐫𝐨𝐫: {ce}. 𝐑𝐞𝐭𝐫𝐲𝐢𝐧𝐠 𝐢𝐧 𝟏𝟓𝐬...")
            time.sleep(15)
        except Exception as e:
            logger.critical(f"💥 𝐔𝐧𝐫𝐞𝐜𝐨𝐯𝐞𝐫𝐚𝐛𝐥𝐞 𝐞𝐫𝐫𝐨𝐫: {e}", exc_info=True)
            logger.info("🔄 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐢𝐧 𝟑𝟎𝐬 𝐝𝐮𝐞 𝐭𝐨 𝐜𝐫𝐢𝐭𝐢𝐜𝐚𝐥 𝐞𝐫𝐫𝐨𝐫...")
            time.sleep(30)
        finally:
            logger.warning("🔴 𝐏𝐨𝐥𝐥𝐢𝐧𝐠 𝐬𝐭𝐨𝐩𝐩𝐞𝐝. 𝐖𝐢𝐥𝐥 𝐫𝐞𝐬𝐭𝐚𝐫𝐭 𝐢𝐟 𝐢𝐧 𝐥𝐨𝐨𝐩...")
            time.sleep(1)