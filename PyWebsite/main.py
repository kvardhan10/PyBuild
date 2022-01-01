from website import create_app
#the folder website now becomes package and create_app a method. y'know how it works:)

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)
