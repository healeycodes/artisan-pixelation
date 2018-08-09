### artisan pixelation

<br>

Inspired by Kensuke Koike's real life pixelation art, this program which performs an approximation of his [Avatar](https://www.youtube.com/watch?v=U1KiC0AXhHg) piece.

![Avatar by Koike](https://github.com/healeycodes/artisan-pixelation/blob/master/images/avatar-kensuke-koike.png)

* `pip install requirements.txt`
* `python side-by-side.py image.png` The first argument should be an image.
* `--resolution 22` (optional arg) How many blocks you want to break the image into
* `--density 4` (optional arg) How little of the image you want to remain - higher is more destruction.

The resulting image will be saved as `combined.png`. You can use `Image.show()` for testing and a temporary image will be opened in a default program. See the [Pillow docs](https://pillow.readthedocs.io/en/5.2.x/) for more. Only tested with Python 3.5 and up.

### Examples

1.

![George Washington](https://github.com/healeycodes/artisan-pixelation/blob/master/images/g-wash-processed.png)

2.

![Girl With a Pearl Earing](https://github.com/healeycodes/artisan-pixelation/blob/master/images/girl-processed.png)

3.

![Mona Lisa](https://github.com/healeycodes/artisan-pixelation/blob/master/images/mona-processed.png)

<br>

Thanks to https://www.kensukekoike.com.
