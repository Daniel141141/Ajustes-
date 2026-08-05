from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(text="Bem-vindo! O app precisa de acesso.", font_size=18)
        self.btn = Button(text="Solicitar Acesso e Ativar", size_hint=(1, 0.3))
        self.btn.bind(on_press=self.pedir_permissao)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def pedir_permissao(self, instance):
        try:
            from android.permissions import request_permissions, Permission
            
            def callback(permissions, results):
                if all(results):
                    self.label.text = "Permissão concedida! Iniciando processos..."
                else:
                    self.label.text = "Permissão negada pelo usuário."

            request_permissions([Permission.CAMERA], callback)
            
        except Exception as e:
            self.label.text = "Rodando em ambiente de teste."

if __name__ == '__main__':
    CameraApp().run()
  
