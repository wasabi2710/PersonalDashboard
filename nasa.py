import aiohttp
import asyncio
import random

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
async def fetch_rover():
    rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2?&api_key=Cn4olVQe0e0UohRWOydacvDuLMFDD1HtuR0uTy3W'
    rover_images_data = await fetch_url(rover_url)
    image_urls = [item['img_src'] for item in rover_images_data['photos']]
    random_image_url = random.choice(image_urls)
    return random_image_url

async def fetch_nasa():
    apod_url = 'https://api.nasa.gov/planetary/apod'
    apod_params = {
        'api_key': 'Cn4olVQe0e0UohRWOydacvDuLMFDD1HtuR0uTy3W', 
    }
    apod_data = await fetch_url(apod_url + '?' + '&'.join([f'{k}={v}' for k, v in apod_params.items()]))
    return apod_data

