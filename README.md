# Imagga Image Tagging

This Python script uses the Imagga API to retrieve the top 10 tags for a given image.

## Prerequisites

- Python 3.x
- `requests` library
- `json` library

## Installation

1. Install the required libraries:

   ```
   pip install requests
   ```

2. Obtain an Imagga API key and secret. You can sign up for a free Imagga account at [https://imagga.com/](https://imagga.com/).

## Usage

1. Replace the `image_path` variable with the path to the image file you want to analyze. If the image is on your desktop, you can use the provided code:

   ```python
   image_path = Path("~/Desktop/image.jpg").expanduser()
   ```

   Make sure to replace `"image.jpg"` with the actual filename of your image.

2. Update the `headers` dictionary with your Imagga API key and secret:

   ```python
   headers = {
       'accept': "application/json",
       'authorization': "Basic <your_api_key>:<your_api_secret>"
   }
   ```

   Replace `<your_api_key>` and `<your_api_secret>` with your actual Imagga API credentials.

3. Run the script:

   ```
   python imagga_tags.py
   ```

   The script will print the top 10 tags for the specified image.

## Example Output

```
landscape
nature
outdoor
tree
grass
field
sky
plant
green
summer
```

## Customization

- To change the image, update the `image_path` variable with the path to the new image file.
- To retrieve more or fewer tags, modify the `for i in range(10):` loop.
- If you want to use a remote image URL instead of a local file, update the `querystring` dictionary with the image URL:

  ```python
  querystring = {"image_url": "https://example.com/image.jpg"}
  ```

## License

This project is licensed under the [MIT License](LICENSE).
