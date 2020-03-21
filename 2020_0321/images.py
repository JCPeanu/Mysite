from jinja2 import Template
def imagesHTML():
    with open('images.html') as f:
        s = f.read()
    return s
def main():
    image_list = [
        { 'title': 'Commedian', 
          'desc': "First, this is a banana duct taped to the wall, and this banana plus the duct tape cost $120,000.",
          'url': "https://ichef.bbci.co.uk/news/1024/cpsprodpb/0CE6/production/_110020330_banana.jpg"},
        { 'title': 'Untitled',
          'desc': 'This is a yellow and blue artwork that was made by Mark Rothko, and it was sold for $46.5 million.',
          'url': "https://www.elitereaders.com/wp-content/uploads/2016/01/idiculous-paintings-insanely-sold-for-millions-of-dollars-1280x720.jpg" },
        { 'title': 'Black Fire 1',
          'desc': 'This is a black artwork that was made by Barnett Newman called Black Fire 1, and it was sold for $84.2 million.',
          'url': "https://www.christies.com/img/LotImages/2014/NYR/2014_NYR_02847_0034_000(barnett_newman_black_fire_i).jpg"}
    ]
    tmpl = Template(imagesHTML())
    
    print(tmpl.render({'images': image_list }))
main()
