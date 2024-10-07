import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videogame_store.settings')
django.setup()

from games.models import Category, Game

def load_data():
    # Crear categorías
    cat1 = Category.objects.create(name='Acción', image='categories/accion.jpg')
    cat2 = Category.objects.create(name='Aventura', image='categories/aventura.jpg')
    cat3 = Category.objects.create(name='Deportes', image='categories/deportes.jpg')
    cat4 = Category.objects.create(name='Estrategia', image='categories/estrategia.jpg')
    cat5 = Category.objects.create(name='Puzzle', image='categories/puzzle.jpg')

    # Crear juegos para cada categoría
    Game.objects.create(name='Juego de Acción 1', description='El mejor juego de acción', price=19.99, image='games/accion1.jpg', category=cat1)
    Game.objects.create(name='Juego de Acción 2', description='Un segundo juego de acción', price=29.99, image='games/accion2.jpg', category=cat1)

    Game.objects.create(name='Juego de Aventura 1', description='Emocionante juego de aventura', price=15.99, image='games/aventura1.jpg', category=cat2)
    Game.objects.create(name='Juego de Aventura 2', description='Segunda entrega de aventura', price=25.99, image='games/aventura2.jpg', category=cat2)

    Game.objects.create(name='Juego de Deportes 1', description='Un juego de deportes popular', price=9.99, image='games/deportes1.jpg', category=cat3)
    Game.objects.create(name='Juego de Deportes 2', description='El mejor juego de deportes', price=12.99, image='games/deportes2.jpg', category=cat3)

    Game.objects.create(name='Juego de Estrategia 1', description='Juego de estrategia avanzado', price=19.99, image='games/estrategia1.jpg', category=cat4)
    Game.objects.create(name='Juego de Estrategia 2', description='Juego de estrategia en tiempo real', price=22.99, image='games/estrategia2.jpg', category=cat4)

    Game.objects.create(name='Juego de Puzzle 1', description='Desafiante juego de puzzle', price=8.99, image='games/puzzle1.jpg', category=cat5)
    Game.objects.create(name='Juego de Puzzle 2', description='Puzzle con niveles avanzados', price=14.99, image='games/puzzle2.jpg', category=cat5)

    print("Datos cargados exitosamente.")

if __name__ == '__main__':
    load_data()
