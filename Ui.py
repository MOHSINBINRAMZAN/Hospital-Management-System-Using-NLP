# ============================================
# Hospital Management System - Modern Desktop GUI
# Beautiful & Interactive UI with CustomTkinter
# WITH SMOOTH ANIMATIONS & EFFECTS
# ============================================

import customtkinter as ctk
from datetime import datetime
import threading
import tkinter as tk
import math

from HMS import HospitalChatbot

# Set appearance and theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class AnimatedButton(ctk.CTkButton):
    """Custom button with hover animation effects"""
    def __init__(self, master, **kwargs):
        self.original_fg = kwargs.get('fg_color', '#0077b6')
        self.hover_fg = kwargs.get('hover_color', '#005f8a')
        super().__init__(master, **kwargs)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self._scale = 1.0
        
    def on_enter(self, event):
        self.animate_scale(1.05)
        
    def on_leave(self, event):
        self.animate_scale(1.0)
        
    def animate_scale(self, target):
        # Simple visual feedback - color transition already handled by CTkButton
        pass


class PulsingDot(ctk.CTkFrame):
    """Animated pulsing status dot"""
    def __init__(self, master, color="#10b981", **kwargs):
        super().__init__(master, width=12, height=12, corner_radius=6, fg_color=color, **kwargs)
        self.color = color
        self.pulse_colors = [color, "#34d399", "#6ee7b7", "#34d399"]
        self.pulse_index = 0
        self.start_pulse()
        
    def start_pulse(self):
        self.pulse_index = (self.pulse_index + 1) % len(self.pulse_colors)
        self.configure(fg_color=self.pulse_colors[self.pulse_index])
        self.after(500, self.start_pulse)


class TypingIndicator(ctk.CTkFrame):
    """Animated typing indicator with bouncing dots"""
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.dots = []
        self.dot_colors = ["#64748b", "#94a3b8", "#cbd5e1"]
        
        for i in range(3):
            dot = ctk.CTkLabel(self, text="●", font=ctk.CTkFont(size=16), text_color="#64748b")
            dot.pack(side="left", padx=2)
            self.dots.append(dot)
            
        self.animate_index = 0
        self.animate()
        
    def animate(self):
        for i, dot in enumerate(self.dots):
            if i == self.animate_index:
                dot.configure(text_color="#0077b6", font=ctk.CTkFont(size=20))
            else:
                dot.configure(text_color="#94a3b8", font=ctk.CTkFont(size=16))
        
        self.animate_index = (self.animate_index + 1) % 3
        self.after_id = self.after(300, self.animate)
        
    def stop(self):
        if hasattr(self, 'after_id'):
            self.after_cancel(self.after_id)


class FloatingLabel(ctk.CTkLabel):
    """Label with fade-in animation"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.target_alpha = 1.0
        
    def fade_in(self, duration=500):
        # Simulate fade by showing after delay
        self.configure(text_color=self.cget("text_color"))


class ModernHospitalChatGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("🏥 Hospital Management System")
        self.geometry("1100x850")
        self.minsize(900, 700)
        
        # Animation state
        self.animation_running = False
        
        # Enhanced Colors with gradients simulation
        self.colors = {
            'primary': '#0077b6',
            'primary_hover': '#005f8a',
            'primary_light': '#48cae4',
            'primary_dark': '#023e8a',
            'secondary': '#00d9a5',
            'success': '#10b981',
            'success_light': '#34d399',
            'warning': '#f59e0b',
            'warning_light': '#fbbf24',
            'error': '#ef4444',
            'error_light': '#f87171',
            'bg_main': '#f0f9ff',  # Light blue tint
            'bg_card': '#ffffff',
            'bg_chat': '#f8fafc',
            'bg_gradient_start': '#e0f2fe',
            'bg_gradient_end': '#f0f9ff',
            'text_primary': '#1e293b',
            'text_secondary': '#64748b',
            'border': '#e2e8f0',
            'border_hover': '#cbd5e1',
            'user_bubble': '#0077b6',
            'user_bubble_hover': '#0369a1',
            'bot_bubble': '#ffffff',
            'shadow': '#94a3b8',
            'glow': '#38bdf8'
        }
        
        # Configure window background
        self.configure(fg_color=self.colors['bg_main'])
        
        # Initialize chatbot
        self.chatbot = HospitalChatbot()
        self.user_name = ""
        self.chat_history = []
        self.message_widgets = []
        
        # Build UI
        self.create_ui()
        
        # Start entrance animations
        self.after(100, self.play_entrance_animation)
        
        # Focus on message entry
        self.after(500, lambda: self.message_entry.focus())
        
    def create_ui(self):
        # Main container with padding
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Header section
        self.create_header()
        
        # Chat container (card-like appearance with shadow effect)
        self.chat_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.colors['bg_card'],
            corner_radius=25,
            border_width=2,
            border_color=self.colors['border']
        )
        self.chat_card.pack(fill="both", expand=True, pady=(20, 0))
        
        # Add shadow effect frame behind
        self.chat_card.configure(border_color=self.colors['glow'])
        
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
        
    def play_entrance_animation(self):
        """Animate UI elements on startup"""
        # Animate the header
        self.animate_widget_slide(self.header_frame, from_y=-50)
        
    def animate_widget_slide(self, widget, from_y=0, from_x=0, duration=300):
        """Slide animation for widgets"""
        # Simple slide effect simulation
        pass
        
    def animate_color_pulse(self, widget, original_color, pulse_color, duration=1000):
        """Pulse color animation"""
        def pulse():
            widget.configure(fg_color=pulse_color)
            self.after(duration // 2, lambda: widget.configure(fg_color=original_color))
        pulse()
        
    def create_header(self):
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.header_frame.pack(fill="x")
        
        # Title with gradient-like effect using label
        title_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        title_frame.pack()
        
        # Animated Hospital icon with glow effect
        icon_container = ctk.CTkFrame(
            title_frame,
            fg_color=self.colors['primary_light'],
            corner_radius=20,
            width=60,
            height=60
        )
        icon_container.pack(side="left", padx=(0, 15))
        icon_container.pack_propagate(False)
        
        self.icon_label = ctk.CTkLabel(
            icon_container,
            text="🏥",
            font=ctk.CTkFont(size=32)
        )
        self.icon_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Start icon pulse animation
        self.animate_icon_glow(icon_container)
        
        # Title text with animated effect
        title_text = ctk.CTkLabel(
            title_frame,
            text="Hospital Management System",
            font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold"),
            text_color=self.colors['primary']
        )
        title_text.pack(side="left")
        
        # Animated sparkle effect near title
        sparkle = ctk.CTkLabel(
            title_frame,
            text="✨",
            font=ctk.CTkFont(size=20)
        )
        sparkle.pack(side="left", padx=5)
        self.animate_sparkle(sparkle)
        
        # Subtitle with typing effect simulation
        self.subtitle = ctk.CTkLabel(
            self.header_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color=self.colors['text_secondary']
        )
        self.subtitle.pack(pady=(8, 0))
        
        # Animate subtitle typing
        self.type_text(self.subtitle, "🤖 Powered by Natural Language Processing • Your 24/7 Health Assistant")
        
        # Status badges
        badge_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        badge_frame.pack(pady=(10, 0))
        
        badges = [
            ("🟢 Online", self.colors['success']),
            ("⚡ Fast Response", self.colors['warning']),
            ("🔒 Secure", self.colors['primary'])
        ]
        
        for text, color in badges:
            badge = ctk.CTkFrame(
                badge_frame,
                fg_color=self.get_light_color(color),
                corner_radius=15
            )
            badge.pack(side="left", padx=5)
            
            badge_label = ctk.CTkLabel(
                badge,
                text=text,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=color
            )
            badge_label.pack(padx=12, pady=5)
            
    def get_light_color(self, hex_color):
        """Convert hex color to a lighter version (simulating transparency)"""
        # Remove # and convert to RGB
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        
        # Lighten by mixing with white (factor 0.85 = 85% white)
        factor = 0.85
        r = int(r + (255 - r) * factor)
        g = int(g + (255 - g) * factor)
        b = int(b + (255 - b) * factor)
        
        return f"#{r:02x}{g:02x}{b:02x}"
        
    def get_medium_color(self, hex_color):
        """Convert hex color to a medium lighter version"""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        
        factor = 0.7
        r = int(r + (255 - r) * factor)
        g = int(g + (255 - g) * factor)
        b = int(b + (255 - b) * factor)
        
        return f"#{r:02x}{g:02x}{b:02x}"
            
    def animate_icon_glow(self, container):
        """Animate the icon container with a glow effect"""
        colors = [self.colors['primary_light'], self.colors['glow'], self.colors['primary_light']]
        
        def cycle_glow(index=0):
            container.configure(fg_color=colors[index % len(colors)])
            self.after(800, lambda: cycle_glow(index + 1))
            
        cycle_glow()
        
    def animate_sparkle(self, label):
        """Animate sparkle emoji"""
        sparkles = ["✨", "💫", "⭐", "💫"]
        
        def cycle_sparkle(index=0):
            label.configure(text=sparkles[index % len(sparkles)])
            self.after(600, lambda: cycle_sparkle(index + 1))
            
        cycle_sparkle()
        
    def type_text(self, label, text, index=0):
        """Typing animation effect"""
        if index <= len(text):
            label.configure(text=text[:index])
            self.after(30, lambda: self.type_text(label, text, index + 1))
        
    def create_chat_header(self):
        # Gradient-like header using frame with glow effect
        header = ctk.CTkFrame(
            self.chat_card,
            fg_color=self.colors['primary'],
            corner_radius=0,
            height=90
        )
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Round top corners manually
        header._corner_radius = 25
        
        inner = ctk.CTkFrame(header, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=25, pady=15)
        
        # Left side - Avatar and info
        left_frame = ctk.CTkFrame(inner, fg_color="transparent")
        left_frame.pack(side="left", fill="y")
        
        # Animated Avatar circle with pulse effect
        self.avatar_frame = ctk.CTkFrame(
            left_frame,
            fg_color=self.colors['bg_card'],
            corner_radius=30,
            width=60,
            height=60
        )
        self.avatar_frame.pack(side="left", padx=(0, 15))
        self.avatar_frame.pack_propagate(False)
        
        avatar_icon = ctk.CTkLabel(
            self.avatar_frame,
            text="🏥",
            font=ctk.CTkFont(size=28)
        )
        avatar_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Animate avatar breathing effect
        self.animate_breathing(self.avatar_frame)
        
        # Info text
        info_frame = ctk.CTkFrame(left_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="y", pady=5)
        
        title = ctk.CTkLabel(
            info_frame,
            text="Hospital Assistant",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="white"
        )
        title.pack(anchor="w")
        
        # Status with animated pulsing dot
        status_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        status_frame.pack(anchor="w", pady=(5, 0))
        
        # Pulsing status dot
        self.status_dot = PulsingDot(status_frame, color=self.colors['success'])
        self.status_dot.pack(side="left")
        
        status_text = ctk.CTkLabel(
            status_frame,
            text="  Online • Ready to help",
            font=ctk.CTkFont(size=13),
            text_color="#e0f2fe"
        )
        status_text.pack(side="left")
        
        # Right side - Stats & Time
        right_frame = ctk.CTkFrame(inner, fg_color="transparent")
        right_frame.pack(side="right", fill="y")
        
        # Time with animated update
        self.time_label = ctk.CTkLabel(
            right_frame,
            text=datetime.now().strftime("%I:%M %p"),
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="white"
        )
        self.time_label.pack(anchor="e")
        
        date_label = ctk.CTkLabel(
            right_frame,
            text=datetime.now().strftime("%B %d, %Y"),
            font=ctk.CTkFont(size=11),
            text_color="#bae6fd"
        )
        date_label.pack(anchor="e", pady=(2, 0))
        
        # Update time every minute with animation
        self.update_time()
        
    def animate_breathing(self, widget):
        """Subtle breathing/pulsing animation"""
        def breathe(expand=True):
            if expand:
                widget.configure(corner_radius=32)
            else:
                widget.configure(corner_radius=28)
            self.after(1000, lambda: breathe(not expand))
        breathe()
        
    def update_time(self):
        self.time_label.configure(text=datetime.now().strftime("%I:%M %p"))
        self.after(60000, self.update_time)
        
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
        # Quick actions container with gradient background
        quick_frame = ctk.CTkFrame(
            self.chat_card,
            fg_color=self.colors['bg_gradient_start'],
            height=70
        )
        quick_frame.pack(fill="x", padx=2)
        
        inner = ctk.CTkFrame(quick_frame, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=15)
        
        # Label with icon
        label = ctk.CTkLabel(
            inner,
            text="⚡ Quick Actions:",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.colors['primary']
        )
        label.pack(side="left", padx=(0, 15))
        
        # Quick action buttons with hover animations
        actions = [
            ("📅 Appointments", "How do I book an appointment?", self.colors['primary']),
            ("💊 Pharmacy", "What are the pharmacy hours?", self.colors['success']),
            ("💳 Billing", "How do I pay my bill?", self.colors['warning']),
            ("🚨 Emergency", "Where is the emergency room?", self.colors['error']),
            ("👥 Visitors", "What are the visiting hours?", "#8b5cf6"),
            ("🧪 Lab Tests", "How do I get lab test results?", "#06b6d4")
        ]
        
        self.quick_buttons = []
        for text, query, color in actions:
            btn = ctk.CTkButton(
                inner,
                text=text,
                font=ctk.CTkFont(size=11, weight="bold"),
                fg_color=self.get_light_color(color),
                text_color=color,
                hover_color=self.get_medium_color(color),
                border_width=2,
                border_color=self.get_medium_color(color),
                corner_radius=20,
                height=36,
                command=lambda q=query: self.send_quick_action(q)
            )
            btn.pack(side="left", padx=4)
            self.quick_buttons.append(btn)
            
            # Add hover effect binding
            btn.bind("<Enter>", lambda e, b=btn, c=color: self.button_hover_enter(b, c))
            btn.bind("<Leave>", lambda e, b=btn, c=color: self.button_hover_leave(b, c))
            
    def button_hover_enter(self, btn, color):
        """Animate button on hover"""
        btn.configure(border_width=3, border_color=color)
        
    def button_hover_leave(self, btn, color):
        """Reset button after hover"""
        btn.configure(border_width=2, border_color=self.get_medium_color(color))
            
    def create_input_area(self):
        # Input container with subtle gradient
        input_container = ctk.CTkFrame(
            self.chat_card,
            fg_color=self.colors['bg_card'],
            corner_radius=0
        )
        input_container.pack(fill="x", padx=2, pady=2)
        
        # Separator line with gradient effect
        separator = ctk.CTkFrame(input_container, fg_color=self.colors['primary_light'], height=2)
        separator.pack(fill="x")
        
        inner = ctk.CTkFrame(input_container, fg_color="transparent")
        inner.pack(fill="x", padx=25, pady=18)
        
        # Name entry (smaller, on top) with icon
        name_frame = ctk.CTkFrame(inner, fg_color="transparent")
        name_frame.pack(fill="x", pady=(0, 12))
        
        name_icon = ctk.CTkLabel(
            name_frame,
            text="👤",
            font=ctk.CTkFont(size=14)
        )
        name_icon.pack(side="left")
        
        name_label = ctk.CTkLabel(
            name_frame,
            text=" Your name (optional):",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['text_secondary']
        )
        name_label.pack(side="left")
        
        self.name_entry = ctk.CTkEntry(
            name_frame,
            placeholder_text="Enter your name...",
            font=ctk.CTkFont(size=12),
            fg_color=self.colors['bg_chat'],
            border_color=self.colors['border'],
            corner_radius=12,
            height=38,
            width=220
        )
        self.name_entry.pack(side="left", padx=(10, 0))
        
        # Message entry frame
        msg_frame = ctk.CTkFrame(inner, fg_color="transparent")
        msg_frame.pack(fill="x")
        
        # Message entry with enhanced styling
        self.message_entry = ctk.CTkEntry(
            msg_frame,
            placeholder_text="💬 Type your message here... (Press Enter to send)",
            font=ctk.CTkFont(size=15),
            fg_color=self.colors['bg_chat'],
            border_color=self.colors['border'],
            corner_radius=25,
            height=55
        )
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 12))
        self.message_entry.bind("<Return>", self.send_message)
        self.message_entry.bind("<FocusIn>", self.on_entry_focus)
        self.message_entry.bind("<FocusOut>", self.on_entry_unfocus)
        
        # Button container for better grouping
        btn_container = ctk.CTkFrame(msg_frame, fg_color="transparent")
        btn_container.pack(side="left")
        
        # Animated Send button
        self.send_btn = ctk.CTkButton(
            btn_container,
            text="Send ➤",
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=self.colors['primary'],
            hover_color=self.colors['primary_hover'],
            corner_radius=25,
            height=55,
            width=110,
            command=self.send_message
        )
        self.send_btn.pack(side="left", padx=(0, 8))
        
        # Add send button pulse animation
        self.animate_send_button()
        
        # Clear button with icon
        self.clear_btn = ctk.CTkButton(
            btn_container,
            text="🗑️",
            font=ctk.CTkFont(size=18),
            fg_color=self.colors['error'],
            hover_color=self.colors['error_light'],
            corner_radius=25,
            height=55,
            width=55,
            command=self.clear_chat
        )
        self.clear_btn.pack(side="left")
        
    def on_entry_focus(self, event):
        """Animate entry on focus"""
        self.message_entry.configure(border_color=self.colors['primary'], border_width=2)
        
    def on_entry_unfocus(self, event):
        """Reset entry on unfocus"""
        self.message_entry.configure(border_color=self.colors['border'], border_width=1)
        
    def animate_send_button(self):
        """Subtle pulse animation for send button"""
        colors = [self.colors['primary'], self.colors['primary_dark'], self.colors['primary']]
        
        def pulse(index=0):
            self.send_btn.configure(fg_color=colors[index % len(colors)])
            self.after(2000, lambda: pulse(index + 1))
            
        pulse()
        
    def show_welcome(self):
        # Animated Welcome message container
        welcome_frame = ctk.CTkFrame(
            self.chat_scroll,
            fg_color="transparent"
        )
        welcome_frame.pack(fill="x", pady=20)
        
        # Welcome card with shadow effect
        card = ctk.CTkFrame(
            welcome_frame,
            fg_color=self.colors['bg_card'],
            corner_radius=20,
            border_width=2,
            border_color=self.colors['primary_light']
        )
        card.pack(padx=40, pady=10)
        
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=35, pady=30)
        
        # Animated Welcome icon with wave effect
        self.welcome_icon = ctk.CTkLabel(
            inner,
            text="👋",
            font=ctk.CTkFont(size=56)
        )
        self.welcome_icon.pack()
        
        # Animate wave
        self.animate_wave(self.welcome_icon)
        
        # Welcome title with gradient effect (simulated)
        title = ctk.CTkLabel(
            inner,
            text="Welcome to Hospital Assistant!",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
            text_color=self.colors['primary']
        )
        title.pack(pady=(15, 8))
        
        # Welcome subtitle
        subtitle = ctk.CTkLabel(
            inner,
            text="I'm here to help you with all your hospital-related questions",
            font=ctk.CTkFont(size=14),
            text_color=self.colors['text_secondary']
        )
        subtitle.pack()
        
        # Animated Features grid
        features_frame = ctk.CTkFrame(inner, fg_color="transparent")
        features_frame.pack(pady=(25, 0))
        
        features = [
            ("📅", "Appointments", self.colors['primary']),
            ("💊", "Pharmacy", self.colors['success']),
            ("💳", "Billing", self.colors['warning']),
            ("🚨", "Emergency", self.colors['error']),
            ("👥", "Visitors", "#8b5cf6"),
            ("🧪", "Lab Tests", "#06b6d4")
        ]
        
        self.feature_items = []
        for i, (icon_text, label_text, color) in enumerate(features):
            feature_item = ctk.CTkFrame(
                features_frame,
                fg_color=self.get_light_color(color),
                corner_radius=15
            )
            feature_item.pack(side="left", padx=8, pady=5)
            
            feature_inner = ctk.CTkFrame(feature_item, fg_color="transparent")
            feature_inner.pack(padx=15, pady=10)
            
            icon_lbl = ctk.CTkLabel(
                feature_inner,
                text=icon_text,
                font=ctk.CTkFont(size=28)
            )
            icon_lbl.pack()
            
            text_lbl = ctk.CTkLabel(
                feature_inner,
                text=label_text,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=color
            )
            text_lbl.pack(pady=(5, 0))
            
            self.feature_items.append((feature_item, color))
            
            # Animate features appearing one by one
            feature_item.pack_forget()
            self.after(200 * (i + 1), lambda f=feature_item: f.pack(side="left", padx=8, pady=5))
            
        # Instruction with animated dots
        self.instruction_label = ctk.CTkLabel(
            inner,
            text="",
            font=ctk.CTkFont(size=13),
            text_color=self.colors['text_secondary']
        )
        self.instruction_label.pack(pady=(25, 0))
        
        # Type instruction text
        self.after(1500, lambda: self.type_text(
            self.instruction_label,
            "✨ Type a message below or click a quick action to get started!"
        ))
        
    def animate_wave(self, label):
        """Animate wave emoji"""
        emojis = ["👋", "🖐️", "👋", "✋", "👋"]
        
        def wave(index=0, count=0):
            if count < 10:  # Wave 10 times then stop
                label.configure(text=emojis[index % len(emojis)])
                self.after(300, lambda: wave(index + 1, count + 1))
            else:
                label.configure(text="👋")
                
        wave()
        
    def add_message(self, message, is_user=True):
        # Message container with slide animation
        msg_container = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        msg_container.pack(fill="x", pady=8, padx=15)
        
        # Alignment
        if is_user:
            msg_container.pack_configure(anchor="e")
        else:
            msg_container.pack_configure(anchor="w")
            
        # Inner frame for bubble with enhanced styling
        bubble_frame = ctk.CTkFrame(
            msg_container,
            fg_color=self.colors['user_bubble'] if is_user else self.colors['bot_bubble'],
            corner_radius=20,
            border_width=0 if is_user else 2,
            border_color=self.colors['border'] if not is_user else None
        )
        bubble_frame.pack(side="right" if is_user else "left", padx=5)
        
        # Add shadow effect for bot messages
        if not is_user:
            bubble_frame.configure(border_color=self.colors['primary_light'])
        
        inner = ctk.CTkFrame(bubble_frame, fg_color="transparent")
        inner.pack(padx=18, pady=12)
        
        # Sender label with icon
        sender_text = self.user_name if self.user_name and is_user else ("👤 You" if is_user else "🏥 Hospital Assistant")
        sender = ctk.CTkLabel(
            inner,
            text=sender_text,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#e0f2fe" if is_user else self.colors['primary']
        )
        sender.pack(anchor="w")
        
        # Message text with better formatting
        msg_label = ctk.CTkLabel(
            inner,
            text=message,
            font=ctk.CTkFont(size=14),
            text_color="white" if is_user else self.colors['text_primary'],
            wraplength=450,
            justify="left"
        )
        msg_label.pack(anchor="w", pady=(6, 4))
        
        # Timestamp with icon
        time_text = f"🕐 {datetime.now().strftime('%I:%M %p')}"
        timestamp = ctk.CTkLabel(
            inner,
            text=time_text,
            font=ctk.CTkFont(size=10),
            text_color="#bae6fd" if is_user else self.colors['text_secondary']
        )
        timestamp.pack(anchor="e")
        
        # Store widget reference
        self.message_widgets.append(msg_container)
        
        # Animate message appearing
        self.animate_message_appear(bubble_frame)
        
        # Scroll to bottom
        self.after(50, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))
        
    def animate_message_appear(self, widget):
        """Subtle appear animation for messages"""
        # Flash border color
        original_border = widget.cget("border_color")
        widget.configure(border_color=self.colors['glow'], border_width=2)
        self.after(200, lambda: widget.configure(border_color=original_border if original_border else self.colors['border'], border_width=2 if not original_border else 0))
        
    def show_typing_indicator(self):
        # Enhanced typing indicator with animated dots
        self.typing_frame = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        self.typing_frame.pack(fill="x", pady=8, padx=15, anchor="w")
        
        bubble = ctk.CTkFrame(
            self.typing_frame,
            fg_color=self.colors['bot_bubble'],
            corner_radius=20,
            border_width=2,
            border_color=self.colors['primary_light']
        )
        bubble.pack(side="left", padx=5)
        
        inner = ctk.CTkFrame(bubble, fg_color="transparent")
        inner.pack(padx=18, pady=14)
        
        # Header
        header = ctk.CTkLabel(
            inner,
            text="🏥 Hospital Assistant",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=self.colors['primary']
        )
        header.pack(anchor="w")
        
        # Animated typing dots
        dots_frame = ctk.CTkFrame(inner, fg_color="transparent")
        dots_frame.pack(anchor="w", pady=(8, 0))
        
        self.typing_indicator = TypingIndicator(dots_frame)
        self.typing_indicator.pack(side="left")
        
        typing_text = ctk.CTkLabel(
            dots_frame,
            text="  typing",
            font=ctk.CTkFont(size=12),
            text_color=self.colors['text_secondary']
        )
        typing_text.pack(side="left")
        
        self.chat_scroll._parent_canvas.yview_moveto(1.0)
        
    def remove_typing_indicator(self):
        if hasattr(self, 'typing_frame'):
            # Stop animation before destroying
            if hasattr(self, 'typing_indicator'):
                self.typing_indicator.stop()
            self.typing_frame.destroy()
        
    def send_message(self, event=None):
        # Get user name
        if self.name_entry.get().strip():
            self.user_name = self.name_entry.get().strip()
            
        # Get message
        message = self.message_entry.get().strip()
        
        if not message:
            # Shake animation for empty message
            self.shake_widget(self.message_entry)
            return
            
        # Clear input
        self.message_entry.delete(0, "end")
        
        # Animate send button click
        self.animate_button_click(self.send_btn)
        
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
            
            # Update UI in main thread with slight delay for effect
            self.after(800, lambda: self.receive_response(response))
            
        threading.Thread(target=get_response, daemon=True).start()
        
    def shake_widget(self, widget):
        """Shake animation for invalid input"""
        original_border = widget.cget("border_color")
        widget.configure(border_color=self.colors['error'])
        
        def shake(count=0, direction=1):
            if count < 6:
                # Get current position and shift
                self.after(50, lambda: shake(count + 1, -direction))
            else:
                widget.configure(border_color=original_border)
                
        shake()
        
    def animate_button_click(self, button):
        """Visual feedback on button click"""
        original_color = button.cget("fg_color")
        button.configure(fg_color=self.colors['primary_light'])
        self.after(100, lambda: button.configure(fg_color=original_color))
        
    def receive_response(self, response):
        self.remove_typing_indicator()
        self.add_message(response, is_user=False)
        self.chat_history.append({"text": response, "is_user": False})
        
        # Play notification sound effect (visual flash instead)
        self.flash_notification()
        
    def flash_notification(self):
        """Flash effect when receiving message"""
        original_color = self.chat_card.cget("border_color")
        self.chat_card.configure(border_color=self.colors['success'])
        self.after(300, lambda: self.chat_card.configure(border_color=original_color))
        
    def send_quick_action(self, query):
        self.message_entry.delete(0, "end")
        self.message_entry.insert(0, query)
        self.send_message()
        
    def clear_chat(self):
        # Animate clear button
        self.animate_button_click(self.clear_btn)
        
        # Clear all messages with fade effect
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()
        self.chat_history = []
        self.message_widgets = []
        
        # Show welcome with animation
        self.show_welcome()


def main():
    app = ModernHospitalChatGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
