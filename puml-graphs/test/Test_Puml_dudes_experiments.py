from unittest import TestCase
from plantuml.API_Plant_UML import API_Plant_UML
from utils.Dev import Dev
from utils.Files import Files
from utils.Show_Img import Show_Img
from utils.aws.Lambdas import Lambdas


class Test_Puml_dudes_experiments(TestCase):

    def setUp(self):
        self.plantuml    = API_Plant_UML()

    def test_create_puml____reader_sends_feedback(self):
        puml_file = '../diagrams/reader-sends-feedback.puml'
        png_file  =  '/tmp/{0}.png'.format(Files.file_name(puml_file))
        puml      = Files.contents(puml_file)
        img_url   = 'https://github.com/DinisCruz/Book_Generation_Z_Developer/raw/dudes-test/puml-graphs/dudes/puml/'
        puml      = puml.replace("<img:","<img:{0}".format(img_url))

        puml_to_png = Lambdas('utils.puml_to_png').invoke


        self.plantuml.puml_to_png_using_lambda_function(puml, png_file)

    # dudes
    def test_puml___dudes_creation(self):

        target_file = '/tmp/dudes-puml.png'
        puml        = Files.contents('../dudes/puml/first-test.puml')

        #Dev.pprint(puml)
        #self.plantuml.puml_to_png_via_local_server(puml, target_file)
        self.plantuml.puml_to_png_using_lambda_function(puml,target_file)

        #Show_Img.from_path(png_file)
        #Dev.pprint(png_file)

