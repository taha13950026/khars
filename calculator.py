from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# تنظیم پس‌زمینه پنجره (برای محیط ویندوز)
Window.clearcolor = get_color_from_hex("#4BEC00") 

class CoDCalculator(App):
    def build(self):
        self.title = "COD MISSION: CALCULATE"
        
        # رنگ‌های تم کال آف دیوتی
        COLOR_BLACK = get_color_from_hex("#0059FD")      # مشکی عمیق
        COLOR_GRAY = get_color_from_hex("#8E3A3A")       # خاکستری تیرهy
        COLOR_MILITARY_GREEN = get_color_from_hex("#040401") # سبز نظامی
        COLOR_TEXT = get_color_from_hex("#761BB8")        # سفید مایل به خاکستری
        COLOR_ACCENT = get_color_from_hex("#66008B")     # قرمز تیره (برای دکمه پاک کردن)

        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=10)

        # نمایشگر (Display) - شبیه به رادار یا صفحه نمایش نظامی
        self.display = TextInput(
            text='0',
            multiline=False,
            readonly=True,
            halign='right',
            font_size='40sp',
            background_color=COLOR_BLACK,
            foreground_color=get_color_from_hex("#13B513"), # سبز فسفری مثل رادار
            input_filter='none'
        )
        main_layout.add_widget(self.display)

        # چیدمان دکمه‌ها
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
        ]

        grid = GridLayout(cols=4, spacing=10)

        for row in buttons:
            for label in row:
                # تعیین رنگ دکمه‌ها بر اساس نوع آن‌ها
                if label == '=':
                    btn_color = COLOR_MILITARY_GREEN
                elif label == 'C':
                    btn_color = COLOR_ACCENT
                elif label in ['/', '*', '-', '+']:
                    btn_color = COLOR_GRAY
                else:
                    btn_color = COLOR_BLACK

                btn = Button(
                    text=label,
                    font_size='25sp',
                    background_normal='', # برای اینکه رنگ خودمان اعمال شود
                    background_color=btn_color,
                    color=COLOR_TEXT,
                    bold=True
                )
                
                # اتصال دکمه به تابع کلیک
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)

        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        current_text = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = '0'
        elif button_text == '=':
            try:
                # محاسبه نتیجه
                result = str(eval(current_text))
                self.display.text = result
            except Exception:
                self.display.text = "ERROR"

        else:
            if current_text == '0':
                self.display.text = button_text
            else:
                self.display.text += button_text

if __name__ == '__main__':
    CoDCalculator().run()
