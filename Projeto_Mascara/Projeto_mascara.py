import dlib

opcoes = dlib.shape_predictor_training_options()
dlib.train_shape_predictor("recursos/pessoas_mascara.xml", "recursos/Pessoas.dat", opcoes)

opcoes = dlib.simple_object_detector_training_options()
opcoes.add_left_right_image_flips = True
opcoes.C = 5

dlib.train_simple_object_detector("recursos/pessoas_mascara.xml", "recursos/Pessoas.svm", opcoes)
