from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
import arabic_reshaper
from bidi.algorithm import get_display

Window.size = (400, 700)

# ---------- Arabic Fix ----------
def fix_ar(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

# ---------- TEXTS ----------
EN_TEXT = """My Beloved Nika,

On this magical day, I want to pour my heart out to you. 
You are the most incredible person I've ever met - a beautiful soul 
with a heart of gold that shines brighter than a thousand suns. 🌟

Every moment with you feels like a dream come true. 
Your laughter is my favorite melody, your smile my daily sunshine, 
and your presence in my life is the greatest blessing I could ever ask for.

You have this magical ability to make everything better, 
to turn ordinary days into extraordinary memories, 
and to fill every space you enter with warmth and light.

Today, I celebrate YOU - the amazing, strong, beautiful woman 
who has captured my heart completely. May this year bring you 
all the joy, love, and success that you truly deserve.

I love you more than words can express,
More than the stars in the sky,
And more than forever itself. 💕

Forever yours...
"""

ID_TEXT = """Sayangku Nika yang tercinta,

Di hari spesialmu ini, izinkan aku mengungkapkan perasaan terdalamku.
Kamu adalah anugerah terindah yang pernah Tuhan berikan dalam hidupku. 🌸

Setiap detik bersamamu adalah harta karun yang tak ternilai.
Senyummu adalah matahari pagiku, tawamu adalah musik terindah,
dan kehadiranmu adalah alasan mengapa dunia terasa begitu sempurna.

Kamu memiliki keajaiban yang bisa mengubah hari biasa menjadi luar biasa,
mengubah sedih menjadi bahagia, dan membuat setiap momen terasa istimewa.

Hari ini, kurayakan dirimu - wanita kuat, cantik, dan mengagumkan
yang telah mencuri hatiku sepenuhnya. Semoga tahun ini membawakanmu
semua kebahagiaan, cinta, و keberhasilan yang layak kamu dapatkan.

Aku mencintaimu lebih dari kata-kata bisa ucapkan,
Lebih dari bintang di langit,
Dan lebih dari selamanya. 💝

Selalu milikmu...
"""

AR_TEXT = "[font=Amiri-Regular.ttf]" + fix_ar("""يا حبيبتي نيكا،

في يوم ميلادك الجميل، أريد أن أخبرك بأنكِ نور حياتي وسعادتي.
أنتِ أجمل ما حدث لي، وقلبكِ الطيب هو أعظم هدية تلقيتها. 🌹

كل لحظة معكِ هي كنز ثمين، وكل يوم بوجودكِ هو عيد.
ابتسامتكِ تشرق كالشمس، وعيناكِ تتلألأان كالنجوم،
وحبكِ هو أجمل شعور عرفته في حياتي.

أنتِ معجزة حقيقية، امرأة قوية ورائعة
تملئين حياتي بالفرح والحب والسعادة.
أتمنى لكِ عامًا مليئًا بالأحلام التي تتحقق،
والضحكات التي لا تنتهي، والحب الذي يزداد يومًا بعد يوم.

أحبكِ أكثر مما تستطيع الكلمات التعبير عنه،
أكثر من النجوم في السماء،
وأكثر من الأبد نفسه. 💖

إلى الأبد حبيبكِ...
""") + "[/font]"

FOOTER = "[font=Amiri-Regular.ttf]" + fix_ar("""
1 / 1 / 2026
— محمد (أمير)
— Mohamed (Ameer)
""") + "[/font]"

# ---------- تقسيم النص ----------
TEXT_PARTS = [
    EN_TEXT + "\n\n" + ID_TEXT + "\n\n",
    AR_TEXT + "\n\n",
    FOOTER
]

# ---------- شاشة البداية ----------
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        with layout.canvas.before:
            Color(0.96, 0.93, 0.95, 1)
            self.bg = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(on_resize=lambda *_: setattr(self.bg, 'size', Window.size))

        label1 = Label(
            text="Happy Birthday Nika!",
            font_name="DancingScript-Regular.ttf",
            font_size=32,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            color=(0.3,0.2,0.4,1)
        )
        label2 = Label(
            text="— Amir",
            font_name="DancingScript-Regular.ttf",
            font_size=24,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            color=(0.3,0.2,0.4,1)
        )
        layout.add_widget(label1)
        layout.add_widget(label2)
        self.add_widget(layout)

# ---------- شاشة النصوص ----------
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = FloatLayout()

        # Background
        with root.canvas.before:
            Color(0.96, 0.93, 0.95, 1)
            self.bg = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(on_resize=lambda *_: setattr(self.bg, 'size', Window.size))

        # Title
        title = Label(
            text="Happy Birthday 🤍",
            font_name="DancingScript-Regular.ttf",
            font_size=40,
            pos_hint={"center_x": 0.5, "top": 0.96},
            opacity=0,
            color=(0.4, 0.2, 0.4, 1)
        )
        root.add_widget(title)
        Animation(opacity=1, duration=2).start(title)

        # Scroll
        self.scroll = ScrollView(
            size_hint=(0.9, 0.78),
            pos_hint={"center_x": 0.5, "y": 0.05},
            scroll_type=['bars', 'content'],
            bar_width=10,
            do_scroll_y=True,
            do_scroll_x=False
        )

        # Label
        self.label = Label(
            text="",
            font_name="DancingScript-Regular.ttf",
            font_size=16,
            size_hint_y=None,
            halign="left",
            valign="top",
            markup=True,
            color=(0.2, 0.2, 0.3, 1),
            text_size=(380, None),
            padding=(10, 10),
            shorten=False,
            line_height=1.2
        )

        self.label.bind(
            width=lambda *_: setattr(self.label, "text_size", (self.label.width, None)),
            texture_size=lambda *_: setattr(self.label, "height", self.label.texture_size[1])
        )

        self.scroll.add_widget(self.label)
        root.add_widget(self.scroll)
        self.add_widget(root)

        # Typing effect
        self.part_index = 0
        self.char_index = 0
        self.typing_event = Clock.schedule_interval(self.type_text, 0.035)

        Clock.schedule_once(self.scroll_to_top, 0.1)

    def scroll_to_top(self, dt):
        self.scroll.scroll_y = 1

    def type_text(self, dt):
        if self.part_index >= len(TEXT_PARTS):
            self.typing_event.cancel()
            return False

        current_part = TEXT_PARTS[self.part_index]

        if current_part.startswith("[font"):
            self.label.text += current_part
            self.part_index += 1
            self.char_index = 0
            return

        if self.char_index < len(current_part):
            self.label.text += current_part[self.char_index]
            self.char_index += 1
        else:
            self.part_index += 1
            self.char_index = 0

# ---------- App ----------
class BirthdayApp(App):
    def build(self):
        sm = ScreenManager()
        splash = SplashScreen(name="splash")
        main = MainScreen(name="main")
        sm.add_widget(splash)
        sm.add_widget(main)

        # بعد 3 ثواني انتقل للشاشة الرئيسية
        Clock.schedule_once(lambda dt: setattr(sm, "current", "main"), 3)
        return sm

if __name__ == "__main__":
    BirthdayApp().run()
