from flet import *
def main(page:Page):
    page.title ="Tito"
    page.scroll ='auto'
    page.window.top = 1
    page.window.left = 1200
    page.window.width = 350
    page.window.height = 700
    page.bgcolor = 'white'
    page.theme_mode =ThemeMode.LIGHT
    
    Flashlight = Flashlight()
    page.overlay.append(Flashlight)
    ph = PermissionHandler()
    page.overlay.append(ph)
    def open_app(e):
        ph.open_app_settings()
    page.add(

         AppBar(
             title= Text('Flach Light [TA]'),
             color= 'white',
             bgcolor= "#ffc831",
             actions= [
                 IconButton (Icons.SETTINGS,on_click=open_app)
                 
            ]
             
         ),
         Row([
             Text('\n\nFlach Light App',size=31,color='black')
         ],alignment=MainAxisAlignment.CENTER),
         Row([
             Image(src=f"im.png", width= 160)
             ],alignment=MainAxisAlignment.CENTER
         ),
         Row([
             
             ElevatedButton(
                 
                  "ON",
                  width= 100,
                  icon=Icons.PLAY_ARROW,
                  style=ButtonStyle(
                      bgcolor="#ffc831",
                      color='white',
                      padding=15,
                      shape=ContinuousRectangleBorder(radius=100)
                  ),
                  on_click=lambda _: Flashlight.turn_on()
             ),
              ElevatedButton(
                 
                  "OF",
                  width= 100,
                  icon=Icons.PLAY_DISABLED_SHARP,
                  style=ButtonStyle(
                      bgcolor="#ffc831",
                      color='white',
                      padding=15,
                      shape=ContinuousRectangleBorder(radius=100)
                  ),
                  on_click=lambda _: Flashlight.turn_off()
             )

         ],alignment=MainAxisAlignment.CENTER),
         Row([
             Text('\n\n TITOU SIDKOUM',size=20,color='black')
         ],alignment=MainAxisAlignment.CENTER),

             




         






    )





    page.update()
app(main)
