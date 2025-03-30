import requests
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image


class PageFirst(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image(source="Image/img.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))

        self.add_widget(self.image)
        self.button = MDRectangleFlatButton(text="Click", pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                            text_color=(1, 1, 1, 1),
                                            font_size=32,
                                            md_bg_color=(118 / 255, 181 / 255, 197 / 255, 0.1),
                                            size_hint=(0.3, 0.1),
                                            line_color=(118 / 255, 181 / 255, 197 / 255, 0.4),
                                            on_press=self.switch)

        self.add_widget(self.button)

    def switch(self, instance):
        self.manager.current = "ConvertPage"
        self.manager.transition.direction = "left"


class PageSecond(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Currency API call
        url = "https://open.er-api.com/v6/latest/USD"
        data = requests.get(url)
        self.currency_rates_json = data.json()
        self.currency_code = ["AUD", "CNY", "EUR", "GBP", "INR", "JPY", "KRW"]
        self.country_name = ["Australia", "China", "Europe Region", "Great British", "India", "Japan", "South Korea"]
        self.currency_symbol = ["AU$", "¥", "€", "£", "₹", "¥", "₩"]

        # Create most outer layout
        self.bxlayout = MDBoxLayout(orientation="vertical", padding=10, size=(1, 1), spacing=10)

        # Create inner box layout
        self.val_bxlayout = MDBoxLayout(orientation="vertical", size_hint_y=0.35, spacing=5)
        self.title_lbl = MDLabel(text="Currency Converter", size_hint_y=0.3, halign="center", theme_text_color="Custom",
                                 text_color=(136 / 255, 131 / 255, 131 / 255, 1))
        self.input_txt = MDTextField(hint_text="Amount in USD", multiline=False, halign="center",
                                     font_size=18, size_hint=(1, 0.6))
        self.calculate_btn = MDRectangleFlatButton(text="Calculate", size_hint=(1, 0.16),
                                                   md_bg_color=(23 / 255, 145 / 255, 152 / 255, 1),
                                                   line_color=(0, 0, 0, 0),
                                                   on_release=self.update_result,
                                                   theme_text_color="Custom", text_color=(1, 1, 1, 1))

        # Create inner gridlayout
        self.grid = MDGridLayout(cols=3, size=(1, 0.65), spacing=10)

        # Using loop value call from API
        for i in range(len(self.currency_code)):
            self.data = MDCard(
                style="elevated",
                ripple_behavior=True,
                padding=10,
                orientation="vertical",
                md_bg_color=(72 / 255, 176 / 255, 181 / 255, 1)

            )
            self.card_country_lbl = MDLabel(text=self.country_name[i], font_size=20, size=(1, 0.5),
                                            theme_text_color="Custom", text_color=(1, 1, 1, 1))
            self.card_currency_rate_lbl = MDLabel(
                text=f"{self.currency_symbol[i]}" + " " + f"{round(self.currency_rates_json["rates"].get(self.currency_code[i]), 3)}",
                font_size=26,
                size=(1, 0.5), theme_text_color="Custom", text_color=(1, 1, 1, 1))

            # Add card labels
            self.data.add_widget(self.card_country_lbl)
            self.data.add_widget(self.card_currency_rate_lbl)

            # Add card in gridlayout
            self.grid.add_widget(self.data)

        self.button_1 = MDRectangleFlatButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                              text_color=(1, 1, 1, 1),
                                              md_bg_color=(23 / 255, 145 / 255, 152 / 255, 1),
                                              line_color=(23 / 255, 145 / 255, 152 / 255, 1),
                                              size_hint=(1, 0.1), on_press=self.switch)

        # Add widget inner boxlayout
        self.val_bxlayout.add_widget(self.title_lbl)
        self.val_bxlayout.add_widget(self.input_txt)
        self.val_bxlayout.add_widget(self.calculate_btn)

        # Add widget outer layout
        self.bxlayout.add_widget(self.val_bxlayout)
        self.bxlayout.add_widget(self.grid)
        self.bxlayout.add_widget(self.button_1)

        # Add main outer layout to the screen
        self.add_widget(self.bxlayout)

    def switch(self, instance):
        self.input_txt.text = ""
        self.manager.current = "HomePage"
        self.manager.transition.direction = "right"

    def update_result(self, instance):
        try:
            if self.input_txt.text == "0" or self.input_txt.text == "":
                self.grid.clear_widgets()
                # Using loop value call from API
                for i in range(len(self.currency_code)):
                    self.data = MDCard(
                        style="elevated",
                        ripple_behavior=True,
                        padding=10,
                        orientation="vertical",
                        md_bg_color=(72 / 255, 176 / 255, 181 / 255, 1)

                    )
                    self.card_country_lbl = MDLabel(text=self.country_name[i], font_size=20, size=(1, 0.5),
                                                    theme_text_color="Custom", text_color=(1, 1, 1, 1))
                    self.card_currency_rate_lbl = MDLabel(
                        text=f"{self.currency_symbol[i]}" + " " + f"{round(self.currency_rates_json["rates"].get(self.currency_code[i]), 3)}",
                        font_size=26,
                        size=(1, 0.5), theme_text_color="Custom", text_color=(1, 1, 1, 1))

                    # Add card labels
                    self.data.add_widget(self.card_country_lbl)
                    self.data.add_widget(self.card_currency_rate_lbl)

                    # Add card in gridlayout
                    self.grid.add_widget(self.data)
            else:
                self.grid.clear_widgets()
                for i in range(len(self.currency_code)):
                    self.data = MDCard(
                        style="elevated",
                        ripple_behavior=True,
                        padding=10,
                        orientation="vertical",
                        md_bg_color=(72 / 255, 176 / 255, 181 / 255, 1)
                    )
                    self.card_country_lbl = MDLabel(text=self.country_name[i], font_size=20,
                                                    size=(1, 0.5), theme_text_color="Custom", text_color=(1, 1, 1, 1))
                    self.card_currency_rate_lbl = MDLabel(
                        text=f"{self.currency_symbol[i]}" + " " + f"{round(float(self.input_txt.text) * self.currency_rates_json["rates"].get(self.currency_code[i]), 3)}",
                        font_size=26,
                        size=(1, 0.5),
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1))

                    # Add card labels
                    self.data.add_widget(self.card_country_lbl)
                    self.data.add_widget(self.card_currency_rate_lbl)

                    # Add card in gridlayout
                    self.grid.add_widget(self.data)
        except:
            self.grid.clear_widgets()
            # Using loop value call from API
            for i in range(len(self.currency_code)):
                self.data = MDCard(
                    style="elevated",
                    ripple_behavior=True,
                    padding=10,
                    orientation="vertical",
                    md_bg_color=(72 / 255, 176 / 255, 181 / 255, 1)

                )
                self.card_country_lbl = MDLabel(text=self.country_name[i], font_size=20, size=(1, 0.5),
                                                theme_text_color="Custom", text_color=(1, 1, 1, 1))
                self.card_currency_rate_lbl = MDLabel(
                    text=f"{self.currency_symbol[i]}" + " " + f"{round(self.currency_rates_json["rates"].get(self.currency_code[i]), 3)}",
                    font_size=26,
                    size=(1, 0.5), theme_text_color="Custom", text_color=(1, 1, 1, 1))

                # Add card labels
                self.data.add_widget(self.card_country_lbl)
                self.data.add_widget(self.card_currency_rate_lbl)

                # Add card in gridlayout
                self.grid.add_widget(self.data)


class ConverterApp(MDApp):
    def build(self):
        sc = MDScreenManager()
        sc.add_widget(PageFirst(name="HomePage"))
        sc.add_widget(PageSecond(name="ConvertPage"))
        return sc


if __name__ == "__main__":
    ConverterApp().run()
