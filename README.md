# gradio Digit Recognition

Repository for testing gradio framework and with digit recognition

## This repository is created to hold my project which purpose was to learn:
 * Gradio framework
 * Tensorflow for handwritten digit recognition

In this repository there are multiple models which were trained with different layers configuration and different ```quality metrics```
like:
* Accuracy - the most basic metric which shows how close a given set of measurements (observations or readings) are to their true value and it's calculated using following formula
$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
* Precision - describes how close the measurements are to each other, here is formula for that
$$Precision = \frac{TP}{TP + FP}$$
* Recall - is the fraction of relevant instances that were retrieved
$$Recall = \frac{TP}{TP + FN}$$
* F1-Score - is the harmonic mean of Precision and Recall. It provides a balance between precision and recall
$$F1 = 2 \cdot \frac{precision \cdot recall}{precision + recall}$$

```where $TP$ = True positive, $TN$ - True negative, $FP$ - False positive, $FN$ - False negative```

Here is confusion matrix describing TP, TN, FP, FN:

<img title="Confusion matrix" alt="confusion matrix" src="/img/ConfusionMatrix.png">