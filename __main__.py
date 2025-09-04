import __init__ as init

window = init.windowsetup()
images = init.selectimage("./train")

images_gen = images.getrootimages()

def nextimage():
    try:
        image_path = next(images_gen)
        
        window.current_image_path = image_path
        window.label(image_path, 0, 0, 20, 20)
        window.image(image_path, 0, 1, 20, 20, 512, 512)
    except StopIteration:
        window.label("Congrats, You've completed the database", 0, 2, 20, 20)

def classimage(colour:str, object:str):
    window.classification(colour, object)


window.button("Next Image", 1, 1, nextimage, 20, 5)
window.button("square", 0, 2, lambda: classimage("red", "person"), 20, 5)
window.button("save", 0, 3, lambda: window.savelabel(), 20, 5)


window.windowcreate()