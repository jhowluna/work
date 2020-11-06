import dlib

# opcoes = dlib.shape_predictor_training_options()
# dlib.train_shape_predictor("recursos/EPI.xml", "recursos/EPI.dat", opcoes)

opcoes = dlib.simple_object_detector_training_options()
opcoes.add_left_right_image_flips = True
opcoes.C = 5

dlib.train_simple_object_detector("recursos/EPI.xml", "recursos/EPI.svm", opcoes)
