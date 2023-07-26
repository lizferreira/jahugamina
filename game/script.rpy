# Coloca el código de tu juego en este archivo.
# Declara los personajes usados en el juego como en el ejemplo:

define a = Character("Alejo Garcia")

#etiqueta de posicion
transform center:
        xalign 0.5  
        yalign 2.15

transform left:
        xalign -0.15
        yalign 2.15

#etiqueta de transiciones
define annoytheuser = Dissolve(1.0)



# El juego comienza aquí.

label start:
$ renpy.music.play("music_instrumental.mp3") #musica

scene asuncion
with annoytheuser

show alejogarcia at center
with annoytheuser
# Presenta las líneas del diálogo.

a "Hola, me llamo Alejo García, soy un navegante y explorador portugués y descubrí el Paraguay en el año 1524"

a "Juguemos!"

#Pregunta 1
show alejogarcia at center
with annoytheuser

label geografia_1: #etiqueta pregunta 1
        a "¿Es Asunción la capital de Paraguay?"

show alejogarcia at left
with annoytheuser
menu:
        "Si":
                jump choice1_yes
        "No":
                jump choice1_no

label choice1_yes:
        $ menu_flag = True 
        a "Respuesta correcta. Bien facil!"
        a "Continuemos!"
        jump choice1_done

label choice1_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"                        
        jump geografia_1
label choice1_done:

hide alejogarcia

#Pregunta 2      
show alejogarcia at center
with annoytheuser

label geografia_2:
        a "¿Paraguay limita al norte con Brasil?"       

show alejogarcia at left
with annoytheuser

menu:
        
        "Si":
                jump choice2_yes
        "No":
                jump choice2_no

label choice2_yes:
        $ menu_flag = True 
        a "Excelente!"
        a "Adelante con la siguiente!"
        jump choice2_done

label choice2_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_2
label choice2_done:

hide alejogarcia

#Pregunta 3
show alejogarcia at center
with annoytheuser

label geografia_3:
        a "¿Es el guaraní la moneda oficial de Paraguay?"

show alejogarcia at left
with annoytheuser

menu:

        "Si":
                jump choice3_yes
        "No":
                jump choice3_no

label choice3_yes:
        $ menu_flag = True 
        a "Respuesta correcta"
        a "Muy bien!. Siguiente pregunta"
        jump choice3_done

label choice3_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_3
label choice3_done:

hide alejogarcia

#Pregunta 4
show alejogarcia at center
with annoytheuser

label geografia_4:
        a "El cerro Naranjo se encuentra situada en el departamento de:"

show alejogarcia at left
with annoytheuser

menu:

        "Caaguazú":
                jump choice4_no
        "Cordillera": 
                jump choice4_yes

label choice4_yes:
        $ menu_flag = True 
        a "Excelente. ¡Pasemos a la siguiente!"
        jump choice4_done

label choice4_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_4
label choice4_done:

hide alejogarcia

#Pregunta 5
show alejogarcia at center
with annoytheuser

label geografia_5:
        a "La superficie del Paraguay es:"

show alejogarcia at left
with annoytheuser

menu:

        "406,502 km²":
                jump choice5_no
        "406,752 km²":
                jump choice5_yes

label choice5_yes:
        $ menu_flag = True 
        a "Estupendo! Vamos al próximo tema!"
        jump choice5_done

label choice5_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_5
label choice5_done:

hide alejogarcia

#Pregunta 6
show alejogarcia at center
with annoytheuser

label geografia_6:
        a "¿El Pico Tres Kandú es la montaña más alta de Paraguay?"

show alejogarcia at left
with annoytheuser

menu:

        "Si":
                jump choice6_no
        "No":
                jump choice6_yes

label choice6_yes:
        $ menu_flag = True 
        a "Muy bien!. Sigamos con la siguiente pregunta!"
        jump choice6_done

label choice6_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_6
label choice6_done:

hide alejogarcia

#Pregunta 7
show alejogarcia at center
with annoytheuser

label geografia_7:
        a "¿Es el Gran Pantanal la mayor área de humedales en Paraguay?"

show alejogarcia at left
with annoytheuser

menu:

        "Si":
                jump choice7_yes
        "No":
                jump choice7_no

label choice7_yes:
        $ menu_flag = True 
        a "Respuesta correcta"
        a "Magnífico! Continuemos!"
        jump choice7_done

label choice7_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_7
label choice7_done:

hide alejogarcia

#Pregunta 8
show alejogarcia at center
with annoytheuser

label geografia_8:
        a "¿La Hidroeléctrica Itaipú está ubicada en el Río Paraná?"

show alejogarcia at left
with annoytheuser

menu:

        "Si":
                jump choice8_yes
        "No":
                jump choice8_no

label choice8_yes:
        $ menu_flag = True 
        a "Muy bien!. Adelante con la próxima pregunta!"
        jump choice8_done

label choice8_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_8
label choice8_done:

hide alejogarcia

#Pregunta 9
show alejogarcia at center
with annoytheuser

label geografia_9:
        a "¿El Parque Nacional Ybycuí es uno de los más grandes de Paraguay?"

show alejogarcia at left
with annoytheuser

menu:

        "Si":
                jump choice9_no
        "No":
                jump choice9_yes

label choice9_yes:
        $ menu_flag = True 
        a "Fabuloso! Sigamos con la última pregunta!"
        jump choice9_done

label choice9_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_9
label choice9_done:

hide alejogarcia

#Pregunta 10:
show alejogarcia at center
with annoytheuser

label geografia_10:
        a "¿El departamento de Canindeyú se encuentra al sureste de Paraguay?"


show alejogarcia at left
with annoytheuser

menu:

        "Si":
                jump choice10_yes

        "No":
                jump choice10_no

label choice10_yes:
        $ menu_flag = True
        a "Sí, el departamento de Canindeyú se encuentra al sureste de Paraguay"
        a "¡Excelente trabajo! Has respondido correctamente todas las preguntas. Tu conocimiento es realmente impresionante. ¡Sigue así!"
        jump choice10_done

label choice10_no:
        $ menu_flag = False
        a "Respuesta incorrecta. Intente de nuevo"
        jump geografia_10
label choice10_done:
# Finaliza el juego:
hide alejogarcia
$ renpy.music.stop()

return