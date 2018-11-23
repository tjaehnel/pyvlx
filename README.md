PyVLX - controling VELUX windows with Python
============================================

[![Build Status](https://travis-ci.org/Julius2342/pyvlx.svg?branch=master)](https://travis-ci.org/Julius2342/pyvlx)

PyVLX uses the Velux KLF 200 interface to control io-Homecontrol devices, e.g. Velux Windows.

NEW API!!!
----------

Velux published a new API. Connecting to the new API is still work in progress.

The [current state can be found here](https://github.com/Julius2342/pyvlx/blob/master/examples/demo.py).

This wrapper can already:

* Login to KLF 200 with password
* Retrieve scene list
* Run/activate scene
* Set position of specific window (50%)

Stay tuned!

<!--
Installation
------------

PyVLX can be installed via:

```bash
pip3 install pyvlx
```
-->

Basic Operations
----------------

```python
"""Just a demo of the new PyVLX module."""
import asyncio
from pyvlx import PyVLX


async def main(loop):
    """Demonstrate functionality of PyVLX."""
    pyvlx = PyVLX('pyvlx.yaml', log_frames=True, loop=loop)
    # Alternative:
    # pyvlx = PyVLX(host="192.168.2.127", password="velux123", loop=loop)

    await pyvlx.connect()
    await pyvlx.load_scenes()
    await pyvlx.scenes["All Windows Closed"].run()

    await pyvlx.load_nodes()
    await pyvlx.nodes['Bath'].open()
    await pyvlx.nodes['Bath'].close()
    await pyvlx.nodes['Bath'].set_position_percent(45)

if __name__ == '__main__':
    # pylint: disable=invalid-name
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(main(LOOP))
    # LOOP.run_forever()
    LOOP.close()
```


