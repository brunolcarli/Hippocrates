import os
import joblib
import graphene
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import skimage
from skimage.io import imread
from skimage.transform import resize


class PredictionType(graphene.ObjectType):
    """
    Prediction response structure.
    """
    estimator = graphene.String(description='Estimator model used.')
    prediction = graphene.String(description='Model prediction result.')


class Query(graphene.ObjectType):
    """
    API available queries.
    """

    # Version
    api_version = graphene.String(description='Return the current API version.')

    def resolve_api_version(self, info, **kwargs):
        return settings.VERSION

    # predict
    predict = graphene.Field(
        PredictionType,
        description='Predicts a melanoma class for a image file.'
    )

    def resolve_predict(self, info, **kwargs):
        files = info.context.FILES
        image = files.get('File')
        # The estimator may be chosen by parameter in the future
        estimator = 'SGDClassifier(random_state=2154)_v_1.model'

        if not image:
            raise Exception('ERROR: No file received. Aborting.')

        path = default_storage.save('hippocrates/image.jpeg', ContentFile(image.read()))
        img = imread(path)
        img = resize(img, (80, 80))

        # load model and predict value
        classifier = joblib.load(f'api/dumped_estimators/{estimator}')
        prediction = classifier.predict([img])

        # delete created file
        garbage = open(path)
        os.remove(garbage.name)

        return PredictionType(estimator=estimator, prediction=prediction[0])
