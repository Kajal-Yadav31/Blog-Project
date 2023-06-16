from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image": "mountain.png",
        "author" : "ABCD",
        "date": date(2022, 7, 31),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!",
        "content": " As designers attempting to creating functional work,  what have you. The purpose of this is so the person viewing the prototype has a chance to actually feel and understand the idea behind what you have created. designers may use squares and rectangles to help you visualize what should and could be in a specific location."
    },
    {
        "slug" : "programming-is-fun",
        "image": "code-snippet.png",
        "author" : "XYZ",
        "date": date(2023, 6, 17),
        "title": "Programming is Great!",
        "excerpt": "Did you ever spend hour searching that one error in your code?",
        "content": "As designers attempting to creating functional work, oftentimes we are required to make our designs look as finished as possible. most times you will have to make sure the prototype looks finished by inserting text or photos or what have you."
    },
    {
        "slug" : "into-the-woods",
        "image": "view.png",
        "author" : "ABCD",
        "date": date(2024, 8, 9),
        "title": "Nature at its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in there!",
        "content": " As designers attempting to creating functional work, oftentimes we are required to make our designs look as finished as possible. designers may use squares and rectangles to help you visualize what should and could be in a specific location."
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug )
    return render(request, "blog/post-detail.html", {"post": identified_post})
