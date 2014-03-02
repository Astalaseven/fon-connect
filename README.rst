===========
fon-connect
===========

Connect easily to FON (Belgacom) Network!

Installation
------------

.. code-block:: bash

    pip install fon


Usage
-----

You need to store your credentials in :code:`~/.config/fon`

.. code-block:: ini

    [fon]
    username = user@belgacomfon.be
    password = mAhPassw0rdZ

fon-connect tests if the connection is active by querying :code:`perdu.com` by default.
To change this behavior, add :code:`url = http://myurl.example.com/page` to the end of :code:`~/.config/fon`

Use it with:

.. code-block:: bash

    fon

Alternatively, you can give your username, password and the test url as parameters (all are optional).

.. code-block:: bash

    fon -u user@belgacomfon.be -p mAhPassw0rdZ --url=http://myurl.example.com/page

You also can specify another path for the configuration file with `-c /path/to/file`

fon-connect also has a persistent mode (activate it with :code:`-P` or :code:`--persist`) which tests the connection, reconnects if necessary, sleeps for 10 seconds and loops.

Full help :

.. code-block:: bash

    fon -h


=======
License
=======

fon-connect is available under the MIT license.

Original code from Gatien Bovyn at https://github.com/Astalaseven/fon-connect.

Changes made by Nikita Marchant at https://github.com/C4ptainCrunch/fon-connect.

====
Misc
====

* Feel free to report bugs or submit pull request.
* This code should work on belgian (Belgacom) FON portals. I hope it also works on other carriers portals but if not, please report and I'll try to fix it.