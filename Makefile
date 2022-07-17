all: install zipapp
freeze:
	python -m pip freeze > requirements.txt
install:
	python -m pip install --upgrade -r requirements.txt --target src
zipapp:
	python -m zipapp -p "interpreter" -o ncsgitops-agent.pyz src 

test: freeze install zipapp
	python ./ncsgitops-agent.pyz
