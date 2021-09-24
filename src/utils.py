import os
import cv2
import pandas as pd
import numpy as np
import ast


def apk(actual, predicted, k=3):
    """Computes average precision at k between two lists of items"""
    if len(predicted) > k:
        predicted = predicted[:k]
    score = 0.0
    num_hits = 0.0
    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)
    if not actual:
        return 0.0
    return score / min(len(actual), k)

def mapk(actual, predicted, k=3):
    """Computes mean average precision at k between two lists of lists of items"""
    return np.mean([apk(a, p, k) for a, p in zip(actual, predicted)])

def preds2catids(predictions):
    return pd.DataFrame(np.argsort(-predictions, axis=1)[:, :3], columns=['a', 'b', 'c'])

def f2cat(filename: str) -> str:
    return filename.split('.')[0]

def list_all_categories():
    files = os.listdir(os.path.join(INPUT_DIR, 'train_sim_animals'))
    return sorted([f2cat(f) for f in files], key=str.lower)


def df_to_image_array(df, size, lw=6):
    df['drawing'] = df['drawing'].apply(ast.literal_eval)
    x = np.zeros((len(df), size, size))
    for i, raw_strokes in enumerate(df.drawing.values):
        x[i] = draw_cv2(raw_strokes, size=size, lw=lw)
    x = x / 255.
    x = x.reshape((len(df), size, size, 1)).astype(np.float32)
    return x

def draw_cv2(raw_strokes, size=256, lw=6, time_color=True):
    img = np.zeros((256, 256), np.uint8)
    for t, stroke in enumerate(raw_strokes):
        for i in range(len(stroke[0]) - 1):
            color = 255 - min(t, 10) * 13 if time_color else 255
            _ = cv2.line(img, (stroke[0][i], stroke[1][i]),
                         (stroke[0][i + 1], stroke[1][i + 1]), color, lw)
    if size != 256:
        return cv2.resize(img, (size, size))
    else:
        return img


# class MulticlassTruePositives(tf.keras.metrics.Metric):
#     def __init__(self, name='multiclass_true_positives', **kwargs):
#         super(MulticlassTruePositives, self).__init__(name=name, **kwargs)
#         self.true_positives = self.add_weight(name='tp', initializer='zeros')

#     def update_state(self, y_true, y_pred, sample_weight=None):
#         y_pred = tf.reshape(tf.argmax(y_pred, axis=1), shape=(-1, 1))
#         values = tf.cast(y_true, 'int32') == tf.cast(y_pred, 'int32')
#         values = tf.cast(values, 'float32')
#         if sample_weight is not None:
#             sample_weight = tf.cast(sample_weight, 'float32')
#             values = tf.multiply(values, sample_weight)
#         self.true_positives.assign_add(tf.reduce_sum(values))

#     def result(self):
#         return self.true_positives

#     def reset_states(self):
#         # The state of the metric will be reset at the start of each epoch.
#         self.true_positives.assign(0.)


# class PerformanceVisualizationCallback(Callback):
#     def __init__(self, model, validation_data, image_dir):
#         super().__init__()
#         self.model = model
#         self.validation_data = validation_data
        
#         os.makedirs(image_dir, exist_ok=True)
#         self.image_dir = image_dir

#     def on_epoch_end(self, epoch, logs={}):
#         y_pred = np.asarray(self.model.predict(self.validation_data[0]))
#         y_true = self.validation_data[1]             
#         y_pred_class = np.argmax(y_pred, axis=1)

#         # plot and save confusion matrix
#         fig, ax = plt.subplots(figsize=(16,12))
#         plot_confusion_matrix(y_true, y_pred_class, ax=ax)
#         fig.savefig(os.path.join(self.image_dir, f'confusion_matrix_epoch_{epoch}'))

#        # plot and save roc curve
#         fig, ax = plt.subplots(figsize=(16,12))
#         plot_roc(y_true, y_pred, ax=ax)
#         fig.savefig(os.path.join(self.image_dir, f'roc_curve_epoch_{epoch}'))

