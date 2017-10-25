from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from logic import DNA


class CustomLayout(GridLayout):

    def clear_given_DNA(self):
        self.ids.given_DNA.text = ""

    def clear_mRNA(self):
        self.ids.mRNA.text = ""

    def clear_res(self):
        self.ids.res_amino.text = ""

    def transcript(self):
        dna_samp = DNA(self.ids.given_DNA.text, "./tables/" + self.ids.code_table.text + ".csv")
        
        if self.ids.template.active:
            self.ids.mRNA.text = dna_samp.template2mRNA()
        else:
            self.ids.mRNA.text = dna_samp.coding2mRNA()

    def translate(self):
        dna_samp = DNA(self.ids.mRNA.text, "./tables/" + self.ids.code_table.text + ".csv")

        self.ids.res_amino.text = dna_samp.translate(self.ids.mRNA.text)

class DNAApp(App):
    title = 'DNA'
    icon = 'icon.png'

if __name__ in ('__main__', '__android__'):
    DNAApp().run()
