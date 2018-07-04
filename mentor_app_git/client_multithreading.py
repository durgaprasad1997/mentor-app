
import threading
import click
import sys,os,django
import requests
from requests.auth import HTTPBasicAuth
from onlineapp.models import *

@click.group()
@click.pass_context
def cli(ctx):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "onlineproject.settings")
    django.setup()
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")

    print("main thread")


def get_students_by_id(id):

    url = "http://localhost:8000/api/v1/students/"+str(id)+"/"
    r = requests.get(url,auth=HTTPBasicAuth('durgaprasad', 'durgaprasad'))

    print(r)
    print(r.content)



@cli.command()
@click.pass_context
def getallstudents(ctx):

    #l=(Colleges.objects.values_list("id"))
    #get_students_by_id(1)


    t1 = threading.Thread(target=get_students_by_id, args=(1,))
    t2 = threading.Thread(target=get_students_by_id, args=(2,))
    t3 = threading.Thread(target=get_students_by_id, args=(3,))

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()





if __name__=='__main__':

    cli(obj={})
