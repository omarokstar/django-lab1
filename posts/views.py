from django.shortcuts import render

# Create your views here.
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post.", "img_url": 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fphotos%2Fbird-blue-clouds-weather-pen-8788491%2F&psig=AOvVaw1ywBAtuu7LJpdEgTJ4xPh2&ust=1748867723027000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMC9qY2e0I0DFQAAAAAdAAAAABAG'},
    {"id": 2, "title": "Second Post", "content": "This is the second post.", "img_url": 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fphotos%2Fbird-blue-clouds-weather-pen-8788491%2F&psig=AOvVaw1ywBAtuu7LJpdEgTJ4xPh2&ust=1748867723027000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMC9qY2e0I0DFQAAAAAdAAAAABAG'},
    {"id": 3, "title": "Third Post", "content": "This is the third post.", "img_url": 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fphotos%2Fbird-blue-clouds-weather-pen-8788491%2F&psig=AOvVaw1ywBAtuu7LJpdEgTJ4xPh2&ust=1748867723027000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMC9qY2e0I0DFQAAAAAdAAAAABAG'},
]

# list all posts
def index(request):
    return render(request, 'posts/index.html', context={'posts':posts})


# view specific post
def show(request, id):

    # get the object
    post = next((post for post in posts if post['id'] == int(id)),None)
    return render(request, 'posts/show.html', context={'post': post})
