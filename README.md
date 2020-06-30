# openstack_schedules
minimal implementation of web interface to access a swagger based openstack api and provide a list of running servers. It also contians some illustrative codes on how to access and manipulate the openstack sdk.


also run the following command inside the python-flask-server folder to start the swagger spi server. This folder has to run on the same container where openstack controller is running.

``` docker build -t server . && docker run server ```
