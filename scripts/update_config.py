#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新 TrendRadar 配置文件中的企业微信 Webhook URL
从环境变量 WEWORK_WEBHOOK 读取 URL 并更新 config/config.yaml
"""

import os
import re
import sys

def update_wework_webhook():
    """更新企业微信 webhook URL"""
    webhook_url = os.getenv('WEWORK_WEBHOOK')
    
    if not webhook_url:
        print("❌ 错误: 未找到环境变量 WEWORK_WEBHOOK")
        sys.exit(1)
    
    config_path = 'config/config.yaml'
    
    # 读取配置文件
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ 错误: 找不到配置文件 {config_path}")
        sys.exit(1)
    
    # 更新 wework webhook_url
    # 使用更精确的替换模式
    pattern = r'(wework:\s*\n\s+webhook_url:\s*["\'])(.*?)(["\'])'
    replacement = f'\\1{webhook_url}\\3'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    # 确保 notification.enabled 为 true
    new_content = re.sub(
        r'(notification:\s*\n\s+)enabled:\s*false',
        r'\1enabled: true',
        new_content
    )
    
    # 写回配置文件
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ 配置更新成功")
    print(f"   - wework webhook URL 已设置")
    print(f"   - notification.enabled 已确保为 true")

if __name__ == '__main__':
    update_wework_webhook()
