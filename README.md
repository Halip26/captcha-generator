# Captcha Genrator

A simple image captcha genrator

### Changes Made

- Redefined __random__ as a global variable, so that it can be accessed by other functions.
- Created the __generate_image()__ function to encapsulate complex logic related to generating captcha image, which also updates __random__ global variable and makes __photo__ available globally. It's called on button click, and also on application startup to (re)display captcha image.
- Removed redundant checks of __isinstance(data, BytesIO)__ on each __generate()__ call.
