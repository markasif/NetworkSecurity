from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score,precision_score,recall_score
import sys

def get_classification_score(y_true,y_pred) -> ClassificationMetricArtifact:
    try:
        model_fit_score = f1_score(y_true,y_pred)
        model_recall_score = recall_score(y_true,y_pred)
        model_precision_score = precision_score(y_true,y_pred)

        classification_metric = ClassificationMetricArtifact(f1_score=model_fit_score,
                                                             recall_score=model_recall_score,
                                                             precision_score=model_precision_score
                                                             )
        return classification_metric
    except Exception as e:
        raise NetworkSecurityException(e,sys)