# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
 
# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(32, 32))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 32, 32, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img
 
# load an image and predict the class
def run_example(file):
	# load the image
	img = load_image(file)
	# load model
	model = load_model('small_model.h5')
	# predict the class
	result = model.predict(img, experimental_relax_shapes=True)
	return(result[0])
 
# entry point, run the example
if __name__ == "__main__":
	for i in range(0, 11):
		file = str(i) + '.png'
		res = run_example(file)
		if res > 0.5:
			print("t,{}".format(res))
		else:
			print("f,{}".format(res))
