import os
import joblib
import graphene
from django.conf import settings
from django.core.files.storage import default_storage
from skimage.io import imread
from skimage.transform import resize
from django.core.files.base import ContentFile


class ScoreType(graphene.ObjectType):
    """
    Evaluation metrics.
    """
    accuracy = graphene.Float()
    precision = graphene.Float()
    sensitivity = graphene.Float()
    specificity = graphene.Float()
    f1 = graphene.Float()


class ModelType(graphene.ObjectType):
    """
    Estimator metadata.
    """
    reference = graphene.String()
    estimator = graphene.String()
    train_score = graphene.Float()
    correct_percentage = graphene.Float()
    test_scores = graphene.Field(ScoreType)
    set_scores = graphene.Field(ScoreType)
    test_baseline_accuracy = graphene.Float()
    set_baseline_accuracy = graphene.Float()
    sample_split_rate = graphene.String()


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

    # models
    models = graphene.List(ModelType)

    def resolve_models(self, info, **kwargs):
        path = 'api/dumps/'
        models_available = []
        for dump in os.listdir(path):
            data = joblib.load(path+dump)
            models_available.append(
                ModelType(
                    reference=dump,
                    estimator=str(data['model']._final_estimator),
                    train_score=data['score'],
                    correct_percentage=data['correct_percentage'],
                    test_scores=data.get('test_scores', {}),
                    set_scores=data.get('set_scores', {}),
                    test_baseline_accuracy=data.get('test_baseline_accuracy'),
                    set_baseline_accuracy=data.get('set_baseline_accuracy'),
                    sample_split_rate=dump.split('_')[0]
                )
            )
        return models_available

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
