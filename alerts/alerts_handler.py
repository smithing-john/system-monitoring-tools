#!/usr/bin/env python3
"""
Alert handler for system monitoring
Supports email and Slack notifications
"""

import smtplib
import json
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class AlertHandler:
    """Handle system alerts via multiple channels"""
    
    def __init__(self, config):
        self.config = config
        self.email_enabled = config.get('alerts', {}).get('enabled', False)
        self.email_recipient = config.get('alerts', {}).get('email', '')
        self.slack_webhook = config.get('alerts', {}).get('slack_webhook', '')
    
    def send_email_alert(self, alert_type, severity, metrics):
        """Send email alert"""
        if not self.email_enabled or not self.email_recipient:
            return False
        
        try:
            # Load email template
            with open('alerts/email_template.html', 'r') as f:
                template = f.read()
            
            # Replace placeholders
            html_content = template.replace('{{ALERT_TYPE}}', alert_type)
            html_content = html_content.replace('{{SEVERITY}}', severity)
            html_content = html_content.replace('{{TIMESTAMP}}', 
                                               datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            html_content = html_content.replace('{{CPU_PERCENT}}', str(metrics.get('cpu', 0)))
            html_content = html_content.replace('{{MEMORY_PERCENT}}', str(metrics.get('memory', 0)))
            html_content = html_content.replace('{{DISK_PERCENT}}', str(metrics.get('disk', 0)))
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'System Alert: {alert_type}'
            msg['From'] = 'monitoring@system.local'
            msg['To'] = self.email_recipient
            
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            
            # Send email (would need actual SMTP config)
            print(f"Email alert would be sent to {self.email_recipient}")
            return True
            
        except Exception as e:
            print(f"Failed to send email alert: {e}")
            return False
    
    def send_slack_alert(self, alert_type, severity, metrics, hostname):
        """Send Slack alert"""
        if not self.slack_webhook:
            return False
        
        try:
            # Load Slack template
            with open('alerts/slack_template.json', 'r') as f:
                template = json.load(f)
            
            # Replace placeholders in template
            template_str = json.dumps(template)
            template_str = template_str.replace('{{ALERT_TYPE}}', alert_type)
            template_str = template_str.replace('{{SEVERITY}}', severity)
            template_str = template_str.replace('{{HOSTNAME}}', hostname)
            template_str = template_str.replace('{{TIMESTAMP}}', 
                                               datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            template_str = template_str.replace('{{CPU_PERCENT}}', str(metrics.get('cpu', 0)))
            template_str = template_str.replace('{{MEMORY_PERCENT}}', str(metrics.get('memory', 0)))
            template_str = template_str.replace('{{DISK_PERCENT}}', str(metrics.get('disk', 0)))
            
            payload = json.loads(template_str)
            
            # Send to Slack (would need actual webhook)
            print(f"Slack alert would be sent to webhook")
            # response = requests.post(self.slack_webhook, json=payload)
            return True
            
        except Exception as e:
            print(f"Failed to send Slack alert: {e}")
            return False
    
    def trigger_alert(self, alert_type, severity, metrics, hostname='localhost'):
        """Trigger alerts across all configured channels"""
        results = {
            'email': False,
            'slack': False
        }
        
        if self.email_enabled:
            results['email'] = self.send_email_alert(alert_type, severity, metrics)
        
        if self.slack_webhook:
            results['slack'] = self.send_slack_alert(alert_type, severity, metrics, hostname)
        
        return results