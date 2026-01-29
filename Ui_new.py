# ============================================
# Hospital Management System - Modern Desktop GUI
# Beautiful & Interactive UI with CustomTkinter
# ============================================

import customtkinter as ctk
from datetime import datetime
import threading
import tkinter as tk

from HMS import HospitalChatbot

# Set appearance and theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class ModernHospitalChatGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Hospital Management System")
        self.geometry("1000x800")
        self.minsize(800, 600)
        
        # Colors
        self.colors = {
            'primary': '#0077b6',
            'primary_hover': '#005f8a',
            'primary_light': '#48cae4',
            'secondary': '#00d9a5',
            'success': '#10b981',
            'warning': '#f59e0b',
            'error': '#ef4444',
            'bg_main': '#f0f4f8',
            'bg_card': '#ffffff',
            'bg_chat': '#f8fafc',
            'text_primary': '#1e293b',
            'text_secondary': '#64748b',
            'border': '#e2e8f0',
            'user_bubble': '#0077b6',
            'bot_bubble': '#ffffff'
        }
        
        # Configure window background
        self.configure(fg_color=self.colors['bg_main'])
        
        # Initialize chatbot
        self.chatbot = HospitalChatbot()
        self.user_name = ""
        self.chat_history = []
        
        # Build UI
        self.create_ui()
        
        # Focus on message entry
        self.after(100, lambda: self.message_entry.focus())
        
    def create_ui(self):
        # Main container with padding
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Header section
        self.create_header()
        
        # Chat container (card-like appearance)
        self.chat_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.colors['bg_card'],
            corner_radius=20,
            border_width=1,
            border_color=self.colors['border']
        )
        self.chat_card.pack(fill="both", expand=True, pady=(20, 0))
        
        # Chat header
        self.create_chat_header()
        
        # Chat messages area
        self.create_chat_area()
        
        # Quick actions
        self.create_quick_actions()
        
        # Input area
        self.create_input_area()
        
        # Show welcome message
        self.show_welcome()
        
    def create_header(self):
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x")
        
        # Title with gradient-like effect using label
        title_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_frame.pack()
        
        # Hospital icon
        icon_label = ctk.CTkLabel(
            title_frame,
            text="🏥",
            font=ctk.CTkFont(size=36)
        )
        icon_label.pack(side="left", padx=(0, 10))
        
        # Title text
        title_text = ctk.CTkLabel(
            title_frame,
            text="Hospital Management System",
            font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"),
            text_color=self.colors['primary']
        )
        title_text.pack(side="left")
        
        # Subtitle
        subtitle = ctk.CTkLabel(
            header_frame,
            text="Powered by Natural Language Processing • Your 24/7 Health Assistant",
            font=ctk.CTkFont(size=13),
            text_color=self.colors['text_secondary']
        )
        subtitle.pack(pady=(5, 0))
        
    def create_chat_header(self):
        # Gradient-like header using frame
        header = ctk.CTkFrame(
            self.chat_card,
            fg_color=self.colors['primary'],
            corner_radius=0,
            height=80
        )
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Round top corners manually
        header._corner_radius = 20
        
        inner = ctk.CTkFrame(header, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=25, pady=15)
        
        # Left side - Avatar and info
        left_frame = ctk.CTkFrame(inner, fg_color="transparent")
        left_frame.pack(side="left", fill="y")
        
        # Avatar circle
        avatar_frame = ctk.CTkFrame(
            left_frame,
            fg_color=self.colors['bg_card'],
            corner_radius=25,
            width=50,
            height=50
        )
        avatar_frame.pack(side="left", padx=(0, 15))
        avatar_frame.pack_propagate(False)
        
        avatar_icon = ctk.CTkLabel(
            avatar_frame,
            text="🏥",
            font=ctk.CTkFont(size=24)
        )
        avatar_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Info text
        info_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="y", pady=5)
        
        title = ctk.CTkLabel(
            info_frame,
            text="Hospital Assistant",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="white"
        )
        title.pack(anchor="w")
        
        # Status with green dot
        status_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        status_frame.pack(anchor="w", pady=(3, 0))
        
        status_dot = ctk.CTkLabel(
            status_frame,
            text="●",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['success']
        )
        status_dot.pack(side="left")
        
        status_text = ctk.CTkLabel(
            status_frame,
            text=" Online • Ready to help",
            font=ctk.CTkFont(size=12),
            text_color="#e0e0e0"
        )
        status_text.pack(side="left")
        
        # Right side - Time
        time_label = ctk.CTkLabel(
            inner,
            text=datetime.now().strftime("%I:%M %p"),
            font=ctk.CTkFont(size=12),
            text_color="#cccccc"
        )
        time_label.pack(side="right", pady=10)
        
        # Update time every minute
        self.update_time(time_label)
        
    def update_time(self, label):
        label.configure(text=datetime.now().strftime("%I:%M %p"))
        self.after(60000, lambda: self.update_time(label))
        
    def create_chat_area(self):
        # Chat container
        chat_container = ctk.CTkFrame(self.chat_card, fg_color=self.colors['bg_chat'])
        chat_container.pack(fill="both", expand=True, padx=2, pady=0)
        
        # Scrollable frame for messages
        self.chat_scroll = ctk.CTkScrollableFrame(
            chat_container,
            fg_color="transparent",
            scrollbar_button_color=self.colors['border'],
            scrollbar_button_hover_color=self.colors['primary']
        )
        self.chat_scroll.pack(fill="both", expand=True, padx=10, pady=15)
        
    def create_quick_actions(self):
        # Quick actions container
        quick_frame = ctk.CTkFrame(self.chat_card, fg_color=self.colors['bg_chat'], height=60)
        quick_frame.pack(fill="x", padx=2)
        
        inner = ctk.CTkFrame(quick_frame, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=12)
        
        # Label
        label = ctk.CTkLabel(
            inner,
            text="Quick Actions:",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=self.colors['text_secondary']
        )
        label.pack(side="left", padx=(0, 15))
        
        # Quick action buttons
        actions = [
            ("📅 Appointments", "How do I book an appointment?"),
            ("💊 Pharmacy", "What are the pharmacy hours?"),
            ("💳 Billing", "How do I pay my bill?"),
            ("🚨 Emergency", "Where is the emergency room?"),
            ("👥 Visitors", "What are the visiting hours?"),
            ("🧪 Lab Tests", "How do I get lab test results?")
        ]
        
        for text, query in actions:
            btn = ctk.CTkButton(
                inner,
                text=text,
                font=ctk.CTkFont(size=11),
                fg_color="transparent",
                text_color=self.colors['text_secondary'],
                hover_color=self.colors['primary_light'],
                border_width=1,
                border_color=self.colors['border'],
                corner_radius=20,
                height=32,
                command=lambda q=query: self.send_quick_action(q)
            )
            btn.pack(side="left", padx=4)
            
    def create_input_area(self):
        # Input container
        input_container = ctk.CTkFrame(
            self.chat_card,
            fg_color=self.colors['bg_card'],
            corner_radius=0
        )
        input_container.pack(fill="x", padx=2, pady=2)
        
        # Separator line
        separator = ctk.CTkFrame(input_container, fg_color=self.colors['border'], height=1)
        separator.pack(fill="x")
        
        inner = ctk.CTkFrame(input_container, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=15)
        
        # Name entry (smaller, on top)
        name_frame = ctk.CTkFrame(inner, fg_color="transparent")
        name_frame.pack(fill="x", pady=(0, 10))
        
        name_label = ctk.CTkLabel(
            name_frame,
            text="Your name (optional):",
            font=ctk.CTkFont(size=11),
            text_color=self.colors['text_secondary']
        )
        name_label.pack(side="left")
        
        self.name_entry = ctk.CTkEntry(
            name_frame,
            placeholder_text="Enter your name",
            font=ctk.CTkFont(size=12),
            fg_color=self.colors['bg_chat'],
            border_color=self.colors['border'],
            corner_radius=10,
            height=35,
            width=200
        )
        self.name_entry.pack(side="left", padx=(10, 0))
        
        # Message entry frame
        msg_frame = ctk.CTkFrame(inner, fg_color="transparent")
        msg_frame.pack(fill="x")
        
        # Message entry
        self.message_entry = ctk.CTkEntry(
            msg_frame,
            placeholder_text="Type your message here... (Press Enter to send)",
            font=ctk.CTkFont(size=14),
            fg_color=self.colors['bg_chat'],
            border_color=self.colors['border'],
            corner_radius=25,
            height=50
        )
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.message_entry.bind("<Return>", self.send_message)
        
        # Send button
        self.send_btn = ctk.CTkButton(
            msg_frame,
            text="Send ➤",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.colors['primary'],
            hover_color=self.colors['primary_hover'],
            corner_radius=25,
            height=50,
            width=100,
            command=self.send_message
        )
        self.send_btn.pack(side="left", padx=(0, 5))
        
        # Clear button
        self.clear_btn = ctk.CTkButton(
            msg_frame,
            text="🗑️",
            font=ctk.CTkFont(size=16),
            fg_color=self.colors['warning'],
            hover_color="#fbbf24",
            corner_radius=25,
            height=50,
            width=50,
            command=self.clear_chat
        )
        self.clear_btn.pack(side="left")
        
    def show_welcome(self):
        # Welcome message container
        welcome_frame = ctk.CTkFrame(
            self.chat_scroll,
            fg_color="transparent"
        )
        welcome_frame.pack(fill="x", pady=20)
        
        # Welcome card
        card = ctk.CTkFrame(
            welcome_frame,
            fg_color=self.colors['bg_card'],
            corner_radius=15,
            border_width=1,
            border_color=self.colors['border']
        )
        card.pack(padx=40, pady=10)
        
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=30, pady=25)
        
        # Welcome icon
        icon = ctk.CTkLabel(
            inner,
            text="👋",
            font=ctk.CTkFont(size=48)
        )
        icon.pack()
        
        # Welcome title
        title = ctk.CTkLabel(
            inner,
            text="Welcome to Hospital Assistant!",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=self.colors['primary']
        )
        title.pack(pady=(10, 5))
        
        # Welcome subtitle
        subtitle = ctk.CTkLabel(
            inner,
            text="I'm here to help you with all your hospital-related questions",
            font=ctk.CTkFont(size=13),
            text_color=self.colors['text_secondary']
        )
        subtitle.pack()
        
        # Features
        features_frame = ctk.CTkFrame(inner, fg_color="transparent")
        features_frame.pack(pady=(20, 0))
        
        features = [
            ("📅", "Appointments"),
            ("💊", "Pharmacy"),
            ("💳", "Billing"),
            ("🚨", "Emergency"),
            ("👥", "Visitors"),
            ("🧪", "Lab Tests")
        ]
        
        for icon_text, label_text in features:
            feature_item = ctk.CTkFrame(features_frame, fg_color="transparent")
            feature_item.pack(side="left", padx=10)
            
            icon_lbl = ctk.CTkLabel(
                feature_item,
                text=icon_text,
                font=ctk.CTkFont(size=24)
            )
            icon_lbl.pack()
            
            text_lbl = ctk.CTkLabel(
                feature_item,
                text=label_text,
                font=ctk.CTkFont(size=10),
                text_color=self.colors['text_secondary']
            )
            text_lbl.pack()
            
        # Instruction
        instruction = ctk.CTkLabel(
            inner,
            text="Type a message below or click a quick action to get started!",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['text_secondary']
        )
        instruction.pack(pady=(20, 0))
        
    def add_message(self, message, is_user=True):
        # Message container
        msg_container = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        msg_container.pack(fill="x", pady=5, padx=10)
        
        # Alignment
        if is_user:
            msg_container.pack_configure(anchor="e")
        else:
            msg_container.pack_configure(anchor="w")
            
        # Inner frame for bubble
        bubble_frame = ctk.CTkFrame(
            msg_container,
            fg_color=self.colors['user_bubble'] if is_user else self.colors['bot_bubble'],
            corner_radius=18,
            border_width=0 if is_user else 1,
            border_color=self.colors['border']
        )
        bubble_frame.pack(side="right" if is_user else "left", padx=5)
        
        inner = ctk.CTkFrame(bubble_frame, fg_color="transparent")
        inner.pack(padx=15, pady=10)
        
        # Sender label
        sender_text = self.user_name if self.user_name and is_user else ("You" if is_user else "🏥 Hospital Assistant")
        sender = ctk.CTkLabel(
            inner,
            text=sender_text,
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#e0e0e0" if is_user else self.colors['primary']
        )
        sender.pack(anchor="w")
        
        # Message text
        msg_label = ctk.CTkLabel(
            inner,
            text=message,
            font=ctk.CTkFont(size=13),
            text_color="white" if is_user else self.colors['text_primary'],
            wraplength=400,
            justify="left"
        )
        msg_label.pack(anchor="w", pady=(5, 3))
        
        # Timestamp
        timestamp = ctk.CTkLabel(
            inner,
            text=datetime.now().strftime("%I:%M %p"),
            font=ctk.CTkFont(size=9),
            text_color="#b0b0b0" if is_user else self.colors['text_secondary']
        )
        timestamp.pack(anchor="e")
        
        # Scroll to bottom
        self.chat_scroll._parent_canvas.yview_moveto(1.0)
        
    def show_typing_indicator(self):
        # Typing indicator
        self.typing_frame = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        self.typing_frame.pack(fill="x", pady=5, padx=10, anchor="w")
        
        bubble = ctk.CTkFrame(
            self.typing_frame,
            fg_color=self.colors['bot_bubble'],
            corner_radius=18,
            border_width=1,
            border_color=self.colors['border']
        )
        bubble.pack(side="left", padx=5)
        
        inner = ctk.CTkFrame(bubble, fg_color="transparent")
        inner.pack(padx=15, pady=12)
        
        typing_label = ctk.CTkLabel(
            inner,
            text="🏥 Hospital Assistant is typing...",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['text_secondary']
        )
        typing_label.pack()
        
        self.chat_scroll._parent_canvas.yview_moveto(1.0)
        
    def remove_typing_indicator(self):
        if hasattr(self, 'typing_frame'):
            self.typing_frame.destroy()
        
    def send_message(self, event=None):
        # Get user name
        if self.name_entry.get().strip():
            self.user_name = self.name_entry.get().strip()
            
        # Get message
        message = self.message_entry.get().strip()
        
        if not message:
            return
            
        # Clear input
        self.message_entry.delete(0, "end")
        
        # Clear welcome message on first message
        if not self.chat_history:
            for widget in self.chat_scroll.winfo_children():
                widget.destroy()
                
        # Add user message
        self.add_message(message, is_user=True)
        self.chat_history.append({"text": message, "is_user": True})
        
        # Show typing indicator
        self.show_typing_indicator()
        
        # Get response in thread
        def get_response():
            response = self.chatbot.process_query(message, self.user_name if self.user_name else None)
            
            # Update UI in main thread
            self.after(500, lambda: self.receive_response(response))
            
        threading.Thread(target=get_response, daemon=True).start()
        
    def receive_response(self, response):
        self.remove_typing_indicator()
        self.add_message(response, is_user=False)
        self.chat_history.append({"text": response, "is_user": False})
        
    def send_quick_action(self, query):
        self.message_entry.delete(0, "end")
        self.message_entry.insert(0, query)
        self.send_message()
        
    def clear_chat(self):
        # Clear all messages
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()
        self.chat_history = []
        self.show_welcome()


def main():
    app = ModernHospitalChatGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
