from flask import Flask
app = Flask(__name__)
import random

too_high='<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2VoZHE2MXl3N3VsbmZ4c2k0MW5yOTQ4czQxNHp2bjUzcmMyZHRhdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KpAPQVW9lWnWU/200.webp">'
too_low='<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmZnem5yZXB0NTdpaDRsNzQ4NGxtbzAyNTg0azRicGczeTlhbXVrcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IevhwxTcTgNlaaim73/200.webp">'
good_job='<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXIwMGdmcG9mN2l2NTY0Z2pwZTRnZDZjY2dyNjd3OTIwMWEwMHBuMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Hc8PMCBjo9BXa/giphy.webp">'
image='<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXRlZ2RjODk3dzN3M3M0ZTUyYXAxMDAzbmliZDFtMnhqaHVodDZ0eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1yLBg64OwNvcdom7Rs/giphy.gif">'

@app.route('/')
def guess_head():
    return "<h1>Guess a number</h1>"+'<p>Type your guess in the URL like this: /5</p>'+image

guess = random.randint(1,10)

@app.route('/<int:your_guess>')
def guess_page(your_guess):
    if your_guess < guess:
        return "<h1>Too low!</h1>"+too_low
    elif your_guess > guess:
        return "<h1>Too high!</h1>"+too_high
    else:
        return "<h1>Good job!</h1>"+good_job

if __name__ == '__main__':
    app.run(debug=True)

