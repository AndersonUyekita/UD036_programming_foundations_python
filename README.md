# Programming Foundations with Python

#### Tags
* Author: AH Uyekita
* Date: 07/12/2018
* Cod: nd036

This introduction course aims to shows the essentials of the Python pogramming.

## Lesson 01 - Introduction

Installation and some quizzes to test the programming level.

## Lesson 02 - Functions

How to create/compound a function and how to use it.

Code examples:
* lesson02_prank.py

## Lesson 03 - Classes: Draw a Turtle

Introduction to the _classes_ and how to works a `method`.

The example `lesson03_mindstorms.py` will use the library `turtle` to draw a turtle drawing a square.

Code examples:
* lesson03_mindstorms.py

Classes could be interpreted as a blueprint of something.

* Classes = Blueprint of a building;
* Any building is a instance of the blueprint (class).

## Lesson 04 - Classes: Send Text

In this lesson, Kunal teaches how to send SMS message from a package called [`Twilio`](https://www.twilio.com).

```{py}
brad = turtle.Turtle()
client = rest.TwilioRestClient()
```
In both lines, an object will be created (brad and client), turtle and rest meaning that inside these folders there are two classes (`Turtle()` and `TwilioRestClient()`) which draw a square and send SMS, each one with your own `def __init__():`.

## Lesson 05 - Classes: Profanity Editor

This lesson talks about how to import a txt file using the `open()` function. Kunal shows the built-in functions and explained that all those are available no matter what.

The mini-project of the lesson is a word checker, which access the internet to do it (check if a word is bad).

## Lesson 06 - Classes: Movie Website

This lesson talks about a creation a new _class_ (Movie) and examples of _instances_ (Godfather and ET) of this new _class_. The constructor is necessary to registry the varibles of this new class, such as movie_title, storyline, poster_image_url, and trailer_youtube_url (also called as instance variables). Lastly, the instances methods (show_trailer()).

## Lesson 07 - Classes: Advanced Topics

The last lesson of this course, cover class child and reusing methods. This is a good strategy to share same variables instance between _classes_.
