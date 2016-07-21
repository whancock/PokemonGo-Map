# uwsgi --socket 0.0.0.0:8000 --protocol=http --pyargv "-u trunkatron -l 'WashingtonDC' -st 10 -p junkthetrunk" -w wsgi



from runserver import app

if __name__ == "__main__":
    app.run()