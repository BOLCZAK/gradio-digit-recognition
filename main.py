import gradio as gr
import tensorflow as tf

models = ['model.keras', 'model_all.keras', 'model_f1.keras', 'model_precision.keras', 'model_recall.keras']

# model = tf.keras.models.load_model('model.keras')

def recognize_digit(image, model_name):
    print(model_name)
    model = tf.keras.models.load_model(model_name)

    if image is not None:
        image = image.reshape((1, 28, 28, 1)).astype('float32') / 255

        prediciton = model.predict(image)

        return {str(i): float(prediciton[0][i]) for i in range(10)}
    else:
        return 'Something went wrong'


iface = gr.Interface(
    fn=recognize_digit,
    inputs=[gr.Image(
                shape=(28, 28),
                image_mode='L',
                invert_colors=True,
                source='canvas'),
            gr.Dropdown(
                label="Select Model",
                choices=[m for m in models],
                type="value",
                interactive=True)],
    outputs=gr.Label(num_top_classes=10),
    live=True
)

iface.launch()