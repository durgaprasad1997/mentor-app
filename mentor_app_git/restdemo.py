
import click
import urllib.request
from onlineapp.views import *
from rest_framework import serializers
from django.core import serializers
import django,os,sys


@click.group()
@click.pass_context
def cli(ctx):
    print("in click")


@cli.command()
@click.argument('id',nargs=1)
@click.pass_context
def id(ctx,id):

    url = r"http://samples.openweathermap.org/data/2.5/weather?id="
    api= "&appid=58bfc2109f60ad477f96f17a3eec5919"
    data=url+id+api
    f = urllib.request.urlopen(data)
    print(f.read().decode('utf-8'))



@cli.command()
@click.argument('city',nargs=1)
@click.argument('country',nargs=1)
@click.pass_context
def name(ctx,city,country):

    url = r"http://api.openweathermap.org/data/2.5/weather?q="
    api="&appid=58bfc2109f60ad477f96f17a3eec5919"
    data=url+city+","+country+api

    f = urllib.request.urlopen(data)
    print(f.read().decode('utf-8'))


@cli.command()
@click.argument('lat',nargs=1)
@click.argument('lon',nargs=1)
@click.pass_context
def coord(ctx,lat,lon):

    url = r"http://api.openweathermap.org/data/2.5/weather?"
    coord="lat="+lat+"&lon="+lon
    api="&appid=58bfc2109f60ad477f96f17a3eec5919"

    data=url+coord+api

    f = urllib.request.urlopen(data)
    print(f.read().decode('utf-8'))






if __name__=='__main__':

    cli(obj={})
