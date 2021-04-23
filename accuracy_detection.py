from utils.metrics import *
from utils.system_metrics import *
import pandas as pd


def evaluate_accuracy_algo(model_name, predictions, labels, verbose=False):
    """
        Evaluate model's realistic accuracy using various scoring measures:
        top1, top5, entropy, bvsb, expected accuracy, gini index, balanced accuracy, cross entropy

        Params:
            predictions: a list containing confidences for all the classes with a shape of (samples, classes)
            labels: a list containing the actual class labels
            verbose: (bool) are the scores printed out. (default = False)

        Returns:
            df (pandas.DataFrame): dataframe with the results.
        """

    df = pd.DataFrame(columns=["M.Name", "Top1", "Top5", "Entropy", "BVSB", "Exp.accuracy",
                                               "Gini", "B.accuracy", "C.Entropy"])

    top1_acc = top1_accuracy(predictions, labels)
    top5_acc = topk_accuracy(predictions, labels, 5)
    exp_acc = expected_accuracy(predictions, labels)
    exp_entr = expected_entropy(predictions)
    bvsb_val = expected_bvsb(predictions)
    gini = expected_gini_index(predictions)
    cross_entr = expected_cross_entropy(predictions, labels)
    b_acc = balanced_accuracy(predictions, labels)

    df.loc[0] = [model_name, top1_acc, top5_acc, exp_entr, bvsb_val, exp_acc, gini, b_acc, cross_entr]

    if verbose:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        print(df)

    return df


def evaluate_accuracy_sys(model_name, server_predictions, client_predictions, labels, verbose=False):
    """
        Evaluate model's realistic accuracy using various scoring measures:
        top1, top5, entropy, bvsb, expected accuracy, gini index, balanced accuracy, cross entropy

        Params:
            predictions: a list containing confidences for all the classes with a shape of (samples, classes)
            labels: a list containing the actual class labels
            verbose: (bool) are the scores printed out. (default = False)

        Returns:
            df (pandas.DataFrame): dataframe with the results.
        """

    df = pd.DataFrame(columns=["M.Name", "C.Entropy", "Conf. Diff."])

    cr_entropy = expected_cross_entropy_srv(server_predictions, client_predictions)
    conf_diff = expected_confidence_diff(server_predictions, client_predictions, labels)

    df.loc[0] = [model_name, cr_entropy, conf_diff]

    if verbose:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        print(df)

    return df



