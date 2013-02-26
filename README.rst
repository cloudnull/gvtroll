Googel Voice Messager
#####################
:date: 2012-02-26 16:22
:tags: Google, Google Voice, SMS,
:category: \*nix

Send Messages from the CLI using Google Voice
=============================================

General Overview
----------------

This application will send messages using a Google Python Library. The messages will be delivered as SMS messages to a target number.

The gvtroll.py script is based on the original work provided by Zack Feldstine. ``https://github.com/jrcloud``


Functions of the Application :
  * Send Messages
  * Send a Randomly generated message
  * Send messages to a list of numbers


Prerequisites :
  * Python => 2.6 but < 3.0
  * Python Google Voice Library. `bwpayne-pygooglevoice-auth-fix` is included
  
    * Original URL : ``http://code.google.com/p/pygooglevoice/``
    * Auth Fix URL : ``http://code.google.com/r/bwpayne-pygooglevoice-auth-fix/``


Installation :

  Installation is simple::

    git clone git://github.com/cloudnull/gvtroll.git
    cd troll/bwpayne-pygooglevoice-auth-fix
    python setup.py install
    
  Now go run the script "gvtroll.py" or put the script where you want it.
  I have also included the mimic script which was part of a Google Python Class I participated in, which is used to generate the random text message.


Application Usage
-----------------

Here is the Basic Usage

    .. code-block:: bash

        gvtroll.py -u GOOGLE@EMAILADDRESS -p PASSWORD -n PHONENUMBER


Run ``gvtroll.py -h`` for a full list of available flags and operations